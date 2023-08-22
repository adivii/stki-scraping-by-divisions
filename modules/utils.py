import modules.scraping as scraper

def getKodeProdi():
  url = 'http://repository.lppm.unila.ac.id/view/divisions/'

  scrap_result = scraper.parsePage(scraper.getDriver(), url)
  cat = scraper.getDivisionLink(scrap_result, '#content > div > ul > li > ul > li > ul > li > a')

  return cat

def getYears(kodeProdi):
  url = f'http://repository.lppm.unila.ac.id/view/divisions/{kodeProdi}/'
  scrap_result = scraper.parsePage(scraper.getDriver(), url)
  years = scraper.getYear(scrap_result, '#content > div > ul > li > a')

  return years