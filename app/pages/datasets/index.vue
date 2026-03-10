<script setup lang="ts">
useSeoMeta({
  title: 'All Datasets',
  description: 'Browse all Marathi and Maharashtra datasets for AI and ML.',
})

const { data: datasets } = await useAsyncData('datasets-all', () =>
  queryCollection('datasets').all()
)

const { data: categories } = await useAsyncData('datasets-categories', () =>
  queryCollection('categories').order('order', 'ASC').all()
)

const selectedCategory = ref('')
const selectedModality = ref('')
const selectedLicense = ref('')
const selectedStatus = ref('')
const searchQuery = ref('')

const categoryNames = computed(() =>
  (categories.value || []).map(c => c.slug)
)

const modalityOptions = computed(() =>
  [...new Set(datasets.value?.map(d => d.modality))].sort()
)

const licenseOptions = computed(() =>
  [...new Set(datasets.value?.map(d => d.license))].sort()
)

const filteredDatasets = computed(() => {
  return (datasets.value || []).filter(d => {
    if (selectedCategory.value && d.category !== selectedCategory.value) return false
    if (selectedModality.value && d.modality !== selectedModality.value) return false
    if (selectedLicense.value && d.license !== selectedLicense.value) return false
    if (selectedStatus.value === 'ready' && d.extraction_status !== 'ready') return false
    if (selectedStatus.value === 'subset_needed' && d.extraction_status !== 'subset_needed') return false
    if (searchQuery.value) {
      const q = searchQuery.value.toLowerCase()
      return d.title.toLowerCase().includes(q)
        || d.description.toLowerCase().includes(q)
        || (d.organization || '').toLowerCase().includes(q)
        || (d.ai_use_cases || []).some(u => u.toLowerCase().includes(q))
        || (d.build_ideas || []).some(b => b.toLowerCase().includes(q))
        || (d.starter_idea || '').toLowerCase().includes(q)
    }
    return true
  })
})

function clearFilters() {
  selectedCategory.value = ''
  selectedModality.value = ''
  selectedLicense.value = ''
  selectedStatus.value = ''
  searchQuery.value = ''
}
</script>

<template>
  <UDashboardPanel>
    <template #header>
      <UDashboardNavbar :title="`All Datasets (${filteredDatasets.length})`">
        <template #leading>
          <UDashboardSidebarCollapse />
        </template>
      </UDashboardNavbar>
    </template>

    <template #body>
      <div class="flex flex-col gap-4 p-4">
        <div class="flex flex-col sm:flex-row gap-2 w-full">
          <UInput
            v-model="searchQuery"
            icon="i-lucide-search"
            placeholder="Search datasets, use cases, ideas..."
            class="flex-1"
          />
          <USelectMenu
            v-model="selectedCategory"
            :items="[{ label: 'All Categories', value: '' }, ...categoryNames.map(c => ({ label: c, value: c }))]"
            class="w-full sm:w-48"
          />
          <USelectMenu
            v-model="selectedModality"
            :items="[{ label: 'All Modalities', value: '' }, ...modalityOptions.map(m => ({ label: m, value: m }))]"
            class="w-full sm:w-40"
          />
          <USelectMenu
            v-model="selectedStatus"
            :items="[{ label: 'All Status', value: '' }, { label: 'Ready to use', value: 'ready' }, { label: 'MH subset needed', value: 'subset_needed' }]"
            class="w-full sm:w-44"
          />
        </div>

        <div v-if="filteredDatasets.length" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
          <DatasetCard
            v-for="dataset in filteredDatasets"
            :key="dataset.stem"
            :dataset="dataset"
          />
        </div>

        <div v-else class="text-center py-12 text-(--ui-text-muted)">
          <UIcon name="i-lucide-search-x" class="size-12 mx-auto mb-3 opacity-50" />
          <p>No datasets match your filters.</p>
          <UButton
            class="mt-3"
            variant="outline"
            color="neutral"
            @click="clearFilters"
          >
            Clear filters
          </UButton>
        </div>
      </div>
    </template>
  </UDashboardPanel>
</template>
