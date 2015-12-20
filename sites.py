from commons import *

fields = 'date keyword headline url intro referer'.split()


class NdtvScraper(object):
    
    def __init__(self):
        self.url= lambda keyword:'http://www.ndtv.com/topic/{}/news/page-1'.format('-'.join(keyword.split()))
        self.params= lambda keyword: None
        self.time_format='%A %B %d, %Y'

    def extract_articles(self,soup):
        data=(dict(
            url=li.find('a').get('href'),
            intro=li.find('p','intro').text.strip(),
            date=li.find('p','list_dateline').text.split('|')[-1].strip(),
            headline=li.find('a').text,
            )for li in soup.select('div#news_list > * > ul > li'))
        return data

    def next_page(self,soup):
        url=soup.find('div',id='inside_pagination').find('a',href=True,text=re.compile('Next')).get('href')
        return url



class IndianExpressScraper(object):
    
    def __init__(self):
        self.url= lambda keyword:'http://indianexpress.com'
        self.params= lambda keyword: dict(s=keyword)
        self.time_format='%B %d, %Y at %I:%M %p'

    def extract_articles(self,soup):
        data=(dict(
            url=details.find('a',href=True,title=True).get('href'),
            date=re.search('Updated: (.+)?',details.find('time').text).group(1),
            headline=details.find('a',title=True).get('title'),
            intro=details.p.text
            )
            for details in soup.select('div.search-result > div.details '))
        return data

    def next_page(self,soup):
        url=soup.find('a',class_='next',href=True).get('href')
        print url
        return url
    




scrapers = dict(
    indianexpress=IndianExpressScraper,
    ndtv=NdtvScraper)