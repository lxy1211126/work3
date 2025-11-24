#include <opencv2/opencv.hpp>
#include <vector>  // 用于vector容器
using namespace cv;
using namespace std;

int main() {
    // 读取图片
    Mat img = imread("/home/bb/cai.jpg");
    vector<Mat> channels;  
    split(img, channels); 
    // BGR顺序对应channels[0]、channels[1]、channels[2]
    imwrite("b_channel.jpg", channels[0]);  
    imwrite("g_channel.jpg", channels[1]);  
    imwrite("r_channel.jpg", channels[2]); 
    // 显示
    imshow("Original Image", img);
    imshow("B Channel", channels[0]);
    imshow("G Channel", channels[1]);
    imshow("R Channel", channels[2]);
    waitKey(0);        
    destroyAllWindows(); 
    return 0;
}