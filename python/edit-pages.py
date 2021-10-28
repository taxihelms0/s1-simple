import os

print("edit pages")

os.chdir('..')
os.chdir('_posts')
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  # print(f)
  if '.md' in f:
    print(f)
    # open file
    with open(f, "r") as infile:
      data = infile.readlines()
      # print(data[1])
    infile.close()
    
    i = 0
    layout_flag = False
    while i < len(data):
      if "layout: post" in data[i]:
        print("layout declaration found! moving on...")
        layout_flag = True
      i += 1
    
    
    if layout_flag is False:
      print("editing:", data[1])
      data[0] = "---\nlayout: post\n"  
      with open(f, "w") as outfile:
        outfile.writelines(data)
      outfile.close()
    