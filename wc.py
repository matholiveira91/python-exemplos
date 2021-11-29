#!/usr/bin/python3
#pip install wordcloud antes de tudo
import numpy as np
from PIL import Image
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt 

#REFERENCES INDIAN PYTHONISTA
#REFERENCES UMANGAHUJA1
def create_wc(text):
    mask = np.array(Image.open('mobi.png'))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white", mask = mask).generate(text)
    plt.imshow(wc)
    plt.axis('off')
    #plt.show()
    
    wc.to_file("wc.png")
   
       
    
at=open('LICENSE','r')
for t in  at:
    create_wc(t)
