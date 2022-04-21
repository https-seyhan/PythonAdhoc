import scrapy
#run as scrapy crawl asxdataextract -o output.csv in the terminal
class AsxDataExtract(scrapy.Spider):
    name='asxdataextract'
    allowed_domains = ["listcorp.com/asx/sectors",] # domains
    start_urls = ["https://www.listcorp.com/asx/sectors/information-technology"]
    #category = 'information-technology'
    #links = {}
    print("Test")
    def parse(self, response):
        query = '//*[@class="v-datatable v-table theme--light"]//tbody/tr'
        #query= '//*[@class ="v-table__overflow"]//tbody/tr'
        urls = response.xpath(query).extract()
        print("URLS!!!!!  ",urls)
