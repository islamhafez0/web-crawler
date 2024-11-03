from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
  name = "mycrawler"
  allowed_domains = ["toscrape.com"]
  start_urls = ["http://books.toscrape.com"]

  rules = (
    Rule(LinkExtractor(allow="catalogue/category")),
    Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
  )

  def parse_item(self, response):
    yield {
      "title": response.css(".product_main h1::text").get(),
      "price": response.css(".price_color::text").get(),
      "availability": response.css(".availability::text").getall()[1].strip(),  
      "category": response.css("ul.breadcrumb li a::text").getall()[-1].strip(),
      "description": response.css("#product_description + p::text").get(),
      "img_url": response.urljoin(response.css(".item.active img::attr(src)").get())
    }