<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { fetchEvent, getExportEventCsvUrl, getExportEventPdfUrl, downloadUrl } from '@/utils/api'
import type { EventDetail } from '@/types/event'

const route = useRoute()
const router = useRouter()
const { locale } = useI18n()

const event = ref<EventDetail | null>(null)
const loading = ref(true)
const compareMode = ref(false)

const title = computed(() => {
  if (!event.value) return ''
  const match = event.value.titles.find(t => t.language === locale.value)
  return match?.title ?? event.value.titles[0]?.title ?? ''
})

const description = computed(() => {
  if (!event.value) return null
  const match = event.value.descriptions.find(d => d.language === locale.value)
  return match?.content ?? match?.summary ?? null
})

const countryLabels: Record<string, string> = {
  TW: '🇹🇼 Taiwan',
  JP: '🇯🇵 Japan',
  KR: '🇰🇷 South Korea',
  US: '🇺🇸 United States',
  GB: '🇬🇧 United Kingdom',
  CN: '🇨🇳 China (official)',
}

function formatDate(dateStr: string, precision: string): string {
  const d = new Date(dateStr)
  if (precision === 'year') return String(d.getFullYear())
  if (precision === 'month') return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`
  return d.toLocaleDateString()
}

onMounted(async () => {
  try {
    event.value = await fetchEvent(route.params.id as string)
  } catch (err) {
    console.error('Failed to load event', err)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="content" style="max-width:960px">
    <div v-if="loading" class="loading">{{ $t('timeline.loading') }}</div>
    <div v-else-if="!event" class="empty-state">
      <p>Event not found.</p>
    </div>
    <template v-else>
      <div class="detail-header">
        <a class="back-link" @click="router.push('/timeline')">&larr; {{ $t('event.back') }}</a>
        <h1>{{ title }}</h1>
        <div class="export-buttons">
          <button class="export-btn" @click="downloadUrl(getExportEventCsvUrl(event.id, locale), `event_${event.id}_${locale}.csv`)">{{ $t('export.csv_event') }}</button>
          <button class="export-btn" @click="downloadUrl(getExportEventPdfUrl(event.id, locale), `event_${event.id}_${locale}.pdf`)">{{ $t('export.pdf_event') }}</button>
        </div>
        <p class="page-subtitle">
          {{ formatDate(event.date, event.date_precision) }}
          <template v-if="event.date_end">
            &ndash; {{ formatDate(event.date_end, event.date_precision) }}
          </template>
          <span v-if="event.category" class="tag" style="margin-left:8px">
            {{ $t(`categories.${event.category}`) }}
          </span>
        </p>
      </div>

      <!-- Description -->
      <div v-if="description" class="detail-section">
        <p style="font-size:15px;line-height:1.8;white-space:pre-line">{{ description }}</p>
      </div>

      <!-- Tags -->
      <div v-if="event.tags.length > 0" class="detail-section">
        <div class="event-meta" style="display:flex;gap:6px;flex-wrap:wrap">
          <span v-for="tag in event.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
      </div>

      <!-- Location -->
      <div v-if="event.location" class="detail-section">
        <h2>{{ $t('event.location') }}</h2>
        <p>{{ event.location.names[locale] || event.location.country }}</p>
      </div>

      <!-- Perspectives -->
      <div v-if="event.perspectives.length > 0" class="detail-section">
        <div class="section-header">
          <h2>{{ $t('event.perspectives') }}</h2>
          <button v-if="event.perspectives.length > 1" class="compare-toggle" @click="compareMode = !compareMode">
            {{ compareMode ? $t('event.standard_view') : $t('event.compare_view') }}
          </button>
        </div>

        <!-- Comparison Grid -->
        <div v-if="compareMode" class="compare-grid">
          <div v-for="p in event.perspectives" :key="p.id" class="compare-column">
            <div class="compare-country">{{ countryLabels[p.country_code] || p.country_code }}</div>
            <div class="compare-text">{{ p.viewpoint }}</div>
          </div>
        </div>

        <!-- Standard Stacked View -->
        <template v-else>
          <div v-for="p in event.perspectives" :key="p.id" class="perspective-card">
            <div class="perspective-country">{{ countryLabels[p.country_code] || p.country_code }}</div>
            <div class="perspective-text">{{ p.viewpoint }}</div>
          </div>
        </template>
      </div>
      <div v-else class="detail-section">
        <p class="page-subtitle">{{ $t('event.no_perspectives') }}</p>
      </div>

      <!-- Sources -->
      <div v-if="event.sources.length > 0" class="detail-section">
        <h2>{{ $t('event.sources') }}</h2>
        <ul class="source-list">
          <li v-for="s in event.sources" :key="s.id">
            <a :href="s.url" target="_blank" rel="noopener" class="source-url">{{ s.title || s.url }}</a>
            <div class="source-meta">
              {{ s.publisher }} &middot; {{ s.language }} &middot;
              {{ $t('event.importance') }}: {{ Math.round(s.reliability * 100) }}%
            </div>
          </li>
        </ul>
      </div>
    </template>
  </div>
</template>

<style scoped>
.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
  padding-bottom: 4px;
  border-bottom: 1px solid var(--color-border);
}
.section-header h2 {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}
.compare-toggle {
  font-size: 13px;
  padding: 4px 12px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background: var(--color-surface);
  color: var(--color-primary);
  cursor: pointer;
  transition: background 0.15s;
}
.compare-toggle:hover {
  background: var(--color-tag);
}

/* Comparison Grid */
.compare-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}
.compare-column {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
}
.compare-country {
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 10px;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--color-primary);
  color: var(--color-primary);
}
.compare-text {
  font-size: 14px;
  line-height: 1.7;
  white-space: pre-line;
}

.export-buttons {
  display: flex;
  gap: 8px;
  margin: 12px 0;
}

.export-btn {
  padding: 6px 14px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background: var(--color-surface);
  color: var(--color-text);
  font-size: 13px;
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
}

.export-btn:hover {
  background: var(--color-primary);
  color: #fff;
  border-color: var(--color-primary);
}
</style>
