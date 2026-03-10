# Awesome Marathi Datasets [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated catalog of public-domain and openly licensed datasets for building AI infrastructure for Marathi and Maharashtra — voice agents, agri advisory, smart-city apps, legal RAG, climate tools, and beyond.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Datasets](https://img.shields.io/badge/datasets-170%2B-blue.svg)](#contents)

## Contents

- [Language and NLP Corpora](#language-and-nlp-corpora)
- [Speech and Audio](#speech-and-audio)
- [Vision, OCR and Multimodal](#vision-ocr-and-multimodal)
- [Geospatial and GIS](#geospatial-and-gis)
- [Agriculture and Rural](#agriculture-and-rural)
- [Health and Nutrition](#health-and-nutrition)
- [Education and Skills](#education-and-skills)
- [Economy, Labour and Finance](#economy-labour-and-finance)
- [Environment, Climate and Disaster](#environment-climate-and-disaster)
- [Transport and Urban](#transport-and-urban)
- [Governance, Census and Legal](#governance-census-and-legal)
- [Culture, Media and Heritage](#culture-media-and-heritage)
- [Real-Time Streams and APIs](#real-time-streams-and-apis)
- [Agentic, Instruction and RAG](#agentic-instruction-and-rag)
- [Benchmarks, Tools and Dialects](#benchmarks-tools-and-dialects)
- [Quick Start](#quick-start)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## Language and NLP Corpora

Foundation datasets for Marathi language models, NER, sentiment analysis, machine translation, and text processing.

> **[Full table →](categories/01-language-nlp.md)**

- [L3Cube-MahaCorpus](https://github.com/l3cube-pune/MarathiNLP) - Largest Marathi monolingual corpus with 24.8M sentences and 289M tokens for language model pretraining. `Text` `CC-BY-NC-SA-4.0`
- [AI4Bharat Samanantar](https://huggingface.co/datasets/ai4bharat/samanantar) - 3.32M English-Marathi parallel sentence pairs for machine translation. `Parallel Text` `CC0-1.0`
- [AI4Bharat IndicCorp v2](https://huggingface.co/datasets/ai4bharat/IndicCorpV2) - Part of a 20.9B token multilingual corpus with substantial Marathi coverage. `Text` `CC0-1.0`
- [L3Cube-MahaSent-MD](https://github.com/l3cube-pune/MarathiNLP) - Multi-domain sentiment dataset with 60,000 samples across 4 domains. `Text` `CC-BY-NC-SA-4.0`
- [L3Cube-MahaNER](https://huggingface.co/l3cube-pune/marathi-ner) - 25,000 manually tagged sentences with 8 entity classes for named entity recognition. `Text` `CC-BY-NC-SA-4.0`
- [OSCAR 23.01 (Marathi)](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301) - Web-crawled corpus with 729K documents and 252M words. `Text` `CC0-1.0`
- [mC4 (Marathi)](https://huggingface.co/datasets/mc4) - Multilingual colossal cleaned crawled corpus with approximately 7.8M Marathi documents. `Text` `ODC-BY-1.0`
- [Marathi Wikipedia Dump](https://dumps.wikimedia.org/mrwiki/) - Full dump of approximately 101,000 Marathi Wikipedia articles for knowledge extraction. `Text` `CC-BY-SA-3.0`

## Speech and Audio

Voice and audio datasets for ASR, TTS, speaker identification, and voice-first public services in Marathi.

> **[Full table →](categories/02-speech-audio.md)**

- [Mozilla Common Voice (Marathi)](https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0) - Crowd-sourced read-speech recordings with approximately 21 hours of validated Marathi transcriptions. `Speech + Text` `CC0`
- [AI4Bharat IndicVoices](https://huggingface.co/datasets/ai4bharat/IndicVoices) - Large-scale multilingual speech corpus with 7,348 hours across 22 Indian languages including Marathi. `Speech + Text` `CC-BY-4.0`
- [AI4Bharat Shrutilipi](https://huggingface.co/datasets/ai4bharat/Shrutilipi) - Pseudo-labeled ASR corpus mined from All India Radio with approximately 1,020 hours of Marathi. `Speech + Text` `CC-BY-4.0`
- [AI4Bharat Kathbath](https://huggingface.co/datasets/ai4bharat/Kathbath) - Crowdsourced human-labeled ASR dataset for 12 Indian languages including Marathi. `Speech + Text` `CC0`
- [Google FLEURS (Marathi)](https://huggingface.co/datasets/google/fleurs) - Few-shot speech benchmark with 2,009 sentences for ASR evaluation and speech language identification. `Speech + Text` `CC-BY-4.0`
- [IIT Madras IndicTTS (Marathi)](https://www.iitm.ac.in/donlab/indictts/database) - Studio-quality single-speaker TTS corpus with male and female Marathi recordings. `Speech + Text` `Academic`

## Vision, OCR and Multimodal

Image, OCR, satellite imagery, and multimodal datasets for document processing, scene understanding, and remote sensing in Maharashtra.

> **[Full table →](categories/03-vision-ocr-multimodal.md)**

- [CVQA](https://huggingface.co/datasets/afaji/cvqa) - Culturally-diverse multilingual visual question answering benchmark with Marathi questions annotated by native speakers. `Image + Text` `CC-BY-SA`
- [COCO Captions Marathi](https://huggingface.co/datasets/Singhchandann/coco-captions_marathi) - 414K rows of Marathi translations of MS-COCO image captions verified by native speakers. `Text` `CC-BY-NC-ND-4.0`
- [IndicSTR12](https://cvit.iiit.ac.in/research/projects/cvit-projects/indicstr) - Scene text recognition dataset covering 12 Indian languages including Marathi from natural scenes. `Image` `Research`
- [Bharat Scene Text Dataset](https://github.com/Bhashini-IITJ/BharatSceneTextDataset) - Large-scale scene text dataset with 5,113 Marathi word annotations and polygon bounding boxes. `Image` `Apache-2.0`
- [Devanagari Handwritten Character Dataset](https://archive.ics.uci.edu/dataset/389/devanagari+handwritten+character+dataset) - 92K handwritten character images with 46 classes applicable to Marathi character recognition. `Image` `CC-BY-4.0`
- [EuroSAT](https://github.com/phelber/EuroSAT) - Sentinel-2 satellite image dataset for land use and land cover classification applicable to Maharashtra. `Satellite Imagery` `MIT`

## Geospatial and GIS

GIS layers, satellite imagery, boundary data, and spatial datasets for Maharashtra mapping, urban planning, and environmental monitoring.

> **[Full table →](categories/04-geospatial-gis.md)**

- [MRSAC Geoportal](https://geoportal.mrsac.org.in/explore/) - Maharashtra Remote Sensing Application Centre with 50+ geospatial layers covering land use, boundaries, and watersheds. `WMS / Vector` `OGL-India`
- [Bhuvan NRSC Open EO Data](https://bhuvan-app3.nrsc.gov.in/data/) - ISRO satellite imagery including Resourcesat, AWiFS, and Cartosat DEM for Maharashtra. `Raster` `OGL-India`
- [OpenStreetMap Geofabrik (Western Zone)](https://download.geofabrik.de/asia/india/western-zone.html) - Crowdsourced vector map data with roads, buildings, and POIs covering Maharashtra. `Vector` `ODbL-1.0`
- [Copernicus Sentinel-2](https://browser.dataspace.copernicus.eu/) - 10m resolution 13-band optical satellite imagery with 5-day revisit for Maharashtra. `Raster` `Copernicus Open`
- [DataMeet Village Boundaries (Maharashtra)](https://github.com/datameet/indian_village_boundaries) - Community-digitized village-level boundary polygons for all 36 Maharashtra districts. `Vector` `ODbL-1.0`
- [ESA WorldCover 10m](https://worldcover2021.esa.int/download) - Sentinel-derived global land cover with 11 classes at 10m resolution. `Raster` `CC-BY-4.0`

## Agriculture and Rural

Crop production, market prices, soil health, irrigation, and rural development datasets for Maharashtra precision agriculture and agri-advisory AI.

> **[Full table →](categories/05-agriculture-rural.md)**

- [data.gov.in Crop Production Statistics](https://www.data.gov.in/catalog/district-wise-season-wise-crop-production-statistics) - District-wise, season-wise crop area, production, and yield data for Maharashtra from 1997 onwards. `Tabular` `GODL`
- [AgMarkNet Daily Market Prices](https://agmarknet.gov.in/) - Daily wholesale mandi prices for 300+ commodities across Maharashtra APMCs. `Tabular` `GODL`
- [Soil Health Card Portal](https://soilhealth.dac.gov.in/soil-health-map/MAHARASHTRA) - Millions of soil test results with N, P, K, pH, and micronutrients at village and district level. `Tabular` `GODL`
- [ICRISAT District Level Database](http://data.icrisat.org/dld/) - 571 districts, 1,030 variables, and 11M+ data points covering crops, irrigation, and infrastructure from 1966 to 2020. `Tabular` `CC-BY-4.0`
- [IMD Gridded Rainfall Data](https://www.imdpune.gov.in/cmpg/Griddata/Rainfall_25_NetCDF.html) - High-resolution daily gridded rainfall dataset covering 1901 to 2024. `Gridded` `Gov Open`
- [NASA MODIS NDVI (MOD13Q1)](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod13q1-061) - 16-day composite vegetation index at 250m resolution from 2000 to present. `Raster` `Open`
- [CHIRPS Rainfall Data](https://www.chc.ucsb.edu/data/chirps) - High-resolution daily rainfall estimates at 0.05 degree resolution from 1981 to near-present. `Gridded` `Public Domain`

## Health and Nutrition

Public health, disease surveillance, nutrition, and healthcare facility datasets for Maharashtra health AI and public service delivery.

> **[Full table →](categories/06-health-nutrition.md)**

- [NFHS-5 Maharashtra](http://rchiips.org/nfhs/) - District-level data on health, nutrition, fertility, and demographic indicators from the National Family Health Survey. `Tabular` `Open`
- [HMIS](https://hmis.mohfw.gov.in/) - Monthly facility-level health data from all government health facilities covering maternal health, immunisation, and disease reporting. `Tabular` `Gov Open`
- [IDSP](https://idsp.mohfw.gov.in/) - Weekly disease outbreak data covering epidemic-prone diseases across Maharashtra districts. `Tabular` `Gov Open`
- [IHME Global Burden of Disease](https://vizhub.healthdata.org/gbd-results/) - Comprehensive disease burden estimates for Maharashtra covering 292 causes and 88 risk factors from 1990 to present. `Tabular` `Open`
- [NHP (National Health Profile)](https://cbhidghs.mohfw.gov.in/) - Comprehensive health statistics including infrastructure, human resources, and disease burden for Maharashtra. `Tabular` `Gov Open`

## Education and Skills

School statistics, higher education data, skill development, and literacy datasets for Maharashtra education AI and workforce planning.

> **[Full table →](categories/07-education-skills.md)**

- [UDISE+](https://udiseplus.gov.in/) - Comprehensive annual school-level data on enrolment, infrastructure, and teachers for 1.1 lakh+ Maharashtra schools. `Tabular` `Gov Open`
- [ASER](https://asercentre.org/) - Household-based survey of learning outcomes across rural Maharashtra districts since 2005. `Tabular` `Open`
- [NIRF Rankings](https://www.nirfindia.org/) - National Institutional Ranking Framework data covering teaching, research, and outcome metrics for Maharashtra institutions. `Tabular` `Gov Open`
- [AISHE](https://aishe.gov.in/) - Annual census of higher education institutions covering enrolment, faculty, and programmes for Maharashtra. `Tabular` `Gov Open`
- [NAS (National Achievement Survey)](https://nas.gov.in/) - Large-scale assessment of student learning outcomes in Classes 3, 5, 8, and 10 across Maharashtra schools. `Tabular` `Gov Open`

## Economy, Labour and Finance

Economic indicators, employment surveys, financial data, and budget datasets for Maharashtra economic analysis and fintech AI.

> **[Full table →](categories/08-economy-labour-finance.md)**

- [RBI DBIE](https://data.rbi.org.in/DBIE/) - Comprehensive economic and financial statistics with Maharashtra state-level data covering real sector and public finance. `Tabular` `Gov Open`
- [PLFS](https://microdata.gov.in/NADA/index.php/catalog/PLFS) - Quarterly and annual employment and unemployment indicators with state-level Maharashtra tabulations. `Tabular` `Open`
- [Maharashtra Economic Survey](https://mahades.maharashtra.gov.in/esm.do?type=R) - Annual publication covering GSDP, agriculture, industry, infrastructure, and social indicators. `Tabular` `Gov Open`
- [NSO Annual Survey of Industries](https://www.mospi.gov.in/annual-survey-industries) - Factory-level data on manufacturing output, employment, and capital investment from Maharashtra. `Tabular` `Open`
- [MSME Udyam Registration](https://www.data.gov.in/resource/list-msme-registered-units-under-udyam) - Enterprise-level registration data for 8.9 lakh+ MSMEs in Maharashtra. `Tabular` `Gov Open`

## Environment, Climate and Disaster

Climate data, air quality, flood monitoring, forest cover, and disaster resilience datasets for Maharashtra environmental AI and early warning systems.

> **[Full table →](categories/09-environment-climate-disaster.md)**

- [CPCB Air Quality Index](https://airquality.cpcb.gov.in/ccr/) - Continuous ambient air quality monitoring from 20+ Maharashtra stations including PM2.5, PM10, and NO2. `Tabular` `Gov Open`
- [ERA5 Reanalysis](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) - Hourly global climate reanalysis at 0.25 degree resolution covering Maharashtra from 1940 to present. `Gridded` `Copernicus Open`
- [IMD Climate Data](https://mausam.imd.gov.in/) - Historical climate normals, rainfall, and temperature data from Maharashtra stations. `Tabular` `Gov Open`
- [CWC Flood Forecasting](https://ffs.india-water.gov.in/) - Real-time and historical water level and discharge data from Maharashtra river gauging stations. `Tabular` `Gov Open`
- [EM-DAT Disaster Database](https://public.emdat.be/) - International disaster database recording natural and technological disasters in Maharashtra since 1900. `Tabular` `Open`

## Transport and Urban

Transit feeds, road networks, smart city data, and urban planning datasets for Maharashtra mobility AI and infrastructure optimization.

> **[Full table →](categories/10-transport-urban-infrastructure.md)**

- [Pune PMPML Open Data](http://opendata.punecorporation.org/Citizen/CitizenDatasets/Index?categoryId=15) - Bus route, stop, and BRTS information for Pune Mahanagar Parivahan Mahamandal Limited. `Tabular / Geospatial` `Gov Open`
- [Mumbai BEST Bus Data (ChaloBEST)](http://chalobest.in/) - Community-created GTFS feed for Mumbai BEST bus network with 400+ routes. `GTFS` `Open`
- [Smart Cities Mission (Pune and Nagpur)](https://smartcities.data.gov.in/city/maharashtra) - Urban data covering infrastructure, mobility, environment, and governance indicators. `Tabular` `Gov Open`
- [Indian Railways (Maharashtra Routes)](https://www.data.gov.in/sector/railways) - Train schedules, station data, and route information for Maharashtra railway stations. `Tabular` `Gov Open`
- [OpenStreetMap (Maharashtra Roads)](https://download.geofabrik.de/asia/india/maharashtra.html) - Community-mapped road network, building footprints, and POI data for Maharashtra. `Geospatial` `ODbL`

## Governance, Census and Legal

Census tables, election data, crime statistics, legal texts, and government data for Maharashtra civic AI, legal RAG, and demographic analysis.

> **[Full table →](categories/11-governance-census-demographics-legal.md)**

- [Census 2011 Maharashtra](https://censusindia.gov.in/census.website/data/census-tables) - Comprehensive demographic data including population, literacy, and workers for 36 districts and 43,000+ villages. `Tabular` `Gov Open`
- [Election Commission of India (Maharashtra)](https://www.eci.gov.in/) - Constituency-wise election results for Lok Sabha and Vidhan Sabha elections in Maharashtra. `Tabular` `Gov Open`
- [Maharashtra Government Resolutions (mahGRs)](https://github.com/orgpedia/mahGRs) - Full text of approximately 47,000 Government Resolutions from 33 departments in Marathi and English. `Text` `CC-BY-4.0`
- [IndiaCode (Maharashtra Acts)](https://www.indiacode.nic.in/handle/123456789/2517/) - Digital repository of all Maharashtra state enactments including acts, rules, and regulations. `Text` `Gov Open`
- [Indian Kanoon (Bombay High Court)](https://indiankanoon.org/browse/bombay/) - Searchable database of Bombay High Court judgments with full text for legal research. `Text` `Open`
- [NCRB Crime in India](https://www.ncrb.gov.in/) - Annual crime statistics covering IPC crimes, crimes against women, and cybercrime for Maharashtra. `Tabular` `Gov Open`

## Culture, Media and Heritage

Public domain Marathi literature, heritage site data, tourism statistics, and cultural media datasets for Maharashtra cultural AI and digital humanities.

> **[Full table →](categories/12-culture-media-tourism-heritage.md)**

- [Wikisource Marathi](https://mr.wikisource.org/) - Public domain Marathi literature including 1,000+ books and classical texts like Dnyaneshwari and Dasbodh. `Text` `CC-BY-SA-4.0`
- [ASI Protected Monuments (Maharashtra)](https://asi.nic.in/protected-monuments-in-maharashtra/) - 529 centrally and state protected archaeological monuments and heritage sites in Maharashtra. `Tabular` `Gov Open`
- [NDLI Marathi Collection](https://ndl.iitkgp.ac.in/) - Digital library providing access to Marathi books, manuscripts, and research articles. `Text / Multimedia` `Open`
- [UNESCO World Heritage Sites (Maharashtra)](https://whc.unesco.org/) - Documentation for five Maharashtra UNESCO sites including Ajanta, Ellora, and Elephanta Caves. `Text / Images` `Open`
- [Marathi Wikipedia Articles](https://dumps.wikimedia.org/mrwiki/) - Full dump of 90,000+ Marathi Wikipedia articles for knowledge extraction and digital humanities. `Text` `CC-BY-SA-3.0`

## Real-Time Streams and APIs

Live data feeds and public APIs for weather, market prices, traffic, and other real-time Maharashtra data sources.

> **[Full table →](categories/13-realtime-streams-apis.md)**

- [data.gov.in APIs](https://www.data.gov.in/apis) - Open Government Data platform providing 100,000+ APIs across sectors for Maharashtra. `API` `Gov Open`
- [CPCB Air Quality Real-Time API](https://airquality.cpcb.gov.in/ccr/) - Continuous real-time air quality index and pollutant data from Maharashtra monitoring stations. `API` `Gov Open`
- [IMD Weather Feeds](https://mausam.imd.gov.in/) - Weather forecasts, warnings, and current conditions for Maharashtra cities via RSS and web services. `API` `Gov Open`
- [AgMarkNet Daily Prices API](https://www.agmarknet.gov.in/PriceAndArrivals/CommodityDailyStateWise.aspx) - Daily wholesale commodity prices and arrival data from agricultural mandis across Maharashtra. `API` `Gov Open`

## Agentic, Instruction and RAG

Instruction-tuning data, RAG-ready document collections, QA pairs, and structured schemas for building Marathi AI agents and tool-calling systems.

> **[Full table →](categories/14-agentic-instruction-rag.md)**

- [Maharashtra Government Resolutions for RAG](https://github.com/orgpedia/mahGRs) - Approximately 47,000 bilingual Government Resolutions structured for RAG pipelines over policy documents. `Text` `CC-BY-4.0`
- [AI4Bharat IndicQA (Marathi)](https://huggingface.co/datasets/ai4bharat/IndicQA) - Expert-generated reading comprehension dataset with context-question-answer triples for extractive QA. `Text` `CC-BY-4.0`
- [L3Cube-MahaSQuAD](https://github.com/l3cube-pune/MarathiNLP) - First comprehensive SQuAD-style QA dataset for Marathi with 142K samples. `Text` `Open Research`
- [Marathi Alpaca](https://huggingface.co/datasets/smallstepai/marathi-instruction-tuning-alpaca) - Marathi translation of the Stanford Alpaca instruction-tuning dataset with approximately 52K instructions. `Text` `Open Research`
- [OpenAssistant OASST (Marathi)](https://huggingface.co/datasets/OpenAssistant/oasst1) - Human-annotated assistant-style conversations in 35 languages including Marathi. `Text` `Apache-2.0`

## Benchmarks, Tools and Dialects

Evaluation benchmarks, dialect resources, tokenizers, and cross-cutting tools for Marathi NLP ecosystem development.

> **[Full table →](categories/15-benchmarks-fairness-dialects-tools.md)**

- [IndicGLUE (Marathi)](https://huggingface.co/datasets/ai4bharat/indic_glue) - Natural language understanding benchmark for 11 Indian languages covering categorisation, headline prediction, and paraphrase tasks. `Text` `Open Research`
- [FLORES-200 (Marathi)](https://huggingface.co/datasets/facebook/flores) - Human-translated evaluation benchmark for machine translation covering 200+ languages with 3,001 sentences. `Parallel Text` `CC-BY-SA-4.0`
- [IndicXTREME (Marathi)](https://huggingface.co/collections/ai4bharat/indicxtreme-66c59f576386ba2955650030) - Comprehensive NLU benchmark of 9 tasks across 20 Indian languages. `Text` `Open Research`
- [L3Cube-MahaNLP Toolkit](https://github.com/l3cube-pune/MarathiNLP) - Comprehensive Marathi NLP library including MahaBERT, MahaRoBERTa, word embeddings, and downstream task tools. `Models / Tools` `Open Research`
- [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library) - Python library for Indian language text processing with tokenisation, normalisation, and transliteration. `Tools` `GPL-v3`
- [iNLTK](https://github.com/goru001/inltk) - Deep learning NLP library supporting Marathi with pre-trained models, text generation, and sentence embeddings. `Tools` `MIT`

## Quick Start

1. **Browse by category** -- Each of the 15 categories above links to a detailed table with size, license, modality, and direct download links.
2. **Search the full catalog** -- Open [`CATALOG.md`](CATALOG.md) for a single flat list of every dataset, searchable with Ctrl+F.
3. **Read the data cards** -- The [`data_cards/`](data_cards/) directory contains structured metadata cards for selected datasets with provenance, schema, and usage notes.

## Contributing

Contributions are welcome! Whether you have discovered a new open dataset, spotted a broken link, or want to add a data card, please see [CONTRIBUTING.md](CONTRIBUTING.md) for submission guidelines and quality criteria.

## Roadmap

We are actively expanding coverage and improving metadata quality. See [future/ROADMAP.md](future/ROADMAP.md) for planned additions including new dataset categories, automated link checking, and community data card reviews.

## License

This catalog is licensed under [CC-BY-4.0](LICENSE). Individual datasets retain their own licenses as noted in each entry.

