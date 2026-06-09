<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { fetchEvents, fetchCategories } from '@/utils/api'
import type { EventListItem } from '@/types/event'

const { locale } = useI18n()
const router = useRouter()

const events = ref<EventListItem[]>([])
const categories = ref<string[]>([])
const loading = ref(true)
const searchQuery = ref('')
const selectedCategory = ref('')
const selectedImportance = ref(0)

const grouped = computed(() => {
  const map = new Map<number, EventListItem[]>()
  for (const e of events.value) {
    const year = new Date(e.date).getFullYear()
    if (!map.has(year)) map.set(year, [])
    map.get(year)!.push(e)
  }
  return Array.from(map.entries()).sort(([a], [b]) => b - a)
})

const importanceFilter = computed(() => Number(selectedImportance.value))

async function load() {
  loading.value = true
  try {
    const res = await fetchEvents({
      lang: locale.value,
      category: selectedCategory.value || undefined,
      importance_min: importanceFilter.value || undefined,
      limit: 500,
    })
    events.value = res.events
  } finally {
    loading.value = false
  }
}

function getTitle(e: EventListItem): string {
  const match = e.titles.find(t => t.language === locale.value)
  return match?.title ?? e.titles[0]?.title ?? ''
}

function getSummary(e: EventListItem): string {
  const match = e.descriptions.find(d => d.language === locale.value)
  return match?.summary ?? match?.content ?? ''
}

function formatDate(e: EventListItem): string {
  const d = new Date(e.date)
  if (e.date_precision === 'year') return String(d.getFullYear())
  if (e.date_precision === 'month') return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`
  return d.toLocaleDateString()
}

watch(locale, load)
watch(selectedCategory, load)
watch(selectedImportance, load)

onMounted(async () => {
  try {
    categories.value = await fetchCategories()
  } catch { /* ignore */ }
  await load()
})
</script>

<template>
  <aside class="sidebar">
    <h3>{{ $t('timeline.filter') }}</h3>
    <div class="filter-group">
      <label>{{ $t('nav.search') }}</label>
      <div class="search-input-wrapper">
        <input v-model="searchQuery" :placeholder="$t('search.placeholder')" />
      </div>
    </div>
    <div class="filter-group">
      <label>{{ $t('event.category') }}</label>
      <select v-model="selectedCategory">
        <option value="">{{ $t('timeline.all_categories') }}</option>
        <option v-for="c in categories" :key="c" :value="c">
          {{ $t(`categories.${c}`) }}
        </option>
      </select>
    </div>
    <div class="filter-group">
      <label>{{ $t('event.importance') }}</label>
      <select v-model="selectedImportance">
        <option :value="0">{{ $t('timeline.all_categories') }}</option>
        <option :value="80">80+</option>
        <option :value="90">90+</option>
        <option :value="100">100</option>
      </select>
    </div>
  </aside>
  <div class="content">
    <h1 class="page-title">{{ $t('timeline.title') }}</h1>
    <p class="page-subtitle">{{ $t('timeline.subtitle') }}</p>

    <div v-if="loading" class="loading">{{ $t('timeline.loading') }}</div>
    <div v-else-if="events.length === 0" class="empty-state">
      <p>{{ $t('timeline.no_events') }}</p>
    </div>
    <template v-else>
      <div v-for="[year, evts] in grouped" :key="year">
        <h2 class="year-heading">{{ year }}</h2>
        <div
          v-for="e in searchQuery
            ? evts.filter(ev => getTitle(ev).toLowerCase().includes(searchQuery.toLowerCase()))
            : evts"
          :key="e.id"
          class="event-card"
          @click="router.push(`/event/${e.id}`)"
        >
          <div class="event-date">{{ formatDate(e) }}</div>
          <div class="event-title">{{ getTitle(e) }}</div>
          <div v-if="getSummary(e)" class="event-summary">{{ getSummary(e) }}</div>
          <div class="event-meta">
            <span v-if="e.category" class="tag">{{ $t(`categories.${e.category}`) }}</span>
            <span v-if="e.location" class="tag">{{ e.location.country }}</span>
            <span class="importance-bar" :title="`${$t('event.importance')}: ${e.importance}`">
              <span class="fill" :style="{ width: e.importance + '%' }"></span>
            </span>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>
