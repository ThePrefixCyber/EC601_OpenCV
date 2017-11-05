#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:40:20 2017

@author: Jack
"""

import cv2
import sys
import numpy as np

def Add_salt_pepper_Noise(srcArr, pa, pb):
    
    row,col = srcArr.shape
    

    
    out = np.copy(srcArr)
    
    # Salt mode
    
    num_salt = np.ceil(row * col * pa)    
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in srcArr.shape]
    out[coords] = 255
    
    # Pepper mode
    num_pepper = np.ceil(row * col * pb) 
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in srcArr.shape]
    out[coords] = 0
    return out
    
    
def Add_gaussian_Noise(srcArr, mean, sigma):
    
    
    
    row,col = srcArr.shape
    gauss = np.random.normal(mean,sigma,(row,col))
    gauss = gauss.reshape(row,col)
    noisy = srcArr + gauss
    return noisy


def main():
    image = cv2.imread(sys.argv[1],0)
    
    #Ni
    #cv2.imshow("Original image", image)
    
    dest = "./7x7/"
    
    
    noise_img = image.copy()
    mean = 0;
    sigma = 50;
    noise_img = Add_gaussian_Noise(noise_img, mean, sigma)
    cv2.imwrite(dest + "Gaussian Noise.jpg", noise_img)
    
    noise_dst = noise_img.copy()
    noise_dst = cv2.blur(noise_dst,(7,7))
    cv2.imwrite(dest + "Box filter gaussian.jpg", noise_dst)
    
    noise_dst1 = noise_img.copy()
    noise_dst1 = cv2.GaussianBlur(noise_dst1,(7,7),1.5)
    cv2.imwrite(dest + "Gaussian filter gaussian.jpg", noise_dst1)
    
    noise_dst2 = noise_img.copy()
    noise_dst2 = noise_dst2.astype(np.uint8)
    noise_dst2 = cv2.medianBlur(noise_dst2,7)
    cv2.imwrite(dest + "Median filter gaussian.jpg", noise_dst2)

    
    noise_img2 = image.copy()
    pa = 0.01
    pb = 0.01
    noise_img2 = Add_salt_pepper_Noise(noise_img2, pa, pb)
    cv2.imwrite(dest + "Salt and Pepper Noise.jpg", noise_img)
    
    noise_dst3 = noise_img.copy()
    noise_dst3 = cv2.blur(noise_dst3,(7,7))
    cv2.imwrite(dest + "Box filter salt.jpg", noise_dst3)
    
    noise_dst4 = noise_img.copy()
    noise_dst4 = cv2.GaussianBlur(noise_dst4,(7,7),1.5)
    cv2.imwrite(dest + "Gaussian filter salt.jpg", noise_dst4)
    
    noise_dst5 = noise_img2.copy()
    noise_dst5 = noise_dst5.astype(np.uint8)
    noise_dst5 = cv2.medianBlur(noise_dst5,7)
    cv2.imwrite(dest + "Median filter salt.jpg", noise_dst5)  
    
    
    #cv2.waitKey(0)
    exit(0)


if __name__ == "__main__":
    main()