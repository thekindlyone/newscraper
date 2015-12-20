import gevent
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
from gevent.queue import Queue
from os.path import exists,splitext,dirname
import os
import csv
from itertools import product
from commons import *
from sites import *
import argparse

scribe_q = Queue()


def crawler(args):
    try:
        site,keyword,newer_than,total = args
        print "started {} {}".format(site,keyword)
        scraper=scrapers[site]()
        if not newer_than and not total:
            total=20
        url=scraper.url(keyword)
        params=scraper.params(keyword)
        t=1
        while True:
            with gevent.Timeout(60, False):
                soup,referer=get_soup(url, params)
            data = scraper.extract_articles(soup)
            for item in data:
                date=datetime.strptime(item['date'],scraper.time_format)
                item['date']=date.strftime('%B %d, %Y %I:%M %p')
                item['referer']=referer
                item['keyword']=keyword
                if newer_than and date <= newer_than:
                    return '{} {} Exit Clause: Date'.format(site,keyword)
                scribe_q.put(item)
                t+=1
            if total and t>=total:
                break
            
            url=handle(lambda: scraper.next_page(soup))
            if not url:
                return '{} {} Exit Clause: Exhausted Results'.format(site,keyword)
            params=None
        print "finished {} {}".format(site,keyword)
    except:
        traceback.print_exc()
        print url



def scribe(filename):
    # if not os.path.exists(filename):
    donelist=[]
    directory=dirname(filename)
    if directory and not exists(directory):
        os.makedirs(directory)
    c=0
    fn,ext = splitext(filename)
    while exists(filename):
        c+=1
        filename = '{}{}'.format(fn,c)+ext

    with open(filename,'w') as f:
        writer = csv.DictWriter(f, fieldnames=fields, dialect='excel', restval="N/A")
        writer.writeheader()    
        while True:
            data = scribe_q.get()
            if data == 'quit':
                break
            if data['url'] not in donelist:
                writer.writerow({k.encode('utf-8'):v.encode('utf-8').replace(';',',') for k,v in data.iteritems()})
                donelist.append(data['url'])
    print 'written {} records to {}'.format(len(donelist),filename)




    

def main():
    parser=argparse.ArgumentParser(
        description="Scrapes news article links from Indian news websites")    

    parser.add_argument('keywords',help='''
comma separated keywords to search for. eg:
newscrape.py "election,national herald"
        ''')

    parser.add_argument('-o','--output',help='specify output file path. default= ./articles.csv',default='articles.csv')
    
    parser.add_argument(
        '-s','--sites',
        help='comma separated sites to scrape. available options: {}\n default: ALL'.format(','.join(scrapers.keys())))
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d','--daysold',help='Max days old news to scrape',type=int)
    group.add_argument('-D','--date',help='Exact date of oldest news to scrape (dd/mm/yyyy)')
    group.add_argument('-t','--total',help='total articles to be extracted from each site')
    
    parser.add_argument('-p','--poolsize',help='specify no. of concurrent greenlets',type=int,default=5)


    args=parser.parse_args()
    newer_than = None

    if args.daysold:
        delta = timedelta(days=args.daysold)
        newer_than=datetime.now()-delta
    if args.date:
        newer_than=datetime.strptime(args.date,'%d/%m/%Y')
    
    keywords=[k.strip() for k in args.keywords.split(',')]
    if args.sites:
        sites = [s.strip() for s in args.sites.split(',')]
    else:
        sites = scrapers.keys()

    gevent.spawn(scribe,args.output)

    if args.poolsize>15:
        args.poolsize=15
    pool=Pool(args.poolsize)
    jobs = ([site,keyword,newer_than,args.total] for keyword,site in product(keywords,sites))
    output = pool.map(crawler,jobs)
    scribe_q.put('quit')
    print '*'*20,"\nREPORT\n",'*'*20
    for l in output:
        print l

if __name__ == '__main__':
    main()


