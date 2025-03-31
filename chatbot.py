import urllib
import bs4 as bs
import re
import nltk
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize

nltk.download('punkt');
nltk.download('stopwords');

art_text = urllib.request.urlopen('https://en.wikipedia.org/wiki/IPhone_14').read();
art_pars = bs.BeautifulSoup(art_text,'lxml')
eth = ''

for p in art_pars.find_all('p'):
  eth += p.text.lower()
eth = re.sub(r'\s+', ' ',re.sub(r'\[[0-9]*\]', ' ',eth));
senlist = nltk.sent_tokenize(eth);
# print(senlist)


def answer(question):
  tokques = word_tokenize(question);
  nosw= [word.lower() for word in tokques if not word in stopwords.words()]
  whw = ['what', 'when', 'where', 'who', 'whom', 'which', 'whose', 'why' , 'how'];
  for wh in whw:
    for qus in nosw:
        if wh == qus:
            nosw.remove(wh)
  joined = (" ").join(nosw);
  print(joined)
  senlist.append(joined)
  vectorizer = TfidfVectorizer()
  sen_vectors = vectorizer.fit_transform(senlist);
  vector_values = cosine_similarity(sen_vectors[-1],sen_vectors);
  ans = senlist[vector_values.argsort()[0][-2]]
  chk = vector_values.flatten()
  chk.sort()
  senlist.remove(joined)

  if chk[-2] == 0:
    return "Sorry, don't know that";
  else:
    return ans
