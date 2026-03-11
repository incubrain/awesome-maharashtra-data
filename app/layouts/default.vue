<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const { data: categories } = await useAsyncData('nav-categories', () =>
  queryCollection('categories').order('order', 'ASC').all()
)

const { data: allDatasets } = await useAsyncData('nav-datasets', () =>
  queryCollection('datasets').select('stem', 'title', 'description', 'category', 'ai_use_cases').all()
)

function getCategoryCount(slug: string) {
  return allDatasets.value?.filter(d => d.category === slug).length || 0
}

const categoryNavItems = computed<NavigationMenuItem[]>(() =>
  (categories.value || []).map(cat => ({
    label: cat.title,
    icon: cat.icon,
    to: `/categories/${cat.slug}`,
    badge: String(getCategoryCount(cat.slug)),
  }))
)

const mainNavItems: NavigationMenuItem[] = [
  { label: 'Home', icon: 'i-lucide-home', to: '/' },
  { label: 'Data Gaps', icon: 'i-lucide-search-x', to: '/gaps' },
]

const searchGroups = computed(() => [{
  id: 'datasets',
  label: 'Datasets',
  items: (allDatasets.value || []).map(d => ({
    label: d.title,
    suffix: d.category,
    to: `/datasets/${datasetSlug(d.stem)}`,
    icon: 'i-lucide-database',
  })),
}])
</script>

<template>
  <UDashboardGroup>
    <UDashboardSidebar collapsible resizable>
      <template #header="{ collapsed }">
        <NuxtLink to="/" class="flex items-center gap-2 px-1">
          <UIcon name="i-lucide-database" class="size-6 text-(--ui-primary) shrink-0" />
          <span v-if="!collapsed" class="font-semibold text-sm truncate">Marathi Datasets</span>
        </NuxtLink>
      </template>

      <template #default="{ collapsed }">
        <UDashboardSearchButton :collapsed="collapsed" />
        <UNavigationMenu :collapsed="collapsed" :items="mainNavItems" orientation="vertical" />
        <UDivider />
        <UNavigationMenu :collapsed="collapsed" :items="categoryNavItems" orientation="vertical" />
      </template>

      <template #footer="{ collapsed }">
        <div class="flex items-center" :class="collapsed ? 'justify-center' : 'justify-between px-2'">
          <UColorModeButton />
          <UButton
            v-if="!collapsed"
            icon="i-lucide-message-square-plus"
            color="neutral"
            variant="ghost"
            to="https://github.com/awesome-marathi-datasets/awesome-marathi-datasets/issues/new?template=dataset_request.md&title=%5BDataset+Request%5D+"
            target="_blank"
            aria-label="Request a dataset"
          />
        </div>
      </template>
    </UDashboardSidebar>

    <UDashboardSearch :groups="searchGroups" />

    <slot />
  </UDashboardGroup>
</template>
