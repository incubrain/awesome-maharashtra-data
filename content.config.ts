import { defineContentConfig, defineCollection } from '@nuxt/content'
import { datasetSchema, categorySchema } from './content.collections'

export default defineContentConfig({
  collections: {
    datasets: defineCollection({
      type: 'data',
      source: 'datasets/**/*.yml',
      schema: datasetSchema,
    }),
    categories: defineCollection({
      type: 'data',
      source: 'categories/*.yml',
      schema: categorySchema,
    }),
  },
})
