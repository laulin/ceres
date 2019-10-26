FROM ubuntu:18.10
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install mako pyyaml
COPY example/ /root/example
WORKDIR  /root
COPY dist/ceres-1.0.0-py3-none-any.whl /tmp/ceres-1.0.0-py3-none-any.whl
RUN pip3 install /tmp/ceres-1.0.0-py3-none-any.whl
