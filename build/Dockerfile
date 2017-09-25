FROM python:2.7.14-alpine3.6

RUN mkdir -p /usr/src/app 

RUN apk update && apk add \
  bash \
  util-linux \
  coreutils \
  binutils \
  findutils \
  grep 

WORKDIR /usr/src/app

COPY ./build-deployment-package.sh /

ENTRYPOINT ["/bin/bash", "/build-deployment-package.sh"]
