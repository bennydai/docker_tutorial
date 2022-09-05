## Basic Example
To run this code, you will first need to build the image. We will call the image name basic for the time being.

```bash
cd docker
docker build -t basic .
```

To allow for GUI operations, the library ```ffmpeg``` was installed as running a ```pip install opencv-python``` does not provide full GUI operations. Keep in mind, most Docker images are headless by default.

We rely on the use of ```docker-compose``` to illustrate the parameters needed to run the program. We contain the commands needed to run docker in a convenient script in ```run.sh```.

To run the program:
```bash
./run.sh
```

For more details about the parameters needed for GUI-bypass, refer to the wiki in GUI.
