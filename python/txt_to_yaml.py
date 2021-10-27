'''
txt_to_yaml.py
reads text file list of events with the following characteristics
  file name YYYY.txt (ex 2014.txt)
  line formats: 
    MM/DD Event Title with a bunch of information
      or
    MM/DD - MM/DD Event Title with a bunch of information
parses data to 
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

# open outfile
outfile_name = '_events.txt'
try:
  outfile = open(outfile_name, "w")
  print("writing to", outfile_name)
except:
  print("could not open", outfile_name)

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

        # Format Title
        title = ""
        i = 1
        # skip over date values
        if end_date != date:
          # end date and date are different
          # skip both dates and hyphen
          i = 3
        while i < len(words):
          title += words[i]
          # add space if it is not the last word
          if i != len(words)-1:
            title += " "
          i += 1

        # remove illegal chars 
        title = title.replace('w/', 'with')
        title = title.replace('"', '')
        title = title.replace('/', '-')
        title = title.replace(':', ' -')
        title = title.replace('&', 'and')

        # generate artists 

        # generate categories
        categories = {"visual"}

        #generate description

        # generate links

        # generate post_url

        # generate asset_folder
        asset_folder = "/assets/{}/{}"
        asset_folder = asset_folder.format(year, date_string)

        # Write data to outfile
        # print(".")
        try:
          outfile.write("- title: ")
          outfile.write(title)

          outfile.write("\n\tyear: ")
          outfile.write(str(year))

          outfile.write("\n\tdate: ")
          outfile.write(date_string)

          outfile.write("\n\tend_date: ")
          if end_date_string != date_string:
            outfile.write(end_date_string)

          outfile.write("\n\tartists:")
          # for artist in artists:
          #   outfile.write("\n\t\t- ")
          #   outfile.write(arist)

          outfile.write("\n\tcategories:")
          # todo: declare categories
          for category in categories:
            outfile.write("\n\t\t- ")
            outfile.write(category)

          outfile.write("\n\tdescription: ")

          outfile.write("\n\tlinks:")
          # for link in links:
          #   outfile.write("\n\t\t- ")
          #   outfile.write(link)

          outfile.write("\n\tpost_url: ")
          # todo: concatenate event title

          outfile.write("\n\tasset_folder: ")
          outfile.write(asset_folder)

          outfile.write("\n\n")

        except:
          print("could not write", title)
          
    infile.close()
    year += 1
print("done")
outfile.close()
print("file closed")