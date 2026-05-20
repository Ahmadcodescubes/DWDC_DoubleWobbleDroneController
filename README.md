# DWDC — Double Wobble Drone

**DWDC (Double Wobble Drone Controller)** is an open-source budget drone project that includes:

- Complete drone source code
- PC-based controller code
- 3D printable files for the drone frame and mounting parts
- All required design files to build the project from scratch

The goal of this project is to provide a simple and affordable drone platform that anyone can build at home using commonly available components.

---

## Required Parts

## Drone (DW)

| Quantity | Part |
|--------:|------|
| 1x | Arduino Nano |
| 1x | 3S LiPo battery (any size that fits the frame) |
| 2x | 30A ESC (Electronic Speed Controller) |
| 2x | Brushless motors (2200KV or lower recommended) |
| 2x | SG90 9g servo motors |
| 1x | NRF24L01 wireless transceiver (PA + LNA version with antenna optional) |
| 1x | I2C gyroscope/IMU (recommended for rotation measurement and stabilization) |

### Notes

- If you use the PA + LNA version of the NRF24L01, the required antenna mounting hole is already included in the 3D files.
- Clean wire routing is critical. Poor cable management can introduce signal interference and unstable behavior.
- Use proper decoupling capacitors and ensure the NRF24L01 receives a stable 3.3V supply.

---

## Controller

| Quantity | Part |
|--------:|------|
| 1x | Any game controller connected to a PC |
| 1x | Any microcontroller with exposed SPI pins |
| 1x | NRF24L01 wireless transceiver (PA + LNA optional) |

### Optional

- A custom 3D-printed shield or enclosure can be designed to mount the microcontroller and radio to your controller.
- If you create a useful enclosure, consider sharing it with the community.

---

## Features

- Low-cost design using widely available components
- Wireless control using NRF24L01 modules
- Stabilization support through an I2C gyroscope/IMU
- Fully 3D-printable structure
- Open-source code and design files

---

## Project Goal

The purpose of DWDC is to make drone building accessible to hobbyists, students, and makers without requiring expensive proprietary hardware.

If everything goes as planned, this project should serve as a straightforward and inexpensive drone that people can build, modify, and improve on their own.

---

## License and Usage

These files are provided for **personal and educational use only**.

> **Commercial use is strictly prohibited without prior written permission from the author.**

If you wish to use any part of this project commercially, contact the author for authorization.

---

## Contributing

Suggestions, improvements, and custom 3D designs are welcome. If you develop better parts, enclosures, or software enhancements, consider sharing them so others can benefit.

---

## AI Usage

AI was not, and will not be used, on this project. Any submissions that include fully AI generated content that has no prior human alterations and inspections will not be public.
