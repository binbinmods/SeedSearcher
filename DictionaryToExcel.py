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
    # get_base_dictionaries()

    caravanDict = {"Acolyte Tunic":["CPNRPRS","BY8P4EZ","BYSZPFX","T23K2EH","95M86EB"],"Acolyte Tunic (Corrupted)":["X4K66Y6"],"Advanced Handbook":["DFHZSGR","YK9RBX8","824DQRM","D6Y6Z4N","PE5H6FT"],"Advanced Handbook (Corrupted)":["MZRP3FQ","63HRCPK","Q3BFWGH","TD5NEG4","NY2ZGMP"],"Agate Amulet":["EE6SKHY","GZZBHYE"],"Alarm Bell":["ZBDW4PC","MGE8EZQ","ZRG3GZT","P3PFGE9","D5HM66T"],"Alarm Bell (Corrupted)":["YRQSD8Q","3HNSF89","CWFMP8Y","HQYQHKD","T6DS69Y"],"Alchemy Pot":["8D9383T","EMWHS3C","BT5RG4A","NH4PCSN","CHZECQS"],"Alchemy Pot (Corrupted)":["RXKK6PF","N4GRHFQ","4WQ4DHB","SS2S2DH","8ZRD4DQ"],"All-seeing Amulet":["MYE6KF9","KPM4QYA","AEHYPA4","GS5FZFR","WG8NXGP"],"All-seeing Amulet (Corrupted)":["K4Q5HNQ","W5YNBDM","2C8GP3K","H84XFXQ","R63XKZ4"],"Amber Amulet":["SRWSXBQ","9E6HAZX","SMHM6ZY","NNX9Z4P","T5SNNGG"],"Amber Amulet (Corrupted)":["KP3EFH8","PE6G933","H3R3XZQ","T3CZRMY","H4CCDB3"],"Amethyst Ring":["TE64ZG8","2MS5562","M64X2YM","SMHM6ZY","Z9TQAMC"],"Amethyst Ring (Corrupted)":["WFGZHF5","ED8G8R8","FKX2RFK","39BXMQK","H3SB968"],"Amulet of Protection":["6DZ8S3A","F6SRTNP","KP8FCWT","MWBFKEH","M54YFSB"],"Amulet of Protection (Corrupted)":["XAH6YHF","GRA2SA4","MMAWGGK","5KMQYBM","4T25MQA"],"Amulet of Speed":["ZRG3GZT","BDDDE5R","6D4RQEB","H2XD53B","D86QC2B"],"Amulet of Speed (Corrupted)":["KNYZ26B","KS4H593","55DTDF3","95S49RS","QRFWRHD"],"Amulet of Thorns":["MSYFWE4","SGMTZFQ","EAZF8NT","CDBNFGY","D6EW6NP"],"Amulet of Thorns (Corrupted)":["PZDYXYA","BXQTCWH","KRBH4KT","Z428T8Y","PHS5ETK"],"Aquamarine Bracelet":["TAYHKE6","ZBDW4PC","ZB4NCAH","X5HNECG","AZHNRNC"],"Aquamarine Bracelet (Corrupted)":["G2FK4ZG","R2YF6Y9","FCS8Z8N","TFC58E3","CBPY2S4"],"Archmage Book":["9GXEDXW","H2G8W9H","FNBNPQH","B2R2GSG","9K58K8F"],"Archmage Book (Corrupted)":["4928FMS","6RAY5EA","CHCX85P","4MPHWCD","4MPHWCD"],"Assassin Tools":["H62NZX8","PMPEFGS","553QFN8","5CPRXTF","F4FE2ND"],"Assassin Tools (Corrupted)":["K94SY6A","FCZWGCB","ARRFR4G","EXQYSQ3","A5BQANB"],"Avoidance Collar":["D4DBRFX","59N9M5B","6EZMA6K","PCKE8DM","Q8TKBAF"],"Avoidance Collar (Corrupted)":["RMQC3GX","CARMKRW","W449SDH","2YCYHEG","2YCYHEG"],"Ball of Wool":["FYQ9HMN","PRSH66A","2ZM3289","SDCWKGY","65TE2SQ"],"Bandages":["GQRPFSZ","AZHNRNC","63KB93D","F3RP9PK","6PXR4C8"],"Bandages (Corrupted)":["QPEXY32","EYMMS4D","X6GRWZH","NQDQBCP","66GADF4"],"Battle Axe":["Z9TQAMC","WSBBD3Y","8SMSRBN","B452M5Z","8MGKNDA"],"Battle Axe (Corrupted)":["SXRFBA8","S3NWNYB","5R6PWHW","62SGABX","9EBHS83"],"Beer Mug":["TAYHKE6","A4PWYTW","RZ24PQW","N94RHZG","PMX4944"],"Beer Mug (Corrupted)":["SGXZHNP","EN5X3KD","CF6Y8B6","K3T9R4T","K4FDPAD"],"Bell":["FMT63K2","CH4BX2M","3XZZ3M2","5QZ2Z3N","QT2KZXE"],"Bell (Corrupted)":["Q6RD4AN","5P6AR4G","AFNZA4C","XDTZYK2","GYCQAXH"],"Berserk Potion":["5GRZKWP","KRAR3DH","YTXD9YA","QPX9M2Q","KZRFAAY"],"Berserk Potion (Corrupted)":["KPKX94N","8FPQBGB","P9N3T35","XRERWY3","F2BBAET"],"Berserker Claw":["92WXERY","MNSCEAD","H36WWM9","FH2GCMM","PK5EHDK"],"Berserker Claw (Corrupted)":["T6F46NK","SSAR862","5QDD4SD","HXNZSTC","RMQWA84"],"Blackguard":["H865NKK","84BC4Z9","HZCAPC8","WDQAZAT","SZBEPMH"],"Blackguard (Corrupted)":["KN69SKT","BWEX36G","ACWEY8C","AWSGFPE","ACWEY8C"],"Bloodguard":["FY6XXXA","WTQ2XQC","TNRN8FM","YC8PGA8","YQHAM4W"],"Bloodguard (Corrupted)":["5FR55SX","AGPET8X","9Z25YFC","9RAWA8T","PHTRK8R"],"Bloodstone":["B6TC46N","MNYYSW4","2AMMMAS","KHEFW3P","ZS2N56S"],"Bloodstone (Corrupted)":["PBP3GMY","ZNAFG6Z","ZWGC2HK","2G9R8R6","2G9R8R6"],"Blunderbuss":["G2FK4ZG","GNGCZBZ","Y6PYQDZ","KP3EFH8","EBHEFX6"],"Blunderbuss (Corrupted)":["3NC94ZE","RC6TT94","XMTPCCN","8XSH3TB","CSNT2S5"],"Bone Ring":["M4RMCEZ","6NCAEBC","6AS9RPB","6K84WQ2","9G2XS83"],"Bone Ring (Corrupted)":["5NTQRF5","HBNAHAQ","BEE6GZ6","G4ZENTX","G4ZENTX"],"Boots of Swiftness":["KRQPHZM","E4AAHPA","5M5FPZA","AYTXPZ9","XZMGNMB"],"Boots of Swiftness (Corrupted)":["9QRZ5YM","8H3N629","SZBEPMH","X2NMDXZ","49K3XKC"],"Brass Amulet":["XFK9XN6","K3E48QD","PCZGW6W","T5W8W23","PD3AFT9"],"Brass Amulet (Corrupted)":["2GSZ4AE","WHHNRM4","XDG94FW","EZ2SKEK","GK93NTQ"],"Breastplate":["XFK9XN6","KB6W58Z","DYPG443","F5MEHWZ","6PXR4C8"],"Breastplate (Corrupted)":["XSQYPBF","4ZWSD6G","FPX3FYD","6EWWDNX","95FQPBT"],"Brigand Armor":["3ES4K4K","CM3MX63","DSZQB3Q","RDQG9C2","PA9ZREQ"],"Brigand Armor (Corrupted)":["CX8SNY3","QBN3ANK","Z8STW3K","QC9TNPM","463M5CN"],"Bucket":["GG2R4YS","ZPXGTWR","AFCENRE","CPF42T4","PAPMEG5"],"Bucket (Corrupted)":["DDS6WAQ","SZ4F4NY","A48MDYN","E36NE2P","8WN4MA3"],"Burning Orb":["RZPF9FX","8Y8X9WQ","X93HC2R","5FCR9EC","S9BESTN"],"Burning Orb (Corrupted)":["8MD9N8E","H2XD53B","2AMMMAS","3HSXPRM","PRM235Y"],"Butcher Block":["96KB22S","MBBN8FE","S3XKRYE","KQ5SCYT","TNSMXKH"],"Butcher Block (Corrupted)":["N9SQP5N","5D3DRWD","E5BPMCA","9QC9CCA","CBKG3G9"],"Butcher's Knife":["8SMSRBN","PA9ZREQ","MYFNPS6","FX9T9ZW","FMZT9MT"],"Butcher's Knife (Corrupted)":["MHY6Z36","2NRGGC8","TR6463C","SZBEPMH","Z3NF3YR"],"Cauldron":["Z9TQAMC","PCZGW6W","WFYR5TD","QZKP6KG","AQYPF5T"],"Cauldron (Corrupted)":["ZQHZSNX","84APXP4","NNQNNA5","XTS4N8N","ATPW9YH"],"Chalice of Kings":["S9BESTN","S9PMBAA","ZECTASR","MG4WZ52","659XKTN"],"Chalice of Kings (Corrupted)":["PK589EY","QFK28A6","8ZX39GF","58F5ZY4","QFK28A6"],"Chalice of Queens":["F5MEHWZ","PSEGDKX","ED8APGF","R59EPRH","6C6FPX5"],"Chalice of Queens (Corrupted)":["8MHNYGQ","FGPSPWE","YE8EMEM","EHWWCR6","GPPTWY3"],"Cheese":["TBZW5W2","63STAXE","TE64ZG8","PF96M2T","2MS5562"],"Cheese (Corrupted)":["K3E48QD","FTZXBWQ","PSEGDKX","8X9MPHP","44RW3PD"],"Clairvoyant Scroll":["Y4C8XHH","KXDADD4","3W9G2RM","B8NF86C","NGH9ZE6"],"Clairvoyant Scroll (Corrupted)":["WENRHMC","E5A4QW3","SN3Q2A5","BQY6KKW","2ADRSBD"],"Clergy Amulet":["Z9TQAMC","RZPF9FX","W9PPD9F","BCR9GFW","D5HM66T"],"Clergy Amulet (Corrupted)":["5RWQMMB","N59ESZB","TFTHW8Z","WX96KDE","5ZAN523"],"Cloak of Evasion":["RKTFFRG","3MX8GGQ","C94MCRY","KNA2Q5G","CH4BX2M"],"Cloak of Evasion (Corrupted)":["GSXG9B6","SM9FYRE","NR4YFCX","EAMK6Z6","2X3QKNC"],"Cloak of Speed":["FY9ZQ5S","FBQSRC6","BTM8Y8E","AKAQ5EN","5DYD5X9"],"Cloak of Speed (Corrupted)":["E2C42GD","TFSC8E9","9HKT423","BH484Y3","RDZKS6N"],"Club (Corrupted)":["CZKHABC"],"Cold Book":["2HMBW9B","3MX8GGQ","C94MCRY","KZRFAAY","AYTXPZ9"],"Cold Book (Corrupted)":["FX2KBS4","B362HMH","GDNQMX3","GQBG8X4","YT4FGRD"],"Continuum Blade":["ME4CBB4","PN9BBNR","TNHDTRD","ZMQ2BTR","D86QC2B"],"Continuum Blade (Corrupted)":["WM5BH3E","5ZSDX9H","KH5GCDK","RW36KDS","4WM4S8B"],"Crank Crossbow":["8BM3CAB","44RW3PD","8AC8Q2K","TTWQ3XS","ZK3MFHF"],"Crank Crossbow (Corrupted)":["KH3SDRR","TFNRHMF","MS6YMRH","MAEZXMQ","KH3SDRR"],"Crossbow":["QPGDG32","3RH2EFZ","PMWNDAM","338GPBW","3RH2EFZ"],"Crusader Helmet":["M4RMCEZ","Y6SY2DR","QRHDDRE","TP8AQR2","KQPKRC5"],"Crusader Helmet (Corrupted)":["RKPWNCS","T69HEF3","MG63CDE","P5GA5RB","P5GA5RB"],"Crystal Ball":["T5SNNGG","FTZXBWQ","262PRNK","KMEWXZA","44RW3PD"],"Crystal Ball (Corrupted)":["MN9MZ6S","SBS438A","MEPWRTR","HYFDBEB","Z9TGQTN"],"Cup of Death":["8253EXW","ZBDW4PC","CPF42T4","T66FQBM","F5ZK3GQ"],"Cup of Death (Corrupted)":["R26QC6D","F6Z4P8E","4HTAPEM","AKAQ5EN","5AAAWYZ"],"Cursed Dagger":["PCZGW6W","5K3B2NB","56QTQPN","3KMQRKG","4ZK42RK"],"Cursed Dagger (Corrupted)":["HAYG8AK","R4KHRFR","2YHQ6MT","FGB2HNH","5P5PH4W"],"Dagger":["M64X2YM","TKQTTED","3MX8GGQ","F3RP9PK","35H9A46"],"Dagger (Corrupted)":["G5TB5FF","8D9383T","8NSCSES","AD8DE2E","92K9M5M"],"Dark Hood":["R2YF6Y9","6MRMNAB","96E9YW5","GY6WFB6","YBX44TK"],"Dark Hood (Corrupted)":["GNGY4D9","3K4QPSM","YC8Q9Q3","SY688BB","QTQNPFZ"],"Darkflame Ring":["MAFXBAZ","5YD9Y56","6NTHE5M","TMZMATY","583RR9M"],"Darkflame Ring (Corrupted)":["FTZTWZ8","6TERPR5","489MA2R","YKPRCRF","6YPCZ6B"],"Dart Pouch":["9GBGZSW","D2FPMHY","TH4YYWN","TTRX8PR","XTP49TX"],"Dart Pouch (Corrupted)":["AWPDY33"],"Destroyer Gauntlets":["C2CSHPH","FDHTHTB","2BZW49R","Q3N2K4C","KW6KEDX"],"Destroyer Gauntlets (Corrupted)":["AG8KZ3X","9HFEPYP","DMNDSM5","Z6KKBYK","E9R2F2D"],"Detox Potion":["2ZB28T5","RKTFFRG","TKQTTED","8SMSRBN","9K98Q6P"],"Detox Potion (Corrupted)":["PBCS4BD","XEFAM3W","5299C6A","SX8SXBH","888BB56"],"Diamond Ring":["9MD56MW","R553HYN","F6M63MS","T958M3P","G84GKBB"],"Diamond Ring (Corrupted)":["GCTAMYC","BZTEPXD","HAMZRSY","D53BFWA","KZZ2GFP"],"Dimensional Crystal":["36PK53K","98YT95B","QHBF5WR","CKYYHMZ","WEZAS68"],"Dimensional Crystal (Corrupted)":["2XH8AA9","MXGT5KT","6KHMHBZ","2DHHQKG","6WM3C63"],"Dirty Bandages":["AWDNB5H","Q2PKZ6Z","2NC5XY4","C8TCHMK","CNZNFPX"],"Dirty Bandages (Corrupted)":["4ARCFRF"],"Divination Orb":["RKTFFRG","PSEGDKX","5GRZKWP","HFF93YM","M43RCAT"],"Divination Orb (Corrupted)":["ZKFPZ2Q","4Q62CX6","TRTKBAC","8PC4X2F","W4MENXH"],"Dream Sphere":["SRWSXBQ","WSBBD3Y","W9PPD9F","MN9MZ6S","F3RP9PK"],"Dream Sphere (Corrupted)":["3PEZ4NY","P6QMYXK","SXBDRZ3","5P9CRES","AD4YKQN"],"Dreamcatcher":["DYGY93G","8YEWT5N","C5RCQTE","TM9CNXY","XGQGPKK"],"Dreamcatcher (Corrupted)":["DE93KHK","HBXFK8A","6HY6BNH","5BNDCP2","MP2FTE9"],"Druidic Amulet":["2GSZ4AE","5EHKG23","FDQ6Y39","E685PCQ","QC9TNPM"],"Druidic Amulet (Corrupted)":["B2AMT3D","CC9WE3A","HZQ5C4R","SQN4Y54","EQ684Z6"],"Dynamite":["ZB4NCAH","262PRNK","PD3AFT9","KMEWXZA","TNAZ6NK"],"Dynamite (Corrupted)":["GG2R4YS","46D9ANW","TMB92FG","9A6CCH6","XS4GNTH"],"Eldritch Ring":["W2X5EFM","B5ZXK6F","R4XSEA6","5MF48DH","AD8DE2E"],"Eldritch Ring (Corrupted)":["ZMZQ2QT","9DMXWKA","SBZN9Z5","DPKMS55","KR626C8"],"Elven Quiver":["2ZB28T5","A4PWYTW","DYPG443","F3RP9PK","9K98Q6P"],"Elven Quiver (Corrupted)":["GG85G9P","2EKH9KY","SFDDEG8","PNSDN84","8ZKX28F"],"Emerald Necklace":["TBZW5W2","TE64ZG8","9E6HAZX","2ZB28T5","3ES4K4K"],"Emerald Necklace (Corrupted)":["SMHM6ZY","QSBH4K8","SHBTCFA","2EFRQKH","PSATF5T"],"Emerald Staff":["Q324GE6","2G3REAW","5H5QPZ9","GK93NTQ","PY6YY6R"],"Emerald Staff (Corrupted)":["ZMBA4ZK","4TNAHQ6","8XA3ERS","WGWDSEH","69ZASZ9"],"Endless Bag":["ED8APGF","TPADYND","4KM4H2W","9Q4A26R","HTFRZSW"],"Endless Bag (Corrupted)":["64X4ECY","2XMXMSF","TAQ3YR8","KS3Y2AY","ADA3NKX"],"Exotic Spices":["K2CPB49","TK5T6CG","DD8TYSM","TQGNZG8","GNQXBDQ"],"Exotic Spices (Corrupted)":["CBBZND9","FABPCS4","THPSCXQ","YTHSQZQ","ED5ED4R"],"Faith Ring":["2MS5562","4R99DRS","6KQSWKH","FTZXBWQ","ZPXGTWR"],"Faith Ring (Corrupted)":["8AC8Q2K","D5GRQR3","PG4FQGH","8HCZ9EN","NGH6N4D"],"Fervent Ring":["YK6KYT4","Q6RD4AN","SHKHYSY","3BZ9MFX","R6E8BY2"],"Fervent Ring (Corrupted)":["Z9HYMBZ","T8FQ6ET","854T3ZW","333W2AP","WH49RZ3"],"Fiery Wand":["MRZW9FB","YB6DFWY","33D4WMX","95TWNDB","NZY3YAD"],"Fire Book":["ZBDW4PC","YRQSD8Q","6PXR4C8","KMEWXZA","Y4C8XHH"],"Fire Book (Corrupted)":["6EWR8QE","GQMBP2R","NP64W5C","SEMXNC9","QGEA8D9"],"Fishing Rod":["W4TM3EA","ME4CBB4","KRAR3DH","QE3K8T2","6K4N2HF"],"Fishing Rod (Corrupted)":["HAHKPRG","FGWKGN3","2M4H2AA","2ZX38WK","NWT6DKM"],"Flail":["FX2KBS4","ED8G8R8","E4AAHPA","H2G8W9H","AYTXPZ9"],"Flail (Corrupted)":["BBDXBXP","RKT8G6X","HKZSZTC","DXZSCWC","RR88R56"],"Flaming Sword":["93FQNPB","GTPWD5R","T3CZRMY","NY3FKAZ","NCKMHH3"],"Flaming Sword (Corrupted)":["P883K3T","R5RTMXQ","28E8BZF","HM56X2P","Y8W2FDW"],"Flute":["GG2R4YS","GQRPFSZ","DYPG443","WQCKTF8","XP4TYDA"],"Flute (Corrupted)":["4QK383Z","GZFMFAX","9AT8AW9","EGWABGZ","2ST2GKD"],"Fork":["63STAXE","2TBK4T4","C9GT6DZ","M5F39AF","TK9K4AT"],"Fork (Corrupted)":["RGFGQFK","SZYE4HG","4XFQXWB","4KX9SWB","FAZ8B23"],"Fountain Pen":["FRTTNP3","Y5SDRWY","RW6R4B6","EEZH8B6","HXFADCF"],"Fountain Pen (Corrupted)":["NXFBWDG","2M922QQ","T5QFXGZ","DZH9RRH","NXFBWDG"],"Four Leaf Clover":["2HMBW9B","6KQSWKH","5FCR9EC","MX5KKGM","3NC94ZE"],"Four Leaf Clover (Corrupted)":["DATR6G8","SSER6N6","2YC5NNK","YMHGMZN","23SRT89"],"Frostfire Ring":["WQCKTF8","6ZSW3QA","5AK3CMQ","ZCCDE6D","C6EAEKB"],"Frostfire Ring (Corrupted)":["FG33HED","X64WCCA","Z2QGX2D","9YZ6DSX","563DPPE"],"Frostguard":["FHFX9W6","XZMGNMB","CX8SNY3","W4CK5C9","2YXFP3A"],"Frostguard (Corrupted)":["5FX9QWE","SE5H8WK","YHD6GPD","M8M8Y4F","DCDE5TH"],"Frozen Orb":["8QEDK6E","2G3REAW","KXKSSGC","FMZT9MT","BFCA6EM"],"Frozen Orb (Corrupted)":["RCT5THZ","NE4SEGW","YYP23HD","4R93CMP","P8PH6PN"],"Garnet Earrings":["B58MBRA","8253EXW","T5SNNGG","4R99DRS","RZPF9FX"],"Garnet Earrings (Corrupted)":["Y4C8XHH","9MD56MW","RDQG9C2","6ZSW3QA","R24QWKG"],"Gauntlets":["262PRNK","PSEGDKX","WRTXBNX","92WXERY","CPD5YBQ"],"Gauntlets (Corrupted)":["X2ETBCA","C48QZ9X","BMTGPMA","RNDTQ3H","QZ9HP96"],"Gihl Runestone":["8BQHWXZ","5R2RNX9","RD6MH4E","X4E2KMG","68FGBGQ"],"Glacial Hammer":["FBQSRC6","YBP4Q98","5SMWTGF","6PD6685","6Z5FSAS"],"Glacial Hammer (Corrupted)":["3E9W86Q","WRFS5ZZ","FZKFN4Z","23653GX","5SRXBHP"],"Gladiator Helmet":["28NEYRK","4R55NXA","6YEGCMN","H89F54B","WYRMHXP"],"Gladiator Helmet (Corrupted)":["9M4WXTR","K4KKGGP","EBHRX4B","PMX492Z","HFFY986"],"Gloves":["X88W35G","W92ZTCG","H8FQS68","24C8BQK","MSH83RP"],"Gloves of Agility":["SRWSXBQ","WSBBD3Y","4GWTPAM","58W662M","WHPEN9F"],"Gloves of Agility (Corrupted)":["XR6Q9WQ","98YNGG4","GNBWYWT","MHX9ZAS","N2F5P43"],"Goggles":["2MS5562","BCR9GFW","FY6XXXA","WXKMXTF","ZPDCZFM"],"Goggles (Corrupted)":["DFHZSGR","4XZEMFZ","B4F83RP","CPHEPHH","45W3K86"],"Gold Chain":["MAFXBAZ","9E6HAZX","TAYHKE6","3ES4K4K","GG2R4YS"],"Gold Chain (Corrupted)":["PN9BBNR","34M59RZ","CDAKGG2","BDZKBKP","XN6NWEA"],"Gold Ring":["2ZB28T5","GQRPFSZ","HE3D5D2","ZB4NCAH","X5HNECG"],"Gold Ring (Corrupted)":["YRQSD8Q","SBS438A","F9EHPMY","Z5YP2YN","5MF48DH"],"Golden Bell":["5A5KREP","68MNWKF","8YWG46D","NSDPZ5N","KK3ADG4"],"Golden Bell (Corrupted)":["6RMGGCM","H53F43R","ARB5D5E","6RMGGCM","H53F43R"],"Golden Chalice":["2MS5562","MAFXBAZ","AFCENRE","NNGD36T","SBS438A"],"Golden Chalice (Corrupted)":["YSS8WCR","S64S32D","T294DYN","5YCZSR2","99KNHXZ"],"Golden Cross":["3ES4K4K","NNX9Z4P","KYFBCQN","MX5KKGM","9K98Q6P"],"Golden Cross (Corrupted)":["E36NE2P","T2FANG9","K6QRZ64","WGWPMK5","EA38SBC"],"Golden Harp":["EQ53ACT","4FNAXZ6","ERNCADE","3NW6CA6","66ERFQP"],"Golden Harp (Corrupted)":["53PDNHM","WAXFBA3","KM98BYX","PG2TSBM","5RKHW8H"],"Greater Health Potion":["FMZT9MT","8NSCSES","H4AZTT9","EBCQRGW","PDKXZRA"],"Greater Health Potion (Corrupted)":["BK8GMEP","SSCYFTY","BGQX9RE","A45CZ4R","GAFMKE6"],"Greater Mana Potion":["6KQSWKH","3NC94ZE","GZZXYBQ","QQYMSCA","EE4ND6N"],"Greater Mana Potion (Corrupted)":["8NQDB4H","564SQMN","NNRAM4T","FX3GG3A","NZK2SEM"],"Handbook":["TE64ZG8","2TBK4T4","HE3D5D2","AFCENRE","ME4CBB4"],"Handbook (Corrupted)":["Z8KTBWN","CDCPYCR","XGWD596","GX82REW","AYENPH5"],"Healing Book":["K3E48QD","RZ24PQW","HFF93YM","RPMWT3D","9MD56MW"],"Healing Book (Corrupted)":["HAZMGY5","Z8AYZEF","N9RNDX2","NNR4E9H","K54W98S"],"Health Potion":["GZWFP6S","44RW3PD","8QEDK6E","6Z8R55F","ZNMTHXK"],"Health Potion (Corrupted)":["ZZKQBEQ","GWEBE4E","GT4APP4","FQ4H3WY","GCS6A8B"],"Heart Amulet":["PF96M2T","9E6HAZX","SMHM6ZY","GNGCZBZ","AZHNRNC"],"Heart Amulet (Corrupted)":["2HMBW9B","92WXERY","DR2XTFP","8AE8NW3","SMWDE58"],"Heart of Thorns":["ZBDW4PC","FKX2RFK","FBYX9MP","DQA6GCC","R6B6X6Q"],"Heart of Thorns (Corrupted)":["6KW34W3","F2R9PEG","QK6DXQG","G39WW63","G6DTS44"],"Heater Shield":["GQRPFSZ","4GWTPAM","ZERPCPE","KRQPHZM","QFKMWBW"],"Heater Shield (Corrupted)":["RY3KW34","RKCEQSP","YWRNEFB","2RK4BZX","NY3P36P"],"Heavy Belt":["4R99DRS","CPF42T4","SBS438A","9A6P9Q6","9NDB5WH"],"Heavy Belt (Corrupted)":["AKKCFGQ","8MG9ND3","BK8GMEP","29K6KET","QPF4DCF"],"Helmet":["8253EXW","A4PWYTW","HE3D5D2","W9PPD9F","D4X8YNN"],"Helmet (Corrupted)":["M6WADEG","AKKCFGQ","E85EG2M","68TPXFF","S52MEEK"],"Holy Book":["M6WADEG","35H9A46","QZA3SA2","RPSKMWQ","9GXEDXW"],"Holy Book (Corrupted)":["FCS8Z8N","B28WQBQ","X2YNKCZ","TN65S9Z","2QCTCW8"],"Holy Hammer":["G5TB5FF","3WT8WW3","5NGRBGS","S6TW39S","ATSMM6Z"],"Holy Hammer (Corrupted)":["8XQQPCP","P8FMEGS","D3S4BC4","8XQQPCP","P8FMEGS"],"Horned Helmet":["AZHNRNC","T235PEN","4FNAXZ6","S4HW6N9","BK6YBTE"],"Horned Helmet (Corrupted)":["8DBEADD","TQ9RXNZ","NAPPWMW","ZQPFX6W","Q2WP53P"],"Hourglass of Death":["8253EXW","K3E48QD","4R99DRS","8BM3CAB","6GMHSHH"],"Hourglass of Death (Corrupted)":["H865NKK","8EX8B5F","X9WWKEN","EGTNDA6","XXR4TKF"],"Hunting Ring":["B58MBRA","8Y8X9WQ","X93HC2R","AGXQHPF","ABPCRS8"],"Hunting Ring (Corrupted)":["YTXD9YA","DMBP9SM","6A38BE2","3RBP6FP","M3H9EKW"],"Icy Wand":["YTF6NPZ","YTGGGSE","P6PGCSE","SGPZBGA","YTGGGSE"],"Icy Wand (Corrupted)":["3AC9DX3","WQR6KB4","3AC9DX3","WQR6KB4","3AC9DX3"],"Iron Wand":["AW2K4AR","NSDWWH8","XYST55F","XK5D6W6","NSDWWH8"],"Jade Ring":["MAFXBAZ","3ES4K4K","TDR2BPN","F5MEHWZ","D4X8YNN"],"Jade Ring (Corrupted)":["ZNXAKDB","N59ESZB","3PEZ4NY","HSQQFE5","Q6RD4AN"],"Justicar Ring":["2MS5562","5RM2XRY","YNDAEBS","WG8PWNX","ARW4XKR"],"Justicar Ring (Corrupted)":["69Q865B","8FMX54T","CWGYZ8Q","CDBKD5B","5WQC592"],"Kite Shield":["CGBQZWE","NHT46SS","ZZB98WS","D2WXZQK","29TCNY4"],"Kite Shield (Corrupted)":["H56955F","36BTMQM","KKT9C4E","XQKGC8R","XTB8XWA"],"Lapis Necklace":["TE64ZG8","PF96M2T","M64X2YM","2HMBW9B","ZB4NCAH"],"Lapis Necklace (Corrupted)":["XGN4TSG","953AGDH","62SGABX","APGT2HC","E4BCXTN"],"Large Pouch":["8BM3CAB","B362HMH","Y2B5ZFE","FTBDCG8","3X46GWG"],"Large Pouch (Corrupted)":["CRP88SZ","5ASH8FY","5AM586W","4BZ8WHK","KBPMXCE"],"Lava Potion":["XFK9XN6","NNX9Z4P","8Z43GCZ","M43RCAT","RSHKWQ2"],"Lava Potion (Corrupted)":["RY3KW34","M4RBDMB","NC39ZDN","R8CRTGP","DXNQXFM"],"Leather Armor":["28N2MEK","W5W3E38","SACQPKG","GRP3YP9","GBTGEFK"],"Leather Boots":["TBZW5W2","TAYHKE6","ZB4NCAH","29HSMRB","SDF5DSX"],"Leather Boots (Corrupted)":["PKAH6F4","ASP989H","TK5QR8D","Z5DYF3H","A6GF2CW"],"Leather Gloves":["RGFGQFK","GNGCZBZ","PAPMEG5","9A4E2EK","EQ53ACT"],"Leather Gloves (Corrupted)":["W4TM3EA","E2A5G5R","YSZDDSD","YH985XS","5FR55SX"],"Life Essence":["CXF5XMC","YAXM8P8","5YWTXN8","6DZ8S3A","9ZAW3KQ"],"Life Essence (Corrupted)":["4DFQANE","6GP3NCC","R64HKCM","4EPWYCP","ZNW8T2R"],"Lightning Book":["M6WADEG","XTHPZHK","FTZXBWQ","QZA3SA2","6SMQNKN"],"Lightning Book (Corrupted)":["DSZQB3Q","WQQAFX9","SHBTCFA","WR63Z9G","PNSDN84"],"Lightning Spear":["RKTFFRG","4HTAPEM","TAP4GWT","39ZMHAM","RGRYXSX"],"Lightning Spear (Corrupted)":["MWTG9B2","AP43YXS","3GSPAQG","HZ4DFNS","3GSPAQG"],"Lockpicks":["YSQ95KX","EBFKRA8","PG466T2","DWFHXW5","NDX9EY5"],"Long Bow":["WFYR5TD","R66ZQQ9","BRCDMXR","6ZZ9BF6","YCT2KSN"],"Long Bow (Corrupted)":["G9YZ3TG","A8MQ6BQ","BY2KM5D","WB29R6H","MZCT63W"],"Lucky Paw":["8SMSRBN","C2CSHPH","N9PY6YX","DDWYNF9","SZ54PSA"],"Lucky Paw (Corrupted)":["93FQNPB","G6AYFH6","6DM8AC9","KRT5YHX","3WE6DFM"],"Madness Ring":["GPXX64T","5SNXRZK","6H4YAC2","YQPKQCM","Q5YW3G2"],"Madness Ring (Corrupted)":["8D6QTAA","8K8KWNN","G4YHDQW","FFR2BRE","52ASZMM"],"Magic Tome":["63STAXE","9E6HAZX","M43RCAT","R66ZQQ9","6K4N2HF"],"Magic Tome (Corrupted)":["W4TM3EA","A2T3TEN","M5KQQ5M","K5PZEMR","RK58PM5"],"Magus Staff":["63STAXE","M64X2YM","PCZGW6W","C94MCRY","FX2KBS4"],"Magus Staff (Corrupted)":["GNGCZBZ","RWPE2EH","532WMRK","X5AG3N3","XG2MWGE"],"Mana Potion":["9E6HAZX","YSS8WCR","6ZZ9BF6","2GSZ4AE","C2CSHPH"],"Mana Potion (Corrupted)":["B8MXWN8","WPYB9X5","2ED3QGQ","KBK58SZ","DKWZQ5P"],"Megaphone":["T66FQBM","59983BM","5QZ94XC","BZTNN6K","HXH85NK"],"Megaphone (Corrupted)":["B6E9BWD","ANH29SP","86F6Y39","N5SDBR9","BA6G454"],"Merchant Badge":["4GWTPAM","6PXR4C8","TAETY3D","2Z6W4KB","GSCAMWN"],"Merchant Badge (Corrupted)":["2TBK4T4","BCR9GFW","B8MXWN8","4GM8BSZ","D9DKGGC"],"Mind Book":["QPX9M2Q","4SATMXS","9GXEDXW","FHFX9W6","DATR6G8"],"Mind Book (Corrupted)":["PCHBWC6","YMGN26G","8R296EN","YXZ332G","KRTEWKN"],"Mixed Salad":["SMHM6ZY","W2X5EFM","MX5KKGM","ED8G8R8","EQ53ACT"],"Mixed Salad (Corrupted)":["HFF93YM","GMC9WYF","KPKX94N","FZ9XRG5","Y9NQYCG"],"Mnem Runestone":["ATB68F3","9293YTN","PHGAR9K","6BKWS22","H2HH3G3"],"Mnem Runestone (Corrupted)":["PQFDBFQ"],"Morning Star":["B58MBRA","XTHPZHK","86T2MKD","YTXD9YA","CXF5XMC"],"Morning Star (Corrupted)":["PN4MXHC","NAPPWMW","HQYQHKD","993P6HH","MPGDA54"],"Ninja Scroll":["T5SNNGG","TDR2BPN","HE3D5D2","RZ24PQW","EB8HENS"],"Ninja Scroll (Corrupted)":["SF259HW","H3KGQ62","6DT636G","FTBADYY","43DEEGF"],"Noble Shield":["M64X2YM","YRQSD8Q","D4X8YNN","WQCKTF8","9P9FXKQ"],"Noble Shield (Corrupted)":["NDPXY2M","SHHE4X3","45EEMAH","YBX44TK","MKNAQFD"],"Obsidian Dagger":["PF96M2T","RGFGQFK","X85A9B9","DSZQB3Q","FHFX9W6"],"Obsidian Dagger (Corrupted)":["X2CN8RT","BF3FNBF","DXASDPT","32DWF3T","9FYD2XS"],"Old Horseshoe":["2TBK4T4","3B2Z85N","XQW2WEY","8YGXD9B","FFCDXPA"],"Old Horseshoe (Corrupted)":["B58MBRA","W2Q4EA8","S6TW39S","YD2PDER","QA6ZP6W"],"Onyx Amulet":["TBZW5W2","M6WADEG","ZB4NCAH","X5HNECG","3B2Z85N"],"Onyx Amulet (Corrupted)":["T94FW3D","M4KDAB2","W8H3N6M","86GYCPH","EYS3TYQ"],"Opal Ring":["BYK8MXX","ZZSZ5TR","RDKPXN3","QMKHB6B","TGK6CDF"],"Opal Ring (Corrupted)":["QPX9M2Q"],"Orb of Storms":["T5W8W23","H36DK9N","KZRFAAY","RDQG9C2","YK9RBX8"],"Orb of Storms (Corrupted)":["ZY9HKBA","GK2S29H","5P45CAK","ZQRDCMQ","33R8MPG"],"Penitence Ring":["K3E48QD","FMT63K2","36RRD8W","ATHQKNY","9RPGTNG"],"Penitence Ring (Corrupted)":["QCBFG3F","G98YN86","9AFZXC3","G98YN86","9AFZXC3"],"Piggy Bank":["WH9CBZA","EZY8ZGY","P6DMHP6","AGD4YXF","WTQ4RKE"],"Pious Ring":["63STAXE","59YH2YA","HMKZCPC","XPA6X2A","Z8KTBWN"],"Pious Ring (Corrupted)":["KMA86EY","PXTCNQ2","FMQ6FWW","CACC9XY","T6KTHAF"],"Platemail":["ZPXGTWR","NFM2G45","ZYH6DY6","NKWNNNZ","G3F2C2T"],"Platemail (Corrupted)":["PWZEYAC","KA5B4RA","2TX6N8G","RFP9SAX","MQHNN59"],"Platinum Ring":["ET2BNQ3","TTWQ3XS","EGQKRDW","MFBKBKM","EGSDCQA"],"Platinum Ring (Corrupted)":["84Y4CSB","NZEZ9ND","P644YWZ","WX64SXF","FH2M9EP"],"Pointy Hat":["RGFGQFK","PA9ZREQ","MEPWRTR","36PK53K","GYR8GFA"],"Pointy Hat (Corrupted)":["FCZ3RMA","K6HTZ3M","P2XMP6N","9G33NAR","4TRNSXZ"],"Poisoned Dagger":["TE64ZG8","KB6W58Z","86T2MKD","RPMWT3D","BWF62TT"],"Poisoned Dagger (Corrupted)":["556SMZN","AG54TRS","D3S9B3G","XM8PFCC","YMQFC5B"],"Powder Cask":["WFYR5TD","8KP8SC3","8YEWT5N","2MRPPM4","WHHNRM4"],"Powder Cask (Corrupted)":["YGQQBC9","M4RBDMB","YZ5B8GN","BA25XFC","6WEMPQH"],"Quill":["WFGZHF5","F5MEHWZ","QSTS565","ABPCRS8","ZNXAKDB"],"Quill (Corrupted)":["B6SFWEF","2AY2WXT","AD4YKQN","M3T8BCH","A3356N6"],"Raven Staff":["4CS663F","T958M3P","T3YH8CA","E3KSQ34","X9WXECM"],"Raven Staff (Corrupted)":["FWPRZP9","3XSN5S9","RCEPR8H","AEDYGM5","MYGHDT3"],"Redsteel Cloak":["DDWYNF9","BCN4XGW","CKRE8FM","YC8RSR4","MDBTHR3"],"Redsteel Cloak (Corrupted)":["WYFFCA6","PCH5MHG","ZXRHYSQ","PSGDHNH","NTHH453"],"Reinforced Armor":["SRWSXBQ","TDR2BPN","8X9MPHP","SDF5DSX","CPD5YBQ"],"Reinforced Armor (Corrupted)":["MAFXBAZ","Q324GE6","F9EHPMY","GG3M4KF","2NSG3HM"],"Rejuvenation Potion":["KWXER98","KRAR3DH","ED8G8R8","2QNA8YD","HZCMADS"],"Rejuvenation Potion (Corrupted)":["5RM2XRY","HPW65A5","96B44RW","QZWPTYH","N9NPWAS"],"Ring of Hope":["BCR9GFW","BXQWP33","E8C2EBP","S3YCYSW","HCZNFPP"],"Ring of Hope (Corrupted)":["RN6X4W4","SNNNX93","98PSRR3","59QXHDG","ZCACNPH"],"Ring of Protection":["SRWSXBQ","MAFXBAZ","RZ24PQW","Q324GE6","4GWTPAM"],"Ring of Protection (Corrupted)":["3XZZ3M2","F6M63MS","MHY6Z36","DSY95NH","RMTZQQS"],"Round Shield":["TDR2BPN","MGE8EZQ","GNGCZBZ","P3PFGE9","8Z43GCZ"],"Round Shield (Corrupted)":["C9GT6DZ","R9DCZ4Y","FHE5BPR","GFS4SKD","REWHEZX"],"Royal Coin":["D4X8YNN","556SMZN","QSTS565","PAPMEG5","86T2MKD"],"Royal Coin (Corrupted)":["63KB93D","5ZFM2AW","XQDKX9Q","EWH8HYS","Y6KCSZH"],"Ruby Amulet":["63STAXE","PF96M2T","2MS5562","SRWSXBQ","XFK9XN6"],"Ruby Amulet (Corrupted)":["2HMBW9B","PCZGW6W","FX2KBS4","N2NSDMY","CM3MX63"],"Runic Dice":["KNA2Q5G","YTXD9YA","GZWFP6S","6EWR8QE","ZNMTHXK"],"Runic Dice (Corrupted)":["8TNQRQC","X3ANCWE","YDZFZB9","A2RW5T4","SZMD3SC"],"Rusty Boots":["TAYHKE6","X5HNECG","YRQSD8Q","556SMZN","KWXER98"],"Rusty Boots (Corrupted)":["9TXRGF5","YBP4Q98","EBHAF8F","Z8RBPS4","SFAKS9K"],"Sacred Tablet":["A4PWYTW","5GRZKWP","9A4E2EK","KNA2Q5G","KMEWXZA"],"Sacred Tablet (Corrupted)":["KQWFA52","YCDA5AG","5HMSDQE","285458R","9HC535N"],"Salt":["TBZW5W2","X5HNECG","W9PPD9F","P3PFGE9","MX5KKGM"],"Salt (Corrupted)":["WSBBD3Y","WHPEN9F","S64S32D","MYE6KF9","EN5NYYF"],"Samurai Armor":["TBZW5W2","X5HNECG","T5W8W23","5Y6C484","EDCWNQQ"],"Samurai Armor (Corrupted)":["B8MZWN8","GMASC45","XF3DKYM","B8MZWN8","GMASC45"],"Sapphire Ring":["9NP8ENH","ADK8WBF","8SD3WX6","6RHXCTZ","3Q3E63Z"],"Sapphire Ring (Corrupted)":["Y5CSNT2","S85YE9K","SXXYPNT","3GGNYAG","4ZZ249C"],"Savant Robe":["XTHPZHK","9P9FXKQ","QZKP6KG","Q6ZCAQR","XDG94FW"],"Savant Robe (Corrupted)":["ZHDMA88","S28CKYF","ZDQQNCY","N4EWNMT","S28CKYF"],"Scholar Robe":["5CGTQTX","XSQKR4R","NXZF665","KW2RQHP","NXZF665"],"Scholar Robe (Corrupted)":["ZHPD32F"],"Scroll of Resurrection":["XFK9XN6","W9PPD9F","ZPXGTWR","XP4TYDA","EB8HENS"],"Scroll of Resurrection (Corrupted)":["KNY6T2D","8XKQZPF","M9AWFWH","5RRTR6G","AETGSRX"],"Scryer Staff":["FDHTHTB","35PZS85","GK2H38K","2QY2MYP","W64NWXW"],"Scryer Staff (Corrupted)":["3CFMRSB","FQWAKWB","QYP32FY","FQWAKWB","QYP32FY"],"Seashell Amulet":["Z9TQAMC","M6WADEG","GG2R4YS","GQRPFSZ","ZRG3GZT"],"Seashell Amulet (Corrupted)":["B452M5Z","5M5FPZA","XR6Q9WQ","WSBN3G9","GEZTYEN"],"Seashell Ring":["9NDB5WH","KHAKWQP","TMRG546","PPQAYZG","TR6463C"],"Seashell Ring (Corrupted)":["FBSKH38","Q59F35C","99WHE98","MX3RBM5","233GWEW"],"Serenity Ring":["M3TPE82","DW5P3NQ","MCDNP2N","TFTHW8Z","BTRHWD3"],"Serenity Ring (Corrupted)":["QCGB948","PCAQ4T5","CGDYSTP","FK6HAGF","FK6HAGF"],"Shackles Of War":["SM9FYRE","42R59XE","B8CR83F","DSSFZZS","H4CCDB3"],"Shackles Of War (Corrupted)":["Q4TBK4X","W5W5YMG","9EAAHNK","2ADDB3C","3KTYQKC"],"Shadow Book":["2HMBW9B","KWXER98","T235PEN","XYWEKKE","YXXRDGY"],"Shadow Book (Corrupted)":["PCZGW6W","ZDPYKAW","TQGNZG8","ABK3PPK","F562THF"],"Shadow Cloak":["3ES4K4K","29HSMRB","N2NSDMY","8DBEADD","N9PY6YX"],"Shadow Cloak (Corrupted)":["63KB93D","3W9G2RM","A8PAYRP","GMH2DWN","S6EKMYC"],"Shadow Orb":["ZRG3GZT","PD3AFT9","D5HM66T","6GMHSHH","B5ZXK6F"],"Shadow Orb (Corrupted)":["2FCSXWS","MCDNP2N","HYDHCET","5PEA8KZ","T4AADD9"],"Short Sword":["8ASWBQZ","CF8Z353","8D2NYD9","83FGGT9","9XZR66T"],"Short Sword (Corrupted)":["PCRMRWY","QY3AMB5","PCRMRWY","QY3AMB5","PCRMRWY"],"Shoulder Plate":["GQRPFSZ","3B2Z85N","FTZXBWQ","P3PFGE9","GZWFP6S"],"Shoulder Plate (Corrupted)":["Y6Q9SSB","PFP23DM","ZGFQQZH","DSX48ZM","G4P6FZF"],"Sidearm":["WFGZHF5","9P9FXKQ","CXF5XMC","TM5QA3C","A829C4X"],"Sidearm (Corrupted)":["CGNBDYM","ZZKQBEQ","EPBD3K2","EKFN534","E86RCMB"],"Silver Chalice":["9QGA9NE","FT6N8PA","TY5Q3C6","DTHMC82","PHK98EQ"],"Silver Chalice (Corrupted)":["E2NW9ED"],"Silver Ring":["SXBDRZ3","FAZTTYY","KR626C8","8BKECCD","KR626C8"],"Simple Hat":["QZDWYGS","428YWN5","KPE4DFH","428YWN5","KPE4DFH"],"Singing Sword":["8YGXD9B","2Z6W4KB","23FAAET","3NW6CA6","SMM6XDT"],"Singing Sword (Corrupted)":["EQ53ACT","QTPD45T","TNC4845","8CRFMHN","HT46CHY"],"Slingshot":["HSH6NWY","C9KDQ8H","8T5AHDH","HHN8DEH","ZTN696M"],"Slippers":["EEFQ9SM","PHPY5HF","F4YPWXM","X59FSG3","4645KQW"],"Small Chest":["YGKDCBN","TMNPQ44","6G4GYFZ","8GCZPFH","N2DW2CE"],"Small Chest (Corrupted)":["ZQ88YNN","ZCSN884","5YPWM56","Q6TYAG8","5W6QMGC"],"Small Pouch":["SMHM6ZY","WFGZHF5","RZ24PQW","TKQTTED","T235PEN"],"Small Pouch (Corrupted)":["E5ATXWE","4T3GRYQ","H49K4Z9","DK8QNHB","2YXQPMR"],"Soap":["BZ8ECCQ","B3PK5WR","TKZWHHD","RQSZH39","C6PMBSC"],"Spiked Bracers":["PF96M2T","MGE8EZQ","WRTXBNX","TAETY3D","6SMQNKN"],"Spiked Bracers (Corrupted)":["F5MEHWZ","AQYPF5T","ZG82B53","ZS2N56S","H4XHCDD"],"Spiked Shoulderpads":["E3BTQQG","Z498DZ4","PY6N23A","SQ3R2BT","99CHDNP"],"Spiked Shoulderpads (Corrupted)":["3CYN9XB","3MN8AKD","DBZ6ACG","36FZANQ","GM8ZBAM"],"Spyglass":["YGAQSCX","NA9SXYG","QWRSMZF","B5XNXP9","EGDH4BB"],"Spyglass (Corrupted)":["PASNXGC","PASNXGC"],"Stainless Cuirass":["QQYMSCA","RC6TT94","6MBQ8YH","DTY6Q4C","8H8RAWS"],"Stainless Cuirass (Corrupted)":["YCGG8CR","5C4RP59","KTYTQNQ","6E9KYT5","BPM8PTH"],"Steadfast Boots":["3WT8WW3","ECPSN9Y","8FRNAMR","958R2S9","MWMSDBT"],"Steadfast Boots (Corrupted)":["NZ3EBDN","2KARXEZ","QE444ST","2PKR5E9"],"Steadfast Shield":["K3E48QD","MGE8EZQ","G2FK4ZG","8Z43GCZ","YTXD9YA"],"Steadfast Shield (Corrupted)":["A5XWSAW","EKFAYCB","35PZS85","9FTHMHN","8CFMA43"],"Steel Rod":["4R99DRS","8Y8X9WQ","QZA3SA2","FT39A8T","P3ZH3ZQ"],"Steel Rod (Corrupted)":["GTPWD5R","3G9QPFP","KRAT8D2","5E5Q8QK","DYSWSZX"],"Stimulant Pills":["ENT2ACC","Q2QY6HM","8P5EGBN","AH26HQH","M8K39G4"],"Stimulant Pills (Corrupted)":["BS6YY63","3HXFRQG","F8N6TMF","BS6YY63","3HXFRQG"],"Stone Amulet":["2ZB28T5","NNX9Z4P","WFGZHF5","DYPG443","RGFGQFK"],"Stone Amulet (Corrupted)":["8FGPKWN","BP66CMG","XGQGPKK","C6HTRGT","ZMZDRRS"],"Surprise Box":["KK2DTWP","6DS48P2","9Q3BNFS","9Q3BNFS","9Q3BNFS"],"Surprise Gift Box":["TE64ZG8","M64X2YM","5FCR9EC","RPMWT3D","CM3MX63"],"Surprise Gift Box (Corrupted)":["8WNP46W","R6E8BY2","X4GSDA8","W33ETS6","XMMY94F"],"Terror Ring":["TKQTTED","6K4N2HF","B452M5Z","GPCYF2C","ECPSN9Y"],"Terror Ring (Corrupted)":["R4KG9BP","MDS88AM","BPM5C4S","EZ5WW2N","W2363RP"],"Tesseract":["WQCKTF8","RSHKWQ2","XQW2WEY","9MD56MW","9NDB5WH"],"Tesseract (Corrupted)":["2FFETF2","EBMHW2P","HNGKWE6","SQBE4KT","ZCGG3TE"],"The Porcupine":["5EF95B6","Y58P9FD","HQAMZGX","6HS5DD6","WQKCMMH"],"The Porcupine (Corrupted)":["GKH6NFC","XSF4TY9","4AXTWGH","T6NRT2K","BCXGKQZ"],"The Proficient":["FMT63K2","ME4CBB4","35H9A46","2G3REAW","KXKSSGC"],"The Proficient (Corrupted)":["XMPARQC","EE4ND6N","9N6RZAA","F5DQ3C4","RR88R56"],"Thermal Amulet":["56QTQPN","MAC64TX","5GB55BF","BX8Z5DA","B52HCKD"],"Thermal Amulet (Corrupted)":["HXNZSTC","ESDNMNC","FK8B6M6","H6FZ392","H85GNAC"],"Thermal Ring":["B58MBRA","TDR2BPN","HE3D5D2","8Y8X9WQ","TKQTTED"],"Thermal Ring (Corrupted)":["35H9A46","6AS9RPB","DNX5ZY6","YWWGA5N","FZ2T84K"],"Thorny Ring":["63STAXE","8253EXW","T5SNNGG","RZPF9FX","FMT63K2"],"Thorny Ring (Corrupted)":["C2CSHPH","ZECTASR","BDSMD24","QRS23HW","EGHQAYH"],"Torch":["3B2Z85N","262PRNK","DYPG443","NNGD36T","AGXQHPF"],"Torch (Corrupted)":["4QTEWAY","35H5Q9Q","H85H5ME","BG98KKZ","K6EW534"],"Tourist Map":["TBZW5W2","63STAXE","TE64ZG8","PF96M2T","SRWSXBQ"],"Tourist Map (Corrupted)":["2MS5562","FTZXBWQ","DYPG443","WSBBD3Y","RGFGQFK"],"Turbo Boots":["WWRK3NB","86GYCPH","BN8XPCQ","8RCX8XT","X2NMDXZ"],"Turbo Boots (Corrupted)":["5B936TM","9S6GZR8","9S6GZR8"],"Twin Blades":["X93HC2R","DFHZSGR","BGYY6G6","CH4BX2M","CXF5XMC"],"Twin Blades (Corrupted)":["DK6KXGR","82QCNK5","66ERFQP","AHK2R8F","35WD89F"],"Venom Amulet":["TBZW5W2","4R99DRS","RZPF9FX","XTHPZHK","G2FK4ZG"],"Venom Amulet (Corrupted)":["6SMQNKN","E4AAHPA","MP26X38","32FKE3A","W8283DS"],"Veteran Armor":["ZPXGTWR","9A4E2EK","BRCDMXR","8MD9N8E","AKKCFGQ"],"Veteran Armor (Corrupted)":["5EF95B6","Z5YP2YN","BNKKWQT","WX96KDE","Z9GBBZ5"],"Vile Ring":["4QTEWAY","PN4MXHC","DB3Q99A","DSY95NH","6MRMNAB"],"Vile Ring (Corrupted)":["K8KR4W8","RPNWDBG","SGBT4HR","SEZC2TM","GRP3YP9"],"Viper Ring":["KB6W58Z","AF4QMHW","NXAHQP5","C9KTGM5","BXQWP33"],"Viper Ring (Corrupted)":["FK895F4","EXCDHY4","3QG5BXX","QDRASSD","9QT2AMQ"],"Virulent Ring":["WKH5DQX","BFCA6EM","8FGPKWN","SY2BB86","BCN4XGW"],"Virulent Ring (Corrupted)":["KEBAA44","N4K3MGF","TH9ZSK8","N4K3MGF","TH9ZSK8"],"Vision Ring":["XFK9XN6","NNX9Z4P","HE3D5D2","T5W8W23","FTZXBWQ"],"Vision Ring (Corrupted)":["G2FK4ZG","AFCENRE","WQCKTF8","KWXER98","DYGY93G"],"Voodoo Doll":["TAYHKE6","MX4TXZ4","8YEWT5N","T9SCD9N","G29269K"],"Voodoo Doll (Corrupted)":["AQEFDGN","9K93CTA","PBNFZG3","C53D59R","YM549R5"],"War Banner":["B58MBRA","6KQSWKH","D5HM66T","4SATMXS","CPD5YBQ"],"War Banner (Corrupted)":["K5ZGGCH","5K3YK23","R96NTWH","4XFKAS2","8BCZKSQ"],"War Drum":["8253EXW","T5SNNGG","5FCR9EC","8MD9N8E","RBKPDW2"],"War Drum (Corrupted)":["RSQ42CX","QDWM9NM","MAQ8FQT","RKW8E3N","MRQS24Q"],"War Hammer":["2ZB28T5","3B2Z85N","W2X5EFM","CM3MX63","SDF5DSX"],"War Hammer (Corrupted)":["YAKZWN2","MCXYWM4","6T4GTR6","4PDM4TE","6YEQRZS"],"Warrior Code":["FT39A8T","SXY5M3D","9TXRGF5","WMYDNQS","DDS6WAQ"],"Warrior Code (Corrupted)":["RZS4CN6","6Q9GXYQ","DB846WZ","XCBW8G5","P8G2X8W"],"Water Vase":["PF96M2T","6KQSWKH","ZRG3GZT","NNGD36T","8Z43GCZ"],"Water Vase (Corrupted)":["44RW3PD","9Q4A26R","H93C3WT","SZYE4HG","M62989Q"],"Weapon Pouch":["XTHPZHK","NNGD36T","SBS438A","8YGXD9B","FZE8MZW"],"Weapon Pouch (Corrupted)":["SZ54PSA","5MF9ZGK","324E449","9PPF3F8","8MPS3AZ"],"Winged Wand":["6GMHSHH","E3MDTBP","E5ATXWE","PCK9ERY","3FZ2ZGF"],"Winged Wand (Corrupted)":["6YAABS6","K4D2D92","NSCMB34","4PT2G24","CWXHGPY"],"Woolly Hat":["FMT63K2","WFYR5TD","N94RHZG","GSCAMWN","CZZY6A3"],"Woolly Hat (Corrupted)":["59N9M5B","BEXQ3QN","GFF4G5Q","N8BBNTR","9AX3AMX"],"Xul Runestone":["WPN2P2S","THPN3K8","WZANS8T","NNXPPMC","QYSNNWF"],"Xul Runestone (Corrupted)":["K69TN2Y"],"Yin Yang Badge":["3NC94ZE","X85A9B9","QT2KZXE","4T3GRYQ","TMB92FG"],"Yin Yang Badge (Corrupted)":["8SR3NPD","6C4D83E","MM88C8E","AGE5S26","6SB2FC5"]}

    # print(a["Advanced Handbook"])
    shopDict = {}

    guaranteedDict = {}

    mythicDict = {}

    dict_sheet_pairs = [
        (caravanDict, 'Caravan Items'),
        # (shopDict, 'Shop Items'),
        # (guaranteedDict, 'Boss Drops'),
        # (mythicDict, 'Mythics')
    ]
    
    

    dicts_to_excel(dict_sheet_pairs, 'SeedList.xlsx')