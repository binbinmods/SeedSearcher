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

        public static void LogAllItems()
        {  
            LogInfo("LogAllItems - Start");
            Dictionary<string,List<string>> itemDict = [];
            string[] testSeeds = ["test1","test2","test3"];
            foreach(string testSeed in testSeeds)
            {
                string randomSeed = Functions.RandomStringSafe(7f).ToUpper();
                // string testSeed = "test1";
                List<string> itemList = GetItemsFromSeed(_seed:testSeed,_madness:0);
                LogDebug(string.Join(", ", itemList));
                itemList = GetItemsFromSeed(_seed:testSeed,_madness:1);
                LogDebug(string.Join(", ", itemList));
                itemList = GetItemsFromSeed(_seed:testSeed,_madness:8,_corruptorCount:8,_poverty:true);
                LogDebug(string.Join(", ", itemList));

                foreach(string item in itemList)
                {
                    if(!itemDict.ContainsKey(item))
                    {
                        itemDict.Add(item, []);
                    }
                    itemDict[item].Append(testSeed);
                }                
            }
            LogDebug($"Dictionary - {CustomFunctions.ToDebugString(itemDict)}");
        }
        internal static List<string> GetItemsFromSeed(string _seed = "", string _shop = "caravanshop", string _node = "", int _townReroll = 0, bool _obeliskChallenge = false, int _madness = 0, int _corruptorCount = 0, bool _poverty = false)
        {
            LogInfo("GetItemsFromSeed - Start");

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
            LogInfo("GetItemsFromSeed - Start 1");

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

            LogInfo("GetItemsFromSeed - Mid 1");
            
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

            LogInfo("GetItemsFromSeed - Mid 2");
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
            LogInfo("GetItemsFromSeed - Mid 3");
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
            LogInfo("GetItemsFromSeed - End 1");
            #pragma warning disable Harmony003 // Harmony non-ref patch parameters modified
            LogInfo($"SHOP CONTENTS for {_shop} at node {node} in seed {_seed} (reroll: {(reroll == "" ? _townReroll.ToString() : reroll)}, {(_obeliskChallenge ? "OC " : "")}madness {_madness.ToString()}|{_corruptorCount.ToString() + (_poverty ? " with poverty" : "")})");
            
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