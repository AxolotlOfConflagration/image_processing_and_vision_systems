import matplotlib as plt
import numpy as np
import cv2

def graphical_interpetation():
    img = cv2.imread("put.png")
    cv2.imshow("image", img)
    hist = cv2.calcHist([img], [0], None, [256], [0,256])
    plt.plot(hist)
    plt.xlim(0,255)
    plt.show()
    key = cv2.waitKey(0)

def histogram_alignment():
    img = cv2.imread("put.png")
    cv2.imshow('img', img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(img)
    cv2.imshow('equalized img', equalized)
    hist = cv2.calcHist([equalized], [0], None, [256], [0,256])
    plt.plot(hist)
    plt.ylim(0,256)
    plt.show()
    key = cv2.waitKey(0)

def histogram_rgb():
    img = cv2.imread("2.jpeg",)
    cv2.imshow("image", img)
    color = ('r', 'g', 'b')
    for channel, c in enumerate(color):
        hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
        plt.subplot(1,3, channel+1)
        plt.title('Channel {}, color {} '.format(channel, c))
        plt.plot(hist, color = c)
        plt.xlim([0, 256])

    plt.show()
    key = cv2.waitKey(0)
