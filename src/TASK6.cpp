#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int main() {
    Mat img = imread("/home/bb/cai.jpg");
    int h = img.rows, w = img.cols;
    Point2f center(w/2.0f, h/2.0f);
    Mat M = getRotationMatrix2D(center, 45, 1.0);
    // 计算新尺寸
    double cos_val = abs(M.at<double>(0,0));
    double sin_val = abs(M.at<double>(0,1));
    int new_w = int(h * sin_val + w * cos_val);
    int new_h = int(h * cos_val + w * sin_val);
    // 调整平移
    M.at<double>(0,2) += (new_w/2.0 - center.x);
    M.at<double>(1,2) += (new_h/2.0 - center.y);
    // 旋转
    Mat rotated;
    warpAffine(img, rotated, M, Size(new_w, new_h));
    // 显示对比
    imshow("Original Image", img);
    imshow("Rotated 45° Image", rotated);
    waitKey(0);
    destroyAllWindows();
    // 保存结果
    imwrite("rotated_output.jpg", rotated);
    return 0;
}
