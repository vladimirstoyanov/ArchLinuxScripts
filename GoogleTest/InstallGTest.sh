git clone https://github.com/google/googletest.git
cd googletest        # Main directory of the cloned repository.
mkdir build          # Create a directory to hold the build output.
cd build
cmake ..             # Generate native build scripts for GoogleTest.
make
sudo make install
cd ../,,/
rm -rf googletest
