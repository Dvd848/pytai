FROM debian:bullseye-slim

WORKDIR /home/pytai/workdir/

# https://blog.richard.do/2019/04/17/fix-apt-get-update-hanging-within-ubuntu-docker-container/
RUN apt-get install -y apt-transport-https

RUN apt-get update \
    && apt-get install -y \
        git \
        python3 \
        python3-pip \
        curl \
        openjdk-17-jre-headless \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install --upgrade pyyaml
    
RUN curl -LO https://github.com/kaitai-io/kaitai_struct_compiler/releases/download/0.10/kaitai-struct-compiler_0.10_all.deb \
    && apt-get install ./kaitai-struct-compiler_0.10_all.deb
    
WORKDIR /home/pytai/shared/utils

### Build: docker build -t pytai .
### Run  : docker run -it --rm --mount type=bind,source="$PWD/../",target=/home/pytai/shared/ pytai python3 compile_kaitai_formats.py