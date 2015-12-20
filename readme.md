# Newscraper

## Installation

1. git clone
2. create virtualenv
3. pip install -r requirements.txt

## USAGE

        $ python newscrape.py --help
        usage: newscrape.py [-h] [-o OUTPUT] [-s SITES]
                            [-d DAYSOLD | -D DATE | -t TOTAL] [-p POOLSIZE]
                            keywords

        Scrapes news article links from Indian news websites

        positional arguments:
          keywords              comma separated keywords to search for. eg:
                                newscrape.py "election,national herald"

        optional arguments:
          -h, --help            show this help message and exit
          -o OUTPUT, --output OUTPUT
                                specify output file path. default= ./articles.csv
          -s SITES, --sites SITES
                                comma separated sites to scrape. available options:
                                ndtv,indianexpress default: ALL
          -d DAYSOLD, --daysold DAYSOLD
                                Max days old news to scrape
          -D DATE, --date DATE  Exact date of oldest news to scrape (dd/mm/yyyy)
          -t TOTAL, --total TOTAL
                                total articles to be extracted from each site
          -p POOLSIZE, --poolsize POOLSIZE
                                specify no. of concurrent greenlets
