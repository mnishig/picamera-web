# Pi Camera WebUI demo

This repository is very simple raspberry pi camera app.
App can preview via web and take snapshot store on SD card.

## version

0.1

## system

- Web framework: bottle
- Camera: Raspberry PI and Camera module
- PC and Raspberry　PI must connect same LAN 
<br>

If you use `[mjpg-streamer branch]`, you need install a streaming app on raspberry PI
- Streaming: [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer/tree/master/mjpg-streamer-experimental) or [uStreamer](https://github.com/pikvm/ustreamer)
<br>

## Usage

```
$ pip3 install -r requirements.txt
$ python3 app-mjpg-streamer.py
```
<br>

## Configuration

please adjust your configuration to edit config.json

|Key|Description|
|-|-|
|Host| bind network address (default: 0.0.0.0)|
|Port| bind port (default: 8011)|
|SnapshotURL| snapshot url. (in case of mjpg-streamer: [raspi host]/?action=snapshot )|
|StreamURL| stream url. <br>(in case of mjpg-streamer: [raspi host]/?action=stream) |
|Template| web ui template|
|Debug| debug mode flag (debug mode dose not implemented yet)|
<br>

You can use uStreamer: these URL like following.<br>
- StreamURL: [raspi host]/stream
<br>

## Roadmap

| version | description|
|---------|--------------------------------------------|
| 0.1 | simple function implemented. |
| 0.2 | improve UI |
| 0.3 | ??? |

