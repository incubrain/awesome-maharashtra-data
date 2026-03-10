<script setup lang="ts">
defineProps<{
  dataset: {
    stem: string
    title: string
    description: string
    modality: string
    license: string
    organization?: string
    homepage: string
    huggingface_url?: string
    github_url?: string
    maharashtra_specific?: boolean
    extraction_status?: string
    starter_idea?: string
  }
}>()
</script>

<template>
  <UCard class="hover:ring-(--ui-primary)/50 transition-shadow">
    <div class="flex flex-col gap-3">
      <div class="flex items-start justify-between gap-2">
        <NuxtLink :to="`/datasets/${datasetSlug(dataset.stem)}`" class="font-semibold text-(--ui-text-highlighted) hover:text-(--ui-primary) transition-colors line-clamp-1">
          {{ dataset.title }}
        </NuxtLink>
        <div class="flex items-center gap-1 shrink-0">
          <UBadge v-if="dataset.extraction_status === 'subset_needed'" color="warning" variant="subtle" size="xs">
            MH subset needed
          </UBadge>
          <UBadge v-if="dataset.maharashtra_specific" color="primary" variant="subtle" size="xs">
            MH
          </UBadge>
        </div>
      </div>

      <p class="text-sm text-(--ui-text-muted) line-clamp-2">
        {{ dataset.description }}
      </p>

      <div v-if="dataset.starter_idea" class="flex items-center gap-1.5 text-xs text-(--ui-primary)">
        <UIcon name="i-lucide-lightbulb" class="size-3 shrink-0" />
        <span class="line-clamp-1">{{ dataset.starter_idea }}</span>
      </div>

      <div class="flex flex-wrap gap-1.5">
        <UBadge color="neutral" variant="subtle" size="xs">
          {{ dataset.modality }}
        </UBadge>
        <LicenseBadge :license="dataset.license" />
      </div>

      <div class="flex items-center justify-between pt-1">
        <span v-if="dataset.organization" class="text-xs text-(--ui-text-dimmed) truncate">
          {{ dataset.organization }}
        </span>
        <span v-else />
        <div class="flex items-center gap-1 shrink-0">
          <UButton
            icon="i-lucide-arrow-up-right"
            size="xs"
            color="neutral"
            variant="ghost"
            :to="dataset.homepage"
            target="_blank"
            aria-label="Homepage"
          />
          <UButton
            v-if="dataset.huggingface_url"
            icon="i-simple-icons-huggingface"
            size="xs"
            color="neutral"
            variant="ghost"
            :to="dataset.huggingface_url"
            target="_blank"
            aria-label="HuggingFace"
          />
          <UButton
            v-if="dataset.github_url"
            icon="i-simple-icons-github"
            size="xs"
            color="neutral"
            variant="ghost"
            :to="dataset.github_url"
            target="_blank"
            aria-label="GitHub"
          />
        </div>
      </div>
    </div>
  </UCard>
</template>
