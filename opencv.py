import cv2

img = cv2.imread(r'C:/Users/rites/OneDrive/Documents/opencv/geeksforgeeks.jpg.png')

if img is not None:
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found or could not be loaded.")
    