<script setup lang="ts">
useSeoMeta({
  title: 'Data Gaps',
  description: 'Identify missing and sparse datasets in the Marathi & Maharashtra data ecosystem.',
})

const { data: categories } = await useAsyncData('gaps-categories', () =>
  queryCollection('categories').order('order', 'ASC').all()
)

const selectedCategory = ref('')
const selectedStatus = ref('')

const statusOptions = ['missing', 'sparse', 'adequate']

const categoryMap = computed(() => {
  const map: Record<string, string> = {}
  for (const cat of categories.value || []) {
    map[cat.slug] = cat.title
  }
  return map
})

const filteredGaps = computed(() => {
  return DATA_GAPS.filter(gap => {
    if (selectedCategory.value && gap.category !== selectedCategory.value) return false
    if (selectedStatus.value && gap.status !== selectedStatus.value) return false
    return true
  })
})

const missingCount = computed(() => DATA_GAPS.filter(g => g.status === 'missing').length)
const sparseCount = computed(() => DATA_GAPS.filter(g => g.status === 'sparse').length)

const statusColor = (status: string) => {
  if (status === 'missing') return 'error'
  if (status === 'sparse') return 'warning'
  return 'success'
}

const statusIcon = (status: string) => {
  if (status === 'missing') return 'i-lucide-circle-x'
  if (status === 'sparse') return 'i-lucide-circle-alert'
  return 'i-lucide-circle-check'
}
</script>

<template>
  <UDashboardPanel>
    <template #header>
      <UDashboardNavbar title="Data Gaps Analysis">
        <template #leading>
          <UDashboardSidebarCollapse />
        </template>
      </UDashboardNavbar>
    </template>

    <template #body>
      <div class="flex flex-col gap-6 p-6">
        <!-- Intro -->
        <div class="max-w-3xl">
          <h1 class="text-2xl font-bold text-(--ui-text-highlighted) mb-2">Data Gaps Analysis</h1>
          <p class="text-(--ui-text-muted)">
            Comparing the Marathi & Maharashtra data ecosystem against well-resourced languages and regions.
            These gaps represent opportunities — datasets that could be created, gathered, or digitized
            to unlock new AI capabilities for Marathi speakers.
          </p>
        </div>

        <!-- Summary stats -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-xl">
          <div
            class="flex items-center gap-3 p-4 rounded-lg bg-(--ui-bg-elevated) cursor-pointer hover:ring-1 hover:ring-(--ui-border)"
            :class="selectedStatus === 'missing' ? 'ring-1 ring-red-500' : ''"
            @click="selectedStatus = selectedStatus === 'missing' ? '' : 'missing'"
          >
            <UIcon name="i-lucide-circle-x" class="text-red-500 size-5 shrink-0" />
            <div>
              <div class="text-xl font-bold">{{ missingCount }}</div>
              <div class="text-xs text-(--ui-text-dimmed)">Missing</div>
            </div>
          </div>
          <div
            class="flex items-center gap-3 p-4 rounded-lg bg-(--ui-bg-elevated) cursor-pointer hover:ring-1 hover:ring-(--ui-border)"
            :class="selectedStatus === 'sparse' ? 'ring-1 ring-amber-500' : ''"
            @click="selectedStatus = selectedStatus === 'sparse' ? '' : 'sparse'"
          >
            <UIcon name="i-lucide-circle-alert" class="text-amber-500 size-5 shrink-0" />
            <div>
              <div class="text-xl font-bold">{{ sparseCount }}</div>
              <div class="text-xs text-(--ui-text-dimmed)">Sparse</div>
            </div>
          </div>
          <div
            class="flex items-center gap-3 p-4 rounded-lg bg-(--ui-bg-elevated) cursor-pointer hover:ring-1 hover:ring-(--ui-border)"
            :class="selectedStatus === '' && selectedCategory === '' ? 'ring-1 ring-(--ui-border)' : ''"
            @click="selectedStatus = ''; selectedCategory = ''"
          >
            <UIcon name="i-lucide-list" class="text-(--ui-primary) size-5 shrink-0" />
            <div>
              <div class="text-xl font-bold">{{ DATA_GAPS.length }}</div>
              <div class="text-xs text-(--ui-text-dimmed)">Total Gaps</div>
            </div>
          </div>
        </div>

        <!-- Category filter chips -->
        <div class="flex flex-wrap gap-2">
          <UBadge
            v-for="cat in categories"
            :key="cat.slug"
            :color="selectedCategory === cat.slug ? 'primary' : 'neutral'"
            :variant="selectedCategory === cat.slug ? 'solid' : 'outline'"
            size="md"
            class="cursor-pointer"
            @click="selectedCategory = selectedCategory === cat.slug ? '' : cat.slug"
          >
            <UIcon :name="cat.icon" class="size-3.5 mr-1" />
            {{ cat.title }}
          </UBadge>
        </div>

        <!-- Gap cards -->
        <div class="flex flex-col gap-4">
          <div
            v-for="gap in filteredGaps"
            :key="gap.area"
            class="border border-(--ui-border) rounded-lg p-5"
          >
            <div class="flex items-start justify-between gap-4 mb-3">
              <div class="flex items-center gap-2">
                <UIcon :name="statusIcon(gap.status)" :class="gap.status === 'missing' ? 'text-red-500' : 'text-amber-500'" class="size-5 shrink-0" />
                <h3 class="font-semibold text-(--ui-text-highlighted)">{{ gap.area }}</h3>
              </div>
              <div class="flex items-center gap-2 shrink-0">
                <UBadge :color="statusColor(gap.status) as any" variant="subtle" size="xs">
                  {{ gap.status }}
                </UBadge>
                <NuxtLink :to="`/categories/${gap.category}`">
                  <UBadge color="neutral" variant="outline" size="xs" class="cursor-pointer hover:bg-(--ui-bg-elevated)">
                    {{ categoryMap[gap.category] || gap.category }}
                  </UBadge>
                </NuxtLink>
              </div>
            </div>

            <p class="text-sm text-(--ui-text-muted) mb-3">{{ gap.description }}</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div class="bg-(--ui-bg-elevated) rounded-md p-3">
                <div class="text-xs font-medium text-(--ui-text-dimmed) mb-1 flex items-center gap-1">
                  <UIcon name="i-lucide-globe" class="size-3" />
                  Global Benchmark
                </div>
                <p class="text-xs text-(--ui-text-muted)">{{ gap.benchmark }}</p>
              </div>
              <div class="bg-(--ui-bg-elevated) rounded-md p-3">
                <div class="text-xs font-medium text-(--ui-text-dimmed) mb-1 flex items-center gap-1">
                  <UIcon name="i-lucide-lightbulb" class="size-3" />
                  Opportunity
                </div>
                <p class="text-xs text-(--ui-text-muted)">{{ gap.opportunity }}</p>
              </div>
            </div>
          </div>
        </div>

        <div v-if="!filteredGaps.length" class="text-center py-12 text-(--ui-text-muted)">
          <UIcon name="i-lucide-check-circle" class="size-12 mx-auto mb-3 opacity-50" />
          <p>No gaps match the current filters.</p>
        </div>
      </div>
    </template>
  </UDashboardPanel>
</template>
