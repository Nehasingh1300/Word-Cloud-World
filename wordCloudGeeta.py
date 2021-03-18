from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt #to display our wordcloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image

#Content-related
text = open('Bhagavad-gita_As_It_Is.txt', 'r', encoding="utf8").read()
stopwords = ["Copyright", "one", "Int'l","Email", "Kåñëa","Lord","TRANSLATION", "Reserved", "PURPORT", "Bhaktivedanta", "Book", "ca", "TEXT", "na", "thus","mode", "called", "may"] + list(STOPWORDS)
#stopwords = set(STOPWORDS)

#Appearance-related
custom_mask = np.array(Image.open('book.png'))
wc = WordCloud(background_color = 'white',
               stopwords = stopwords,
               max_words=1000,
               min_font_size=5,
               mask = custom_mask,
               contour_width = 3,
               contour_color = 'black')

wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

#Plotting
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

wc.to_file('geeta1.png')