import bs4
import re
import  requests
import mobafire_scrapper
import itemstonum
import export_items,opening

req = requests.get('https://www.mobafire.com/league-of-legends/champions')
soup_object = bs4.BeautifulSoup(req.content , features="html.parser")
opening.open()
y = input('Enter Path of the game'
          '\tFor Garena 32771 folder path\n')
pathofgame = y + '\Game\Config\Champions\\'

links_with_text = []
for a in soup_object.find_all('a',{"class":re.compile("champ-list__item visible")}, href=True):
    if a.text:
        links_with_text.append(a['href'])
# print(links_with_text)

for h in range(0,len(links_with_text)):


    all_items = mobafire_scrapper.get_item_names(links_with_text[h])
    # print(all_items)
    if all_items == None:
        continue

    items = all_items['c'] + all_items['b'] + all_items['l']

    final =[]
    final = itemstonum.get_item_number(items)
    # print(final)

    core = len(all_items['c'])
    boots = len(all_items['b'])
    lux = len(all_items['l'])
    # print(core,boots,lux)
    # print(boots+core+lux)
    # print(len(final))

    final_di = {
        "title": "MobaFire "+all_items['n'] ,
        "type": "custom" ,
        "map": "any" ,
        "mode": "any" ,
        "priority": "false" ,
        "champion": all_items['n'] ,
        "blocks": [{"items": [] , "type": "Core Items"} ,
                   {"items": [] , "type": "Other Items"} ,
                   {"items": [] , "type": "Boots"}]}

    for i in range(0 , core):
        final_di["blocks"][0]['items'].append({"count": 1 , "id": final[i]} , )
    # print(boots+core , boots + core + lux)
    for i in range(boots+core , boots + core + lux):
        final_di["blocks"][1]['items'].append({"count": 1 , "id": final[i]} , )
    # print(core ,boots+core)
    for i in range(core ,boots+core):
        final_di["blocks"][2]['items'].append({"count": 1 , "id": final[i]} , )

    print(h , 'Importing' , all_items['n'] , 'Build.......')
    export_items.write_items(all_items['n'],final_di,pathofgame)

