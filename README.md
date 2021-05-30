# Pi Camera WebUI demo

This repository is very simple raspberry pi camera app.
App can preview via web and take snapshot store on sd card.

## version

0.1

## system

- Web framework: bottle
- Streaming: mjpg-streamer or ustreamer
- Camera: Raspberry PI and Camera module
- PC and Raspberry　PI must connect same LAN 

## Usage

```
$ pip3 install -r requirements.txt
$ python3 app-mjpg-streamer.py
```
<br>

## Configuration

please adjust your consfiguration to edit config.json

|Key|Description|
|-|-|
|Host| bind network address (default: 0.0.0.0)|
|Port| bind port (default: 8011)|
|SnapshotURL| snapshot url. (in case of mjpg-streame: [raspi host]/?actino=snapshot )|
|StreamURL| stream url. <br>(in case of mjpg-streame: [raspi host]/?actino=straem) |
|Template| web ui template|
|Debug| debug mode flag (debud mode dose not implemented yet)|
<br>

You can use uStreamer: these URL like follwing.<br>
- StreamURL: [raspi host]/stream
<br>

## Loadmap

| version | description|
|---------|--------------------------------------------|
| 0.1 | simple function implemented. |
| 0.2 | improve UI |
| 0.3 | ??? |

