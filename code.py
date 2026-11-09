"""
Project: Real Estate Property Data Collector
Author: Jahanzaib
Description: Automated web scraper designed to parse property listings, 
             extract pricing, location metrics, and agent contact attributes, 
             and serialize them into a structured Excel workbook.
"""

import sys
import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Configure execution pipeline logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Target: Quotes To Scrape (Quotes as mock properties for robust pipeline testing)
# Note: You can easily swap this URL with any live real-estate portal target DOM structure.
BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_FILENAME = "real_estate_leads_export.xlsx"

def extract_property_leads():
    """Fetches target listing pages, parses DOM nodes for property attributes,
    and returns a normalized list of records."""
    property_records = []
    
    logging.info("Initializing Real Estate data ingestion pipeline...")

    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        logging.error(f"Network transport failure: {err}")
        return property_records

    # Parse raw markup payload
    soup = BeautifulSoup(response.text, "html.parser")
    listing_cards = soup.find_all("div", class_="quote")
    
    if not listing_cards:
        logging.warning("No listing nodes resolved in target DOM tree.")
        return property_records

    for idx, card in enumerate(listing_cards, start=1):
        # Extract property description / title equivalent
        title = card.find("span", class_="text").text.strip()
        
        # Extract pseudo-agent / listing owner name
        agent_name = card.find("small", class_="author").text.strip()
        
        # Simulate property pricing based on index logic for pipeline demonstration
        estimated_price_usd = 150000 + (idx * 25500)
        
        # Extract category tags as proxy for property amenities/features
        amenities = [tag.text for tag in card.find_all("a", class_="tag")]
        amenities_formatted = ", ".join(amenities) if amenities else "Standard"

        # Append normalized dictionary record matching real estate schema
        property_records.append({
            "Listing ID": f"PROP-10{idx}",
            "Property Description": title,
            "Listing Agent": agent_name,
            "Valuation (USD)": estimated_price_usd,
            "Amenities / Features": amenities_formatted,
            "Market Status": "Active"
        })

    logging.info(f"Ingestion successful. Total property leads harvested: {len(property_records)}")
    return property_records

def export_leads_to_spreadsheet(records):
    """Serializes property dataset into a clean formatted spreadsheet."""
    if not records:
        logging.warning("Dataset buffer is empty. Skipping spreadsheet serialization.")
        return

    logging.info("Compiling records into pandas DataFrame...")
    dataframe = pd.DataFrame(records)

    # Flush dataframe directly to Excel without internal index column
    dataframe.to_excel(OUTPUT_FILENAME, index=False)
    logging.info(f"Pipeline complete. Spreadsheet persisted to disk: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    harvested_data = extract_property_leads()
    export_leads_to_spreadsheet(harvested_data)
