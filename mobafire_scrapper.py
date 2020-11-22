import bs4
import re
import  requests

def get_item_names(url):


    req = requests.get('https://www.mobafire.com'+ url)
    soup_object = bs4.BeautifulSoup(req.content , features="html.parser")
    # print(url)

    name= soup_object.find('span',{"class":"champ-name"},text=True).get_text()
    # print(name)

    list_of_core = []

    try:
        c_item = soup_object.find("div" , {"class": re.compile("champ-build__section champ-build__section--twoSixth")})
        core = c_item.find_all("b")
        for d in core:
            list_of_core.append(d.get_text())
        # print(list_of_core)
        list_of_boots = []

        c_item = soup_object.find("div" , {"class": re.compile("champ-build__section champ-build__section--oneSixth")})
        core = c_item.find_all("b")
        for d in core:
            list_of_boots.append(d.get_text())
        # print(list_of_boots)

        list_of_luxury = []
        c_item = soup_object.find("div" ,
                                  {"class": re.compile("champ-build__section champ-build__section--half luxury-half")})
        core = c_item.find_all("b")
        for d in core:
            list_of_luxury.append(d.get_text())
        # print(list_of_luxury)
        name_dict = dict.fromkeys('n' , name)
        name_dict.update(dict.fromkeys('c' , list_of_core))
        name_dict.update(dict.fromkeys("b" , list_of_boots))
        name_dict.update(dict.fromkeys("l" , list_of_luxury))

        # name_dict = { i :list_of_core  for i in "c" }
        # print(name_dict)
        return (name_dict)
    except:
        print('\n'+url+'  build not present')
        return (None)


