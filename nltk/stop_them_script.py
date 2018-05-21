from csvencode import csvencode

from stop_words import get_stop_words

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#these downloads are required the first time run
#nltk.download('stopwords')
#nltk.download('punkt')

import csv
import codecs

#creates stop word list
stop_words = list(get_stop_words('en'))         #About 900 stopwords
nltk_words = list(stopwords.words('english')) #About 150 stopwords
stop_words.extend(nltk_words)

#to use this options, make a custom file in the nltk_data/corpora/stopwords/ directory
custom_words = list(stopwords.words('custom')) #About 150 stopwords
stop_words.extend(custom_words)


#opens data
filepath_input = "./stop_them.csv"
f = codecs.open(filepath_input, "r", "utf-8")
sample_data = f.read()
f.close()

#tokenisation of words
words = word_tokenize(sample_data)

#removes standard stop words
clean_data = []
for w in words:
    if w not in stop_words:
        clean_data.append(w)


#print sample_data
print clean_data
print len(sample_data)
print len(clean_data)


filepath_output = "./clean.csv"
f = codecs.open(filepath_output, "w", "utf-8")
for word in clean_data :
	_word = word + "\n"
	f.write(_word)
f.close()

csvencode(filepath_output)

