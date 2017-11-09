import urllib2
import pafy
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_Touhou_Project_characters"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.findAll('dt')
touhou_names = []
for name in name_box:
  name = str(name)
  name = name.split('<')

  real_name = name[1][3:]
  touhou_names.append(real_name[:-1])

print (touhou_names)

url = "https://www.youtube.com/watch?v=1_D7kiOR9fA"
video = pafy.new(url)

description = video.description

# change this into whatever scrape off wiki site
# https://en.wikipedia.org/wiki/List_of_Touhou_Project_characters


good_videos = []

description2 = description.split(' ')

for character in touhou_names:
  character = character.lower()
  if character in description:
    if (video not in good_videos):
      good_videos.append(video)

print(good_videos)
print(good_videos[0].thumb.replace("default", "hqdefault"))
