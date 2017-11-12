import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = np.uint64(0)
    var_t = np.uint64(0)
    location = [0, 0]
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------
    mean_t = np.mean(temp)
    var_t = np.var(temp)
    N = temp.size


    
    

    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            window = src[i:i+stepsize,j:j+stepsize]
            print ((i,j))


            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------

            mean_s = np.mean(window)
            var_s = np.var(window)

            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            a =  0
            
            
            for ii in range(temp.shape[0]):
                for jj in range(temp.shape[1]):
                    a += (temp[ii][jj]-mean_t)*(src[i+ii][j+jj]-mean_s)
            corr = a / (temp.shape[0] * temp.shape[1] * var_t * var_s)
           
            
            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
    return location

def main():
    # load source and template images
    source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
    print(source_img.shape)
    temp = cv2.imread('template.jpg',0) # read image in grayscale
    print(temp.shape)
    location = TemplateMatching(source_img, temp, 20);
    print(location)
    match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

    # Draw a red rectangle on match_img to show the template matching result
    # ------------------ Put your code below ------------------
    (x, y) = location
    (h, w) = temp.shape
    cv2.rectangle(match_img,(x,y),(x+w,y+h),(0,0,255),3)

        
    # Save the template matching result image (match_img)
    # ------------------ Put your code below ------------------ 
    cv2.imwrite('./Out/MyTemplateMatching.jpg', match_img)


    # Display the template image and the matching result
    cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
    cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
    cv2.imshow('TemplateImage', temp)
    cv2.imshow('MyTemplateMatching', match_img)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__ == '__main__':
    main()
