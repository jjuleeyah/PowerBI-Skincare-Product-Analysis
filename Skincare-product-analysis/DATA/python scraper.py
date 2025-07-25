import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL structure
base_url = "https://peronabeauty.com/product-category/skin-care/face-neck/serums-treatment/page/{}/?orderby=date"

# List to hold extracted data
products = []

# Loop through all 10 pages
for page in range(1, 11):
    print(f"Scraping page {page}...")
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all product containers
    items = soup.select("li.product")

    for item in items:
        # Extract product name
        name = item.select_one("h2.woocommerce-loop-product__title")
        name = name.get_text(strip=True) if name else None

        # Extract product price
        price = item.select_one("span.woocommerce-Price-amount")
        price = price.get_text(strip=True) if price else None

        products.append({
            "Name": name,
            "Price": price,
            "Page": page
        })

# Convert to DataFrame
df = pd.DataFrame(products)

# Save to CSV
df.to_csv("perona_serums.csv", index=False)
print("✅ Scraping complete. Data saved to 'perona_serums.csv'")
