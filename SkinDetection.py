import cv2
import numpy as np

def detectSkin():
    print("Enter absolute image path: ")
    image_path = input()

    #Read the image
    img=cv2.imread(image_path)

    #Convert image from BGR to HSV color space
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #Define skin color range for hsv color space 
    HSV_mask = cv2.inRange(img_HSV, (0, 20, 70), (20,255,255)) 
    HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #Convert image from BGR to YCbCr color space
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    #skin color range for HSV color space 
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #Merge HSV and YCbCr masks and apply a median filter
    global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
    global_mask=cv2.medianBlur(global_mask,3)
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))


    HSV_result = cv2.bitwise_not(HSV_mask)
    YCrCb_result = cv2.bitwise_not(YCrCb_mask)
    global_result=cv2.bitwise_not(global_mask)


    #show results
    cv2.imshow("HSV.jpg",HSV_result)
    cv2.imshow("YCbCr.jpg",YCrCb_result)
    cv2.imshow("global_result.jpg",global_result)
    cv2.imshow("Image.jpg",img)
    # Save results(optional)
    # cv2.imwrite("1_HSV.jpg",HSV_result)
    # cv2.imwrite("2_YCbCr.jpg",YCrCb_result)
    # cv2.imwrite("3_global_result.jpg",global_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

detectSkin()