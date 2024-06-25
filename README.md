# Screensaver
A CD type Screensaver, which counts corner hits for ESP32 using SSD1306 OLED Screen

## Hardware Setup

### 1. Connect Screen
- Connect `VCC` from Screen with `3V3` on ESP32
  - Connect `SCL` from Screen with `G32`
  - Connect `SDA` from Screen with `G33`
- Connect Ground (`GND`)

<img src="https://raw.githubusercontent.com/FreakMediaLP/Screensaver/main/circuit%20sketch.png" width="500">

## Software Setup

### 1. Flash Python Interpreter on EPS32

Use a tool f.E. [Thonny](https://thonny.org/) to flash the Micropython Interpreter to the ESP32

### 2. Push Project Files on EPS32

Save following files on the ESP32:
- `boot.py`
- `main.py`
- `ssd1306.py`
