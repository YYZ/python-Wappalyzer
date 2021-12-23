import json
import requests
from Wappalyzer import Wappalyzer, WebPage

wapp = Wappalyzer.latest(technologies_file='Wappalyzer/data/technologies.json')
page = WebPage.new_from_url('https://www.nextdirect.com/nl/en')
print(wapp.analyze_with_categories(page))
# # """
# Changes -
#
# 'scripts' ->> scriptSrc
#
# """
f = open('Wappalyzer/data/technologies-old.json')
x = json.load(f)
starts = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"}
# starts = {"a"}

categories = 'https://raw.githubusercontent.com/AliasIO/wappalyzer/master/src/categories.json'
new_tech_url = 'https://raw.githubusercontent.com/AliasIO/wappalyzer/master/src/technologies/'
all_new_tech = {}
for letter in starts:
    url = new_tech_url + letter + '.json'
    data = requests.get(url)
    tech = json.loads(data.content)
    for item in tech:
        tmp = tech[item]
        if 'scriptSrc' in tmp:
            tmp['scripts'] = tmp['scriptSrc']
        all_new_tech[item] = tmp

print(len(all_new_tech))
print(len(x['technologies']))
print(len(x['categories']))

cats = requests.get(categories)
category_data = json.loads(cats.content)
new_tech_data = {
    '$schema': '../schema.json',
    'categories': category_data,
    'technologies': all_new_tech
}
with open('Wappalyzer/data/technologies.json', 'w',encoding="utf-8") as file:
    json.dump(new_tech_data, file)