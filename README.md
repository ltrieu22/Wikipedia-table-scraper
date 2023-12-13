# Wikipedia table scraper

Python script designed to scrape the first table from any given Wikipedia page and export it as a CSV file.

# Features
- CSV Export: Converts the scraped table data into CSV file, using either comma or semicolon as a delimiter.
- Generates CSV file name based on the wikipedia page title.

# How does it work?
1. URL Input: User specifies the URL of the Wikipedia page.
2. Table scraping: The sccript uses BeautifulSoup4 (bs4) to parse the HTML and extract data from the first table found.
3. Captured data will be structured in a Pandas DataFrame.
4. User can specify a delimiter (comma or semicolon) for CSV file
5. The DataFrame is saved as a CSV file, which is named after the Wikipedia page's title. The CSV file will be saved to the same directory as your Python script

# Installation
1. Install Python along with packages `beautifulsoup4`, `pandas`, and `requests`.
2. Run the script in the project directory using a Wikipedia URL.

# Usage example
```
url = 'https://en.wikipedia.org/wiki/List_of_largest_Italian_companies'
df = scrape_wikipedia_table(url)
csv_filename = extract_filename(url)
df.to_csv(csv_filename, index=False, sep=';')  # Adjust the delimiter as per requirement
