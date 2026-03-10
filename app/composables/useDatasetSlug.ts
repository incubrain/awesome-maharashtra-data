export function datasetSlug(stem: string): string {
  return stem.replace(/^datasets\//, '')
}
