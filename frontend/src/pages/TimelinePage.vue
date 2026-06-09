<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { fetchEvents, fetchCategories, fetchTags } from '@/utils/api'
import type { EventListItem } from '@/types/event'

const { locale } = useI18n()
const router = useRouter()

const events = ref<EventListItem[]>([])
const categories = ref<string[]>([])
const allTags = ref<string[]>([])
const loading = ref(true)
const searchQuery = ref('')
const selectedCategory = ref('')
const selectedTags = ref<string[]>([])
const selectedImportance = ref(0)
let debounceTimer: ReturnType<typeof setTimeout> | null = null

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
    const params: Record<string, unknown> = {
      lang: locale.value,
      limit: 500,
    }
    if (selectedCategory.value) params.category = selectedCategory.value
    if (importanceFilter.value > 0) params.importance_min = importanceFilter.value
    if (searchQuery.value) params.q = searchQuery.value
    if (selectedTags.value.length > 0) params.tags = selectedTags.value.join(',')

    const res = await fetchEvents(params as any)
    events.value = res.events
  } finally {
    loading.value = false
  }
}

function onSearchInput() {
  if (debounceTimer) clearTimeout(debounceTimer)
  debounceTimer = setTimeout(load, 300)
}

function toggleTag(tag: string) {
  const idx = selectedTags.value.indexOf(tag)
  if (idx >= 0) {
    selectedTags.value.splice(idx, 1)
  } else {
    selectedTags.value.push(tag)
  }
  load()
}

function clearFilters() {
  searchQuery.value = ''
  selectedCategory.value = ''
  selectedTags.value = []
  selectedImportance.value = 0
  load()
}

const hasActiveFilters = computed(() =>
  searchQuery.value !== '' ||
  selectedCategory.value !== '' ||
  selectedTags.value.length > 0 ||
  importanceFilter.value > 0
)

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

function goToMap(e: EventListItem) {
  if (e.location) {
    router.push(`/map?event=${e.id}`)
  }
}

watch(locale, load)
watch(selectedCategory, load)
watch(selectedImportance, load)

onMounted(async () => {
  try {
    categories.value = await fetchCategories()
    allTags.value = await fetchTags()
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
        <input v-model="searchQuery" @input="onSearchInput" :placeholder="$t('search.placeholder')" />
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
      <label>{{ $t('event.tags') }}</label>
      <div class="tag-filter-list">
        <label v-for="tag in allTags" :key="tag" class="tag-checkbox">
          <input type="checkbox" :checked="selectedTags.includes(tag)" @change="toggleTag(tag)" />
          <span>{{ tag }}</span>
        </label>
      </div>
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
    <button v-if="hasActiveFilters" class="clear-btn" @click="clearFilters">
      ✕ {{ $t('search.clear') }}
    </button>
  </aside>
  <div class="content">
    <h1 class="page-title">{{ $t('timeline.title') }}</h1>
    <p class="page-subtitle">{{ $t('timeline.subtitle') }}</p>

    <div v-if="loading" class="loading">{{ $t('timeline.loading') }}</div>
    <div v-else-if="events.length === 0" class="empty-state">
      <p>{{ $t('search.no_results') }}</p>
    </div>
    <template v-else>
      <div v-for="[year, evts] in grouped" :key="year">
        <h2 class="year-heading">{{ year }}</h2>
        <div
          v-for="e in evts"
          :key="e.id"
          class="event-card"
          @click="router.push(`/event/${e.id}`)"
        >
          <div class="event-date">{{ formatDate(e) }}</div>
          <div class="event-title">{{ getTitle(e) }}</div>
          <div v-if="getSummary(e)" class="event-summary">{{ getSummary(e) }}</div>
          <div v-if="e.tags.length > 0" class="event-tags">
            <span v-for="tag in e.tags" :key="tag" class="tag">{{ tag }}</span>
          </div>
          <div class="event-meta">
            <span v-if="e.category" class="tag">{{ $t(`categories.${e.category}`) }}</span>
            <span v-if="e.location" class="tag">{{ e.location.country }}</span>
            <button v-if="e.location" class="map-link" @click.stop="goToMap(e)" :title="$t('timeline.show_on_map')">🗺</button>
            <span class="importance-bar" :title="`${$t('event.importance')}: ${e.importance}`">
              <span class="fill" :style="{ width: e.importance + '%' }"></span>
            </span>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<style scoped>
.tag-filter-list {
  max-height: 200px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.tag-checkbox {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  cursor: pointer;
  padding: 2px 4px;
  border-radius: 4px;
  transition: background 0.1s;
}
.tag-checkbox:hover {
  background: var(--color-tag);
}
.tag-checkbox input {
  width: auto;
}
.event-tags {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
  margin-top: 6px;
}
.map-link {
  background: none;
  border: none;
  font-size: 16px;
  cursor: pointer;
  padding: 0 4px;
  line-height: 1;
  opacity: 0.6;
  transition: opacity 0.15s;
}
.map-link:hover {
  opacity: 1;
}
.clear-btn {
  width: 100%;
  padding: 6px 12px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background: var(--color-surface);
  color: var(--color-text-secondary);
  font-size: 13px;
  cursor: pointer;
  transition: background 0.15s, color 0.15s;
}
.clear-btn:hover {
  background: var(--color-tag);
  color: var(--color-primary);
}
</style>
