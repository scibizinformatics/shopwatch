from bs4 import BeautifulSoup
import requests

def Get_Pdt(ItemTag):
	#------get product info
	ItemUrl = ItemTag.a['href']
	ItemImgTag = ItemTag.a.find_all('img')

	for img in ItemImgTag:
		try:
			ItemName = img['alt']
			ItemImg = img['data-original']
			ItemPrice = ItemTag.find('div', {'class' :'product-card__price'}).text
			ItemSale = ItemTag.find('div', {'class' :'product-card__sale'}).text
			ItemOldPrice = ItemTag.find('div', {'class' :'product-card__old-price'}).text

		except (KeyError):
			pass

		except (AttributeError):
			ItemSale = 'No Sale'
			ItemOldPrice = 'None'

	return {
		'pdt_name': ItemName,
		'pdt_url': ItemUrl,
		'pdt_img': ItemImg,
		'pdt_price': ItemPrice,
		'pdt_sale': ItemSale,
		'pdt_old_price': ItemOldPrice,
	}


def Get_Response(pagenum, search):
	#------------- create a soup
	payload = {'page':str(pagenum), 'q':search}
	r = requests.get('http://www.lazada.com.ph/catalog', params=payload)
	html_doc = r.text
	soup = BeautifulSoup(html_doc, 'html.parser')
	return soup


def Scrape_Lazada(search_query):
	#------search query
	search = search_query

	# #------find max pages
	# soup = Get_Response(1)
	# SearchItemsTag = soup.find_all('div', {'data-qa-locator' :'product-item'})
	# pages = soup.find_all('a', {'class' :'c-paging__link'})
	# pages = [int(page.text) for page in pages]
	# maxpage = max(pages)
	maxpage = 1

	RESULTS = []
	for pagenum in range(1,(maxpage+1)):
		soup = Get_Response(pagenum, search)
		SearchItemsTag = soup.find_all('div', {'data-qa-locator' :'product-item'})
		
		for itemtag in SearchItemsTag:
			RESULTS.append(Get_Pdt(itemtag))
	return RESULTS

#------end