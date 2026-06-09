import axios from 'axios'
import type { EventListResponse, EventDetail, GeoJSONCollection } from '@/types/event'

const api = axios.create({
  baseURL: '/api',
  timeout: 30000,
})

export interface FetchEventsParams {
  lang?: string
  category?: string
  country?: string
  q?: string
  tags?: string
  date_from?: string
  date_to?: string
  importance_min?: number
  limit?: number
  offset?: number
}

export async function fetchEvents(params: FetchEventsParams = {}): Promise<EventListResponse> {
  const res = await api.get<EventListResponse>('/events', { params })
  return res.data
}

export async function fetchEvent(id: string): Promise<EventDetail> {
  const res = await api.get<EventDetail>(`/events/${id}`)
  return res.data
}

export async function fetchGeoEvents(params: {
  lang?: string
  date_from?: string
  date_to?: string
  category?: string
} = {}): Promise<GeoJSONCollection> {
  const res = await api.get<GeoJSONCollection>('/events/geo', { params })
  return res.data
}

export async function fetchCategories(): Promise<string[]> {
  const res = await api.get<string[]>('/events/categories')
  return res.data
}

export async function fetchLanguages(): Promise<string[]> {
  const res = await api.get<string[]>('/events/languages')
  return res.data
}

export async function fetchTags(): Promise<string[]> {
  const res = await api.get<string[]>('/events/tags')
  return res.data
}

export interface EventStats {
  total: number
  categories: Record<string, number>
  decades: Record<string, number>
}

export async function fetchStats(): Promise<EventStats> {
  const res = await api.get<EventStats>('/events/stats')
  return res.data
}

export function getExportEventsCsvUrl(params: {
  lang?: string
  category?: string
  q?: string
  date_from?: string
  date_to?: string
} = {}): string {
  const qs = new URLSearchParams()
  if (params.lang) qs.set('lang', params.lang)
  if (params.category) qs.set('category', params.category)
  if (params.q) qs.set('q', params.q)
  if (params.date_from) qs.set('date_from', params.date_from)
  if (params.date_to) qs.set('date_to', params.date_to)
  const query = qs.toString()
  return `/api/export/events/csv${query ? '?' + query : ''}`
}

export function getExportEventCsvUrl(id: string, lang?: string): string {
  const qs = lang ? `?lang=${lang}` : ''
  return `/api/export/events/${id}/csv${qs}`
}

export function getExportEventsPdfUrl(params: {
  lang?: string
  category?: string
} = {}): string {
  const qs = new URLSearchParams()
  if (params.lang) qs.set('lang', params.lang)
  if (params.category) qs.set('category', params.category)
  const query = qs.toString()
  return `/api/export/events/pdf${query ? '?' + query : ''}`
}

export function getExportEventPdfUrl(id: string, lang?: string): string {
  const qs = lang ? `?lang=${lang}` : ''
  return `/api/export/events/${id}/pdf${qs}`
}

export function downloadUrl(url: string, filename: string) {
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
}

export default api
