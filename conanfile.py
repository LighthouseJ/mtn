from conans import ConanFile, CMake


class MtnConan(ConanFile):
    name = "mtn"
    version = "2008a"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Mtn here>"
    settings = "os", "compiler", "build_type", "arch"
    options = { }
    generators = "cmake"
    requires = "ffmpeg/3.4@bincrafters/stable", "libgd/2.2.4@nathanw/testing"
    exports = [ "CMakeLists.txt" ]
    exports_sources = "*.c", "*.h"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
        
    def package(self):
        self.copy("mtn", src="src", dst="bin", keep_path=False)

    def package_info(self):
        pass
        # self.cpp_info.libs = ["hello"]
