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

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
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
