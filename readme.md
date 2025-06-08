# Not A HackPad

Basically a hack pad but with a lot more keys and a lot more LEDs. 

Made because a hackpad was too easy and small. Also I wanted to make it more like a keyboard than a hackpad. I also wanted to use a full pico.

## [BOM](https://docs.google.com/spreadsheets/d/1KeP3WG9XhRpOmTjCqM3hqRnjlMIbq6JLI_i9ZYCvpQc/edit?usp=sharing) | [CAD](https://cad.onshape.com/documents/e09ff01002204229131d6eeb/w/d4ffe006ec67723c6fe73dd8/e/5404e0c7dee7a93a5d70d53f) | [Journal](https://github.com/RunTheBot/NotAHackPad/blob/main/journal.md)

![image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/f2d12adf2dd8d2c5410d7742ce670fa7a0d015b8_image.png)
![image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/e4419d36a5dcb26c27e8058150020da9df8670d5_image.png)
![image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/e38bd65cd81cb741fee232a9d774f51cc142aea5_image.png)

# Features
- 100 keys
- OLED Display
- Barrel Jack Power (Pico power is not enough)
- Auto Polarity Correcting Circuit for Barrel Jack
- 100 Neopixels
- External Power Supply for Neopixels (To run them at full brightness 😈)

# BOM

| Name                       | Quantity | Single Unit Price | Total Price | URL/LCSC                                              |
|----------------------------|----------|-------------------|-------------|-------------------------------------------------------|
| Electronics                |          |                   |             |                                                       |
| C - LEDs                   | 100      |                   | $0.46       | C49678                                                |
| D - Rows/Cols              | 100      |                   | $2.72       | C241939                                               |
| SK6812MINI                 | 100      |                   | $5.89       | C5149201                                              |
| schottky diode             | 1        |                   | $0.29       | C85098                                                |
| IRF3205PBF                 | 2        |                   | $3.74       | C2561                                                 |
| 5v 8A PSU                  | 1        |                   | $11.48      | https://www.aliexpress.com/item/4000521124523.html    |
| IRF9540N                   | 2        |                   | $4.86       | C2575                                                 |
| SSD1306                    | 1        |                   | $3.10       | https://www.aliexpress.com/item/1005005301005280.html |
| Barrel Jack                | 1        |                   | $1.84       | C381116                                               |
| BSS138 (Level Shifter)     | 10       |                   | $0.42       |      C82045                                                 |
| 10K 0603                   | 100      |                   | $0.11       |                 C98220                                      |
| Shipping                   |          |                   | $14.79      |                                                       |
| Misc                       |          |                   |             |                                                       |
| Solder Paste(Sn42Bi58-55g) |          |                   | $9.78       | https://www.aliexpress.com/item/1005006055037674.html |
| Hot Plate (MECHANIC HT-10) |          |                   | $58.68      | https://www.aliexpress.com/item/1005006975087368.html |
| Keys                       |          |                   |             |                                                       |
| Outemu Silent Grays        | 1        | $22.38            | $22.38      | https://www.aliexpress.com/item/1005007052759423.html |
| Key Caps - Printed         |          |                   | $0.00       |                                                       |
| JLC                        |          |                   |             |                                                       |
| PCB                        | 1        | $19.80            | $19.80      |                                                       |
| Shipping                   | 1        | $13.60            | $13.60      |                                                       |
| JLC duties                 |          |                   | $3.57       |                                                       |
|                            |          |                   |             |                                                       |
|                            |          |                   | $142.39     | CAD (Calulations in sheet)                                                  |
|                            |          |                   | $35.12      | USD (Calulations in sheet)                                                   |
|                            |          |                   | $139.08     | Total - USD                                           |
