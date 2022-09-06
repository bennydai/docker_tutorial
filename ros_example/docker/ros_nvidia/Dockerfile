FROM osrf/ros:melodic-desktop-full

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
	software-properties-common \
	&& apt-get autoremove -y \
	&& rm -r /var/lib/apt/lists/*

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]

# Installing Software for Rendering and Editing
RUN apt-get update && apt-get install -y vim git

RUN apt-get install -y --reinstall libcanberra-gtk-module libsm6 libxext6 libxrender-dev

ENV TERM xterm-256color

WORKDIR /root/

# Upgrade Python Packages, cmake and catkin tools
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN pip install cmake --upgrade
RUN pip install catkin-tools
RUN pip install catkin_pkg
RUN apt-get install -y python-catkin-tools
RUN rosdep update

# Setting up ROS catkin_ws
RUN mkdir -p /root/catkin_ws/src

WORKDIR /root/catkin_ws

RUN /bin/bash -c "source /ros_entrypoint.sh; catkin_make"

# Installing Pre-requisite ROS software
# Python GUI tools
RUN echo "debconf debconf/frontend select Noninteractive" | debconf-set-selections && \
	apt-get install -y python-tk python-gtk2 python-gtk2-dev

RUN rosdep update

RUN echo "source /root/catkin_ws/devel/setup.bash" >> /root/.bashrc

# Reseting back
WORKDIR /root
SHELL ["/bin/bash", "-c"]

# nvidia-container-runtime environment parameters
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# NVIDIA OpenGL
RUN apt-get update && apt-get install -y libglvnd-dev
