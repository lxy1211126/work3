cmake_minimum_required(VERSION 3.10)
project(student)
set(STUDENT_SOURCES
    main.cpp
    team.cpp
)
include_directories($
{CMAKE_CURRENT_SOURCE_DIR})   
add_executable(my_student_app 
${STUDENT_SOURCES})
set_target_properties(my_student_app
PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED ON
)