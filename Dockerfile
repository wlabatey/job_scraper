FROM amazonlinux:2017.03
LABEL maintainer="wlab@startmail.com"

WORKDIR /opt

COPY . /opt/job_scraper

RUN yum install -y xz wget find gcc zlib zlib-devel openssl openssl-devel

# Download, compile & install python 3.6.2
RUN wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz \
  && tar -xvf Python-3.6.2.tar.xz \  
  && rm Python-3.6.2.tar.xz \
  && cd Python-3.6.2 \
  && ./configure --enable-optimizations --prefix=/usr/local \ 
  && make \
  && make altinstall 

# Download & install pip along with necessary packages
RUN wget https://bootstrap.pypa.io/get-pip.py \
  && python3 get-pip.py \
  && pip3 install virtualenv


CMD ["/bin/bash"]

#CMD ["/bin/bash", "/opt/job_scraper/build/build.sh"]
