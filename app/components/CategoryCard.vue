<script setup lang="ts">
defineProps<{
  category: {
    title: string
    slug: string
    description: string
    icon: string
    order: number
  }
  count: number
}>()
</script>

<template>
  <NuxtLink :to="`/categories/${category.slug}`" class="block">
    <UCard class="hover:ring-(--ui-primary)/50 transition-shadow cursor-pointer h-full">
      <div class="flex flex-col gap-3">
        <div class="flex items-center gap-3">
          <div class="flex items-center justify-center size-10 rounded-lg bg-(--ui-bg-elevated)">
            <UIcon :name="category.icon" class="size-5 text-(--ui-primary)" />
          </div>
          <div class="min-w-0">
            <h3 class="font-semibold text-sm text-(--ui-text-highlighted) truncate">{{ category.title }}</h3>
            <p class="text-xs text-(--ui-text-dimmed)">{{ count }} datasets</p>
          </div>
        </div>
        <p class="text-sm text-(--ui-text-muted) line-clamp-2">{{ category.description }}</p>
      </div>
    </UCard>
  </NuxtLink>
</template>
