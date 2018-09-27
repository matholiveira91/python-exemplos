#!/usr/bin/python3
#pip install wordcloud antes de tudo
import numpy as np
from PIL import Image
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import tkinter
#REFERENCES INDIAN PYTHONISTA
#REFERENCES UMANGAHUJA1
def create_wc(text):
    mask = np.array(Image.open('cloud.jpg'))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white", mask = mask).generate(text)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
       
    
texto="Somos uma organização regional sem fins lucrativos do Rio Grande do Norte. Temos a finalidade de reunir toda a comunidade ao redor de eventos que enriqueçam nosso trabalho e nosso conhecimento, fornecendo assim um canal direto com profissionais da área."

create_wc(texto)
