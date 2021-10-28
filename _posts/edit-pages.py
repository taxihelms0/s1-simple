import os

print("edit pages")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  if '.md' in f:
    # open file
    with open(f, "r") as infile:
      data = infile.readlines()
      print(data[1])
    infile.close()
    data[0] = "---\nlayout: post\n"
    with open(f, "w") as outfile:
      outfile.writelines(data)

