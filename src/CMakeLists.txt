cmake_minimum_required (VERSION 3.6)
project (mtn C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SRC
  mtn.c
  dirent.c
  win_util.c
)

set(HEADERS
  dirent.h
  optparse.h
  warn_unused.h
  win_util.h
)

add_executable(mtn ${HEADERS} ${SRC})
include_directories(".")
target_link_libraries(mtn  ${CONAN_LIBS})