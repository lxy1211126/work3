cmake_minimum_required(VERSION 3.10)
project(cai)

# 查找系统中的OpenCV
find_package(OpenCV REQUIRED)

# 包含OpenCV头文件
include_directories(${OpenCV_INCLUDE_DIRS})

# 生成可执行文件
add_executable(TASK5 TASK5.cpp)

# 链接OpenCV库
target_link_libraries(TASK5 ${OpenCV_LIBS})
