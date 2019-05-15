import deco

def validColor(rgba): 
  valid = isValidRGB(rgba)
  message = "{} => {}".format(str(valid), rgba)
  color = "green" if valid == True else "red"

  print(deco.color(message, color))

def isValidRGB(rgba):

  rgbMethod = rgba.split("(")[0]
  if rgbMethod == "rgba":
    values = 4
  elif rgbMethod == "rgb":
    values = 3
  else: 
    return False
  

  splitted = rgba.split(",")
  
  if values != len(splitted):
    return False

  splitted[0] = splitted[0][values + 1:]
  splitted[values - 1] = splitted[values - 1][:-1]

  for i,l in enumerate(splitted):
    if l == "":
      return False

    percentage = False
    if "%" in l:
      l = l.strip("%")
      percentage = True
    
    try:
      l = float(l)
    except:
      return False

    if (rgbMethod == "rgba" and i < values - 1) or (rgbMethod == "rgb"):

      if percentage == True and (l < 0 or l > 100):
        return False
      
      elif percentage == False and (l < 0 or l > 255):
        return False

    else:
      if percentage == True and (l < 0 or l > 100):
        return False
      if percentage == False and (l < 0 or l > 1):
        return False

  return True
