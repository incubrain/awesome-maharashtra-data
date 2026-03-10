<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string

const { data: dataset } = await useAsyncData(`dataset-${slug}`, () =>
  queryCollection('datasets').where('stem', '=', `datasets/${slug}`).first()
)

if (!dataset.value) {
  throw createError({ statusCode: 404, statusMessage: 'Dataset not found' })
}

useSeoMeta({
  title: dataset.value.title,
  description: dataset.value.description,
})

const links = computed(() => {
  const items = []
  if (dataset.value?.homepage) items.push({ label: 'Homepage', icon: 'i-lucide-globe', url: dataset.value.homepage })
  if (dataset.value?.huggingface_url) items.push({ label: 'HuggingFace', icon: 'i-simple-icons-huggingface', url: dataset.value.huggingface_url })
  if (dataset.value?.github_url) items.push({ label: 'GitHub', icon: 'i-simple-icons-github', url: dataset.value.github_url })
  if (dataset.value?.paper_url) items.push({ label: 'Paper', icon: 'i-lucide-file-text', url: dataset.value.paper_url })
  if (dataset.value?.direct_download_url) items.push({ label: 'Download', icon: 'i-lucide-download', url: dataset.value.direct_download_url })
  return items
})

// Related datasets from the same category
const { data: relatedDatasets } = await useAsyncData(`related-${slug}`, () =>
  queryCollection('datasets')
    .where('category', '=', dataset.value!.category)
    .select('stem', 'title', 'modality', 'organization')
    .limit(10)
    .all()
)

const filteredRelated = computed(() =>
  (relatedDatasets.value || [])
    .filter(d => datasetSlug(d.stem) !== slug)
    .slice(0, 4)
)

const copiedCitation = ref(false)
function copyCitation() {
  const text = dataset.value?.citation || `${dataset.value?.title}. ${dataset.value?.organization || ''}. ${dataset.value?.homepage}`
  navigator.clipboard.writeText(text)
  copiedCitation.value = true
  setTimeout(() => { copiedCitation.value = false }, 2000)
}
</script>

<template>
  <UDashboardPanel>
    <template #header>
      <UDashboardNavbar>
        <template #leading>
          <UDashboardSidebarCollapse />
          <UButton
            icon="i-lucide-arrow-left"
            color="neutral"
            variant="ghost"
            size="sm"
            to="/datasets"
            class="mr-2"
          />
          <span class="font-semibold truncate">{{ dataset?.title }}</span>
        </template>
      </UDashboardNavbar>
    </template>

    <template #body>
      <div v-if="dataset" class="max-w-3xl mx-auto p-6 flex flex-col gap-6">
        <!-- Header -->
        <div>
          <div class="flex items-center gap-2 mb-2">
            <h1 class="text-2xl font-bold text-(--ui-text-highlighted)">{{ dataset.title }}</h1>
            <UBadge v-if="dataset.maharashtra_specific" color="primary" variant="subtle">MH Specific</UBadge>
            <UBadge v-if="dataset.extraction_status === 'subset_needed'" color="warning" variant="subtle">
              <UIcon name="i-lucide-scissors" class="size-3 mr-1" />
              MH Subset Needed
            </UBadge>
          </div>
          <p class="text-(--ui-text-muted) text-lg">{{ dataset.description }}</p>

          <!-- Starter idea -->
          <div v-if="dataset.starter_idea" class="mt-3 flex items-center gap-2 text-sm">
            <UIcon name="i-lucide-lightbulb" class="size-4 text-(--ui-primary) shrink-0" />
            <span class="text-(--ui-text-muted) italic">{{ dataset.starter_idea }}</span>
          </div>

          <!-- Extraction notice -->
          <div v-if="dataset.extraction_status === 'subset_needed'" class="bg-amber-500/10 border border-amber-500/20 rounded-lg p-4 mt-3">
            <div class="flex items-start gap-2">
              <UIcon name="i-lucide-info" class="size-5 text-amber-500 mt-0.5 shrink-0" />
              <div class="text-sm text-(--ui-text-muted)">
                <span class="font-medium text-(--ui-text-highlighted)">Maharashtra subset not yet extracted.</span>
                This is a global dataset that contains data covering Maharashtra. A regional subset can be extracted
                by filtering on geographic coordinates or administrative boundaries.
              </div>
            </div>
          </div>
        </div>

        <!-- Links -->
        <div class="flex flex-wrap gap-2">
          <UButton
            v-for="link in links"
            :key="link.label"
            :icon="link.icon"
            :to="link.url"
            target="_blank"
            color="neutral"
            variant="subtle"
          >
            {{ link.label }}
          </UButton>
          <UButton
            icon="i-lucide-quote"
            color="neutral"
            variant="subtle"
            @click="copyCitation"
          >
            {{ copiedCitation ? 'Copied!' : 'Copy Citation' }}
          </UButton>
        </div>

        <!-- Quick Start -->
        <div v-if="dataset.quick_start">
          <h2 class="text-lg font-semibold text-(--ui-text-highlighted) mb-3">Quick Start</h2>
          <pre class="bg-(--ui-bg-elevated) border border-(--ui-border) rounded-lg p-4 text-sm font-mono overflow-x-auto whitespace-pre-wrap"><code>{{ dataset.quick_start.trim() }}</code></pre>
        </div>

        <!-- Metadata Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <div class="text-xs text-(--ui-text-dimmed) mb-1">Modality</div>
            <div class="font-medium">{{ dataset.modality }}</div>
          </div>
          <div class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <div class="text-xs text-(--ui-text-dimmed) mb-1">Size</div>
            <div class="font-medium">{{ dataset.size }}</div>
          </div>
          <div class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <div class="text-xs text-(--ui-text-dimmed) mb-1">License</div>
            <div class="font-medium">
              <LicenseBadge :license="dataset.license" size="sm" />
            </div>
          </div>
          <div class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <div class="text-xs text-(--ui-text-dimmed) mb-1">Format</div>
            <div class="font-medium">{{ dataset.format || 'Not specified' }}</div>
          </div>
          <div class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <div class="text-xs text-(--ui-text-dimmed) mb-1">Language</div>
            <div class="font-medium">{{ dataset.language.join(', ') }}</div>
          </div>
          <div class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <div class="text-xs text-(--ui-text-dimmed) mb-1">Update Frequency</div>
            <div class="font-medium">{{ dataset.update_frequency || 'Static' }}</div>
          </div>
          <div v-if="dataset.organization" class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <div class="text-xs text-(--ui-text-dimmed) mb-1">Organization</div>
            <div class="font-medium">{{ dataset.organization }}</div>
          </div>
          <div class="bg-(--ui-bg-elevated) rounded-lg p-4">
            <NuxtLink :to="`/categories/${dataset.category}`" class="block">
              <div class="text-xs text-(--ui-text-dimmed) mb-1">Category</div>
              <div class="font-medium text-(--ui-primary) hover:underline">{{ dataset.category }}</div>
            </NuxtLink>
          </div>
        </div>

        <!-- Schema -->
        <div v-if="dataset.schema?.length">
          <h2 class="text-lg font-semibold text-(--ui-text-highlighted) mb-3">Schema</h2>
          <div class="border border-(--ui-border) rounded-lg overflow-hidden">
            <table class="w-full text-sm">
              <thead>
                <tr class="bg-(--ui-bg-elevated)">
                  <th class="text-left px-4 py-2 font-medium text-(--ui-text-dimmed)">Field</th>
                  <th class="text-left px-4 py-2 font-medium text-(--ui-text-dimmed)">Type</th>
                  <th class="text-left px-4 py-2 font-medium text-(--ui-text-dimmed)">Description</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="col in dataset.schema" :key="col.field" class="border-t border-(--ui-border)">
                  <td class="px-4 py-2 font-mono text-xs text-(--ui-primary)">{{ col.field }}</td>
                  <td class="px-4 py-2 text-xs text-(--ui-text-muted)">{{ col.type }}</td>
                  <td class="px-4 py-2 text-(--ui-text-muted)">{{ col.description }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Build Ideas -->
        <div v-if="dataset.build_ideas?.length">
          <h2 class="text-lg font-semibold text-(--ui-text-highlighted) mb-3">Build With This</h2>
          <div class="flex flex-col gap-2">
            <div
              v-for="idea in dataset.build_ideas"
              :key="idea"
              class="flex items-start gap-2 bg-(--ui-bg-elevated) rounded-lg p-3"
            >
              <UIcon name="i-lucide-rocket" class="size-4 text-(--ui-primary) mt-0.5 shrink-0" />
              <span class="text-sm">{{ idea }}</span>
            </div>
          </div>
        </div>

        <!-- AI Use Cases -->
        <div v-if="dataset.ai_use_cases?.length">
          <h2 class="text-lg font-semibold text-(--ui-text-highlighted) mb-3">AI Use Cases</h2>
          <div class="flex flex-wrap gap-2">
            <UBadge
              v-for="useCase in dataset.ai_use_cases"
              :key="useCase"
              color="primary"
              variant="subtle"
              size="md"
            >
              {{ useCase }}
            </UBadge>
          </div>
        </div>

        <!-- Related Datasets -->
        <div v-if="filteredRelated.length">
          <h2 class="text-lg font-semibold text-(--ui-text-highlighted) mb-3">Related Datasets</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <NuxtLink
              v-for="rel in filteredRelated"
              :key="rel.stem"
              :to="`/datasets/${datasetSlug(rel.stem)}`"
              class="flex items-center gap-3 bg-(--ui-bg-elevated) rounded-lg p-3 hover:ring-1 hover:ring-(--ui-primary)/50 transition-all"
            >
              <UIcon name="i-lucide-database" class="size-4 text-(--ui-text-dimmed) shrink-0" />
              <div class="min-w-0">
                <div class="text-sm font-medium text-(--ui-text-highlighted) truncate">{{ rel.title }}</div>
                <div class="text-xs text-(--ui-text-dimmed)">{{ rel.modality }}</div>
              </div>
            </NuxtLink>
          </div>
        </div>

        <!-- Last Verified -->
        <div v-if="dataset.last_verified" class="text-sm text-(--ui-text-dimmed)">
          Last verified: {{ dataset.last_verified }}
        </div>
      </div>
    </template>
  </UDashboardPanel>
</template>
