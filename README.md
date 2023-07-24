# Coinmarketcap Spider

This is a Scrapy spider project designed to scrape data from the [CoinMarketCap](https://coinmarketcap.com) website. The spider extracts information about cryptocurrencies' names, symbols, and values from the top section of the website. It then iterates over all the pages to collect data from each page.

## Requirements

To run the Coinmarketcap Spider, you need to have the following installed:

- Python (3.6 or above)
- Scrapy (2.5.1 or above)

## Installation

1. Clone the repository or download the spider file `coinmarketcap_spider.py` from this project.

`git clone https://github.com/your_username/coinmarketcap-spider.git`

2. Install Scrapy using pip (if not already installed).

`pip install scrapy`

## Usage

1. Navigate to the project directory containing `coinmarketcap_spider.py`.

2. To run the spider, use the following command:

`scrapy crawl coinmarketcap_spider -o output_file.json`

Replace `output_file.json` with the desired filename to save the scraped data in JSON format. You can use other output formats like CSV or XML as well.

## Spider Details

### Spider Name

- `coinmarketcap_spider`

### Allowed Domains

- `coinmarketcap.com`

### Start URLs

- `https://coinmarketcap.com`

### Data Extraction

The spider extracts the following information from each page:

- Cryptocurrency Name (`name`)
- Cryptocurrency Symbol (`symbol`)
- Cryptocurrency Value (`value`)

### Pagination

The spider handles pagination by looking for the "Next Page" link and following it to scrape data from all available pages.

### Data Cleaning

The spider cleans the extracted `value` data to ensure it contains only the float numbers, removing any commas used as thousand separators.

## Disclaimer

This spider is intended for educational purposes and scraping publicly available data from the CoinMarketCap website. Before scraping any website, make sure to review its terms of service and robots.txt file to ensure you are not violating any rules. Always be respectful of the website's server resources and avoid overloading their servers with too many requests.
