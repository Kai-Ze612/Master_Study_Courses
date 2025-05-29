cmake_minimum_required(VERSION 3.13)
project(sheet02)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
find_package(GTest CONFIG REQUIRED)

# Add include directories for the print library
include_directories(${print_INCLUDE_DIRS})

# If the print library has a specific path, you can specify it
# set(PRINT_INCLUDE_DIR "/path/to/print/include")
# include_directories(${PRINT_INCLUDE_DIR})

add_executable(tests simplevm.cpp tests/test_simplevm.cpp)
target_link_libraries(tests GTest::gtest_main)

# Link against the print library
target_link_libraries(tests ${print_LIBRARIES})

target_compile_options(tests PRIVATE -Wall -Wextra -Wpedantic -Werror -fsanitize=undefined)
target_link_options(tests PRIVATE -fsanitize=undefined)