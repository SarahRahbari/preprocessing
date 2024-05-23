# -*- coding: utf-8 -*-
"""NLP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RAnhqPmatZUVR7WwrU9iO3fKNzCeJXmy
"""

import nltk
nltk.download('punkt')

paragragh="""The evolution of technology has been a transformative journey. From the invention of the wheel to the development of the internet, technology has consistently shaped the course of human history. The wheel, one of the earliest technological innovations, revolutionized transportation and facilitated trade, leading to the growth of civilizations.
The invention of the printing press in the 15th century democratized knowledge, making books accessible to the masses and sparking the Renaissance. The Industrial Revolution in the 18th and 19th centuries saw the advent of machines, factories, and railways, drastically altering the socio-economic landscape.

In the 20th century, technology took a quantum leap with the invention of the computer. Initially used for complex calculations, computers have evolved into indispensable tools for various applications, from business and education to entertainment and communication. The development of the internet further accelerated this digital revolution.
Today, the internet connects billions of people worldwide, enabling instant communication, information exchange, and online commerce.

The advent of smartphones has made technology even more ingrained in our daily lives. These handheld devices serve as portable computers, allowing us to browse the internet, send emails, watch videos, and use various apps on the go. The proliferation of social media platforms has also reshaped our social interactions and the way we consume information.

In recent years, we have witnessed the rise of artificial intelligence (AI) and machine learning, technologies that mimic human intelligence and learn from data. AI has found applications in diverse fields, from healthcare and finance to transportation and entertainment.
 For instance, AI algorithms can analyze medical images to detect diseases, predict stock market trends, drive autonomous vehicles, and recommend movies based on our viewing history.

Another promising technology is blockchain, a decentralized and secure digital ledger system. Originally developed for Bitcoin, a cryptocurrency, blockchain has potential applications beyond digital currencies, such as in supply chain management, voting systems, and identity verification.

Virtual reality (VR) and augmented reality (AR) are other emerging technologies that offer immersive experiences. VR transports us to virtual worlds, while AR overlays digital information onto our physical environment. These technologies have applications in gaming, education, real estate, and more.

The field of biotechnology is also advancing rapidly, with breakthroughs in genetic engineering, stem cell research, and personalized medicine. These developments hold the promise of curing genetic diseases, regenerating damaged tissues, and tailoring treatments to individual patients' genetic profiles.

However, the rapid pace of technological advancement also poses challenges. Issues such as data privacy, cybercrime, and digital addiction have emerged. The increasing automation of jobs raises concerns about job displacement and income inequality. Moreover, the environmental impact of technology, particularly e-waste and energy consumption, cannot be overlooked.

Despite these challenges, technology continues to evolve and shape our future. The ongoing research in quantum computing could potentially revolutionize computing power, opening up new possibilities for data processing and encryption.
The exploration of space technology might pave the way for space tourism and colonization of other planets. The development of nanotechnology could lead to new materials and therapies at the molecular level.

In conclusion, the evolution of technology is a testament to human ingenuity and curiosity. While it brings immense benefits, it also presents challenges that we must address responsibly. As we stand on the brink of new technological frontiers, it is crucial to navigate this journey with foresight and wisdom, ensuring that technology serves humanity's best interests."""

# Tokenizing sentences
sentences = nltk.sent_tokenize(paragragh)
sentences

# Tokenizing word
word = nltk.word_tokenize(paragragh)
word

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')

stemmer = PorterStemmer()
# Stemming
for i in range(len(sentences)):
  words = nltk.word_tokenize(sentences[i])
  words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
  sentences[i] = ' '.join(words)

sentences[1]

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
sentencess = nltk.sent_tokenize(paragragh)

#lemmatization
for i in range(len(sentencess)):
  words = nltk.word_tokenize(sentencess[i])
  words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
  sentencess[i]=' '.join(words)

sentencess[1]

# cleaning the tests
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragragh)
corpus = []
for i in range (len(sentences)):
  review = re.sub('[^a-zA-z]',' ',sentences[i])
  review = review.lower()
  review = review.split()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus.append(review)

  # creatng the bag of words model
  from sklearn.feature_extraction.text import CountVectorizer
  cv = CountVectorizer(max_features = 1500)
  x = cv.fit_transform(corpus).toarray()

x

sentencess = nltk.sent_tokenize(paragragh)
corpus = []
for i in range (len(sentences)):
  review = re.sub('[^a-zA-z]',' ',sentencess[i])
  review = review.lower()
  review = review.split()
  review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus.append(review)

  # creatng the TF-IDF model
  from sklearn.feature_extraction.text import TfidfVectorizer
  tf = TfidfVectorizer()
  x = tf.fit_transform(corpus).toarray()

x