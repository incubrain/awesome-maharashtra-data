#!/usr/bin/env python3
"""
01_agri_advisory_quickstart.py — Starter script for agricultural advisory AI.

Demonstrates loading and exploring Maharashtra agriculture datasets:
1. ICRISAT District Level Database (crop + irrigation data)
2. AgMarkNet mandi price data (via CEDA API)
3. IMD gridded rainfall data exploration

Run with: python 01_agri_advisory_quickstart.py

Requirements: pip install pandas requests matplotlib
"""

import sys

try:
    import pandas as pd
    import requests
except ImportError:
    print("Install dependencies: pip install pandas requests matplotlib", file=sys.stderr)
    sys.exit(1)


def demo_icrisat_dld():
    """Explore ICRISAT District Level Database structure."""
    print("=" * 60)
    print("1. ICRISAT District Level Database")
    print("=" * 60)
    print("""
    Source: http://data.icrisat.org/dld/
    License: CC-BY-4.0
    Coverage: 571 districts, 1966-2020, 1030 variables

    Key datasets for Maharashtra agriculture:
    - Crop area, production, yield by district
    - Irrigation coverage and sources
    - Fertilizer consumption
    - Agricultural GDP

    To download:
    1. Visit http://data.icrisat.org/dld/
    2. Select Maharashtra state
    3. Choose variables (e.g., rice area, wheat production)
    4. Download as Excel/CSV

    Example analysis: Compare crop yield trends across
    Maharashtra districts with rainfall correlation.
    """)


def demo_agmarknet_prices():
    """Demonstrate AgMarkNet price data access."""
    print("=" * 60)
    print("2. AgMarkNet Daily Mandi Prices")
    print("=" * 60)
    print("""
    Source: https://agmarknet.gov.in/
    Cleaned API: https://agmarknet.ceda.ashoka.edu.in/
    License: Government Open Data License

    Maharashtra APMC markets report daily prices for:
    - Cereals (rice, wheat, jowar, bajra)
    - Pulses (tur, moong, urad)
    - Oilseeds (soybean, groundnut)
    - Vegetables, fruits, spices
    - Cotton, sugarcane

    Example: Fetch soybean prices from Latur mandi
    """)

    # Example API call (CEDA Ashoka cleaned data)
    print("  Fetching sample commodity list...")
    try:
        resp = requests.get(
            "https://agmarknet.ceda.ashoka.edu.in/api/commodities",
            timeout=10,
        )
        if resp.ok:
            data = resp.json()
            commodities = data if isinstance(data, list) else data.get("results", [])
            print(f"  Found {len(commodities)} commodities available")
            if commodities:
                for c in commodities[:5]:
                    name = c if isinstance(c, str) else c.get("name", c.get("commodity", str(c)))
                    print(f"    - {name}")
                print("    ...")
        else:
            print(f"  API returned status {resp.status_code} (may require different endpoint)")
    except Exception as e:
        print(f"  Could not reach API: {e}")
        print("  Visit https://agmarknet.ceda.ashoka.edu.in/ for interactive access")


def demo_imd_rainfall():
    """Describe IMD gridded rainfall data."""
    print("\n" + "=" * 60)
    print("3. IMD Gridded Rainfall Data")
    print("=" * 60)
    print("""
    Source: https://www.imdpune.gov.in/cmpg/Griddata/Rainfall_25_NetCDF.html
    License: Government Open
    Resolution: 0.25° x 0.25° (~25km grid), daily, 1901-2024

    Maharashtra bounding box: 15.6°N-22.1°N, 72.6°E-80.9°E

    To use:
    1. Download NetCDF files from IMD Pune
    2. Extract Maharashtra grid cells using xarray:

    ```python
    import xarray as xr

    ds = xr.open_dataset("RF25_ind2023_rfp25.nc")
    mh = ds.sel(lat=slice(15.6, 22.1), lon=slice(72.6, 80.9))
    mh_annual = mh["rf"].resample(time="1Y").sum()
    mh_annual.mean(dim=["lat", "lon"]).plot()
    ```

    AI Use Cases:
    - Monsoon onset prediction
    - Drought early warning for kharif crops
    - Crop-weather correlation models
    - Irrigation scheduling optimization
    """)


def main():
    print("Awesome Marathi Datasets — Agri Advisory Quickstart")
    print("=" * 60)
    print()

    demo_icrisat_dld()
    demo_agmarknet_prices()
    demo_imd_rainfall()

    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("""
    1. Download ICRISAT data for your target districts
    2. Merge with IMD rainfall for crop-weather analysis
    3. Add AgMarkNet prices for market intelligence
    4. Build a simple advisory model:
       Input: district, crop, season, soil type
       Output: yield forecast, price prediction, irrigation advice

    Full dataset catalog: ../categories/05-agriculture-rural.md
    Data cards: ../data_cards/
    """)


if __name__ == "__main__":
    main()
