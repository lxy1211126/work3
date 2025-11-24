import cv2
import numpy as np


img = cv2.imread("/home/bb/cai.jpg")


h, w = img.shape[:2]
new_size = int(np.hypot(w, h)) 
center = (new_size // 2, new_size // 2)  


rotate_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

offset_x = (new_size - w) // 2
offset_y = (new_size - h) // 2
rotate_matrix[0, 2] += offset_x
rotate_matrix[1, 2] += offset_y

rotated_img = cv2.warpAffine(img, rotate_matrix, (new_size, new_size))


cv2.imwrite("/home/bb/rotated_perfect.jpg", rotated_img)

cv2.imshow("Perfect Rotation", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
