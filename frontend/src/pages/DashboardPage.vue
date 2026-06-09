<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { fetchStats } from '@/utils/api'
import type { EventStats } from '@/utils/api'

const stats = ref<EventStats | null>(null)
const loading = ref(true)

const maxCategory = ref(0)
const maxDecade = ref(0)

onMounted(async () => {
  try {
    stats.value = await fetchStats()
    const vals = Object.values(stats.value.categories)
    maxCategory.value = vals.length > 0 ? Math.max(...vals) : 1
    const dvals = Object.values(stats.value.decades)
    maxDecade.value = dvals.length > 0 ? Math.max(...dvals) : 1
  } catch (err) {
    console.error('Failed to load stats', err)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="content" style="max-width: 960px">
    <h1 class="page-title">{{ $t('stats.title') }}</h1>
    <p class="page-subtitle">{{ $t('stats.subtitle') }}</p>

    <div v-if="loading" class="loading">{{ $t('timeline.loading') }}</div>
    <div v-else-if="!stats" class="empty-state">
      <p>No data available.</p>
    </div>
    <template v-else>
      <!-- Summary Cards -->
      <div class="stats-cards">
        <div class="stat-card">
          <div class="stat-value">{{ stats.total }}</div>
          <div class="stat-label">{{ $t('stats.total_events') }}</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">{{ Object.keys(stats.categories).length }}</div>
          <div class="stat-label">{{ $t('stats.categories_count') }}</div>
        </div>
        <div class="stat-card">
          <div class="stat-value">{{ Object.keys(stats.decades).length }}</div>
          <div class="stat-label">{{ $t('stats.decades_count') }}</div>
        </div>
      </div>

      <!-- Category Distribution -->
      <div class="detail-section">
        <h2>{{ $t('stats.category_distribution') }}</h2>
        <div class="bar-chart">
          <div v-for="(count, cat) in stats.categories" :key="cat" class="bar-row">
            <div class="bar-label">{{ $t(`categories.${cat}`) }}</div>
            <div class="bar-track">
              <div class="bar-fill" :style="{ width: (count / maxCategory * 100) + '%' }"></div>
            </div>
            <div class="bar-value">{{ count }}</div>
          </div>
        </div>
      </div>

      <!-- Decade Distribution -->
      <div class="detail-section">
        <h2>{{ $t('stats.decade_distribution') }}</h2>
        <div class="bar-chart">
          <div v-for="(count, decade) in stats.decades" :key="decade" class="bar-row">
            <div class="bar-label">{{ decade }}</div>
            <div class="bar-track">
              <div class="bar-fill decade" :style="{ width: (count / maxDecade * 100) + '%' }"></div>
            </div>
            <div class="bar-value">{{ count }}</div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<style scoped>
.stats-cards {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
}
.stat-card {
  flex: 1;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 20px;
  text-align: center;
}
.stat-value {
  font-size: 36px;
  font-weight: 700;
  color: var(--color-primary);
}
.stat-label {
  font-size: 13px;
  color: var(--color-text-secondary);
  margin-top: 4px;
}
.bar-chart {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.bar-row {
  display: flex;
  align-items: center;
  gap: 12px;
}
.bar-label {
  width: 140px;
  font-size: 14px;
  text-align: right;
  flex-shrink: 0;
}
.bar-track {
  flex: 1;
  height: 24px;
  background: var(--color-border);
  border-radius: 4px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  background: var(--color-primary);
  border-radius: 4px;
  transition: width 0.6s ease;
}
.bar-fill.decade {
  background: var(--color-accent);
}
.bar-value {
  width: 40px;
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text-secondary);
  flex-shrink: 0;
}
</style>