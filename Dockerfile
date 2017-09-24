FROM amazonlinux:2017.03.0.20170812
LABEL maintainer="wlab@startmail.com"

ENV PATH /usr/local/bin:$PATH
ENV LANG en_US.UTF-8

WORKDIR /opt

# Install dependencies, then clean cache
RUN yum install -y \
  findutils \
  xz \
  wget \
  gcc \
  zlib \
  zlib-devel \
  openssl \
  openssl-devel \
  && yum clean all \
  && rm -rf /var/cache/yum/x86_64/latest/*

# Download, compile & install python 3.6.2, then add symlinks to python & python3
RUN wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz \
  && tar -xvf Python-3.6.2.tar.xz \  
  && rm Python-3.6.2.tar.xz \
  && cd Python-3.6.2 \
  && ./configure --enable-optimizations --prefix=/usr/local \ 
  && make \
  && make altinstall \
  && rm -rf Python-3.6.2 \ 
  && cd /usr/local/bin \
  && ln -s python3.6 python \
  && ln -s python3.6 python3 

# Download & install pip along with necessary packages, then add symlinks
RUN wget https://bootstrap.pypa.io/get-pip.py \
  && python get-pip.py \
  && rm get-pip.py \
  && cd /usr/local/bin \
  && ln -s pip3.6 pip \
  && ln -s pip3.6 pip3

# Install virtualenv & awscli
RUN pip3 install virtualenv awscli --no-cache-dir

## To do:

# Create virtual environment with python 3.6, probably in /opt/virtualenv
# Install all pip dependencies inside virtual environment
# Copy all dependencies from /opt/virtualenv/lib/python3.6/site-packages to /opt/dist
# Copy source code from /opt/job_scraper/scraper to /opt/dist
# Share /opt/dist with host using a volume to persist the data. Will be used to test locally or build a deployment package from.
