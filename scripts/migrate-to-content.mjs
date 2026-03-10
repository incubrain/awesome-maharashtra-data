#!/usr/bin/env node
/**
 * Migration script: Convert existing data_cards/*.yaml and categories/*.md
 * into content/datasets/*.yml files for Nuxt Content.
 */

import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync } from 'fs'
import { join, basename } from 'path'

const ROOT = join(import.meta.dirname, '..')
const DATA_CARDS_DIR = join(ROOT, 'data_cards')
const CATEGORIES_DIR = join(ROOT, 'categories')
const OUTPUT_DIR = join(ROOT, 'content', 'datasets')

if (!existsSync(OUTPUT_DIR)) mkdirSync(OUTPUT_DIR, { recursive: true })

// Category file slug mapping
const CATEGORY_MAP = {
  '01-language-nlp': 'language-nlp',
  '02-speech-audio': 'speech-audio',
  '03-vision-ocr-multimodal': 'vision-ocr-multimodal',
  '04-geospatial-gis': 'geospatial-gis',
  '05-agriculture-rural': 'agriculture-rural',
  '06-health-nutrition': 'health-nutrition',
  '07-education-skills': 'education-skills',
  '08-economy-labour-finance': 'economy-labour-finance',
  '09-environment-climate-disaster': 'environment-climate-disaster',
  '10-transport-urban-infrastructure': 'transport-urban-infrastructure',
  '11-governance-census-demographics-legal': 'governance-census-demographics-legal',
  '12-culture-media-tourism-heritage': 'culture-media-tourism-heritage',
  '13-realtime-streams-apis': 'realtime-streams-apis',
  '14-agentic-instruction-rag': 'agentic-instruction-rag',
  '15-benchmarks-fairness-dialects-tools': 'benchmarks-fairness-dialects-tools',
}

// Default language guesses by category
const LANGUAGE_DEFAULTS = {
  'language-nlp': ['mr'],
  'speech-audio': ['mr'],
  'vision-ocr-multimodal': ['mr'],
  'geospatial-gis': ['en'],
  'agriculture-rural': ['en'],
  'health-nutrition': ['en'],
  'education-skills': ['en'],
  'economy-labour-finance': ['en'],
  'environment-climate-disaster': ['en'],
  'transport-urban-infrastructure': ['en'],
  'governance-census-demographics-legal': ['en', 'mr'],
  'culture-media-tourism-heritage': ['mr'],
  'realtime-streams-apis': ['en'],
  'agentic-instruction-rag': ['mr'],
  'benchmarks-fairness-dialects-tools': ['mr'],
}

function slugify(name) {
  return name
    .toLowerCase()
    .replace(/[()]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .substring(0, 80)
}

function escapeYaml(str) {
  if (!str) return '""'
  // Escape strings that contain special YAML characters
  if (str.includes(':') || str.includes('#') || str.includes('"') || str.includes("'") ||
      str.includes('{') || str.includes('}') || str.includes('[') || str.includes(']') ||
      str.includes('*') || str.includes('&') || str.includes('!') || str.includes('|') ||
      str.includes('>') || str.includes('%') || str.includes('@') || str.includes('`') ||
      str.startsWith(' ') || str.endsWith(' ')) {
    return `"${str.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`
  }
  return str
}

function writeDatasetYml(slug, data) {
  const lines = []
  lines.push(`title: ${escapeYaml(data.title)}`)
  lines.push(`homepage: ${escapeYaml(data.homepage)}`)
  lines.push(`category: ${escapeYaml(data.category)}`)
  lines.push(`description: ${escapeYaml(data.description)}`)
  lines.push(`modality: ${escapeYaml(data.modality)}`)
  lines.push(`size: ${escapeYaml(data.size)}`)
  lines.push(`language:`)
  for (const lang of data.language || ['mr']) {
    lines.push(`  - ${lang}`)
  }
  lines.push(`license: ${escapeYaml(data.license)}`)
  lines.push(`ai_use_cases:`)
  for (const uc of data.ai_use_cases || ['General ML']) {
    lines.push(`  - ${escapeYaml(uc)}`)
  }
  lines.push(`maharashtra_specific: ${data.maharashtra_specific ?? true}`)
  lines.push(`huggingface_url: ${escapeYaml(data.huggingface_url || '')}`)
  lines.push(`direct_download_url: ${escapeYaml(data.direct_download_url || '')}`)
  lines.push(`paper_url: ${escapeYaml(data.paper_url || '')}`)
  lines.push(`github_url: ${escapeYaml(data.github_url || '')}`)
  lines.push(`organization: ${escapeYaml(data.organization || '')}`)
  lines.push(`format: ${escapeYaml(data.format || '')}`)
  lines.push(`update_frequency: ${escapeYaml(data.update_frequency || 'static')}`)
  lines.push(`citation: ""`)
  lines.push(`last_verified: "2026-03-07"`)
  lines.push('')

  const outPath = join(OUTPUT_DIR, `${slug}.yml`)
  writeFileSync(outPath, lines.join('\n'), 'utf-8')
  return outPath
}

// ── Phase 1: Migrate existing data cards ──────────────────────────────────────

const existingSlugs = new Set()

console.log('=== Phase 1: Migrating existing YAML data cards ===')

const dataCardFiles = readdirSync(DATA_CARDS_DIR).filter(f => f.endsWith('.yaml') && !f.startsWith('_'))

for (const file of dataCardFiles) {
  const content = readFileSync(join(DATA_CARDS_DIR, file), 'utf-8')

  // Simple YAML parser for our known format (strip comments, parse key: value)
  const data = {}
  const lines = content.split('\n').filter(l => !l.startsWith('#') && !l.startsWith('---') && l.trim())

  let currentKey = null
  let currentArray = null

  for (const line of lines) {
    const trimmed = line.trim()

    // Array item
    if (trimmed.startsWith('- ') && currentKey) {
      if (!currentArray) currentArray = []
      let val = trimmed.slice(2).trim()
      if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1)
      if (val) currentArray.push(val)
      continue
    }

    // Save previous array
    if (currentArray && currentKey) {
      data[currentKey] = currentArray
      currentArray = null
    }

    // Key: value pair
    const colonIdx = trimmed.indexOf(':')
    if (colonIdx > 0) {
      const key = trimmed.substring(0, colonIdx).trim()
      let val = trimmed.substring(colonIdx + 1).trim()

      if (val === '') {
        // Might be start of array
        currentKey = key
        currentArray = []
        continue
      }

      // Remove quotes
      if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1)

      // Handle booleans
      if (val === 'true') val = true
      else if (val === 'false') val = false

      data[key] = val
      currentKey = key
    }
  }

  // Save last array
  if (currentArray && currentKey) {
    data[currentKey] = currentArray
  }

  // Ensure language is an array
  if (data.language && !Array.isArray(data.language)) {
    data.language = [data.language]
  }

  const slug = basename(file, '.yaml')
  existingSlugs.add(slug)

  writeDatasetYml(slug, data)
  console.log(`  ✓ ${slug}`)
}

console.log(`\nMigrated ${dataCardFiles.length} existing data cards.\n`)

// ── Phase 2: Parse category markdown tables ───────────────────────────────────

console.log('=== Phase 2: Parsing category markdown tables ===')

let totalFromMd = 0

const categoryFiles = readdirSync(CATEGORIES_DIR).filter(f => f.endsWith('.md')).sort()

for (const file of categoryFiles) {
  const catKey = basename(file, '.md')
  const categorySlug = CATEGORY_MAP[catKey]
  if (!categorySlug) {
    console.log(`  ⚠ Unknown category file: ${file}`)
    continue
  }

  const content = readFileSync(join(CATEGORIES_DIR, file), 'utf-8')
  const lines = content.split('\n')

  // Find table rows (lines starting with |, skip header and separator)
  const tableRows = lines.filter(l => l.startsWith('|') && !l.startsWith('|--') && !l.startsWith('| Dataset') && !l.startsWith('|--'))

  // Skip header row (first | row) and separator row
  let dataRows = []
  let headerFound = false
  let separatorFound = false

  for (const line of lines) {
    if (!line.startsWith('|')) continue
    if (!headerFound) {
      headerFound = true
      continue
    }
    if (!separatorFound) {
      separatorFound = true
      continue
    }
    dataRows.push(line)
  }

  let catCount = 0

  for (const row of dataRows) {
    // Split by | and trim
    const cells = row.split('|').map(c => c.trim()).filter(c => c)
    if (cells.length < 5) continue

    // Format: Dataset | Size | License | Modality | Links | AI Use Case
    const rawName = cells[0]
    const size = cells[1] || ''
    const license = cells[2] || ''
    const modality = cells[3] || ''
    const linksCell = cells[4] || ''
    const aiUseCase = cells[5] || ''

    // Extract name and description from dataset cell
    // Patterns: "**Name** --- description" or "Name --- description" or just "Name"
    let name = rawName
    let description = ''

    // Remove bold markers
    name = name.replace(/\*\*/g, '')

    // Split on em dash variants
    const dashIdx = name.indexOf(' --- ')
    if (dashIdx > 0) {
      description = name.substring(dashIdx + 5).trim()
      name = name.substring(0, dashIdx).trim()
    } else {
      const emdashIdx = name.indexOf(' — ')
      if (emdashIdx > 0) {
        description = name.substring(emdashIdx + 3).trim()
        name = name.substring(0, emdashIdx).trim()
      }
    }

    // Remove trailing period from description
    if (description.endsWith('.')) description = description.slice(0, -1)

    if (!name || name === 'Dataset') continue

    // Extract links
    let homepage = ''
    let huggingfaceUrl = ''
    let githubUrl = ''

    const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g
    let match
    while ((match = linkRegex.exec(linksCell)) !== null) {
      const label = match[1].toLowerCase()
      const url = match[2]

      if (label.includes('huggingface') || label.includes('hf') || url.includes('huggingface.co')) {
        huggingfaceUrl = url
        if (!homepage) homepage = url
      } else if (label.includes('github') || url.includes('github.com')) {
        githubUrl = url
        if (!homepage) homepage = url
      } else {
        if (!homepage) homepage = url
      }
    }

    // Fallback homepage
    if (!homepage) homepage = 'https://data.gov.in'

    // Generate slug
    const slug = slugify(name)

    // Skip if we already have this from data cards
    if (existingSlugs.has(slug)) {
      continue
    }

    // Parse AI use cases
    const useCases = aiUseCase
      .split(/[;,]/)
      .map(s => s.trim())
      .filter(s => s && s !== 'AI Use Case')

    // Determine if Maharashtra-specific
    const lowerDesc = (description + ' ' + name).toLowerCase()
    const isMH = lowerDesc.includes('maharashtra') || lowerDesc.includes('marathi') ||
                 lowerDesc.includes('mh ') || lowerDesc.includes('pune') ||
                 lowerDesc.includes('mumbai') || categorySlug.includes('language') ||
                 categorySlug.includes('speech')

    const defaultLangs = LANGUAGE_DEFAULTS[categorySlug] || ['en']

    writeDatasetYml(slug, {
      title: name,
      homepage,
      category: categorySlug,
      description: description || `${name} dataset for ${categorySlug.replace(/-/g, ' ')}.`,
      modality,
      size,
      language: defaultLangs,
      license,
      ai_use_cases: useCases.length > 0 ? useCases : ['General ML/AI'],
      maharashtra_specific: isMH,
      huggingface_url: huggingfaceUrl,
      github_url: githubUrl,
      organization: '',
      format: '',
      update_frequency: 'static',
    })

    existingSlugs.add(slug)
    catCount++
  }

  totalFromMd += catCount
  console.log(`  ✓ ${catKey}: ${catCount} new datasets`)
}

console.log(`\nExtracted ${totalFromMd} datasets from markdown tables.`)
console.log(`\nTotal dataset files: ${existingSlugs.size}`)
