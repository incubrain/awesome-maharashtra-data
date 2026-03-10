import { z } from '@nuxt/content'

export const datasetSchema = z.object({
  title: z.string(),
  homepage: z.string(),
  category: z.string(),
  description: z.string(),
  modality: z.string(),
  size: z.string(),
  language: z.array(z.string()),
  license: z.string(),
  ai_use_cases: z.array(z.string()),
  maharashtra_specific: z.boolean().default(true),
  extraction_status: z.enum(['ready', 'subset_needed', 'not_applicable']).optional().default('ready'),
  huggingface_url: z.string().optional().default(''),
  direct_download_url: z.string().optional().default(''),
  paper_url: z.string().optional().default(''),
  github_url: z.string().optional().default(''),
  organization: z.string().optional().default(''),
  format: z.string().optional().default(''),
  update_frequency: z.string().optional().default('static'),
  citation: z.string().optional().default(''),
  last_verified: z.string().optional().default(''),
  schema: z.array(z.object({
    field: z.string(),
    type: z.string(),
    description: z.string().optional().default(''),
  })).optional().default([]),
  starter_idea: z.string().optional().default(''),
  build_ideas: z.array(z.string()).optional().default([]),
  quick_start: z.string().optional().default(''),
})

export const categorySchema = z.object({
  title: z.string(),
  slug: z.string(),
  description: z.string(),
  icon: z.string(),
  priority: z.enum(['high', 'medium', 'low']),
  order: z.number(),
})

export const sotaSchema = z.object({
  category: z.string(),
  title: z.string(),
  last_updated: z.string(),
})
