<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { watch } from 'vue'
import { SUPPORTED_LANGS, LANG_LABELS } from '@/types/event'

const { locale } = useI18n()
const router = useRouter()

watch(locale, (val) => {
  localStorage.setItem('locale', val)
})
</script>

<template>
  <header class="app-header">
    <div class="logo" @click="router.push('/')" style="cursor:pointer">
      <span>China</span>Wall
    </div>
    <nav>
      <router-link to="/timeline">{{ $t('nav.timeline') }}</router-link>
      <router-link to="/map">{{ $t('nav.map') }}</router-link>
    </nav>
    <div class="controls">
      <select class="lang-select" v-model="locale">
        <option v-for="l in SUPPORTED_LANGS" :key="l" :value="l">
          {{ LANG_LABELS[l as keyof typeof LANG_LABELS] }}
        </option>
      </select>
    </div>
  </header>
  <main class="app-main">
    <router-view />
  </main>
</template>
