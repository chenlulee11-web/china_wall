export interface EventTitle {
  id: string
  event_id: string
  language: string
  title: string
}

export interface EventDescription {
  id: string
  event_id: string
  language: string
  summary: string | null
  content: string | null
}

export interface EventLocation {
  id: string
  event_id: string
  lat: number | null
  lng: number | null
  country: string | null
  names: Record<string, string>
}

export interface EventSource {
  id: string
  event_id: string
  language: string
  url: string
  title: string | null
  publisher: string | null
  reliability: number
}

export interface EventPerspective {
  id: string
  event_id: string
  country_code: string
  language: string
  viewpoint: string
  source_url: string | null
}

export interface EventMedia {
  id: string
  event_id: string
  media_type: string
  url: string
  caption: Record<string, string>
  credit: string | null
}

export interface EventListItem {
  id: string
  date: string
  date_end: string | null
  date_precision: string
  category: string | null
  tags: string[]
  importance: number
  titles: EventTitle[]
  descriptions: EventDescription[]
  location: EventLocation | null
  source_count: number
}

export interface EventDetail {
  id: string
  date: string
  date_end: string | null
  date_precision: string
  category: string | null
  tags: string[]
  importance: number
  created_at: string
  updated_at: string
  titles: EventTitle[]
  descriptions: EventDescription[]
  location: EventLocation | null
  sources: EventSource[]
  perspectives: EventPerspective[]
  media: EventMedia[]
}

export interface EventListResponse {
  total: number
  limit: number
  offset: number
  events: EventListItem[]
}

export interface GeoJSONFeature {
  type: 'Feature'
  geometry: {
    type: 'Point'
    coordinates: [number, number]
  }
  properties: {
    event_id: string
    title: string
    date: string
    category: string | null
    names: Record<string, string>
  }
}

export interface GeoJSONCollection {
  type: 'FeatureCollection'
  features: GeoJSONFeature[]
}

export const SUPPORTED_LANGS = ['zh_tw', 'en', 'ja', 'ko'] as const
export type SupportedLang = (typeof SUPPORTED_LANGS)[number]

export const LANG_LABELS: Record<SupportedLang, string> = {
  zh_tw: '繁體中文',
  en: 'English',
  ja: '日本語',
  ko: '한국어',
}
