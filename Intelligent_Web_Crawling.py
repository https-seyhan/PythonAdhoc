import scrapy

#run as scrapy crawl asxdataextract -o output.csv in the terminal
class AsxDataExtract(scrapy.Spider):
    name='asxdataextract' #name of the crawl
    allowed_domains = ["listcorp.com/asx/sectors",] # domain(s) to crawl
    start_urls = ["https://www.listcorp.com/asx/sectors/information-technology"] #start url
    #category = 'information-technology'
    #links = {}
    def parse(self, response):
        query = '//*[@class="v-datatable v-table theme--light"]//tbody/tr' #location to scrap data
        #query= '//*[@class ="v-table__overflow"]//tbody/tr'
        urls = response.xpath(query).extract()
        print("URLS!!!!!  ",urls)
