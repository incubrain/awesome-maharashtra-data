export interface DataGap {
  area: string
  category: string
  status: 'missing' | 'sparse' | 'adequate'
  description: string
  benchmark: string
  opportunity: string
}

// What a well-resourced language/region typically has vs what Marathi/Maharashtra has
export const DATA_GAPS: DataGap[] = [
  // Language & NLP
  {
    area: 'Conversational / Dialogue datasets',
    category: 'language-nlp',
    status: 'missing',
    description: 'No dedicated multi-turn Marathi dialogue or conversational datasets exist.',
    benchmark: 'English has DailyDialog, PersonaChat, MultiWOZ; Hindi has limited options.',
    opportunity: 'Critical for building Marathi chatbots, virtual assistants, and customer service AI.',
  },
  {
    area: 'Commonsense reasoning',
    category: 'language-nlp',
    status: 'missing',
    description: 'No Marathi commonsense knowledge graphs or reasoning datasets.',
    benchmark: 'English has ConceptNet, ATOMIC, WinoGrande, HellaSwag.',
    opportunity: 'Needed for Marathi LLMs to understand cultural context and implicit knowledge.',
  },
  {
    area: 'Hate speech / toxicity (large-scale)',
    category: 'language-nlp',
    status: 'sparse',
    description: 'L3Cube-MahaHate exists but is small. No large-scale, multi-platform toxicity dataset.',
    benchmark: 'English has Jigsaw (1.8M comments), HateXplain with rationale annotations.',
    opportunity: 'Essential for content moderation on Marathi social media platforms.',
  },
  {
    area: 'Summarization corpus',
    category: 'language-nlp',
    status: 'sparse',
    description: 'IndicSentenceSummarization has Marathi but no long-document summarization dataset.',
    benchmark: 'English has CNN/DailyMail, XSum; Chinese has LCSTS.',
    opportunity: 'Required for Marathi news summarization, document understanding, and report generation.',
  },

  // Speech & Audio
  {
    area: 'Emotional speech',
    category: 'speech-audio',
    status: 'missing',
    description: 'No Marathi speech emotion recognition (SER) dataset with emotion labels.',
    benchmark: 'English has IEMOCAP, RAVDESS, CREMA-D; Hindi has limited options.',
    opportunity: 'Needed for call center sentiment analysis, mental health monitoring, accessibility.',
  },
  {
    area: 'Noisy / real-world speech',
    category: 'speech-audio',
    status: 'missing',
    description: 'Existing Marathi ASR datasets are mostly read speech. No noisy, spontaneous, or code-mixed speech data.',
    benchmark: 'English has CHiME, VoxCeleb, AMI Meeting Corpus.',
    opportunity: 'Real-world Marathi speech recognition requires training on market, street, farm environments.',
  },
  {
    area: 'Text-to-Speech (multi-speaker)',
    category: 'speech-audio',
    status: 'sparse',
    description: 'IndicTTS has 1 Marathi speaker. No multi-speaker, multi-style TTS corpus.',
    benchmark: 'English has LibriTTS (2,456 speakers), VCTK (110 speakers).',
    opportunity: 'Needed for natural-sounding Marathi voice assistants and audiobook generation.',
  },

  // Vision / OCR
  {
    area: 'Devanagari scene text in the wild',
    category: 'vision-ocr-multimodal',
    status: 'sparse',
    description: 'BSTD (5K+ Marathi words), IndicSTR12 (27K+), and ICDAR MLT-2019 exist but are modest. No large-scale Marathi-only street sign / billboard dataset.',
    benchmark: 'Chinese has CTW, RCTW with 100K+ street images.',
    opportunity: 'Required for Marathi navigation apps, automated sign reading, smart city infrastructure.',
  },
  {
    area: 'Medical imaging with Marathi reports',
    category: 'vision-ocr-multimodal',
    status: 'missing',
    description: 'No paired medical image + Marathi radiology report dataset exists.',
    benchmark: 'English has MIMIC-CXR (377K images), CheXpert.',
    opportunity: 'Would enable AI-assisted radiology reporting in Marathi for rural hospital networks.',
  },
  {
    area: 'Document layout analysis (Marathi)',
    category: 'vision-ocr-multimodal',
    status: 'sparse',
    description: 'IndicDLP covers 119K pages across 12 Indic languages including Marathi with 42 layout classes, but no Marathi-specific dataset with government form field-level (key-value) annotations exists. No FUNSD/XFUND equivalent for Indian languages.',
    benchmark: 'English has PubLayNet, DocBank, FUNSD. Chinese has CDLA. XFUND covers 7 languages but no Indian.',
    opportunity: 'Key for digitizing Maharashtra government records (7/12 extracts, certificates) and automating form processing.',
  },
  {
    area: 'Annotated Marathi newspaper scan corpus',
    category: 'vision-ocr-multimodal',
    status: 'missing',
    description: 'No annotated dataset of scanned Marathi newspaper pages with OCR ground-truth transcriptions. IndicDLP has ~540 Marathi newspaper pages with layout boxes but no text labels. Raw scans exist in Digital Library of India archives.',
    benchmark: 'Hindi has FIRE-RISOT (100K newspaper articles). Chinese has extensive newspaper OCR corpora.',
    opportunity: 'Newspapers are a primary source of printed Marathi text. Would massively boost printed OCR model quality.',
  },
  {
    area: 'Marathi-English bilingual document OCR',
    category: 'vision-ocr-multimodal',
    status: 'missing',
    description: 'No dedicated dataset for OCR on bilingual Marathi-English documents (government forms, exam papers, bilingual signage). CMATERdb has 150 Devanagari-Roman handwritten pages but no printed bilingual document data.',
    benchmark: 'AksharaOCR provides Sinhala-English mixed OCR (24K+ lines). No equivalent for Marathi-English.',
    opportunity: 'Most Maharashtra government forms are bilingual. Critical for real-world document digitization.',
  },
  {
    area: 'Comprehensive Devanagari conjunct character dataset',
    category: 'vision-ocr-multimodal',
    status: 'sparse',
    description: 'MKI-26 covers 20 conjunct classes, Sanskrit Letter Dataset has 602 classes but only ~13 images each, DevChar has 4M characters with conjuncts. No single dataset comprehensively covers all ~360 common Devanagari conjuncts with sufficient samples per class for deep learning.',
    benchmark: 'Latin OCR has complete glyph coverage. Chinese has stroke-level datasets for all common characters.',
    opportunity: 'Conjuncts are the #1 error source in Devanagari OCR. A focused dataset would directly improve Marathi OCR accuracy.',
  },

  // Geospatial
  {
    area: 'High-res building footprints for Maharashtra',
    category: 'geospatial-gis',
    status: 'sparse',
    description: 'OpenStreetMap has partial coverage. No comprehensive, official building footprint dataset.',
    benchmark: 'US has Microsoft Building Footprints (125M), Google Open Buildings covers Africa.',
    opportunity: 'Needed for urban planning, disaster response, property tax assessment in MH.',
  },
  {
    area: 'Agricultural land parcel boundaries',
    category: 'geospatial-gis',
    status: 'missing',
    description: 'No digitized, geo-referenced field boundary dataset for Maharashtra farmland.',
    benchmark: 'EU has LPIS with field-level boundaries. US has CLU (Common Land Unit).',
    opportunity: 'Would transform precision agriculture, crop insurance, and land record modernization.',
  },

  // Health
  {
    area: 'Electronic health records (Marathi)',
    category: 'health-nutrition',
    status: 'missing',
    description: 'No anonymized Marathi EHR or clinical notes dataset.',
    benchmark: 'English has MIMIC-III/IV. Some de-identified Chinese EHR datasets exist.',
    opportunity: 'Essential for clinical NLP, drug interaction detection, and Marathi health chatbots.',
  },
  {
    area: 'Nutrition / dietary survey (Maharashtra-specific)',
    category: 'health-nutrition',
    status: 'sparse',
    description: 'NFHS has state-level aggregates but no individual-level dietary intake data for MH.',
    benchmark: 'US has NHANES with individual-level dietary recall. UK has NDNS.',
    opportunity: 'Needed for personalized nutrition apps, malnutrition early warning, school meal planning.',
  },

  // Education
  {
    area: 'Marathi educational question banks',
    category: 'education-skills',
    status: 'missing',
    description: 'No structured dataset of Marathi exam questions mapped to curriculum topics.',
    benchmark: 'English has ARC, SciQ, MMLU. Chinese has GAOKAO benchmark.',
    opportunity: 'Would power adaptive learning platforms and automated assessment in Marathi medium schools.',
  },
  {
    area: 'Student learning outcome data',
    category: 'education-skills',
    status: 'sparse',
    description: 'ASER and NAS provide samples but no continuous, longitudinal learning data.',
    benchmark: 'Many OECD nations have PISA longitudinal follow-ups and national learning management data.',
    opportunity: 'Critical for evidence-based education policy and personalized learning interventions.',
  },

  // Economy & Finance
  {
    area: 'Marathi financial news corpus',
    category: 'economy-labour-finance',
    status: 'missing',
    description: 'No labeled Marathi financial sentiment or event dataset.',
    benchmark: 'English has Financial PhraseBank, FiQA. Chinese has FinNL.',
    opportunity: 'Needed for Marathi stock market analysis tools, financial news summarization.',
  },
  {
    area: 'MSME / startup registry with structured data',
    category: 'economy-labour-finance',
    status: 'sparse',
    description: 'Udyam has registration data and Startup India lists 25K+ Maharashtra startups, mentors, and incubators, but no structured dataset with financials, outcomes, or survival data.',
    benchmark: 'US has SEC filings + Crunchbase. UK has Companies House full data.',
    opportunity: 'Would enable MSME lending models, market analysis, and entrepreneurship research.',
  },

  // Agriculture
  {
    area: 'Crop disease images (Maharashtra varieties)',
    category: 'agriculture-rural',
    status: 'missing',
    description: 'No labeled image dataset of diseases on Maharashtra-specific crops (sugarcane, jowar, bajra, grapes).',
    benchmark: 'PlantVillage has 50K images but mainly Western crops. China has custom rice/wheat datasets.',
    opportunity: 'Would enable phone-based crop disease detection apps for MH farmers.',
  },
  {
    area: 'Farm-level input/output economics',
    category: 'agriculture-rural',
    status: 'sparse',
    description: 'ICRISAT VDSA has some villages. No broad, recent farm-level cost-of-cultivation microdata for MH.',
    benchmark: 'US has ARMS (Agricultural Resource Management Survey) at field level.',
    opportunity: 'Essential for input subsidy optimization, credit risk modeling, and procurement planning.',
  },

  // Governance
  {
    area: 'Court judgments in Marathi (structured)',
    category: 'governance-census-demographics-legal',
    status: 'sparse',
    description: 'Indian Kanoon has some Marathi judgments but no structured, NER-tagged legal dataset.',
    benchmark: 'English has CaseLaw Access Project (6.7M decisions). EU has ECHR-CASES.',
    opportunity: 'Would enable legal search, case outcome prediction, and access to justice in Marathi.',
  },
  {
    area: 'RTI response data (structured)',
    category: 'governance-census-demographics-legal',
    status: 'missing',
    description: 'RTI requests and responses exist but are not aggregated or structured as a dataset.',
    benchmark: 'UK has WhatDoTheyKnow with 800K+ structured FOI requests and responses.',
    opportunity: 'Could power government transparency tools, automated RTI assistance, and civic engagement.',
  },

  // Transport
  {
    area: 'Real-time traffic flow data',
    category: 'transport-urban-infrastructure',
    status: 'missing',
    description: 'No open, continuous traffic speed/flow dataset for Mumbai, Pune, or Nagpur.',
    benchmark: 'UK has Highways England (15-min loop data). US has INRIX.',
    opportunity: 'Required for traffic prediction, route optimization, and urban planning models.',
  },

  // Culture
  {
    area: 'Marathi literary corpus (annotated)',
    category: 'culture-media-tourism-heritage',
    status: 'missing',
    description: 'No POS-tagged or semantically annotated Marathi literary text corpus (novels, poetry, drama).',
    benchmark: 'English has BNC, Project Gutenberg with annotations. Japanese has BCCWJ.',
    opportunity: 'Needed for digital humanities research, literary analysis, and cultural preservation.',
  },
  {
    area: 'Tourism POI reviews in Marathi',
    category: 'culture-media-tourism-heritage',
    status: 'missing',
    description: 'No scraped/curated Marathi tourism review dataset for MH points of interest.',
    benchmark: 'English has Yelp (6.9M reviews), TripAdvisor datasets.',
    opportunity: 'Would power Marathi tourism recommendation engines and sentiment-based destination rankings.',
  },

  // Environment
  {
    area: 'Air quality station-level historical data (MH)',
    category: 'environment-climate-disaster',
    status: 'sparse',
    description: 'CPCB has real-time data but no cleaned, aggregated historical time-series for all MH stations.',
    benchmark: 'US EPA has AQS with decades of cleaned, station-level data. EU has EEA AirBase.',
    opportunity: 'Needed for pollution forecasting, health impact studies, and environmental policy.',
  },

  // Benchmarks
  {
    area: 'Marathi LLM evaluation benchmark',
    category: 'benchmarks-fairness-dialects-tools',
    status: 'sparse',
    description: 'IndicGLUE and IndicXTREME exist but no comprehensive Marathi-specific benchmark like MMLU or C-Eval.',
    benchmark: 'English has MMLU, HellaSwag, ARC. Chinese has C-Eval, CMMLU.',
    opportunity: 'Critical for fairly evaluating and comparing Marathi language models.',
  },
]
