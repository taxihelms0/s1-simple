'''
txt_to_yaml.py
reads text file list of events with the following characteristics
  file name YYYY.txt (ex 2014.txt)
  line formats: 
    MM/DD Event Title with a bunch of information
      or
    MM/DD - MM/DD Event Title with a bunch of information
It also creates an individual .md file for the event
'''

import os

def parse_date(yr, dt):
  dt = dt.split('/')
  month = dt[0]
  if len(month) > 1:
    month_string = "{}"
  else: 
    month_string = "0{}"
  month_string = month_string.format(month)
  try:
    day = dt[1]
  except:
    print("couldn't process date: ", words)
  if len(day) > 1:
    day_string = "{}"
  else:
    day_string = "0{}"
  day_string = day_string.format(day)

  dt_string = "{}-{}-{}" 
  dt_string = dt_string.format(yr,month_string,day_string)
  return dt_string

files = [f for f in os.listdir('.') if os.path.isfile(f)]

# open yaml_outfile
yaml_filename = '_events.yml'
try:
  yaml_outfile = open(yaml_filename, "w")
  print("writing to", yaml_filename)
except:
  print("could not open", yaml_filename)

year = 2014
# for f in files:
  # if '.txt' in f and '_' not in f:
while year <= 2018: 
  infile_name = "{}.txt"
  infile_name = infile_name.format(year)
  print(infile_name)
  # infile_name = ""
  # year = infile_name.strip('.txt')
  # open infile and read
  print("reading", infile_name)
  with open(infile_name, "r") as infile:
    data = infile.readlines()
    for line in data:
      words = line.split()
      if words:
        # Format Date
        date = words[0]
        end_date = date
        date_string = parse_date(year, date)
        # print("date:", date_string)
        if words[1] == "-":
          end_date = words[2]
        end_date_string = parse_date(year, end_date)
        # print("end_date:", end_date_string)

        # Format Title & post_url
        title = ""
        post_url = date_string
        i = 1
        # skip over date values
        if end_date != date:
          # end date and date are different
          # skip both dates and hyphen
          i = 3
        
        title = " ".join(words[i:len(words)])
        url_string = words[i].replace('/', '')
        post_url = date_string + "-" + url_string + '.md'

        # remove illegal chars 
        title = title.replace('w/', 'with')
        title = title.replace('"', '')
        title = title.replace('/', '-')
        title = title.replace(':', ' -')
        title = title.replace('&', 'and')

        post_url = post_url.replace('w/', 'with')
        post_url = post_url.replace('"', '')
        post_url = post_url.replace('/', '-')
        post_url = post_url.replace(':', '')
        post_url = post_url.replace('&', '-')
        post_url = post_url.replace(',', '')
        post_url = post_url.replace('---', '')
        post_url = post_url.replace('é', 'e')

        # generate artists 

        # generate categories
        categories = "visual"

        #generate description

        # generate links

        # generate asset_folder
        asset_folder = "/assets/{}/{}"
        asset_folder = asset_folder.format(year, date_string)

        # Write data to yaml_outfile
        try:
          yaml_outfile.write("- post_url: ")
          yaml_outfile.write(post_url)

          yaml_outfile.write("\n  title: ")
          yaml_outfile.write(title)

          yaml_outfile.write("\n  year: ")
          yaml_outfile.write(str(year))

          yaml_outfile.write("\n  date: ")
          yaml_outfile.write(date_string)

          yaml_outfile.write("\n  end_date: ")
          if end_date_string != date_string:
            yaml_outfile.write(end_date_string)

          yaml_outfile.write("\n  artists: ")
          # for artist in artists:
          #   yaml_outfile.write("\n    - ")
          #   yaml_outfile.write(arist)

          yaml_outfile.write("\n  categories: ")
          yaml_outfile.write(categories)

          yaml_outfile.write("\n  description: ")

          yaml_outfile.write("\n  links: ")
          # for link in links:
          #   yaml_outfile.write("\n    - ")
          #   yaml_outfile.write(link)

          yaml_outfile.write("\n  asset_folder: ")
          yaml_outfile.write(asset_folder)

          yaml_outfile.write("\n\n")

        except:
          print("could not write yaml", title)
        
        
    infile.close()
    year += 1
print("done")
yaml_outfile.close()
print("file closed")