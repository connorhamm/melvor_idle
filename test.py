import cv2
import numpy as np
import pyautogui as pag

#getting a small region as a screenshot
region = (0, 0, 1920, 1080)
pag.screenshot('da2.png', region = region)

#using that screenshot to detect where a template might be and saving the image
img_rgb = cv2.imread('da2.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('Capture2.JPG',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.6335
loc = np.where( res >= threshold)
x = loc[1][0] + w / 2
y = loc[0][0] + h / 2

pag.moveTo(x,y)

# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 25)

# # top left point of rectangle
# print("top left point of rectangle: " + str(pt))
# print("bot right point of rectangle: " + str(pt[0] + w) + " , " + str(pt[1] + h))

# # Calculate the difference to find center
# # x = pt[0] + w / 2
# # y = pt[1] + h / 2

# print(str(x) + " , " + str(y))

# # cv2.imshow('Detected',img_rgb)
# cv2.waitKey(0)
# cv2.imwrite('01.png',img_rgb)
# cv2.destroyAllWindows()