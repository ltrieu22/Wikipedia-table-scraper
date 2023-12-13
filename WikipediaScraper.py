import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_wikipedia_table(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})
    if table is None:
        table = soup.find('table')
        if table is None:
            return pd.DataFrame()

    headers = table.find_all('th')
    column_titles = [header.text.strip() for header in headers]

    df = pd.DataFrame(columns=column_titles)

    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]

        if len(row_data) == len(df.columns):
            df.loc[len(df)] = row_data
        else:
            pass

    return df

# Extract filename from URL
def extract_filename(url):
    filename = url.split('/')[-1]  # Get the last part of the URL
    return filename.replace('_', ' ') + '.csv'

# Example usage
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
df = scrape_wikipedia_table(url)

# Save to a CSV file with semicolon as delimiter
csv_filename = extract_filename(url)
df.to_csv(csv_filename, index=False, sep=';')  # Use semicolon as the delimiter
print(f"Data saved to {csv_filename}")

# Print DataFrame
print(df.head(10))
