FROM python:3.7

WORKDIR /root/

RUN pip install --upgrade pip

RUN pip install cmake --upgrade

RUN pip install numpy scipy matplotlib pandas

RUN pip install jupyterlab notebook

RUN pip install opencv-python opencv-contrib-python

RUN pip install pyyaml

RUN pip install panel

RUN apt-get update && apt-get install -y vim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 

WORKDIR /root/
COPY test.py .
COPY yum.jpg .
