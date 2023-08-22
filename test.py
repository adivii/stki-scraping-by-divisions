import modules.scraping as scraper

soup = scraper.parsePage(scraper.getDriver(), 'https://stackoverflow.com/questions/52389692/beautifulsoup-and-prettify-function')

x = soup.select('#question-header > h1 > a')

print(x[0]['href'])