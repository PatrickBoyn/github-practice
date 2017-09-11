from lxml import html
import requests


def scraper(language, word):
	language
	word

	#gets the webpage you're looking for, language and word are passed as part of the funciton
	#to make this easier to deal with, two things are easier to type than a whole website
	page = requests.get('http://www.wordreference.com/' + language + word)
	tree = html.fromstring(page.content)

	#tells the program what words to look for
	words = tree.xpath('//strong/text()')
	definitions = tree.xpath('//td[@class ="ToWrd"]/text()')

	#prints the definitions to as a test
	#in case something goes wrong, and so I know it is working
	print(definitions[1])

	#prints the words you searched for
	print(words[1]) 


	
def printer():
 	works = scraper("enzh/", "cow")
 	f = open(r'C:\Users\dakil\Desktop\Chinese.txt', 'a')
 	f.write(works)
	f.close()

try:
	scraper("enzh/", "cow")
except Exception as e:
	print(' ')
	print('-----')
	print('ERROR')
	print('-----')
	print(' ')
	print(e)