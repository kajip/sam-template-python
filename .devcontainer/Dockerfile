FROM amazonlinux:2.0.20191016.0

ENV LANG=ja_JP.utf8
ENV no_proxy=127.0.0.1,localhost,host.docker.internal

COPY aws/ /root/.aws/

RUN yum install -y glibc-langpack-ja &&\
    yum install -y tar gzip git awscli &&\
    yum install -y unzip &&\
    amazon-linux-extras install docker &&\
    yum install -y python3 &&\
    yum install -y gcc python3-devel &&\
    pip3 install -U pytest boto3 aws-sam-cli &&\
    yum remove -y gcc python3-devel &&\
    rm -rf /tmp/*.zip && yum clean all && rm -rf /var/cache/yum
