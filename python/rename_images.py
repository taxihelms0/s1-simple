import os

dir_flag = False

while dir_flag is False:
  # img_dir = input("image directory path: ")
  img_dir = "assets/2016/2016-06-25-Mistake"
  try:
    os.chdir(img_dir)
    dir_flag = True
  except:
    print("try again")
    dir_flag = False
    break
files = os.listdir('.')
for f in files:
  print(f)
  if f[0] == "_":
    new_f = f.replace("_", "I", 1)
    print("renaming to:", new_f)
    try:
      os.rename(f, new_f)
    except:
      print("could not rename to", new_f )

print("new list of files:")
files = os.listdir('.')
for f in files:
  print(f)