import cv2
# 读取图片
img = cv2.imread("/home/bb/cai.jpg")
# 拆分RGB通道
b, g, r = cv2.split(img)
# 保存R通道图片
cv2.imwrite("/home/bb/r_channel.jpg", r)
# 显示原图和各通道图片
cv2.imshow("Original", img)
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)
cv2.waitKey(0)
cv2.destroyAllWindows()
