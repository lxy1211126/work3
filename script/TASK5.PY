import cv2
import numpy as np

# 固定输入图片路径
img = cv2.imread("/home/bb/cai.jpg")
img_copy = img.copy()  # 保留原图用于对比
# 1. 定义白色范围（BGR格式），筛选非白色区域
lower_white = np.array([240, 240, 240])
upper_white = np.array([255, 255, 255])
# 创建白色区域的掩码（mask中白色区域为255，非白色为0）
mask = cv2.inRange(img, lower_white, upper_white)
# 取反掩码，得到非白色区域的掩码（非白色为255，白色为0）
non_white_mask = cv2.bitwise_not(mask)
# 2. 形态学处理，去除小噪点，让轮廓更清晰
kernel = np.ones((3, 3), np.uint8)
non_white_mask = cv2.erode(non_white_mask, kernel, iterations=1)  # 腐蚀去噪
non_white_mask = cv2.dilate(non_white_mask, kernel, iterations=1)  # 膨胀还原轮廓
# 3. 查找非白色区域的轮廓
contours, _ = cv2.findContours(non_white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. 用绿色荧光色（亮绿色，BGR：0,255,0）描边轮廓，线宽2
cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)

# 5. 显示结果（原图 + 非白色轮廓描边图）
cv2.imshow("Original Image", img)
cv2.imshow("Non-White Contours (Green Glow)", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果
cv2.imwrite("output.jpg", img_copy)
