import pandas as pd
from bs4 import BeautifulSoup
import requests

temp = ['RafaelMiguel03', 'acheamponge', 'JirroReo', 'ron-ligsay', 'jashuleyn', 'yam-1111', 'PaullyMac', 'Novelle-Estrella', 'kisuuuuu', 'LloydLegaspi', 'chrismargo', 'markmcrg', 'OmdenaAI', 'znarfm', 'jrzvnn', 'Karmotrine', 'patkyu', 'Google-Developer-Student-Clubs-PUP-Main']
user_links = ['https://github.com/'+ x for x in temp]

useragent = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"}

output_dict = {
    'name': [],
    'bio': [],
    'contrib': [],
    'followers': [],
    'following': []
}
for i, user in enumerate(user_links):
  r = requests.get(user, headers=useragent)
  soup = BeautifulSoup(r.text)
  print("scraping user #" + str(i+1) + " link: " + user)
  name = soup.select_one("h1.vcard-names > span:nth-of-type(1)")
  if name is not None:
    name = name.text.strip()
  try:
    bio = soup.select("div.p-note.user-profile-bio.mb-3.js-user-profile-bio.f4 > *")[0].text.strip()
  except:
    bio = ""
  try:
    contrib = soup.select_one("div.position-relative > h2").text.replace(" ", "").replace("\n", "").replace("contributionsinthelastyear", "")
  except:
    contrib = ''
  try:
    div = soup.select_one("div.flex-order-1.flex-md-order-none.mt-2.mt-md-0")
    followers = div.select_one("div:nth-of-type(1) > a:nth-of-type(1) > span")
    if followers is not None:
      followers = followers.text
    following = div.select_one("div:nth-of-type(1) > a:nth-of-type(2) > span")
    if following is not None:
      following = following.text
  except:
    followers = ""
    following = ""

  output_dict['name'].append(name)
  output_dict['bio'].append(bio)
  output_dict['contrib'].append(contrib)
  output_dict['followers'].append(followers)
  output_dict['following'].append(following)

df = pd.DataFrame(output_dict)
print(df.head())
df.shape
df.to_csv("github_profiles.csv", index=False)