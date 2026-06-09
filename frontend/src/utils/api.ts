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

export default api
