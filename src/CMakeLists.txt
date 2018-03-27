cmake_minimum_required (VERSION 3.6)
project (mtn C)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(mtn mtn.c dirent.c optparse.h warn_unused.h dirent.h)
include_directories(".")
target_link_libraries(mtn  ${CONAN_LIBS})