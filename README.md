# PunkStation

**PunkStation** is a next-generation gaming console with zero compromises.  
While other platforms rely on 4K, ray tracing, online services, and unnecessary features like **color**, **media reading**, or **comfort**, PunkStation goes straight to the point:

- black-and-white OLED display
- a few buttons
- a buzzer
- no patience
- maximum fun

This is not PlayStation.  
This is **PunkStation**.  
Smaller. Tougher. Louder. And probably cheaper than an HDMI cable.

<img width="817" height="463" alt="obrazek" src="https://github.com/user-attachments/assets/705b0737-2d6b-4143-b763-c8343d63c5ea" />

<img width="802" height="458" alt="obrazek" src="https://github.com/user-attachments/assets/17f539ba-7838-47e2-bbee-dd61bd192625" />


---

## What it does

PunkStation runs a collection of arcade-style games on a **Raspberry Pi Pico** with a **SH1106 128×64 OLED display**.

Included hits:

- **Snack Rider** – a pixel adventure full of monsters, traps, and survival
- **King of Space** – a space shooter where diplomacy is not an option
- **Pong** – proof that humanity peaked technologically a long time ago
- **Lunar Module** – gravity, panic, and poor decision-making
- **Full Speed** – a racing game where everything is fast except the processor

---

## Key features

### Exclusive PunkStation technology
- **Monochrome graphics**  
  Because colors only distract from pure gameplay.

- **No media reader**  
  Discs? Cartridges? Blu-ray?  
  PunkStation refuses to be limited by physical formats.

- **Audio output through a buzzer**  
  Every sound effect feels like a hardware failure, but it is actually a feature.

- **Ultra low-resolution experience**  
  If you cannot tell what killed you, that just means the difficulty is higher.

- **Instant loading**  
  Because there is basically nothing to load.

---

## Hardware

This project uses:

- **Raspberry Pi Pico / Pico-compatible board**
- **SH1106 128×64 OLED over I2C**
- buttons for controls
- **piezo buzzer**
- MicroPython

Pins used in the project:

| Function | Pin |
|---|---:|
| OLED SDA | GP0 |
| OLED SCL | GP1 |
| Up button | GP3 |
| Back / exit button | GP4 |
| Right button | GP7 |
| Down button | GP11 |
| Left button | GP15 |
| Buzzer | GP16 |

> Note: **Lunar Module** also uses **GP20**.

---

## Controls

Controls are fully hardware-based.  
No touchscreen, no gestures, no AI trying to play the game for you.

In general:

- **left / right** – movement
- **up** – action / jump / fire depending on the game
- **special button** – return from the current game

Each game interprets the controls a little differently, because PunkStation believes in personal growth through confusion.

---

## Installation

1. Flash MicroPython onto the Raspberry Pi Pico.
2. Connect the SH1106 OLED display over I2C.
3. Wire the buttons and buzzer according to the pinout above.
4. Upload:
   - the main Python script
   - the `sh1106.py` library
5. Run the project.
6. Prepare for a handheld revolution.

---

## Dependencies

This project uses the following modules:

- `machine`
- `time`
- `random`
- `framebuf`
- `sh1106`

---

## Project philosophy

PunkStation was not created to impress with raw performance.  
It was created to prove that:

- a game can still be great without a GPU the size of a radiator,
- a beep is a valid soundtrack,
- 128×64 pixels are more than enough if you have imagination,
- and a PlayStation competitor does not need to cost hundreds of dollars.

All it needs is a few wires, a Pico, and enough attitude.

---

## Screenshots

There are currently no screenshots, because the true PunkStation experience cannot be captured.  
It must be **survived**.

---

## Future plans

Maybe:
- better menu
- more games
- score saving
- fewer bugs
- more bugs, but stylish ones

Definitely not:
- 3D graphics
- 8K output
- Blu-ray support
- media reading
- unnecessary luxury

---

## Why does this exist?

Because it can.

And because the world needed a console brave enough to say:  
**“No, it absolutely does not need colors.”**

---

## Author

Built with love, irony, and probably a minor electrical incident.

---

## License

Use it, modify it, play with it.  
Just please do not turn it into a corporate product with subscriptions and a battle pass.
