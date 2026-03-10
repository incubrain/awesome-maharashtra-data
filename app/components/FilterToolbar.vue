<script setup lang="ts">
const props = defineProps<{
  categories: string[]
  modalities: string[]
  licenses: string[]
}>()

const selectedCategory = defineModel<string>('category', { default: '' })
const selectedModality = defineModel<string>('modality', { default: '' })
const selectedLicense = defineModel<string>('license', { default: '' })
const searchQuery = defineModel<string>('search', { default: '' })

const categoryOptions = computed(() => [
  { label: 'All Categories', value: '' },
  ...props.categories.map(c => ({ label: c, value: c })),
])

const modalityOptions = computed(() => [
  { label: 'All Modalities', value: '' },
  ...props.modalities.map(m => ({ label: m, value: m })),
])

const licenseOptions = computed(() => [
  { label: 'All Licenses', value: '' },
  ...props.licenses.map(l => ({ label: l, value: l })),
])
</script>

<template>
  <div class="flex flex-col sm:flex-row gap-2 w-full">
    <UInput
      v-model="searchQuery"
      icon="i-lucide-search"
      placeholder="Search datasets..."
      class="flex-1"
    />
    <USelectMenu
      v-model="selectedCategory"
      :items="categoryOptions"
      class="w-full sm:w-48"
    />
    <USelectMenu
      v-model="selectedModality"
      :items="modalityOptions"
      class="w-full sm:w-40"
    />
    <USelectMenu
      v-model="selectedLicense"
      :items="licenseOptions"
      class="w-full sm:w-44"
    />
  </div>
</template>
