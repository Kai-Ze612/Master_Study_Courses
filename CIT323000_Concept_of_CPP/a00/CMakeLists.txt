cmake_minimum_required(VERSION 3.20)
project(a00)

# Force clang-18
set(CMAKE_C_COMPILER clang-18)
set(CMAKE_CXX_COMPILER clang++-18)

## Using C++23
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Use libc++ instead of libstdc++ for include <print>
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wextra -Wall -Werror")

## Add GDB
## -g flag for debugging
## -- -O0 for no optimization, for debugging
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")
set(CMAKE_BUILD_TYPE Debug)

add_executable(a00 src/main.cpp)