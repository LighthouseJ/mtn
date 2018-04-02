from conans import ConanFile, CMake


class MtnConan(ConanFile):
    name = "mtn"
    version = "2008a"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "movie thumbnailer"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "ffmpeg/3.4@bincrafters/stable", "libgd/2.2.4@nathanw/testing"
    exports = [ "src/CMakeLists.txt" ]
    exports_sources = "src/*.h", "src/*.c"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir='src')
        cmake.build()
        cmake.install()
        
    def package(self):
        self.copy("mtn", src="src", dst="bin", keep_path=False)

    def package_info(self):
        pass
        # self.cpp_info.libs = ["hello"]
