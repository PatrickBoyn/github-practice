from lxml import html
import requests

#The lxml bits are not my own, however, the Scraper function is
#This was written in part with a website that had a tutorial on
#scraping with lxml, and I found it to be the easiest option I tried
#I am a language learner, and I use a program called Anki that allows for 
#importing text files of lists of words either seperated by space or comma
#This is meant to save time, all I will eventually have to do is to give the language
#and the word I am searching for once and it will be automatically added to the 
#text file when adding words to something like a flash card file, you have to write them over
#and over, and this seemed like a far simpler thing to do since I had some programming knowledge

def Scraper(language, word):
	#Will be the way you enter the language and the word
	#you are looking for. en, then the abbreviation of the language
	#prints the non english language first however if you want it to do it
	#the other way around, simply switch en, and the other abrreviation
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

Scraper('enzh/', 'dog')
