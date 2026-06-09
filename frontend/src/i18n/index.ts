import { createI18n } from 'vue-i18n'
import zh_TW from './locales/zh_tw'
import en from './locales/en'
import ja from './locales/ja'
import ko from './locales/ko'

const messages = { zh_tw: zh_TW, en, ja, ko }

const i18n = createI18n({
  legacy: false,
  locale: localStorage.getItem('locale') || 'en',
  fallbackLocale: 'en',
  messages,
})

export default i18n
