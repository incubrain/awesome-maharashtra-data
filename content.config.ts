import { defineContentConfig, defineCollection } from '@nuxt/content'
import { datasetSchema, categorySchema, sotaSchema } from './content.collections'

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
    sota: defineCollection({
      type: 'page',
      source: 'sota/**/*.md',
      schema: sotaSchema,
    }),
  },
})
