#include <opencv2/opencv.hpp>
#include<vector>
using namespace cv;
using namespace std;

int main() {
    // 读取图片
    Mat img = imread("/home/bb/cai.jpg");
    Mat img_copy = img.clone();

    // 筛选非白色区域
    Scalar lower_white(240, 240, 240);
    Scalar upper_white(255, 255, 255);
    Mat mask, non_white_mask;
    inRange(img, lower_white, upper_white, mask);
    bitwise_not(mask, non_white_mask);

    // 形态学优化轮廓
    Mat kernel = getStructuringElement(MORPH_RECT, Size(3, 3));
    erode(non_white_mask, non_white_mask, kernel);
    dilate(non_white_mask, non_white_mask, kernel);

    // 查找并描边轮廓
    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    findContours(non_white_mask, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
    drawContours(img_copy, contours, -1, Scalar(0, 255, 0), 2);

    // 显示并保存结果
    imshow("Original", img);
    imshow("Green Contours", img_copy);
    waitKey(0);
    destroyAllWindows();
    imwrite("/home/bb/non_white_contours_cpp_output.jpg", img_copy);

    return 0;
}
