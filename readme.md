
#####This script helps you to clean timestamped subtitle text. It also allows you to transform digits into written numbers (multiple languages) with the help of ‘num2words’, while leaving the digits for the timestamp untouched. 


##Example 
##### text = '[123:123] USA und EU haben keine WSPA damals in 2012 okay ok für z.B. 50% oder 75% z.b.'

##### Output: [123:123] U. S. A. und E. U. haben keine W. S. P. A. damals in zweitausendzwölf O. K. O. K. für zum Beispiel fünfzig Prozent oder fünfundsiebzig Prozent zum Beispiel



#### textReplace()
#####Takes as first argument the .doc file previously processed with docx2txt. And as second argument a dictionary with the word replacements. 

#### findDigit() 
##### Run this function to test if the numbers in your text file get recognized correctly.

#### abbreviation()
##### Assuming you have a data set where abbreviations are capitalized i.e. EU, USA, UEFA – this function takes those abbreviations and puts a sign (default ‘.’) between each letter.

#### toWords() 
##### Takes digits and transforms them into written words, you can change the language by passing a different value for the ‘lang’ parameter. Numbers that are noted in video timestamp notation such as  [12:04] get ignored. 
