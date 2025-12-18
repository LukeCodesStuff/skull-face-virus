# skull-face-virus

A harmless and fun Python script that creates a short visual and audio effect on your screen.

## How it Works

- The script waits for a mouse click.
- When a click is detected:
  - A gray semi-transparent overlay appears.
  - A skull image is displayed slightly below the center of the screen.
  - A music track plays for 3 seconds.
- After 3 seconds, the overlay disappears, and your computer returns to normal.

## Purpose

This project is purely for **educational and entertainment purposes**.  
It is safe to run: **no files are modified or harmed** on your computer.

## Requirements

- Python 3.10+  
- Libraries:
  - `playsound3`
  - `Pillow`
  - `pynput`

Install the dependencies via:

```bash
pip install -r requirements.txt
