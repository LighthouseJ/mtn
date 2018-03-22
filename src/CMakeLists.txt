cmake_minimum_required (VERSION 3.6)
project (mtn)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(mtn mtn.c)