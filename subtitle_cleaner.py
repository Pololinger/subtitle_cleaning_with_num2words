import re 
from num2words import num2words
import docx2txt



test = ' Und der Punkt ist Okay'

file = docx2txt.process("1-hkOiiUCSF28.docx")

ausnahmen = {'okay': 'O. K.',
			 'ok': ' O. K. ',
			 '%':' percent',
			 '€':'euro',
			 '$ ':'dollar',
			 'no.':'number',
			 '#': 'hashtag',
			 'approx.': 'approximately',
			 }


def main(text):	 
	num_reg = r'(?<!\S)\d+(?!\S)'
	text = textReplace(text, ausnahmen)
	text = abbreviation(text) 
	text = re.sub(num_reg, lambda m: num2words(m.group(), lang ='en'), text)
	
	
	with open("output.txt", "w") as text_file:
		print(text, file=text_file)


def textReplace(text, wordDict):
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text


def abbreviation(text):
	r = '(?<=[A-Z])(?=[A-Z])|(?<=[A-Z]{2}) ?'
	text = re.sub(r,'. ', text)
	return text


def findDigit(text):
	
	num_reg = r'(?<=\s)\d+(?=\s)'						
	digits  = re.findall(zahlen_reg, text)  ### Find
	print(digits) 


def toWords(text):
	num_reg = r'(?<!\S)\d+(?!\S)'
	text = re.sub(num_reg, lambda m: num2words(m.group(), lang ='en'), text)   ### Other languages incldue 'de', 'dk', 'es', 'fr', 'it', 'tr'
																			   ###  Check num2words documentation for more languages
	return text


	
main(file)