
# Renkli Görseli Siyah Beyaz Yapma


import cv2 
import numpy as np


# Görseli okuma ve ekranda gösterme

resim = cv2.imread("lena.png")
cv2.imshow("Orjinal Resim",resim)


#gri resmi ekranda gösterme

GriResim = resim[:,:,0]
cv2.imshow("Gri Resim",GriResim)


def siyahBeyazYap(resim,esik):
    en,boy,katman = np.shape(resim) #resmin boyutlarını alıyoruz.

    yeniResim = np.ones((en,boy,katman)) #beyaz bir görsel oluşturuyoruz.

    for i in range(en):

        for j in range(boy):

            if(resim[i,j,0] > esik): #resmin 0.katmanını eşik değer ile karşılaştırıyoruz.

                yeniResim[i,j] = 1

            else:

                yeniResim[i,j]=0

        cv2.imshow("Siyah Beyaz",yeniResim)

siyahBeyazYap(resim,125)

cv2.waitKey()
