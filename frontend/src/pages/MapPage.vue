<script setup lang="ts">
import { ref, onMounted, watch, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import maplibregl from 'maplibre-gl'
import { fetchGeoEvents } from '@/utils/api'

const { locale } = useI18n()
const router = useRouter()

const mapContainer = ref<HTMLDivElement>()
const loading = ref(true)
let map: maplibregl.Map | null = null
let markers: maplibregl.Marker[] = []

async function loadMarkers() {
  if (!map) return
  markers.forEach(m => m.remove())
  markers = []

  try {
    const geo = await fetchGeoEvents({ lang: locale.value })
    for (const feat of geo.features) {
      const [lng, lat] = feat.geometry.coordinates
      const el = document.createElement('div')
      el.style.cssText = `
        width: 14px; height: 14px;
        background: #1a73e8;
        border: 2px solid #fff;
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 1px 4px rgba(0,0,0,0.3);
      `
      el.addEventListener('click', () => {
        router.push(`/event/${feat.properties.event_id}`)
      })

      const popup = new maplibregl.Popup({ offset: 10 }).setText(
        feat.properties.title
      )

      const marker = new maplibregl.Marker({ element: el })
        .setLngLat([lng, lat])
        .setPopup(popup)
        .addTo(map)
      markers.push(marker)
    }
  } catch (err) {
    console.error('Failed to load geo events', err)
  } finally {
    loading.value = false
  }
}

watch(locale, loadMarkers)

onMounted(async () => {
  map = new maplibregl.Map({
    container: mapContainer.value!,
    style: 'https://demotiles.maplibre.org/style.json',
    center: [104, 35],
    zoom: 3,
  })
  map.addControl(new maplibregl.NavigationControl(), 'top-right')
  map.on('load', loadMarkers)
})

onUnmounted(() => {
  map?.remove()
})
</script>

<template>
  <div style="flex:1; position:relative">
    <div v-if="loading" class="loading" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:var(--color-surface);padding:16px 24px;border-radius:8px;z-index:10;box-shadow:0 2px 12px rgba(0,0,0,0.15)">
      {{ $t('timeline.loading') }}
    </div>
    <div ref="mapContainer" class="map-container"></div>
  </div>
</template>
