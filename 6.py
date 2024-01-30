# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:31:23 2023

@author: Omsai
"""
# Tokenization
txt="Welcome to the new year 2023"
x=txt.split()
print(x)

#
import re

def remove_special_characters(text):
    pat=r'[^a-zA-z0-9.,!?/:;\"\'\s]' # other than this are removed
    return re.sub(pat,'', text)

remove_special_characters("007\\ hi ! @ # % * what- are// you doing::?")

#
import re

def remove_special_number(text):
    pattern=r'[^a-zA-z.,!?/:;\"\'\s]' # other than this are removed
    return re.sub(pattern,'', text)

remove_special_number("007\\ hi ! @ # % * what- are// you doing::?")

# 
import re
txt="Welcome to the new year 2023 :;"
x=re.split(r'(?:,|;|\s)*',txt)
print(x)

##  function to remove punctuation
import string

def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text

remove_punctuation('Article: @first sentence of some {important} article!')


"""
Created on Tue May 16 14:52:25 2023

@author: Omsai
"""
'''
r - to count the back slash
^ - except
a-z  -  all letters between a to z
A-Z  -  all letters between A to Z
0-9  -  all digit between 0 to 9
whitespace -  \s
'''
############################
### Stenning #################
'''
process of reducing derived word to their wors steam
remove 'ing' from watching , going
remove 'ed' from watched
remove s/es and ed
PorterStemmer
'''
import nltk
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text

get_stem('going')
get_stem('we are going and eating , watched')

###
line= 'asdf fghj; afed, fjek,asdf, foo'
re.split(r'(?:,|;|\s)\s', line)

###
pattern=r'(?:,|;|\s)\s*'
txt="Welcome to the new year 2023 "
x=re.split(pattern,txt)
print(x)

#### matching the text at the start or end of string
filename='spam.txt'
filename.endswith('.txt')

###
are_name='6 th lane west andheri'
are_name.endswith('west andheri')

###
choices=('https:','ftp')
url='https://www.python.org'
url.startswith(choices)

### Slicing a string
s='ABCDEFGHIJKLM'
print(s[2:7])

print(s[2:7:2])

print(s[-7:-2])

print(s[2:-5])

print(s[6:1:-2])

print(s[6:])

print(s[::-1])          ####  Reverse the string

filename='spam.txt'
filename[-4:]=='.txt'

#
url='https://www.python.org'
url[:5]=='http' or url[:6]=='https' or url[:5]=='https'


"""
Created on Wed May 17 08:20:21 2023

@author: Omsai
"""

from fnmatch import fnmatch,fnmatchcase
# check whether the name is present or not
names=['Dat1.csv','Dat2.csv','config.ini','foo.ini']
[name for name in  names if fnmatch(name,'Dat*.csv')]

###
from fnmatch import fnmatch,fnmatchcase
names=['Andheri East','Parlie East','Dadar West']
[name for name in  names if fnmatch(name,'*East')]

### address end with ST
addresses=['5412 N CLARK ST','1060 W ADDISON ST','1039 W GRANVILLE AVE',
           '2122 N CLARK ST','4802 N BROADWAY']

[name for name in addresses if fnmatch(name,'*ST')]

#############
import string
text='yeah, but no, but yeah, but no, but yeah'
text=='yeah'    # Exact matching
text.startswith('yeah')
text.endswith('no')

text.find('yeah')       # index of yeah

#############################
# match date
text1='11/27/2022'
text2='Nov 27, 2022'

import re
#simple matching : \d+ means matching one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

##############################
text1='11-27-2022'

import re
if re.match(r'\d{2}-\d{2}-\d{4}',text1):
    print('yes')
else:
    print('no')

"""
Created on Wed May 17 14:56:17 2023

@author: Omsai
"""
#### Assignment
txt='This is artificial inteligence era.'
txt.split()

###
text='India : has great, history : in 2023! india; is leading to its? florius future!'
import re
x=re.split(r'(?:,|;|:|!|\s)\s',text)
print(x)

###
text='Rama went to haridwar to get gangajal'
# check the word gangajal
text.endswith('gangajal')

###
#extract date from the text
    
#### searching and replacing text    
import string
text='yeah, but no, but yeah, but no, but yeah'

text.replace('yeah','yap')
 
#######
text2='Today is 17/05/2023 and our exam will start with 03/07/2023'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'(\3-\1-\2)',text2)

####
import re
datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2',text2)

######
newtext,n=datepat.subn(r'\3-\1-\2)',text2)
newtext
n

####### searching and replacing case sensitive text
text='UPPER PYTHON , lower python ,  Mixed Python'
re.findall('PYTHON',text,flags=re.IGNORECASE)
re.sub('python','snake',text,flags=re.IGNORECASE)

"""
Created on Tue May 23 09:20:48 2023

@author: Omsai
"""
# Matched text , If you need to fix this, you might have to use a suitable 

import re
import string
import nltk
text='UPPER PYTHON, lower python ,Mixed Python'
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else :
            return word
    return replace
re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)

#########################
str_pat=re.compile(r'\"(.*)\"')
text1='Computer says "no."'
str_pat.findall(text1)
#Out[12]: ['no.']
text2='Computer says "no." Phone says "yes."'
str_pat.findall(text2)
#Out[17]: ['no." Phone says "yes.']

# In above example there is drawback so we different pattern
str_pat=re.compile(r'\"(.*?)\"')
str_pat.findall(text1)

##########  finding comment in sentence
comment=re.compile(r'/\*(.*?)\*/')
text1='/* this is a comment*/'
comment.findall(text1)

# no output
text2='''/* this is a
    multiline comment */
    '''
comment.findall(text2)

# to overcome above problem we use below code pattern to find multiline comment
comment=re.compile(r'/\*((?:.|\n)*?)\*/')
text2='''/* this is a
    multiline comment */
    '''
comment.findall(text2)

"""
Created on Tue May 23 14:46:32 2023

@author: Omsai
"""
# Removing nummbers from the text
import re
def remove_numbers(text):
    result=re.sub(r'\d+','',text)
    return result
input_str='There are 3 balls in this bag and 12 in the'
remove_numbers(input_str)

'''
pip install inflect
we can also convert numbers to word using  'inflect'
'''
import inflect
p=inflect.engine()

#convert numbers into word
def convert_number(text):
    #split string into list of words
    temp_str=text.split()
    #initialize empty list
    new_string=[]
    for word in temp_str:
        #if word digit , convert
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
            
            #append the word as it is
        else:
            new_string.append(word)
    #join the words of new string to form a string
    temp_str=' '.join(new_string)
    return temp_str

input_str='There are 3 balls in this bag and 12 in the'
convert_number(input_str)           

#### Reverse each word of string
strin='My Name is Jessa'

def reverse_words(text):
    words=text.split(" ")
    new_word=[word[::-1] for word in words]
    
    res_str=" ".join(new_word)
    return res_str

reverse_words(strin)

###### combine all lines in text file into single line 
a=open('sample.txt')
newLine=" "
lines=a.readlines()
for line in lines:
    newLine= newLine +" "+line.rstrip()  

print(newLine)


"""
Created on Wed May 24 14:49:57 2023

@author: Omsai
"""
#################### Unicode
ord('A')
'''
Normalizing Unicode text to standard representation
You're working with Unicode strings , but need to make sure that
all of the strings have the same underlying representation
'''
s1='Spicy Jalape\u00f1o'
s2='Spicy Jalape\u0303o'

print(s1)   #Spicy Jalapeño
print(s2)   #Spicy Jalapẽo
s1==s2      #False

#######
import unicodedata
s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'
t1=unicodedata.normalize('NFC', s1)
t2=unicodedata.normalize('NFC', s2)

t1 == t2
#
print(ascii(t1))    #'Spicy Jalape\xf1o'

t3=unicodedata.normalize('NFD', s1)
t4=unicodedata.normalize('NFD', s2)

t3==t4
print(t3)
print(t4)

#################
t1=unicodedata.normalize('NFC', s1)
''.join(c for c in t1 if not unicodedata.combining(c))  #'Spicy Jalapeño'

##### Working with unicode charcters in regular exprsssion
import re
num=re.compile('\d+')
num.match('123')    #<re.Match object; span=(0, 3), match='123'>

## it is also important to be aware of special cases. 
pat=re.compile('Stra\u00dfe',re.IGNORECASE)
s='straße'
pat.match(s)
pat.match(s.upper())
s.upper()

#### Stripping unwanted charcters from string
# Whitespace stripping
s='     hello world \n'
s.strip()       #'hello world'

s.lstrip()      #'hello world \n'  -> remove left side whitespace

s.rstrip()      #'     hello world'     -> remove right side whitespace

##### Character stripping
t='--------hello========'
t.lstrip('-')
t.rstrip('=')
t.strip('-=')


"""
Created on Thu May 25 08:17:32 2023

@author: Omsai
"""
# Remove all whitespaces
s=' Hello World '
s.replace(' ','')

# Remove whitespaces by re
import re
s=' Hello     World '
re.sub('\s+',' ',s)

###
s = 'pýtĥöñ\fis\tawesome\r\n'  
s

# the first step is to clean up the whitespaces , to do this ,
# make a small traslate  and use translate
s = 'pýtĥöñ\fis\tawesome\r\n'  
remap={
       ord('\t') : ' ',
       ord('\f') : None,
       ord('\r') : None
       }
a=s.translate(remap)
print(a)

'''

'''
import unicodedata
import sys
cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b=unicodedata.normalize('NFD', a)
b
#Out[20]: 'pýtĥöñis awesome\n'
b.translate(cmb_chrs)
b

### another technique to clean text
### involves I/O decoding and encoding functiond
a='pýtĥöñ is awesome\n'
b=unicodedata.normalize('NFD',a)
b.encode('ascii','ignore').decode('ascii')      #Out[33]: 'python is awesome\n'


#########################################
# Aligning the text string
text='Hello World'
text.ljust(20)      #Out[36]: 'Hello World         '

text.rjust(20)      #Out[37]: '         Hello World'

text.center(20)     #Out[38]: '    Hello World     '

##
text.ljust(20,'=')  #'Hello World========='

text.center(20,'*')     #'****Hello World*****'   

#######################
format(text,'>20')      #'         Hello World'

format(text,'<20')      #'Hello World         '

format(text,'=>20')     #'=========Hello World'

format(text,'*^20')     #'****Hello World*****'

'{:>10s} {:>10s}'.format('Hello', 'World')
#Out[47]: '     Hello      World'

"""
Created on Thu May 25 14:52:44 2023

@author: Omsai
"""
x=1.2345
format(x,'>10')
#Out[2]: '    1.2345'
format(x,'^10.2f')
#Out[3]: '   1.23   '

################################
parts=['Is','Chicago','Not','Chicago?']
' '.join(parts)

','.join(parts)

#### another method
a='Is Chicago'
b='Not Chicago'
a+' '+b

###############3
print('{} {}'.format(a,b))

###
print(a+' '+b)

###
a='Hello' 'World'
a

### Interpolating variables in strings
s='{name} has {n} messages'
s.format(name='Gaurav',n=29)

# OR
s='{name} has {n} messages' 
name='Guido'
n=37
s.format_map(vars())

#########
s='Look into my eyes , look into my eyes , the eyes , the eyes,\
 the eyes , not around the eyes , don`t '
import textwrap
print(textwrap.fill(s,10))

print(textwrap.fill(s,25))
#initial_indent
print(textwrap.fill(s,40,initial_indent=' '))   # only indent for first line 
#subsequent_indent
print(textwrap.fill(s,40,subsequent_indent=' '))    # indent for other than first line


"""
Created on Fri May 26 08:21:54 2023

@author: Omsai
"""
### Tokenization

import nltk
nltk.download('punkt')
sen_data='the first sentence is about python . the second sentence is about Django.'
nltk_tokens=nltk.sent_tokenize(sen_data)
print(nltk_tokens)

############ Non-English Tokenization
german_Tokenizer=nltk.data.load('tokenizers/punkt/german.pickle')
german_tokkens=german_Tokenizer.tokenize('Wie geht es Ihnen? Gut, danke.')
print(german_tokkens)

####### Word Tokenization
import nltk
word_data='the first sentence is about python . the second sentence is about Django.'
nltk_tokens=nltk.word_tokenize(word_data)
print(nltk_tokens)

##########
import nltk
nltk.download('stopwords') 

from nltk.corpus import stopwords
stopwords.words('english')

stopwords.words('german')

####
from nltk.corpus import stopwords
print(stopwords.fileids())

##############
from nltk.corpus import stopwords
en_stop=set(stopwords.words('english'))

all_word=['There','is','a','tree','near','the','river']
for word in all_word:
    if word not in en_stop:
        print(word)

##############################
# find synonyms word
import nltk
nltk.download('omw-1.4') 
from nltk.corpus import wordnet
nltk.download('wordnet') 

synonyms=[]

for syn in wordnet.synsets('Soil'):
    for lm in sys.lemmas():
        synonyms.append(lm.name())

print(set(synonyms))

##############################
# find antonyms word
import nltk
nltk.download('omw-1.4') 
from nltk.corpus import wordnet
 
nltk.download('wordnet')

antonyms=[]

for syn in wordnet.synsets('ahead'):
    for lm in sys.lemmas():
        if lm.antonyms():
             antonyms.append(lm.antonyms()[0].name)
             
print(set(antonyms))





