import os
import math

colors = {
  "green": "\033[92m",
  "red": "\033[31m",
  "END": "\x1b[0m"
}

def color(text, color):
  text = colors[color] + text + colors["END"]
  return text

def center(text, spacer):
  offset = int(testOffsetColor(text)) / 2
  if os.get_terminal_size().columns % 2 == 1:
    offset -= 1
  space = spacer * int(((os.get_terminal_size().columns - len(text)) / 2) + offset)
  text = space + text + space
  return text

def clear():
  clear = "clear"
  if os.name == "nt":
    clear = "cls"
  os.system(clear)

def testOffsetColor(string):
  counter = 0
  position = {}
  oldposition = {}
  for i, letter in enumerate(string):
    for color in colors:
      pos = string.find(colors[color], i)
      if(colors[color] in position):
        if int(position[str(colors[color])]) == int(i - 1):
          counter += len(colors[color])
      position[str(colors[color])] = str(pos)

  counter = math.ceil(counter / 2) * 2
  return counter

