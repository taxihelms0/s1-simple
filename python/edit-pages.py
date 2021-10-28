import os

print("edit pages")

# os.chdir('..')
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
    asset_line_string = "asset_folder: {}"
    post_url_string = ""
    while i < len(data):
      if "layout: post" in data[i]:
        print("layout declaration found! moving on...")
        layout_flag = True
      if "post_url: " in data[i]:
        post_url_string = data[i].replace('post_url: ', '')
      if "asset_folder" in data[i]:
        data[i] = asset_line_string.format(post_url_string.replace('.md', ''))
        print(data[i])
      i += 1
    
    
    if layout_flag is False:
      print("editing:", data[1])
      data[0] = "---\nlayout: post\n"  

    with open(f, "w") as outfile:
      outfile.writelines(data)
    outfile.close()
    