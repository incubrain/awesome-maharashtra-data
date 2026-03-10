<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string

const { data: category } = await useAsyncData(`category-${slug}`, () =>
  queryCollection('categories').where('slug', '=', slug).first()
)

if (!category.value) {
  throw createError({ statusCode: 404, statusMessage: 'Category not found' })
}

const { data: datasets } = await useAsyncData(`datasets-cat-${slug}`, () =>
  queryCollection('datasets').where('category', '=', slug).all()
)

const { data: sota } = await useAsyncData(`sota-${slug}`, () =>
  queryCollection('sota').where('category', '=', slug).first()
)

const hasSota = computed(() => !!sota.value)

const tabItems = computed(() => {
  const items: { label: string; icon: string; slot: string; value: string }[] = [
    { label: 'Datasets', icon: 'i-lucide-database', slot: 'datasets', value: 'datasets' },
  ]
  if (hasSota.value) {
    items.push({ label: 'SOTA Research', icon: 'i-lucide-flask-conical', slot: 'sota', value: 'sota' })
  }
  return items
})

useSeoMeta({
  title: category.value.title,
  description: category.value.description,
})
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
            to="/"
            class="mr-2"
          />
          <UIcon v-if="category" :name="category.icon" class="size-5 text-(--ui-primary) mr-2" />
          <span class="font-semibold truncate">{{ category?.title }}</span>
        </template>
      </UDashboardNavbar>
    </template>

    <template #body>
      <div v-if="category" class="flex flex-col gap-4 p-4">
        <div class="mb-2">
          <p class="text-(--ui-text-muted)">{{ category.description }}</p>
          <p class="text-sm text-(--ui-text-dimmed) mt-1">{{ datasets?.length || 0 }} datasets</p>
        </div>

        <!-- Show tabs only when SOTA research exists -->
        <UTabs v-if="hasSota" :items="tabItems" class="w-full">
          <template #datasets>
            <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 pt-4">
              <DatasetCard
                v-for="dataset in datasets"
                :key="dataset.stem"
                :dataset="dataset"
              />
            </div>
          </template>

          <template #sota>
            <div v-if="sota" class="pt-4">
              <div class="flex items-center gap-2 mb-4">
                <UBadge color="primary" variant="subtle" size="sm">
                  Last updated: {{ sota.last_updated }}
                </UBadge>
              </div>
              <div class="prose prose-sm dark:prose-invert max-w-none">
                <ContentRenderer :value="sota" />
              </div>
            </div>
          </template>
        </UTabs>

        <!-- No SOTA: show datasets directly (same as before) -->
        <div v-else class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
          <DatasetCard
            v-for="dataset in datasets"
            :key="dataset.stem"
            :dataset="dataset"
          />
        </div>
      </div>
    </template>
  </UDashboardPanel>
</template>
