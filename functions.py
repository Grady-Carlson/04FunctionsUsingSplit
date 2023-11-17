def meal_time(time):
  hours, minutes = time.split(":")
  otime = int(hours) * 60 + int(minutes)
  if otime >= 420 and otime <= 480:
    return "breakfast"
  elif otime >=720  and otime <= 780:
    return "lunch"
  elif otime >= 1080 and otime <= 1140:
    return "dinner"
  else:
    return "nothing right now"

print("7:30 => " , meal_time("7:30"))
print("21:42 => " , meal_time("21:42"))
print("18:10 => " , meal_time("18:10"))
print("12:02 => " , meal_time("12:02"))
print(" ")



def get_filename_extension(file):
  file, extension = file.split(".")
  return extension

print("Data.csv => " , get_filename_extension("Data.csv"))
print("Powerline.json => " , get_filename_extension("Powerline.json"))
print("RocketLeague.png => " , get_filename_extension("RocketLeague.png"))
print(" ")



def is_image_file(image):
  image, end = image.split(".")
  if end == "png" or end == "jpg" or end == "jpeg" or end == "tiff" or end == "gif":
    return True
  else:
    return False
    

print("dog.png => " , is_image_file("dog.png"))
print("cat.image => " , is_image_file("cat.image"))
print("house.jpeg => " , is_image_file("house.jpeg"))
print("monitor.tiff => " , is_image_file("monitor.tiff"))