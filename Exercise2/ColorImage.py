# -*- coding: utf-8 -*-

import cv2

def main():
    filename = "../Test_images/baboon.jpg"
    src = cv2.imread(filename,cv2.IMREAD_COLOR)
    b,g,r = cv2.split(src)
    ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    y,cb,cr = cv2.split(ycrcb_image)
    hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv_image)
    
    cv2.imshow("Original image",src)
    cv2.imshow("Red",r)
    cv2.imshow("Green",g)
    cv2.imshow("Blue",b)
    cv2.imshow("Y",y)
    cv2.imshow("Cb",cb)
    cv2.imshow("Cr",cr)
    cv2.imshow("Hue",h)
    cv2.imshow("Saturation",s)
    cv2.imshow("Value",v)   
    
    cv2.waitKey(1)
    cv2.imwrite("./Output/Red.jpg",r)
    cv2.imwrite("./Output/Green.jpg",g)
    cv2.imwrite("./Output/Blue.jpg",b)
    cv2.imwrite("./Output/Y.jpg",y)
    cv2.imwrite("./Output/Cb.jpg",cb)
    cv2.imwrite("./Output/Cr.jpg",cr)
    cv2.imwrite("./Output/Hue.jpg",h)
    cv2.imwrite("./Output/Saturation.jpg",s)
    cv2.imwrite("./Output/Value.jpg",v) 

    
    
    exit()    
    

if __name__ == "__main__":
    main()