<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { fetchEvents } from '@/utils/api'
import type { EventListItem } from '@/types/event'

const { locale } = useI18n()
const router = useRouter()

interface TourStop {
  date_from: string
  date_to: string
  category?: string
  tags?: string
}

interface TourRoute {
  id: string
  name: string
  description: string
  icon: string
  stops: TourStop[]
}

const routes: TourRoute[] = [
  {
    id: 'ccp-founding',
    name: 'tour.ccp_founding',
    description: 'tour.ccp_founding_desc',
    icon: '🚩',
    stops: [
      { date_from: '1921-01-01', date_to: '1949-12-31', tags: 'ccp,founding,communist,civil war,pla' },
    ],
  },
  {
    id: 'reform-opening',
    name: 'tour.reform_opening',
    description: 'tour.reform_opening_desc',
    icon: '📈',
    stops: [
      { date_from: '1978-01-01', date_to: '2010-12-31', tags: 'reform,deng xiaoping,market economy,sez' },
    ],
  },
  {
    id: 'human-rights',
    name: 'tour.human_rights',
    description: 'tour.human_rights_desc',
    icon: '✊',
    stops: [
      { date_from: '1957-01-01', date_to: '2022-12-31', category: 'human_rights' },
    ],
  },
  {
    id: 'foreign-relations',
    name: 'tour.foreign_relations',
    description: 'tour.foreign_relations_desc',
    icon: '🌐',
    stops: [
      { date_from: '1949-01-01', date_to: '2020-12-31', tags: 'us-china,diplomacy,foreign policy,trade war,nixon' },
    ],
  },
  {
    id: 'economic-milestones',
    name: 'tour.economic_milestones',
    description: 'tour.economic_milestones_desc',
    icon: '💰',
    stops: [
      { date_from: '1958-01-01', date_to: '2022-12-31', category: 'economy' },
    ],
  },
]

const selectedRoute = ref<TourRoute | null>(null)
const tourEvents = ref<EventListItem[]>([])
const loading = ref(false)
async function selectRoute(route: TourRoute) {
  selectedRoute.value = route
  loading.value = true
  tourEvents.value = []

  try {
    const allEvents: EventListItem[] = []
    for (const stop of route.stops) {
      const res = await fetchEvents({
        lang: locale.value,
        date_from: stop.date_from,
        date_to: stop.date_to,
        category: stop.category || undefined,
        tags: stop.tags || undefined,
        limit: 200,
      })
      allEvents.push(...res.events)
    }
    allEvents.sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime())
    tourEvents.value = allEvents
  } catch (err) {
    console.error('Failed to load tour events', err)
  } finally {
    loading.value = false
  }
}

function backToRoutes() {
  selectedRoute.value = null
  tourEvents.value = []
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
</script>

<template>
  <div class="content" style="max-width: 960px">
    <template v-if="!selectedRoute">
      <h1 class="page-title">{{ $t('tour.title') }}</h1>
      <p class="page-subtitle">{{ $t('tour.subtitle') }}</p>

      <div class="tour-grid">
        <div
          v-for="route in routes"
          :key="route.id"
          class="tour-card"
          @click="selectRoute(route)"
        >
          <div class="tour-icon">{{ route.icon }}</div>
          <div class="tour-name">{{ $t(route.name) }}</div>
          <div class="tour-desc">{{ $t(route.description) }}</div>
        </div>
      </div>
    </template>

    <template v-else>
      <a class="back-link" @click="backToRoutes">&larr; {{ $t('tour.back') }}</a>
      <h1 class="page-title">{{ $t(selectedRoute.name) }}</h1>
      <p class="page-subtitle">{{ $t(selectedRoute.description) }}</p>

      <div v-if="loading" class="loading">{{ $t('timeline.loading') }}</div>
      <div v-else-if="tourEvents.length === 0" class="empty-state">
        <p>{{ $t('tour.no_events') }}</p>
      </div>
      <template v-else>
        <div class="tour-progress">
          <span class="tour-count">
            {{ tourEvents.length }} {{ $t('tour.events_found') }}
          </span>
        </div>
        <div
          v-for="e in tourEvents"
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
          </div>
        </div>
      </template>
    </template>
  </div>
</template>

<style scoped>
.tour-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}
.tour-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 24px;
  cursor: pointer;
  transition: box-shadow 0.15s, border-color 0.15s;
}
.tour-card:hover {
  box-shadow: 0 2px 12px rgba(0,0,0,0.1);
  border-color: var(--color-primary);
}
.tour-icon {
  font-size: 32px;
  margin-bottom: 12px;
}
.tour-name {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 6px;
}
.tour-desc {
  font-size: 13px;
  color: var(--color-text-secondary);
  line-height: 1.5;
}
.tour-progress {
  margin-bottom: 16px;
}
.tour-count {
  font-size: 14px;
  color: var(--color-text-secondary);
}
.back-link {
  display: inline-block;
  margin-bottom: 12px;
  font-size: 14px;
  color: var(--color-primary);
  cursor: pointer;
}
.back-link:hover {
  text-decoration: underline;
}
.event-tags {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
  margin-top: 6px;
}
</style>