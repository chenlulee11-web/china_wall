import { describe, it, expect } from 'vitest'

describe('i18n messages', () => {
  it('zh_tw has required keys', async () => {
    const messages = await import('@/i18n/locales/zh_tw')
    expect(messages.default.nav.timeline).toBe('時間軸')
    expect(messages.default.nav.map).toBe('地圖')
    expect(messages.default.timeline.title).toBeTruthy()
  })

  it('en has required keys', async () => {
    const messages = await import('@/i18n/locales/en')
    expect(messages.default.nav.timeline).toBe('Timeline')
    expect(messages.default.nav.map).toBe('Map')
    expect(messages.default.stats.title).toBeTruthy()
  })

  it('all locales have same structure', async () => {
    const en = (await import('@/i18n/locales/en')).default
    const ja = (await import('@/i18n/locales/ja')).default
    const ko = (await import('@/i18n/locales/ko')).default
    const zh = (await import('@/i18n/locales/zh_tw')).default

    const getKeys = (obj: Record<string, unknown>, prefix = ''): string[] => {
      return Object.entries(obj).flatMap(([k, v]) =>
        typeof v === 'object' && v !== null
          ? getKeys(v as Record<string, unknown>, `${prefix}${k}.`)
          : [`${prefix}${k}`]
      )
    }

    const enKeys = new Set(getKeys(en))
    const jaKeys = new Set(getKeys(ja))
    const koKeys = new Set(getKeys(ko))
    const zhKeys = new Set(getKeys(zh))

    expect(enKeys.size).toBe(jaKeys.size)
    expect(enKeys.size).toBe(koKeys.size)
    expect(enKeys.size).toBe(zhKeys.size)

    const missingInJA = [...enKeys].filter(k => !jaKeys.has(k))
    const missingInKO = [...enKeys].filter(k => !koKeys.has(k))
    const missingInZH = [...enKeys].filter(k => !zhKeys.has(k))

    expect(missingInJA).toEqual([])
    expect(missingInKO).toEqual([])
    expect(missingInZH).toEqual([])
  })
})

describe('event types', () => {
  it('SUPPORTED_LANGS is defined', async () => {
    const types = await import('@/types/event')
    expect(types.SUPPORTED_LANGS).toContain('en')
    expect(types.SUPPORTED_LANGS).toContain('zh_tw')
    expect(types.SUPPORTED_LANGS).toContain('ja')
    expect(types.SUPPORTED_LANGS).toContain('ko')
  })
})
