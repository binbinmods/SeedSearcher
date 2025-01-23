import pandas as pd
import re
import pickle
import os

def dicts_to_excel(dict_sheet_pairs, output_file):
   
    # Create Excel writer object
    with pd.ExcelWriter(output_file) as writer:
        for dictionary, sheet_name in dict_sheet_pairs:
            max_values = max(len(values) for values in dictionary.values())
            
            columns = ['Item'] + [f'Seed {i+1}' for i in range(max_values)]
            df = pd.DataFrame(columns=columns)
            
            for key, values in dictionary.items():
                row = [key] + values + [''] * (max_values - len(values))
                df.loc[len(df)] = row
            
            df.to_excel(writer, sheet_name=sheet_name, index=False)

def pickle_excel(filename:str):
    df = pd.read_excel(filename, sheet_name ="eventReply")

    with open("DataTextReference.pkl", "wb") as f:
        pickle.dump(df, f)    


def lookup_events(filename:str, id_list) ->dict:
    if os.path.exists("DataTextReference.pkl"):
        with open("DataTextReference.pkl", "rb") as f:
            df = pickle.load(f)
    else:
        df = pd.read_excel(filename, sheet_name ="eventReply")
        pickle_excel(filename)

    lookup_dict = dict(zip(df['SSLootList'], df['medsEvent']))
    
    results = {}
    for id_value in id_list:
        results[id_value] = lookup_dict.get(id_value, 'e_sen1_a')
    
    return results

def create_lists():
    regular_drops = """FrozenSewersElves
            FrozenSewersMix
            FrozenSewersRatmen
            Jewelerrings
            Mansionleft
            Mansionleftplus
            Sailor
            Shady
            Stolenitems
            apprentince
            balanceblack
            balanceboth
            balancewhite
            battlefield
            bridge
            chappel
            crane
            crocoloot
            crocosmugglers
            desertreliquary
            dreadcosme
            dreadcuthbert
            dreadfrancis
            dreadhoratio
            dreadjack
            dreadmimic
            dreadpurser
            dreadpurserstash
            dreadrhodogor
            eeriechest_a
            eeriechest_b
            lavacascade
            lootedarmory
            lootsepulchralrare
            obsidianall
            obsidiananvil
            obsidianboots
            obsidianrings
            obsidianrods
            rift
            riftsen
            sahtibernardstash
            sahtidomedesert
            sahtidomeice
            sahtidomemain
            sahtidomemountain
            sahtidomeswamp
            sahtipiratearsenal
            sahtipiratewarehouse
            sahtiplaguecot
            sahtisurgeonarsenal
            sahtisurgeonstash
            sahtitreasurechamber
            sahtivalkyriestash
            thorimsrod
            treasureaquarfall
            uprienergy
            uprimagma
            voidcraftemerald
            voidcraftgolden
            voidcraftobsidian
            voidcraftpearl
            voidcraftring
            voidcraftrodsofblasting
            voidcraftruby
            voidcraftsapphire
            voidcrafttopaz
            voidtreasurejade
            watermill"""
    regular_drops = regular_drops.split()
    pet_drops = """Jelly
            betty
            blobbleed
            blobcold
            blobdire
            blobholy
            bloblightning
            blobmetal
            blobmind
            blobpoison
            blobselem
            blobshadow
            blobsmyst
            blobsphys
            blobwater
            cuby
            cubyd
            daley
            fenny
            fishlava
            inky
            liante
            matey
            mimy
            obechampy
            obechompy
            obechumpy
            oculy
            sharpy
            slimy
            stormy
            wolfy"""
    pet_drops = pet_drops.split()
    boss_drops = """Basthet
            Dryad_a
            Dryad_b
            Faeborg
            Hydra
            Ignidoh
            Mansionright
            Mortis
            Tulah
            Ylmer
            belphyor
            belphyorquest
            burninghand
            dreadhalfman
            elvenarmory
            elvenarmoryplus
            goblintown
            harpychest
            harpyfight
            khazakdhum
            kingrat
            minotaurcave
            sahtikraken
            sahtikrakenmjolmir
            sahtirustkingtreasure
            spiderqueen
            tyrant
            tyrantbeavers
            tyrantchampy
            tyrantchompy
            tyrantchumpy
            upripreboss
            yogger"""
    boss_drops = boss_drops.split()
    mythics = """towntier3
            towntier3_a
            towntier3_b
            ruinedplaza
            ruinedplaza_crit
            voidasmody
            voidshop
            voidtreasure
            voidtreasurejade
            voidtsnemo
            voidtwins
            wareacc1
            wareacc2
            warearm1
            warearm2
            warejew1
            warejew2
            warenavalea
            wareweap1
            wareweap2
            """
    mythics = mythics.split()
    return regular_drops,pet_drops,boss_drops,mythics


def convert_event_to_node(event:str) -> str:
    base:str = event.split("_")
    try:
        base = base[1]
    except:
        print(f"Error with {event}")
        return
    split = re.split('(\d.*)',base)
    return "_".join(split[:-1])

def get_base_dictionaries():
    loot_lists = create_lists()
    ids_to_lookup = loot_lists[1]
    print(ids_to_lookup)

    events = lookup_events('DataTextReference.xlsx', ids_to_lookup)
    for id_value, event in events.items():
        print(f"{{\"{id_value}\", \"{convert_event_to_node(event)}\"}},")

if __name__ == "__main__":
    get_base_dictionaries()

    caravanDict = {}

    shopDict = {}

    guaranteedDict = {}

    mythicDict = {}

    dict_sheet_pairs = [
        (caravanDict, 'Caravan Items'),
        (shopDict, 'Shop Items'),
        (guaranteedDict, 'Boss Drops'),
        (mythicDict, 'Mythics')
    ]
    
    

    # dicts_to_excel(dict_sheet_pairs, 'SeedList.xlsx')