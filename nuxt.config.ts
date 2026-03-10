export default defineNuxtConfig({
  modules: ['@nuxt/ui', '@nuxt/content', '@nuxt/image'],

  ssr: true,

  app: {
    baseURL: process.env.NUXT_APP_BASE_URL || '/',
    head: {
      title: 'Awesome Marathi Datasets',
      meta: [
        { name: 'description', content: 'The definitive catalog of public-domain datasets for building Marathi & Maharashtra AI infrastructure.' },
      ],
      htmlAttrs: { lang: 'en' },
    },
  },

  css: ['~/assets/css/main.css'],

  content: {
    experimental: {
      sqliteConnector: 'native',
    },
  },

  ui: {
    theme: {
      colors: ['primary', 'secondary', 'neutral', 'info', 'success', 'warning', 'error'],
    },
  },

  icon: {
    serverBundle: {
      collections: ['lucide', 'simple-icons'],
    },
  },

  router: {
    options: {
      scrollBehaviorType: 'smooth',
    },
  },

  nitro: {
    prerender: {
      crawlLinks: true,
      autoSubfolderIndex: false,
      failOnError: true,
    },
  },

  compatibilityDate: '2026-03-07',
})
