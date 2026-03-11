<script setup lang="ts">
useSeoMeta({
  title: 'Home',
  description: 'The definitive catalog of public-domain datasets for building Marathi & Maharashtra AI infrastructure.',
})

const { data: allDatasets } = await useAsyncData('home-datasets', () =>
  queryCollection('datasets').all()
)

const { data: categories } = await useAsyncData('home-categories', () =>
  queryCollection('categories').order('order', 'ASC').all()
)

const totalDatasets = computed(() => allDatasets.value?.length || 0)
const totalCategories = computed(() => categories.value?.length || 0)

function getCategoryCount(slug: string) {
  return allDatasets.value?.filter(d => d.category === slug).length || 0
}

// Top 3 missing gaps for the teaser
const topGaps = computed(() =>
  DATA_GAPS.filter(g => g.status === 'missing').slice(0, 3)
)
</script>

<template>
  <UDashboardPanel>
    <template #header>
      <UDashboardNavbar title="Awesome Marathi Datasets">
        <template #leading>
          <UDashboardSidebarCollapse />
        </template>
      </UDashboardNavbar>
    </template>

    <template #body>
      <div class="flex flex-col gap-8 p-6">
        <!-- Hero -->
        <div class="text-center max-w-2xl mx-auto">
          <h1 class="text-3xl font-bold text-(--ui-text-highlighted) mb-3">
            Discover Marathi & Maharashtra Datasets
          </h1>
          <p class="text-(--ui-text-muted) text-lg mb-2">
            {{ totalDatasets }} datasets across {{ totalCategories }} categories.
            Find data, spark ideas, and start building.
          </p>
          <div class="flex justify-center gap-3 mt-4">
            <UButton
              to="/gaps"
              size="lg"
              color="neutral"
              variant="outline"
              icon="i-lucide-search-x"
            >
              What's Missing
            </UButton>
          </div>
        </div>

        <!-- Categories Grid -->
        <div>
          <h2 class="text-xl font-semibold text-(--ui-text-highlighted) mb-4">Browse by Category</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <CategoryCard
              v-for="cat in categories"
              :key="cat.slug"
              :category="cat"
              :count="getCategoryCount(cat.slug)"
            />
          </div>
        </div>

        <!-- Data Gaps Teaser -->
        <div>
          <div class="flex items-center justify-between mb-4">
            <h2 class="text-xl font-semibold text-(--ui-text-highlighted)">Biggest Opportunities</h2>
            <UButton to="/gaps" variant="link" trailing-icon="i-lucide-arrow-right" size="sm">
              View all gaps
            </UButton>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div
              v-for="gap in topGaps"
              :key="gap.area"
              class="border border-(--ui-border) rounded-lg p-4"
            >
              <div class="flex items-center gap-2 mb-2">
                <UIcon name="i-lucide-circle-x" class="text-red-500 size-4 shrink-0" />
                <span class="font-medium text-sm text-(--ui-text-highlighted)">{{ gap.area }}</span>
              </div>
              <p class="text-xs text-(--ui-text-muted) mb-2">{{ gap.opportunity }}</p>
              <NuxtLink :to="`/categories/${gap.category}`">
                <UBadge color="neutral" variant="outline" size="xs" class="cursor-pointer">
                  {{ gap.category }}
                </UBadge>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </template>
  </UDashboardPanel>
</template>
