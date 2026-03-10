<script setup lang="ts">
const props = defineProps<{
  license: string
  size?: 'xs' | 'sm' | 'md'
}>()

const info = computed(() => useLicenseInfo(props.license))
</script>

<template>
  <UPopover :ui="{ content: 'w-72' }">
    <UBadge
      :color="info.color as any"
      variant="outline"
      :size="size || 'xs'"
      class="cursor-help"
    >
      {{ license }}
    </UBadge>

    <template #content>
      <div class="p-3 flex flex-col gap-2.5">
        <div>
          <div class="font-semibold text-sm text-(--ui-text-highlighted)">{{ info.name }}</div>
          <UBadge :color="info.color as any" variant="subtle" size="xs" class="mt-1">
            {{ info.permissivenessLabel }}
          </UBadge>
        </div>

        <p class="text-xs text-(--ui-text-muted) leading-relaxed">{{ info.summary }}</p>

        <div class="grid grid-cols-2 gap-x-3 gap-y-1 text-xs">
          <div class="flex items-center gap-1.5">
            <UIcon
              :name="info.commercial ? 'i-lucide-check' : 'i-lucide-x'"
              :class="info.commercial ? 'text-green-500' : 'text-red-500'"
              class="size-3.5 shrink-0"
            />
            <span>Commercial use</span>
          </div>
          <div class="flex items-center gap-1.5">
            <UIcon
              :name="info.modification ? 'i-lucide-check' : 'i-lucide-x'"
              :class="info.modification ? 'text-green-500' : 'text-red-500'"
              class="size-3.5 shrink-0"
            />
            <span>Modification</span>
          </div>
          <div class="flex items-center gap-1.5">
            <UIcon
              :name="info.distribution ? 'i-lucide-check' : 'i-lucide-x'"
              :class="info.distribution ? 'text-green-500' : 'text-red-500'"
              class="size-3.5 shrink-0"
            />
            <span>Distribution</span>
          </div>
          <div class="flex items-center gap-1.5">
            <UIcon
              :name="info.attribution ? 'i-lucide-x' : 'i-lucide-check'"
              :class="info.attribution ? 'text-amber-500' : 'text-green-500'"
              class="size-3.5 shrink-0"
            />
            <span>{{ info.attribution ? 'Attribution req.' : 'No attribution' }}</span>
          </div>
        </div>

        <div v-if="info.limitations.length" class="border-t border-(--ui-border) pt-2">
          <div class="text-xs font-medium text-(--ui-text-dimmed) mb-1">Limitations</div>
          <ul class="text-xs text-(--ui-text-muted) flex flex-col gap-0.5">
            <li v-for="lim in info.limitations" :key="lim" class="flex items-start gap-1.5">
              <UIcon name="i-lucide-alert-triangle" class="size-3 text-amber-500 mt-0.5 shrink-0" />
              {{ lim }}
            </li>
          </ul>
        </div>
      </div>
    </template>
  </UPopover>
</template>
