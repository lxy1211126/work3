import cv2
import numpy as np
# 读取图片
img = cv2.imread("/home/bb/cai.jpg")
# 定义白色范围
lower_white = np.array([240,240,240])
upper_white = np.array([255,255,255])
# 生成白色区域掩码
mask = cv2.inRange(img, lower_white, upper_white)
# 将白色背景转为黑色
img[mask!=0] = [0,0,0]
# 保存处理后图片
cv2.imwrite("/home/bb/black_bg_output.jpg", img)
# 显示处理后图片
cv2.imshow("Black Background", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
