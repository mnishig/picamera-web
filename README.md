# Pi Camera WebUI demo

This repository is very simple raspberry pi camera app.
App can preview via web and take snapshot store on SD card.

## inspired by
- [flask video stream](https://github.com/miguelgrinberg/flask-video-streaming)
- [RPi-Cam-Web-Interface](https://elinux.org/RPi-Cam-Web-Interface)
- [picamera module sample](https://picamera.readthedocs.io/en/release-1.13/recipes2.html#web-streaming)

## version

0.2

## system

- Web framework: bottle
- Bulma CSS framework
- Camera: Raspberry PI and Camera module
- PC and Raspberry　PI must connect same LAN 
<br>

optional
- Streaming: mjpg-streamer or uStreamer

## Usage

```
$ pip3 install -r requirements.txt
$ python3 app-mjpg-streamer.py (with mjpg-streamer or uStreamer)

or

$  python3 app-waitress.py (direct capture from raspi camera)
```
<br>

## Configuration

please adjust your configuration to edit config.json

|Key|Description|
|-|-|
|Host| bind network address (default: 0.0.0.0)|
|Port| bind port (default: 8080)|
|SnapshotURL| snapshot url. (in case of mjpg-streams: [raspi host]/?action=snapshot )|
|StreamURL| stream url. <br>(in case of mjpg-streams: [raspi host]/?action=stream) |
|Template| web ui template|
|Debug| debug mode flag (debug mode dose not implemented yet)|
<br>

You can use uStreamer: these URL like following.<br>
- StreamURL: [raspi host]/stream
<br>

## Roadmap

| version | description|
|---------|--------------------------------------------|
| 0.1 | simple function implemented |
| 0.2 | improve UI |
| 0.3 | add setting feature |

