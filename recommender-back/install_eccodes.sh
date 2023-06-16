#!/bin/bash

# Fetches the latest version of eccodes and ecbuild which is required to be installed first

git clone https://github.com/ecmwf/ecbuild.git
mkdir ecbuild/build
cd ecbuild/build
cmake ..
make
make install
cd ../..

latest_version=$(curl -s https://api.github.com/repos/ecmwf/eccodes/releases/latest | grep 'tag_name' | cut -d\" -f4)

wget https://github.com/ecmwf/eccodes/archive/refs/tags/${latest_version}.tar.gz
tar -xzvf ${latest_version}.tar.gz
mkdir eccodes-${latest_version}/build
cd eccodes-${latest_version}/build
cmake ..
make
make install

cd ../..
rm -rf ecbuild
rm -rf eccodes-${latest_version}
