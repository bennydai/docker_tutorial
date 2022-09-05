# Docker Tutorial
Docker - this tutorial/overview only examines now how I use Docker on Linux, without the GUI interface.

## How it roughly works
Essentially Docker works much similarly to a Virtual Machine Image in the sense that you can start off with a clean install, and then build your software on top. The huge difference is the portability with the fact that it is much lighter, and that 'forks' of images can be created.

Typically the main use case of Docker is to build a piece of software or an app, which is then deployed on multiple computers or the cloud. This typically results in Docker images running with very little privileges such as access to the network and being able to display GUIs.

In our use case, we rely on it for:
- A much tighter version control of our code and providing isolated environments
- Being able deploy on other devices/cluster whilst developing it on our own devices
  - i.e. Develop code for raspberry pi and deploy through emulation using [QEMU](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/)
- Develop and run code on a shared resource
  - i.e. Installing and running multiple versions of CUDA on a high-powered computer
- "The code you gave me doesn't work on my computer"
  - Docker pretty much removes this problem

## WARNING
- In the way I use Docker in this tutorial may not be ideal for your projects/clients that enforce a security constraint. The way we run Docker to allow for GUI interfacing and network access can lead to a security risk since we allow it to run with all privileges. (Permanently sudo during runtime).
- There are ways to tighten down the security; however it does get quite complicated.
- My suggestion for people in this boat, feel free to develop in Docker; but when it comes time to deploy; since the way you build Docker Images is documented, you can reproduce the libraries on a clean machine with minimal problems.

## Some inherent problems
Although Docker is quite useful in the fact that you could build code in an linux environment while working on a different device (i.e. a MacBook); I have ran into issues or complications in getting it nice and operational for my day-to-day. These issues mainly are resultant of driver mismatches as the Docker Image would be virtualised. Building linux based docker images and running them on linux work very differently - and in effect are not virtualised. (Except for different platform).

Long story short - don't bother trying to get a fully functional ROS operational whilst running MacOS.

## Installation Links
- For installing Docker Engine, the link is [here](https://docs.docker.com/engine/install/ubuntu/)
- Remember to examine the post-installation details [here](https://docs.docker.com/engine/install/linux-postinstall/) to ensure that you don't need to run ```sudo``` everytime you want to interface Docker.
