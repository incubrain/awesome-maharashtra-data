interface LicenseInfo {
  name: string
  permissiveness: 'very-open' | 'permissive' | 'restrictive' | 'proprietary' | 'unknown'
  permissivenessLabel: string
  color: string
  commercial: boolean
  modification: boolean
  distribution: boolean
  attribution: boolean
  shareAlike: boolean
  noDerivatives: boolean
  limitations: string[]
  summary: string
}

const LICENSE_DB: Record<string, LicenseInfo> = {
  'CC0-1.0': {
    name: 'Creative Commons Zero 1.0',
    permissiveness: 'very-open',
    permissivenessLabel: 'Very Open',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: false,
    shareAlike: false,
    noDerivatives: false,
    limitations: [],
    summary: 'No rights reserved. Free for any use without attribution.',
  },
  'CC0': {
    name: 'Creative Commons Zero',
    permissiveness: 'very-open',
    permissivenessLabel: 'Very Open',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: false,
    shareAlike: false,
    noDerivatives: false,
    limitations: [],
    summary: 'No rights reserved. Free for any use without attribution.',
  },
  'CC BY 4.0': {
    name: 'Creative Commons Attribution 4.0',
    permissiveness: 'permissive',
    permissivenessLabel: 'Permissive',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Must give credit'],
    summary: 'Free to use, share, and adapt — even commercially — with attribution.',
  },
  'CC BY 3.0': {
    name: 'Creative Commons Attribution 3.0',
    permissiveness: 'permissive',
    permissivenessLabel: 'Permissive',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Must give credit'],
    summary: 'Free to use, share, and adapt — even commercially — with attribution.',
  },
  'CC BY-SA 4.0': {
    name: 'Creative Commons Attribution-ShareAlike 4.0',
    permissiveness: 'permissive',
    permissivenessLabel: 'Permissive',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: true,
    noDerivatives: false,
    limitations: ['Must give credit', 'Derivatives must use same license'],
    summary: 'Free to use and adapt — even commercially — but derivatives must keep the same license.',
  },
  'CC BY-SA 3.0': {
    name: 'Creative Commons Attribution-ShareAlike 3.0',
    permissiveness: 'permissive',
    permissivenessLabel: 'Permissive',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: true,
    noDerivatives: false,
    limitations: ['Must give credit', 'Derivatives must use same license'],
    summary: 'Free to use and adapt — even commercially — but derivatives must keep the same license.',
  },
  'CC-BY-NC-SA-4.0': {
    name: 'Creative Commons Attribution-NonCommercial-ShareAlike 4.0',
    permissiveness: 'restrictive',
    permissivenessLabel: 'Restrictive',
    color: 'warning',
    commercial: false,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: true,
    noDerivatives: false,
    limitations: ['No commercial use', 'Must give credit', 'Derivatives must use same license'],
    summary: 'Free for non-commercial use with attribution. Derivatives must use the same license.',
  },
  'CC BY-NC 4.0': {
    name: 'Creative Commons Attribution-NonCommercial 4.0',
    permissiveness: 'restrictive',
    permissivenessLabel: 'Restrictive',
    color: 'warning',
    commercial: false,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['No commercial use', 'Must give credit'],
    summary: 'Free for non-commercial use with attribution.',
  },
  'CC BY-ND 4.0': {
    name: 'Creative Commons Attribution-NoDerivatives 4.0',
    permissiveness: 'restrictive',
    permissivenessLabel: 'Restrictive',
    color: 'warning',
    commercial: true,
    modification: false,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: true,
    limitations: ['No modifications allowed', 'Must give credit'],
    summary: 'Can share commercially with attribution, but no modifications allowed.',
  },
  'MIT': {
    name: 'MIT License',
    permissiveness: 'very-open',
    permissivenessLabel: 'Very Open',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Must include license notice'],
    summary: 'Very permissive. Free for any use with license notice.',
  },
  'Apache-2.0': {
    name: 'Apache License 2.0',
    permissiveness: 'permissive',
    permissivenessLabel: 'Permissive',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Must include license notice', 'Must state changes'],
    summary: 'Permissive license with patent grant. Free for commercial use.',
  },
  'GPL-3.0': {
    name: 'GNU General Public License v3.0',
    permissiveness: 'restrictive',
    permissivenessLabel: 'Restrictive',
    color: 'warning',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: true,
    noDerivatives: false,
    limitations: ['Derivatives must be open-source under GPL', 'Must include source code'],
    summary: 'Free to use commercially, but derivatives must be open-source under GPL.',
  },
  'Open Government': {
    name: 'Open Government License (India)',
    permissiveness: 'permissive',
    permissivenessLabel: 'Permissive',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Must acknowledge source'],
    summary: 'Government data free for any use with source acknowledgment.',
  },
  'Gov Open': {
    name: 'Government Open Data',
    permissiveness: 'permissive',
    permissivenessLabel: 'Permissive',
    color: 'success',
    commercial: true,
    modification: true,
    distribution: true,
    attribution: true,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Must acknowledge source'],
    summary: 'Government data free for any use with source acknowledgment.',
  },
  'Various': {
    name: 'Various / Mixed Licenses',
    permissiveness: 'unknown',
    permissivenessLabel: 'Varies',
    color: 'neutral',
    commercial: false,
    modification: false,
    distribution: false,
    attribution: false,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Check individual dataset terms'],
    summary: 'License varies by subset. Check the source for specific terms.',
  },
  'Custom': {
    name: 'Custom License',
    permissiveness: 'unknown',
    permissivenessLabel: 'Check Source',
    color: 'neutral',
    commercial: false,
    modification: false,
    distribution: false,
    attribution: false,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Check source for terms'],
    summary: 'Custom terms apply. Review the source for details.',
  },
  'Proprietary': {
    name: 'Proprietary License',
    permissiveness: 'proprietary',
    permissivenessLabel: 'Proprietary',
    color: 'error',
    commercial: false,
    modification: false,
    distribution: false,
    attribution: false,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Commercial license required', 'No redistribution', 'No modification'],
    summary: 'Proprietary data. Commercial license or subscription required.',
  },
}

function normalizeKey(license: string): string | null {
  const lower = license.toLowerCase().trim()

  // Direct match
  if (LICENSE_DB[license]) return license

  // Case-insensitive match
  for (const key of Object.keys(LICENSE_DB)) {
    if (key.toLowerCase() === lower) return key
  }

  // Fuzzy matching patterns
  if (lower.includes('cc0') || lower.includes('cc-0') || lower === 'public domain') return 'CC0-1.0'
  if (lower.includes('cc by-nc-sa') || lower.includes('cc-by-nc-sa')) return 'CC-BY-NC-SA-4.0'
  if (lower.includes('cc by-nc') || lower.includes('cc-by-nc')) return 'CC BY-NC 4.0'
  if (lower.includes('cc by-nd') || lower.includes('cc-by-nd')) return 'CC BY-ND 4.0'
  if (lower.includes('cc by-sa')) {
    if (lower.includes('3.0') || lower.includes('3')) return 'CC BY-SA 3.0'
    return 'CC BY-SA 4.0'
  }
  if (lower.includes('cc by') || lower.includes('cc-by')) {
    if (lower.includes('3.0') || lower.includes('3')) return 'CC BY 3.0'
    return 'CC BY 4.0'
  }
  if (lower === 'mit') return 'MIT'
  if (lower.includes('apache')) return 'Apache-2.0'
  if (lower.includes('gpl')) return 'GPL-3.0'
  if (lower.includes('gov') || lower.includes('government')) return 'Open Government'
  if (lower.includes('proprietary') || lower.includes('commercial')) return 'Proprietary'
  if (lower.includes('various') || lower.includes('mixed')) return 'Various'

  return null
}

export function useLicenseInfo(license: string): LicenseInfo {
  const key = normalizeKey(license)
  if (key && LICENSE_DB[key]) {
    return LICENSE_DB[key]
  }
  return {
    name: license,
    permissiveness: 'unknown',
    permissivenessLabel: 'Unknown',
    color: 'neutral',
    commercial: false,
    modification: false,
    distribution: false,
    attribution: false,
    shareAlike: false,
    noDerivatives: false,
    limitations: ['Check source for terms'],
    summary: `License: "${license}". Review the source for specific terms and conditions.`,
  }
}
