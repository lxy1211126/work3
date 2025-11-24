#include<opencv2/opencv.hpp>
using namespace cv;

int main(){
    Mat img=imread("/home/bb/111/cai.jpg");//读取
    Mat gray_img;//灰度图转化
    cvtColor(img,gray_img,COLOR_BGR2GRAY);
    imwrite("gray_output.jpg ",gray_img);//保存
    imshow("Gray Image",gray_img);//显示
    waitKey(0);
    destroyAllWindows();
    return 0;
}