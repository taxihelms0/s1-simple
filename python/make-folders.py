import os

os.chdir('_data')
try:
  with open('_events.yml', 'r') as infile:
    data = infile.readlines()
  infile.close()
except:
  print("could not open _events.yml")

    

if data:
  i = 0
  folders = []
  
  year = ""

  asset_line_string = "asset_folder: {}\n"
  post_url_string = ""
  folder_string = "/assets/{}/{}"
  while i < len(data):
    
    folder_string = "/assets/{}/{}"
    if "post_url: " in data[i]:
      post_url_string = data[i].replace('post_url: ', '').strip('- ')
    if "year: " in data[i]:
      year = data[i].replace("year: ", '').strip('\n')
      # print(year.strip())
    if "asset_folder: " in data[i]:
      # print(data[i])
      # print(year)
      # print(post_url_string)
      folder_string = folder_string.format(year.strip(), post_url_string.replace('.md\n',''))
      # print(folder_string)
      folders.append(folder_string)
      print(folder_string)
      data[i] = "  asset_folder: " + folder_string + "\n"
      # print(data[i])
      # print(data[i])
    i += 1

# this is to write the yaml file, leave it commented out
# try:
#   with open('_events.yml', "w") as outfile:
#     outfile.writelines(data)
#   outfile.close()
#   print("_events.yml written")
# except:
#   print("could not write to _events.yml")


os.chdir('..')
for folder in folders:
  print(folder)
    
    
  # if '.yml' in f:
  #   with open(f, "r") as infile:
  #     data = infile.readlines()
  #   infile.close()

