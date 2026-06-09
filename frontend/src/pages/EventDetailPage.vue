<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { fetchEvent } from '@/utils/api'
import type { EventDetail } from '@/types/event'

const route = useRoute()
const router = useRouter()
const { locale } = useI18n()

const event = ref<EventDetail | null>(null)
const loading = ref(true)

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
        <h2>{{ $t('event.perspectives') }}</h2>
        <div v-for="p in event.perspectives" :key="p.id" class="perspective-card">
          <div class="perspective-country">{{ countryLabels[p.country_code] || p.country_code }}</div>
          <div class="perspective-text">{{ p.viewpoint }}</div>
        </div>
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
