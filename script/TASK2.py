import cv2
# 读取图片
img = cv2.imread("/home/bb/cai.jpg")
# 转为灰度图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 保存灰度图
cv2.imwrite("/home/bb/gray_output.jpg", gray_img)
# 显示原图和灰度图
cv2.imshow("Original", img)
cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
