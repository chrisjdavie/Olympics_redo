'''
Created on 23 Oct 2014

@author: chris
'''
import scrapy
from country_medals_c import country_medals

class MedalsSpider(scrapy.Spider):
    name = "medals"
    allowed_domains = ["olympic.it"]
    start_urls = [
        "http://www.olympic.it/english/game/id_W2014"
        ]

    def parse(self, response):
#         filename = response.url.split("/")[-2]
        
        for_cleaning = response.xpath('//table/tr[@valign="top"]/td[@class="testo"]')
        
        for i, a_i in enumerate(for_cleaning):
            test = a_i.xpath('text()').extract()
            if len(test) > 0:
                test = test[0].encode('ascii','ignore')
                if test == '1.': 
                    break
        
        for_cleaning = for_cleaning[i:]
        
        rot = 6
        N = len(for_cleaning)/rot
        for_cleaning = for_cleaning[:N*rot] # not sure about this line - it's meant to remove excess entries, but it's unsophisticated, could probably do this with "the final + 1 entry has italics"
        
        countr_list = []
        
        
        
        for j in range(N):
            print j
            i_0 = j*rot
            rank = int(for_cleaning[i_0+0].xpath('text()').extract()[0].encode('ascii','ignore')[:-1])
            name = for_cleaning[i_0+1].xpath('a/text()').extract()[0]
            
            countr = country_medals(rank,name)
            
            medals = []
            for k in range(3):
                no = int(for_cleaning[i_0+2+k].xpath('text()').extract()[0])
                medals.append(no)
            
            countr.medals_in(medals)
            countr_list.append(countr)
        
        filename = response.xpath('//title/text()').extract()[0][-4:] + '.p'
        import pickle
        
        with open(filename, 'w+') as f:
            pickle.dump(countr_list,f)
            
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class ManySitesMedals(CrawlSpider):
    name = 'all_medals'
    allowed_domains = ['olympic.it']
    start_urls = ['http://www.olympic.it/english/game']

    rules = (

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('/english/game/id_W\d{4}', )), callback='parse_item'),
    )

    def parse_item(self, response):
        
        for_cleaning = response.xpath('//table/tr[@valign="top"]/td[@class="testo"]')
        
        for i, a_i in enumerate(for_cleaning):
            test = a_i.xpath('text()').extract()
            if len(test) > 0:
                test = test[0].encode('ascii','ignore')
                if test == '1.': 
                    break
        
        for_cleaning = for_cleaning[i:]
        
        rot = 6
        N = len(for_cleaning)/rot
        for_cleaning = for_cleaning[:N*rot] # not sure about this line - it's meant to remove excess entries, but it's unsophisticated, could probably do this with "the final + 1 entry has italics"
        
        countr_list = []
        
        
        
        for j in range(N):
            print j
            i_0 = j*rot
            rank = int(for_cleaning[i_0+0].xpath('text()').extract()[0].encode('ascii','ignore')[:-1])
            name = for_cleaning[i_0+1].xpath('a/text()').extract()[0]
            
            countr = country_medals(rank,name)
            
            medals = []
            for k in range(3):
                no = int(for_cleaning[i_0+2+k].xpath('text()').extract()[0])
                medals.append(no)
            
            countr.medals_in(medals)
            countr_list.append(countr)
        
        filename = response.xpath('//title/text()').extract()[0][-4:] + '.p'
        import pickle
        
        with open(filename, 'w+') as f:
            pickle.dump(countr_list,f)

