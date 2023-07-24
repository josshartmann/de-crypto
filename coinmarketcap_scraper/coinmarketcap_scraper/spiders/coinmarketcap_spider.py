import scrapy
import re


class CoinmarketcapSpiderSpider(scrapy.Spider):
    name = "coinmarketcap_spider"
    allowed_domains = ["coinmarketcap.com"]
    start_urls = ["https://coinmarketcap.com"]

    def parse(self, response):
        names = response.css(".kKpPOn::text").getall()
        symbols = response.css(".coin-item-symbol::text").getall()
        values = response.css(".iVdfNf span::text").getall()

        for name, symbol, value in zip(names, symbols, values):
            value = re.search(r"[\d,.]+", value)
            value = float(value.group().replace(",", "")) if value else None

            yield {
                "name": name.strip(),
                "symbol": symbol.strip(),
                "value": value,
            }

        # Check if there's a next page and follow the link
        next_page_link = response.css("li.next a.chevron::attr(href)").get()
        if next_page_link:
            yield scrapy.Request(response.urljoin(next_page_link), callback=self.parse)
