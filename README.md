Slant Scraper
===================

Scrapes info from www.slant.co
Only for educational purposes.
Use at own risk, it might violate Slant policies.

- [x] Versus. A comparison of two techs.
- [ ] Options. A detailed description of a particular option.
- [ ] Topics. A comparison of different topics.

# Dependencies
Install: 
* [Scrapy](http://doc.scrapy.org/en/0.24/intro/install.html)

# Tested configuration
* Python 3.6.4 + Scrapy 1.5

# Usage - Have fun!
```shell
cd slant-scraper/
```

Scrape and save data in JSON lines format:
```shell
scrapy crawl main -o output/result.json
```

For JSON format use:
```shell
scrapy crawl main -o output/result.json -t json
```
