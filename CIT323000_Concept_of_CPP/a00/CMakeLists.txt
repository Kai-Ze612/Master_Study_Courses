cmake_minimum_required(VERSION 3.21)
# Specify compiler before project()
set(CMAKE_CXX_COMPILER "clang++")
project(MyProject CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# For debug builds

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g")
# Add executable
add_executable(helloworld main.cpp)