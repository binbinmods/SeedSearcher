using BepInEx;
using BepInEx.Logging;
using BepInEx.Configuration;
using HarmonyLib;
using static Obeliskial_Essentials.Essentials;
using System;
using static SeedSearcher.CustomFunctions;
using static SeedSearcher.Plugin;
using UnityEngine.Windows.Speech;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Analytics;

// Make sure your namespace is the same everywhere
namespace SeedSearcher
{

    [HarmonyPatch] //DO NOT REMOVE/CHANGE

    public class SeedSearcher
    {
        // To create a patch, you need to declare either a prefix or a postfix. 
        // Prefixes are executed before the original code, postfixes are executed after
        // Then you need to tell Harmony which method to patch.

        #pragma warning disable Harmony003 // Harmony non-ref patch parameters modified
        
        [HarmonyPrefix]
        [HarmonyPatch(typeof(AtOManager), nameof(AtOManager.BeginAdventure))]
        public static void BeginAdventurePrefix(ref AtOManager __instance, out string __state)
        {
            LogInfo("BeginAdventurePrefix - Start");
            __state = __instance.GetGameId();
            LogInfo($"BeginAdventurePrefix - GameID - {__state}");
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(AtOManager), nameof(AtOManager.BeginAdventure))]
        public static void BeginAdventurePostfix(ref AtOManager __instance, string __state)
        {
            LogInfo("BeginAdventurePostfix - Start");
            __instance.SetGameId(__state);
            LogInfo($"BeginAdventurePostfix - GameID - {__instance.GetGameId()}");
        }


        // [HarmonyPrefix]
        // [HarmonyPatch(typeof(AtOManager), nameof(AtOManager.SetGameId))]
        // public static bool SetGameIdPrefix(ref AtOManager __instance, string _gameId = "")
        // {
        //     LogInfo("SetGameIdPrefix - Start");
        //     string currId = __instance.GetGameId();
        //     LogInfo($"SetGameIdPrefix - CurrentGameID = {currId}");

        //     if (_gameId=="")
        //     {
        //         return false;
        //     }
        //     LogInfo("SetGameIdPrefix - End");

        //     return true;
        //     }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(Globals), nameof(Globals.CreateGameContent))]
        public static void CreateGameContentPostfix(ref Globals __instance)
        {
            // Needs to be called here since the game content needs to exist to properly search through it.
            LogInfo("CreateGameContentPostfix - Start");
            LogAllItems();
            LogInfo($"CreateGameContentPostfix - END ");
        }

        public static void LogAllItems()
        {  
            LogInfo("LogAllItems - Start");
            LogCaravanItems();
            // LogGuaranteedDropItems();
            // LogBossDropItems();
            // LogShopItems();
            // LogMythicItems();
            
        }
        internal static void LogPetItems()
        {
            Dictionary<string,string> dropNodeMap = new()
            {
                {"Jelly", "aquar_41"},
                {"betty", "sen_39"},
                {"blobbleed", "sen_29"},
                {"blobcold", "sewers_13"},
                {"blobdire", "velka_37"},
                {"blobholy", "pyr_12"},
                {"bloblightning", "sahti_30"},
                {"blobmetal", "velka_38"},
                {"blobmind", "dread_7"},
                {"blobpoison", "aquar_44"},
                {"blobselem", "voidlow_28"},
                {"blobshadow", "ulmin_59"},
                {"blobsmyst", "voidlow_28"},
                {"blobsphys", "voidlow_28"},
                {"blobwater", "aquar_45"},
                {"cuby", "pyr_9"},
                {"cubyd", "pyr_9"},
                {"daley", "faen_7"},
                {"fenny", "ulmin_6"},
                {"fishlava", "forge_8"},
                {"inky", "aquar_41"},
                {"liante", "lair_5"},
                {"matey", "sahti_20"},
                {"mimy", "dread_10"},
                {"oculy", "aquar_41"},
                {"sharpy", "aquar_18"},
                {"slimy", "lair_7"},
                {"stormy", "aquar_24"},
                {"wolfy", "sen_46"},

            };
            int nSeeds = 300;
            HandleDropItems(dropNodeMap,nSeeds);
        }


        internal static void LogBossDropItems()
        {
            Dictionary<string,string> dropNodeMap = new()
            {
                {"Basthet", "pyr_7"},
                {"Dryad_a", "sen_31"},
                {"Dryad_b", "sen_32"},
                {"Faeborg", "faen_38"},
                {"Hydra", "aquar_35"},
                {"Ignidoh", "velka_32"},
                {"Mansionright", "faen_35"},
                {"Mortis", "ulmin_56"},
                {"Tulah", "lair_8"},
                {"Ylmer", "sen_33"},
                {"belphyor", "secta_5"},
                {"belphyorquest", "velka_8"},
                {"burninghand", "velka_25"},
                {"dreadhalfman", "dread_11"},
                {"elvenarmory", "faen_29"},
                {"elvenarmoryplus", "faen_29"},
                {"goblintown", "velka_6"},
                {"harpychest", "velka_27"},
                {"harpyfight", "velka_27"},
                {"khazakdhum", "velka_29"},
                {"kingrat", "sewers_8"},
                {"minotaurcave", "velka_9"},
                {"sahtikraken", "sahti_65"},
                {"sahtikrakenmjolmir", "sahti_65"},
                {"sahtirustkingtreasure", "sahti_62"},
                {"spiderqueen", "sen_1"},
                {"tyrant", "faen_25"},
                {"tyrantbeavers", "faen_25"},
                {"tyrantchampy", "faen_25"},
                {"tyrantchompy", "faen_25"},
                {"tyrantchumpy", "faen_25"},
                {"upripreboss", "uprising_13"},
                {"yogger", "sen_27"},
            };
            int nSeeds = 300;
            HandleDropItems(dropNodeMap,nSeeds);
        }

        internal static void LogGuaranteedDropItems()
        {
            Dictionary<string,string> dropNodeMap = new()
            {
                {"FrozenSewersElves", "sewers_11"},
                {"FrozenSewersMix", "sewers_11"},
                {"FrozenSewersRatmen", "sewers_11"},
                {"Jewelerrings", "sen_35"},
                {"Mansionleft", "faen_35"},
                {"Mansionleftplus", "faen_35"},
                {"Sailor", "faen_4"},
                // {"Shady", "sen_1"},
                {"Stolenitems", "faen_10"},
                {"apprentince", "sen_24"},
                {"balanceblack", "ulmin_52"},
                {"balanceboth", "ulmin_52"},
                {"balancewhite", "ulmin_52"},
                {"battlefield", "aquar_6"},
                {"bridge", "sen_17"},
                {"chappel", "sen_21"},
                {"crane", "velka_21"},
                {"crocoloot", "aquar_7"},
                {"crocosmugglers", "aquar_48"},
                {"desertreliquary", "ulmin_58"},
                {"dreadcosme", "dread_2"},
                {"dreadcuthbert", "dread_2"},
                {"dreadfrancis", "dread_2"},
                {"dreadhoratio", "dread_2"},
                {"dreadjack", "dread_2"},
                {"dreadmimic", "dread_10"},
                // {"dreadpurser", "sen_1"},
                // {"dreadpurserstash", "sen_1"},
                {"dreadrhodogor", "dread_2"},
                {"eeriechest_a", "sen_6"},
                {"eeriechest_b", "sen_6"},
                {"lavacascade", "velka_22"},
                {"lootedarmory", "pyr_10"},
                {"lootsepulchralrare", "voidlow_18"},
                {"obsidianall", "forge_3"},
                {"obsidiananvil", "forge_3"},
                {"obsidianboots", "forge_3"},
                {"obsidianrings", "forge_3"},
                {"obsidianrods", "forge_3"},
                {"rift", "velka_40"},
                {"riftsen", "sen_48"},
                {"sahtibernardstash", "sahti_52"},
                {"sahtidomedesert", "sahti_49"},
                {"sahtidomeice", "sahti_49"},
                {"sahtidomemain", "sahti_49"},
                {"sahtidomemountain", "sahti_49"},
                {"sahtidomeswamp", "sahti_49"},
                {"sahtipiratearsenal", "sahti_25"},
                {"sahtipiratewarehouse", "sahti_25"},
                {"sahtiplaguecot", "sahti_11"},
                {"sahtisurgeonarsenal", "sahti_13"},
                {"sahtisurgeonstash", "sahti_13"},
                {"sahtitreasurechamber", "sahti_25"},
                {"sahtivalkyriestash", "sahti_19"},
                {"thorimsrod", "forge_8"},
                {"treasureaquarfall", "aquar_28"},
                {"uprienergy", "uprising_5"},
                {"uprimagma", "uprising_4"},
                {"voidcraftemerald", "voidlow_14"},
                {"voidcraftgolden", "voidlow_14"},
                {"voidcraftobsidian", "voidlow_14"},
                {"voidcraftpearl", "voidlow_14"},
                {"voidcraftring", "voidlow_14"},
                // {"voidcraftrodsofblasting", "sen_1"},
                {"voidcraftruby", "voidlow_14"},
                {"voidcraftsapphire", "voidlow_14"},
                {"voidcrafttopaz", "voidlow_14"},
                {"voidtreasurejade", "voidlow_16"},
                {"watermill", "sen_15"},
            };
            int nSeeds = 300;
            HandleDropItems(dropNodeMap,nSeeds);

        }

        internal static void LogShopItems()
        {
            Dictionary<string,string> shopNodeMap = new()
            {
                {"aquarvendor","aquar_26"},
                {"elvenemporium","faen_23"},
                {"felineshop","ulmin_29"},
                {"firebazaar","velka_20"},
                // {"heronshop","ulmin_27"},
                // {"Merchantwares","velka_7"},
                // {"voidshop","voidlow_8"},
                // {"voidtsnemo","voidlow_24"},
                // {"voodooshop", "aquar_23"},
                // {"Jeweler","sen_35"},
                // {"gobletsmerchant","sewers_4"},
                // {"werewolfstall_a","sen_30"},
                // {"werewolfstall_b","sen_30"}
            };

            int nSeeds = 300;
            // LootItem item = lootData.Loot    ItemTable[0];
            HandleDropItems(shopNodeMap,nSeeds);
            

        }

        internal static void HandleDropItems(Dictionary<string,string> lootNodeMap, int nSeeds = 300)
        {
            Dictionary<string,List<string>> outputItemMap = [];

            foreach (string shop in lootNodeMap.Keys)
            {
                LootData lootData = Globals.Instance.GetLootData(shop);
                List<string> validItems = [];
                foreach (LootItem item in lootData.LootItemTable)
                {                
                    if (item.LootCard == null)
                    {
                        continue;
                    }
                    if (item.LootCard.CardName != "")
                    {
                        validItems.Add(item.LootCard.Id);
                    }
                }
                LogDebug($"Shop - {shop} Valid Items - {string.Join(", ",validItems)}");

                for (int i = 0; i < nSeeds; i++)
                {
                string randomSeed = Functions.RandomStringSafe(7f).ToUpper();
                string node = lootNodeMap[shop];
                List<string> itemList = GetItemsFromSeed(_seed:randomSeed,_shop:shop,_node:node, _madness:8,_corruptorCount:8);
                // LogDebug($"Shop - {shop} itemList Items - {string.Join(", ",itemList)}");
                UpdateItemDictForShops(ref outputItemMap,itemList,validItems,randomSeed,shop);
                }
            }
            
            LogDebug($"Shop Items - {SerializeDictionary(outputItemMap)}");
        }

        internal static void LogCaravanItems()
        {
            Dictionary<string,List<string>> itemDict = [];
            // Dictionary<string,string> itemDict = [];
            // LogCaravanItems()
            int nSeeds = 100000;
            for(int i = 0; i<nSeeds; i++)
            {
                // string testSeed = testSeeds[i];
                string randomSeed = Functions.RandomStringSafe(7f).ToUpper();
                
                string shop = "caravanshop";
                string node = "sen_44";
                List<string> itemList = GetItemsFromSeed(_seed:randomSeed,_shop:shop,_node:node, _madness:1);            
                UpdateItemDict(ref itemDict,itemList,randomSeed);
                        
            }
            LogDebug($"Dictionary - {SerializeDictionary(itemDict)}");
        }


        internal static void UpdateItemDictForShops(ref Dictionary<string,List<string>> itemDict, List<string> itemList, List<string> validItems, string seed, string shopName, int count = 5)
        {
            foreach(string item in itemList)
                {
                    if(!validItems.Contains(item))
                    {
                        continue;
                    }

                    CardData cardData = Globals.Instance.GetCardData(item, false);    
                    // if(cardData==null){continue;}
                    if(cardData==null || cardData.CardUpgraded!=Enums.CardUpgraded.Rare){continue;}
                    string key = $"{shopName} - {cardData.CardName}";
                    if(!itemDict.ContainsKey(key))
                    {
                        itemDict.Add(key, []);
                    }
                    if(itemDict[key].Count()<count)
                    {
                        itemDict[key].Add(seed);
                    }                    
                }          
        }

        internal static void UpdateItemDict(ref Dictionary<string,List<string>> itemDict, List<string> itemList, string seed, int count = 5)
        {
            foreach(string item in itemList)
                {
                    CardData cardData = Globals.Instance.GetCardData(item, false);                    
                    string key = cardData.CardUpgraded == Enums.CardUpgraded.Rare ? $"{cardData.CardName} (Corrupted)" : cardData.CardName;
                    if(!itemDict.ContainsKey(key))
                    {
                        itemDict.Add(key, []);
                    }
                    if(itemDict[key].Count()<count)
                    {
                        itemDict[key].Add(seed);
                    }                    
                }          
        }
        internal static List<string> GetItemsFromSeed(string _seed = "", string _shop = "caravanshop", string _node = "", int _townReroll = 0, bool _obeliskChallenge = false, int _madness = 0, int _corruptorCount = 0, bool _poverty = false)
        {
            // LogInfo("GetItemsFromSeed - Start");

            string reroll = "";
            string node = _node; // have to do this because can't use ref keyword w/ default values
            if (_shop == "caravanshop" && node == "")
                node = "sen_44";
            // #TODO: other shops/nodes
            if (_townReroll > 0)
            {
                // #TODO: I have not looked into how the reroll string is generated
                // reroll = ??
            }   

            // AtOManager.Instance.Gettown
            // LogInfo("GetItemsFromSeed - Start 1");

            // if (AtOManager.Instance != null) // a game is in progress
            // {
            //     // replace with current game values if defaults are used
            //     if (_seed == "")
            //     {
            //         string s = AtOManager.Instance.GetGameId();
            //         _seed = s;
            //     }
            //     LogInfo("GetItemsFromSeed - Start 2");
                    
            //     if (node == "")
            //         node = AtOManager.Instance.currentMapNode;
            //     if (_townReroll == 0)
            //         reroll = AtOManager.Instance.shopItemReroll;
            //     if (_obeliskChallenge == false && GameManager.Instance != null && GameManager.Instance.IsObeliskChallenge())
            //         _obeliskChallenge = true;
            //     _madness = _obeliskChallenge ? AtOManager.Instance.GetObeliskMadness() : AtOManager.Instance.GetNgPlus();
            //     _corruptorCount = AtOManager.Instance.GetMadnessDifficulty() - _madness;
            //     _poverty = AtOManager.Instance.IsChallengeTraitActive("poverty") || MadnessManager.Instance != null && MadnessManager.Instance.IsMadnessTraitActive("poverty");
            // }
            #pragma warning restore Harmony003 // Harmony non-ref patch parameters modified

            LootData lootData = Globals.Instance.GetLootData(_shop);
            if (lootData == null)
            {
                LogError("Unable to get shop items for " + _shop + " (shop does not exist!)");
                return null;
            }

            // LogInfo("GetItemsFromSeed - Mid 1");
            
            List<string> ts1 = new List<string>();
            List<string> ts2 = new List<string>();
            for (int index = 0; index < Globals.Instance.CardListByClass[Enums.CardClass.Item].Count; ++index)
                ts2.Add(Globals.Instance.CardListByClass[Enums.CardClass.Item][index]);
            int deterministicHashCode = (node + _seed + reroll).GetDeterministicHashCode();
            UnityEngine.Random.InitState(deterministicHashCode);
            ts2.Shuffle<string>(deterministicHashCode);
            int index1 = 0;
            int num1 = !_obeliskChallenge ? lootData.NumItems : lootData.LootItemTable.Length;
            for (int index2 = 0; index2 < num1 && ts1.Count < lootData.NumItems; ++index2)
            {
                if (index2 < lootData.LootItemTable.Length)
                {
                    LootItem lootItem = lootData.LootItemTable[index2];
                    if ((double)UnityEngine.Random.Range(0, 100) < (double)lootItem.LootPercent)
                    {
                        if (lootItem.LootCard != null)
                        {
                            ts1.Add(lootItem.LootCard.Id);
                        }
                        else
                        {
                            bool flag = false;
                            int num2 = 0;
                            CardData cardData = (CardData)null;
                            for (; !flag && num2 < 10000; ++num2)
                            {
                                if (index1 >= ts2.Count)
                                    index1 = 0;
                                string str = ts2[index1];
                                // if (!ts1.Contains(str) && (!AtOManager.Instance.ItemBoughtOnThisShop(_itemListId, str) && AtOManager.Instance.HowManyTownRerolls() > 0 || AtOManager.Instance.HowManyTownRerolls() == 0))
                                // replaced with a line that DOESN'T check if item has already been bought
                                // usually, if an item has been bought it will not show up in town again
                                if (!ts1.Contains(str))
                                {
                                    cardData = Globals.Instance.GetCardData(str, false);
                                    if (cardData.Item != null && !cardData.Item.DropOnly)
                                    {
                                        if (cardData.CardUpgraded == Enums.CardUpgraded.Rare)
                                            flag = false;
                                        else if (cardData.Item.PercentRetentionEndGame > 0 && (_madness > 2 || _obeliskChallenge))
                                            flag = false;
                                        else if (cardData.Item.PercentDiscountShop > 0 && _poverty)
                                            flag = false;
                                        else if (lootItem.LootType == Enums.CardType.None && cardData.CardRarity == lootItem.LootRarity)
                                            flag = true;
                                        else if (cardData.CardType == lootItem.LootType && cardData.CardRarity == lootItem.LootRarity)
                                            flag = true;
                                    }
                                }
                                ++index1;
                            }
                            if (flag && cardData != null)
                                ts1.Add(cardData.Id);
                        }
                    }
                }
            }

            // LogInfo("GetItemsFromSeed - Mid 2");
            for (int count = ts1.Count; count < lootData.NumItems; ++count)
            {
                bool flag = false;
                int num3 = 0;
                CardData cardData = (CardData)null;
                int num4 = UnityEngine.Random.Range(0, 100);
                while (!flag && num3 < 10000)
                {
                    if (index1 >= ts2.Count)
                        index1 = 0;
                    string str = ts2[index1];
                    // if (!ts1.Contains(str) && (!AtOManager.Instance.ItemBoughtOnThisShop(_itemListId, str) && AtOManager.Instance.HowManyTownRerolls() > 0 || AtOManager.Instance.HowManyTownRerolls() == 0))
                    // replaced with a line that DOESN'T check if item has already been bought
                    // usually, if an item has been bought it will not show up in town again
                    if (!ts1.Contains(str))
                    {
                        cardData = Globals.Instance.GetCardData(str, false);
                        if (cardData.Item != null && !cardData.Item.DropOnly)
                        {
                            if (cardData.CardUpgraded == Enums.CardUpgraded.Rare)
                                flag = false;
                            else if (cardData.Item.PercentRetentionEndGame > 0 && (_madness > 2 || _obeliskChallenge))
                                flag = false;
                            else if (cardData.Item.PercentDiscountShop > 0 && _poverty)
                                flag = false;
                            else if ((double)num4 < (double)lootData.DefaultPercentMythic)
                            {
                                if (cardData.CardRarity == Enums.CardRarity.Mythic)
                                    flag = true;
                            }
                            else if ((double)num4 < (double)lootData.DefaultPercentEpic + (double)lootData.DefaultPercentMythic)
                            {
                                if (cardData.CardRarity == Enums.CardRarity.Epic)
                                    flag = true;
                            }
                            else if ((double)num4 < (double)lootData.DefaultPercentRare + (double)lootData.DefaultPercentEpic + (double)lootData.DefaultPercentMythic)
                            {
                                if (cardData.CardRarity == Enums.CardRarity.Rare)
                                    flag = true;
                            }
                            else if ((double)num4 < (double)lootData.DefaultPercentUncommon + (double)lootData.DefaultPercentRare + (double)lootData.DefaultPercentEpic + (double)lootData.DefaultPercentMythic)
                            {
                                if (cardData.CardRarity == Enums.CardRarity.Uncommon)
                                    flag = true;
                            }
                            else if (cardData.CardRarity == Enums.CardRarity.Common)
                                flag = true;
                        }
                    }
                    ++index1;
                    ++num3;
                    if (!flag && num3 % 100 == 0)
                        num4 += 10;
                }
                if (flag && cardData != null)
                    ts1.Add(cardData.Id);
                else
                    break;
            }
            // LogInfo("GetItemsFromSeed - Mid 3");
            ts1.Shuffle<string>(deterministicHashCode);
            if (!_shop.Contains("towntier") && (!_obeliskChallenge && _madness > 0 || _obeliskChallenge))
            {
                int num5 = 0;
                if (_shop.Contains("exoticshop"))
                    num5 += 8;
                else if (_shop.Contains("rareshop"))
                    num5 += 4;
                if (_obeliskChallenge)
                {
                    if (_madness > 8)
                        num5 += 4;
                    else if (_madness > 4)
                        num5 += 2;
                }
                else
                    num5 += Functions.FuncRoundToInt(0.2f * (float)(_madness + _corruptorCount));
                for (int index3 = 0; index3 < ts1.Count; ++index3)
                {
                    int num6 = UnityEngine.Random.Range(0, 100);
                    CardData cardData = Globals.Instance.GetCardData(ts1[index3], false);
                    if (!(cardData == null))
                    {
                        bool flag = false;
                        if ((cardData.CardRarity == Enums.CardRarity.Mythic || cardData.CardRarity == Enums.CardRarity.Epic) && num6 < 3 + num5)
                            flag = true;
                        else if (cardData.CardRarity == Enums.CardRarity.Rare && num6 < 5 + num5)
                            flag = true;
                        else if (cardData.CardRarity == Enums.CardRarity.Uncommon && num6 < 7 + num5)
                            flag = true;
                        else if (cardData.CardRarity == Enums.CardRarity.Common && num6 < 9 + num5)
                            flag = true;
                        if (flag && cardData.UpgradesToRare != null)
                            ts1[index3] = cardData.UpgradesToRare.Id;
                    }
                }
            }
            // LogInfo("GetItemsFromSeed - End 1");
            #pragma warning disable Harmony003 // Harmony non-ref patch parameters modified
            // LogInfo($"SHOP CONTENTS for {_shop} at node {node} in seed {_seed} (reroll: {(reroll == "" ? _townReroll.ToString() : reroll)}, {(_obeliskChallenge ? "OC " : "")}madness {_madness.ToString()}|{_corruptorCount.ToString() + (_poverty ? " with poverty" : "")})");
            
            return ts1;
            // foreach (string cardID in ts1)
            // {
            //     CardData card = Globals.Instance.GetCardData(cardID);
            //     if (card != null)
            //     {
            //         LogInfo(card.CardName + (card.CardUpgraded == Enums.CardUpgraded.Rare ? " (Corrupted)" : (card.CardUpgraded == Enums.CardUpgraded.A ? " (Blue)" : (card.CardUpgraded == Enums.CardUpgraded.B ? " (Yellow)" : ""))) + " [" + card.Id + "]");

            //     }
            // }
        }
        
    }
}