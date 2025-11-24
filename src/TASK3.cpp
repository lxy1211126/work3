#include<opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int main(){
    Mat img =imread("/home/bb/cai.jpg");
    Scalar lower_white(240,240,240);
    Scalar upper_white(255,255,255);
    Mat mask;
    inRange(img,lower_white,upper_white,mask);//白色范围限定
    img.setTo(Scalar(0,0,0),mask);
    imwrite("black_output.jpg",img);
    imshow("black_output.jpg",img);//显示
    waitKey(0);
    destroyAllWindows();
    return 0;//替换
}