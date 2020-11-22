import os
import json


def write_items(champ_name,final_di,pathofgame):
    # print(champ_name)


    # pathofgame= r'C:\Users\Anwin Kushal\Documents\GAMES\Legue of legends\32771\Game\Config\Champions\\'
    # print(pathofgame+champ_name)

    if not os.path.exists(pathofgame + champ_name):
        os.makedirs(pathofgame + champ_name)

    if not os.path.exists(pathofgame + champ_name + '/Recommended'):
        os.makedirs(pathofgame + champ_name + '/Recommended')

    with open(pathofgame + champ_name + '/Recommended/' + 'mobafire_' + champ_name+'.json' , 'w') as filehandle:
        filehandle.write(json.dumps(final_di))