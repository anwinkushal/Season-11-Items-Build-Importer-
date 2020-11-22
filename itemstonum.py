from bs4 import BeautifulSoup as bs
import requests
import re
# py -m http.server 8000
# req = requests.get('http://localhost:8000/Items%20_%20League%20of%20Legends.html')
# print(req)
#
# soup_obj = bs(req.content,features="html.parser")
#
# item_name=[]
# item_number=[]
#
# for el in soup_obj.find_all("div",{"class":"name","data-v-8141a30c":re.compile("")},text=True):  # find  using class name
#     name = el.get_text()            #from the line get only text
#     item_name.append(name)
# print(item_name)
# # name_dict = dict.fromkeys(item_name,"item_name")
# # print(list(name_dict))
# items = soup_obj.find_all("img",{"data-v-8141a30c":re.compile("")})
#
# for el in items:
#     item_number.append(el['src'][-8:-4])
# print(item_number)
# print(len(item_number) ,len(item_name))
#
# # d =['Boots', 'Faerie Charm', 'Rejuvenation Bead', "Giant's Belt", 'Cloak of Agility']
item_name = ['BOOTS', 'FAERIE CHARM', 'REJUVENATION BEAD', "GIANT'S BELT", 'CLOAK OF AGILITY', 'BLASTING WAND', 'SAPPHIRE CRYSTAL', 'RUBY CRYSTAL', 'CLOTH ARMOR', 'CHAIN VEST', 'NULL-MAGIC MANTLE', 'EMBERKNIFE', 'LONG SWORD', 'PICKAXE', 'B. F. SWORD', 'HAILBLADE', 'DAGGER', 'RECURVE BOW', 'AMPLIFYING TOME', 'VAMPIRIC SCEPTER', "DORAN'S SHIELD", "DORAN'S BLADE", "DORAN'S RING", 'NEGATRON CLOAK', 'NEEDLESSLY LARGE ROD', 'DARK SEAL', 'CULL', 'HEALTH POTION', 'KIRCHEIS SHARD', 'REFILLABLE POTION', 'CORRUPTING POTION', "GUARDIAN'S HORN", 'PORO-SNAX', 'CONTROL WARD', "SHURELYA'S BATTLESONG", 'ELIXIR OF IRON', 'ELIXIR OF SORCERY', 'ELIXIR OF WRATH', 'COMMENCING STOPWATCH', 'STOPWATCH', 'SLIGHTLY MAGICAL FOOTWARE', 'PERFECTLY TIMED STOPWATCH', 'ABYSSAL MASK', "ARCHANGEL'S STAFF", 'MANAMUNE', "BERSERKER'S GREAVES", 'BOOTS OF SWIFTNESS', 'CHEMTECH PUTRIFIER', "SORCERER'S SHOES", 'GLACIAL BUCKLER', 'GUARDIAN ANGEL', 'INFINITY EDGE', 'MORTAL REMINDER', 'LAST WHISPER', "LORD DOMINIK'S REGARDS", "SERAPH'S EMBRACE", "MEJAI'S SOULSTEALER", 'MURAMANA', 'MURAMANA', 'PHAGE', 'PHANTOM DANCER', 'PLATED STEELCAPS', "SERAPH'S EMBRACE", "ZEKE'S CONVERGENCE", 'HEARTHBOUND AXE', "STERAK'S GAGE", 'SHEEN', 'SPIRIT VISAGE', 'WINGED MOONPLATE', 'KINDLEGEM', 'SUNFIRE AEGIS', 'TEAR OF THE GODDESS', 'BLACK CLEAVER', 'BLOODTHIRSTER', 'RAVENOUS HYDRA', 'THORNMAIL', 'BRAMBLE VEST', 'TIAMAT', 'TRINITY FORCE', "WARDEN'S MAIL", "WARMOG'S ARMOR", "RUNAAN'S HURRICANE", 'ZEAL', "RABADON'S DEATHCAP", "WIT'S END", 'RAPID FIRECANNON', 'STORMRAZOR', 'LICH BANE', "BANSHEE'S VEIL", 'AEGIS OF THE LEGION', 'REDEMPTION', 'FIENDISH CODEX', "KNIGHT'S VOW", 'FROZEN HEART', "MERCURY'S TREADS", "GUARDIAN'S ORB", 'AETHER WISP', 'FORBIDDEN IDOL', "NASHOR'S TOOTH", "RYLAI'S CRYSTAL SCEPTER", 'MOBILITY BOOTS', "EXECUTIONER'S CALLING", "GUINSOO'S RAGEBLADE", "CAULFIELD'S WARHAMMER", 'SERRATED DIRK', 'VOID STAFF', 'MERCURIAL SCIMITAR', 'QUICKSILVER SASH', "YOUMUU'S GHOSTBLADE", "RANDUIN'S OMEN", 'HEXTECH ALTERNATOR', 'HEXTECH ROCKETBELT', 'BLADE OF THE RUINED KING', 'HEXDRINKER', 'MAW OF MALMORTIUS', "ZHONYA'S HOURGLASS", 'IONIAN BOOTS OF LUCIDITY', 'MORELLONOMICON', "GUARDIAN'S BLADE", 'UMBRAL GLAIVE', 'SANGUINE BLADE', "GUARDIAN'S HAMMER", 'LOCKET OF THE IRON SOLARI', "SEEKER'S ARMGUARD", 'GARGOYLE STONEPLATE', "SPECTRE'S COWL", "MIKAEL'S BLESSING", 'SCARECROW EFFIGY', 'STEALTH WARD', 'FARSIGHT ALTERATION', 'ORACLE LENS', 'ARDENT CENSER', 'ESSENCE REAVER', "KALISTA'S BLACK SPEAR", "KALISTA'S BLACK SPEAR", "DEAD MAN'S PLATE", 'TITANIC HYDRA', 'CRYSTALLINE BRACER', 'LOST CHAPTER', 'EDGE OF NIGHT', "SPELLTHIEF'S EDGE", 'FROSTFANG', 'SHARD OF TRUE ICE', 'STEEL SHOULDERGUARDS', 'RUNESTEEL SPAULDERS', 'PAULDRONS OF WHITEROCK', 'RELIC SHIELD', "TARGON'S BUCKLER", 'BULWARK OF THE MOUNTAIN', 'SPECTRAL SICKLE', 'HARROWING CRESCENT', 'BLACK MIST SCYTHE', 'OBLIVION ORB', 'IMPERIAL MANDATE', 'FORCE OF NATURE', 'THE GOLDEN SPATULA', 'HORIZON FOCUS', 'COSMIC DRIVE', 'BLIGHTING JEWEL', 'VERDANT BARRIER', 'RIFTMAKER', 'LEECHING LEER', 'NIGHT HARVESTER', 'DEMONIC EMBRACE', 'WATCHFUL WARDSTONE', 'STIRRING WARDSTONE', 'BANDLEGLASS MIRROR', 'VIGILANT WARDSTONE', 'IRONSPIKE WHIP', 'SILVERMERE DAWN', "DEATH'S DANCE", 'CHEMPUNK CHAINSWORD', 'STAFF OF FLOWING WATER', 'MOONSTONE RENEWER', 'GOREDRINKER', 'STRIDEBREAKER', 'DIVINE SUNDERER', "LIANDRY'S ANGUISH", "LUDEN'S TEMPEST", 'EVERFROST', "BAMI'S CINDER", 'FROSTFIRE GAUNTLET', 'TURBO CHEMTANK', 'NOONQUIVER', 'GALEFORCE', 'KRAKEN SLAYER', 'IMMORTAL SHIELDBOW', 'NAVORI QUICKBLADES', 'THE COLLECTOR', 'RAGEKNIFE', 'DUSKBLADE OF DRAKTHARR', 'ECLIPSE', "PROWLER'S CLAW", "SERYLDA'S GRUDGE", "SERPENT'S FANG"]
item_number = ['1001', '1004', '1006', '1011', '1018', '1026', '1027', '1028', '1029', '1031', '1033', '1035', '1036', '1037', '1038', '1039', '1042', '1043', '1052', '1053', '1054', '1055', '1056', '1057', '1058', '1082', '1083', '2003', '2015', '2031', '2033', '2051', '2052', '2055', '2065', '2138', '2139', '2140', '2419', '2420', '2422', '2423', '3001', '3003', '3004', '3006', '3009', '3011', '3020', '3024', '3026', '3031', '3033', '3035', '3036', '3040', '3041', '3042', '3043', '3044', '3046', '3047', '3048', '3050', '3051', '3053', '3057', '3065', '3066', '3067', '3068', '3070', '3071', '3072', '3074', '3075', '3076', '3077', '3078', '3082', '3083', '3085', '3086', '3089', '3091', '3094', '3095', '3100', '3102', '3105', '3107', '3108', '3109', '3110', '3111', '3112', '3113', '3114', '3115', '3116', '3117', '3123', '3124', '3133', '3134', '3135', '3139', '3140', '3142', '3143', '3145', '3152', '3153', '3155', '3156', '3157', '3158', '3165', '3177', '3179', '3181', '3184', '3190', '3191', '3193', '3211', '3222', '3330', '3340', '3363', '3364', '3504', '3508', '3599', '3600', '3742', '3748', '3801', '3802', '3814', '3850', '3851', '3853', '3854', '3855', '3857', '3858', '3859', '3860', '3862', '3863', '3864', '3916', '4005', '4401', '4403', '4628', '4629', '4630', '4632', '4633', '4635', '4636', '4637', '4638', '4641', '4642', '4643', '6029', '6035', '6333', '6609', '6616', '6617', '6630', '6631', '6632', '6653', '6655', '6656', '6660', '6662', '6664', '6670', '6671', '6672', '6673', '6675', '6676', '6677', '6691', '6692', '6693', '6694', '6695']


def get_item_number(items_mix):

    items=[iii.upper() for iii in items_mix]

    # print('-----',items)
    web_item_number = []
    final_json_no = []
    # print(len(items))
    # print(item_number.index('3047'),item_name[61])
    for it in items:

        try:
            web_item_number.append(item_name.index(it))
        except ValueError:
            # print(it)
            if it == 'NINJA TABI':
                web_item_number.append(61)
                # print(it,' plated steelcaps')
            elif it == '':
                web_item_number.append(154)
                # print(it,'Force of Nature')
            else:
                web_item_number.append(0)
                print(it+' <<<<<<<<<<<<<<<<<New Error change Required>>>>>>>>>')

    # print(web_item_number)
    for no in web_item_number:
        final_json_no.append(item_number[no])

    # a=[]
    # for t in final_json_no:
    #     a.append(item_name[item_number.index(t)])
    # print(a)
    # print(len(final_json_no),final_json_no)
    return final_json_no



    # print(len(web_item_number),len(items),len(final_json_no))
    #
    #
    # print('checking...')
    # if len(items) == len(final_json_no):
    #     print('no error')
    # else:
    #     print('error')
    # #
    # print(items[4] , web_item_number[4] , final_json_no[4] ,
    #       item_name.index('Ionian Boots of Lucidity')
    #       ,item_number[item_name.index('Ionian Boots of Lucidity')]
    #       )