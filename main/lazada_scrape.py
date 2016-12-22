from bs4 import BeautifulSoup
import requests


#------search query
search = raw_input('search item: ')
print 'SEARCHING...'


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


	print 'Product name: ', ItemName
	print 'Product url: ', ItemUrl
	print 'Product img: ', ItemImg
	print 'Product price: ', ItemPrice
	print 'Product sale: ', ItemSale
	print 'Product old price: ', ItemOldPrice
	print '\n \n'


def Get_Response(pagenum):
	#------------- create a soup
	payload = {'page':str(pagenum), 'q':search}
	r = requests.get('http://www.lazada.com.ph/catalog', params=payload)
	html_doc = r.text
	soup = BeautifulSoup(html_doc, 'html.parser')
	return soup


#------find max pages
soup = Get_Response(1)
SearchItemsTag = soup.find_all('div', {'data-qa-locator' :'product-item'})
pages = soup.find_all('a', {'class' :'c-paging__link'})
pages = [int(page.text) for page in pages]
maxpage = max(pages)
# maxpage = 1

#------loop over pages
SearchTitle = soup.head.title.text
print 'RESULTS FOR "%s" \n \n' % search

count = 0
for pagenum in range(1,(maxpage+1)):
	soup = Get_Response(pagenum)
	SearchItemsTag = soup.find_all('div', {'data-qa-locator' :'product-item'})
	for itemtag in SearchItemsTag:
		Get_Pdt(itemtag)
		count += 1

	choice = raw_input("NEXT PAGE RESULTS? (Enter or y/n): ")
	if (choice=='y' or choice==''):
		pass	
	else:
		break	

print '%d ITEMS FOUND' % count
print 'END OF SEARCH'

#------end