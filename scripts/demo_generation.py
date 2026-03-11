#!/usr/bin/env python3
"""
Demo: Generate sample metadata for key datasets to show what output looks like.
This doesn't require an API key - uses hardcoded examples based on the dataset patterns.
"""

import yaml
from pathlib import Path
from typing import Dict, Any

# Sample generated metadata for key datasets
DEMO_DATASETS = {
    "ai4bharat-samanantar-mr": {
        "schema": [
            {"field": "english_text", "type": "string", "description": "English sentence from parallel corpus"},
            {"field": "marathi_text", "type": "string", "description": "Marathi translation of the English sentence"},
            {"field": "domain", "type": "string", "description": "Source domain (news, wiki, books, etc.)"},
            {"field": "confidence", "type": "float", "description": "Alignment confidence score (0-1)"}
        ],
        "starter_idea": "Build a Marathi↔English API for translating agricultural advisories and government notices in real-time.",
        "build_ideas": [
            "Create a terminology dictionary extractor that identifies technical terms and their translations for domain-specific glossaries",
            "Fine-tune a quantized transformer model and deploy as a Hugging Face Space for offline translation",
            "Build a crowdsourcing UI for community validation and improvement of translation pairs"
        ],
        "quick_start": "from datasets import load_dataset\nds = load_dataset('ai4bharat/samanantar')\nfor ex in ds['train'].take(3):\n    print(f\"EN: {ex['english_text']}\\nMR: {ex['marathi_text']}\\n\")"
    },
    "l3cube-mahacorpus": {
        "schema": [
            {"field": "text", "type": "string", "description": "Marathi text sentence from the corpus"},
            {"field": "source", "type": "string", "description": "Source of the text (news, books, web, etc.)"},
            {"field": "year", "type": "int", "description": "Year the text was published or crawled"},
            {"field": "length", "type": "int", "description": "Number of tokens in the sentence"}
        ],
        "starter_idea": "Train a Marathi text classifier to identify sentiment or topic for social media monitoring of Marathi-language conversations.",
        "build_ideas": [
            "Build a GPT-style language model for Marathi using this corpus and deploy as a chatbot for agriculture advisory",
            "Create a text summarization service for Marathi news articles to help busy farmers stay informed",
            "Develop spell-check and grammar correction tools specifically for Marathi using this clean corpus"
        ],
        "quick_start": "from datasets import load_dataset\nds = load_dataset('csv', data_files='mahacorpus.csv')\nprint(f\"Total sentences: {len(ds)}\")\nprint(ds['train'][0]['text'][:100])"
    },
    "agmarknet-daily-prices": {
        "schema": [
            {"field": "date", "type": "date", "description": "Date of the market price report"},
            {"field": "commodity", "type": "string", "description": "Name of agricultural commodity (wheat, rice, onion, etc.)"},
            {"field": "market", "type": "string", "description": "APMC market name in Maharashtra"},
            {"field": "price_per_quintal", "type": "float", "description": "Market price in rupees per quintal"},
            {"field": "volume_traded", "type": "int", "description": "Quantity traded in quintals"}
        ],
        "starter_idea": "Build an SMS-based price alert app for farmers to get daily mandi prices in their local language.",
        "build_ideas": [
            "Create a price forecasting model using historical trends to help farmers decide optimal selling time",
            "Build a multi-language mobile app showing regional price variations to help farmers route goods to best markets",
            "Develop a warehouse receipt financing platform that uses price data to determine loan amounts"
        ],
        "quick_start": "import pandas as pd\ndf = pd.read_csv('agmarknet_prices.csv')\nlatest = df[df['date'] == df['date'].max()]\nprint(latest[['commodity', 'market', 'price_per_quintal']].head(10))"
    },
    "mrsac-geoportal": {
        "schema": [
            {"field": "geometry", "type": "geojson", "description": "GeoJSON polygon or point geometry"},
            {"field": "district", "type": "string", "description": "Maharashtra district name"},
            {"field": "land_use_class", "type": "string", "description": "Land use classification (agriculture, urban, water, etc.)"},
            {"field": "area_hectares", "type": "float", "description": "Area covered in hectares"},
            {"field": "year", "type": "int", "description": "Year of the observation"}
        ],
        "starter_idea": "Create a visual dashboard showing real-time land cover changes to track illegal mining or deforestation in Maharashtra.",
        "build_ideas": [
            "Build an automatic alert system for detecting rapid land use changes that might indicate environmental violations",
            "Create a precision agriculture app overlaying land use data with crop type data for optimized resource allocation",
            "Develop a climate impact simulator showing how land use changes affect rainfall and groundwater"
        ],
        "quick_start": "import folium\nimport geopandas as gpd\ngdf = gpd.read_file('mrsac_landuse.shp')\nm = folium.Map(location=[19.5, 76], zoom_start=7)\nfolium.GeoJson(gdf).add_to(m)\nm.save('maharashtra_landuse.html')"
    },
    "soil-health-card-mh": {
        "schema": [
            {"field": "village_code", "type": "string", "description": "Village administrative code"},
            {"field": "phosphorus_mg_kg", "type": "float", "description": "Available phosphorus in mg/kg"},
            {"field": "potassium_mg_kg", "type": "float", "description": "Available potassium in mg/kg"},
            {"field": "nitrogen_mg_kg", "type": "float", "description": "Available nitrogen in mg/kg"},
            {"field": "ph", "type": "float", "description": "Soil pH value (acidity/alkalinity)"},
            {"field": "organic_carbon_percent", "type": "float", "description": "Percentage of organic carbon"}
        ],
        "starter_idea": "Build a recommendation engine that suggests fertilizer types and quantities based on soil test results and crop choice.",
        "build_ideas": [
            "Create a voice-based advisory system in Marathi that tells farmers their soil status and improvement recommendations",
            "Develop a crop rotation recommendation system using soil health data to improve long-term yields",
            "Build a subsidy eligibility checker connecting soil quality with government fertilizer assistance programs"
        ],
        "quick_start": "import pandas as pd\ndf = pd.read_csv('soil_health_mh.csv')\ndeficient = df[df['phosphorus_mg_kg'] < 12]\nprint(f\"Villages with P deficiency: {len(deficient)}\")\nprint(deficient[['village_code', 'phosphorus_mg_kg']].head())"
    },
}

def generate_demo_metadata():
    """Generate sample metadata files for demo datasets."""
    data_cards_dir = Path(__file__).parent.parent / "data_cards"

    print(f"Generating demo metadata for {len(DEMO_DATASETS)} key datasets...\n")

    for slug, metadata in DEMO_DATASETS.items():
        yaml_path = data_cards_dir / f"{slug}.yaml"

        # Load existing data if it exists
        existing = {}
        if yaml_path.exists():
            with open(yaml_path, 'r') as f:
                existing = yaml.safe_load(f) or {}

        # Merge with generated metadata
        updated = {**existing, **metadata}

        # Save
        with open(yaml_path, 'w') as f:
            f.write("---\n")
            yaml.dump(updated, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        print(f"✓ Generated demo for {slug}")
        print(f"  - Schema: {len(metadata['schema'])} fields")
        print(f"  - Starter idea: {metadata['starter_idea'][:60]}...")
        print(f"  - Build ideas: {len(metadata['build_ideas'])} ideas")
        print()

if __name__ == "__main__":
    generate_demo_metadata()
    print("Demo metadata generation complete!")
    print("\nTo see full output:")
    print("  cat data_cards/ai4bharat-samanantar-mr.yaml")
