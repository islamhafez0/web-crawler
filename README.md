# Web Crawler API

### This app provides a straightforward way to crawl book data from the "Books to Scrape" website and transform it into a structured, paginated API. This setup allows easy access to book information, enabling developers to integrate this data into web applications, mobile apps, or other platforms. 

## usage 
- `pip install scrapy`
- customize your app as needed 
- `scrapy crawl mycrawler(identifier) -o output.json`


## Routes
-  `/api/books?page=<page>&per_page=<per_page>`
-  (Single Book): `/api/books/<book_id>`

`Eslam Hafez`
