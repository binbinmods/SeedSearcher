using BepInEx;
using BepInEx.Logging;
using BepInEx.Configuration;
using HarmonyLib;
// using static Obeliskial_Essentials.Essentials;
using System;
// using static SeedSearcher.CustomFunctions;
using static SeedSearcher.Plugin;
using UnityEngine.Windows.Speech;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Analytics;
using System.Text;
using static SeedSearcher.SeedSearcherFunctions;

// Make sure your namespace is the same everywhere
namespace SeedSearcher
{

    [HarmonyPatch] //DO NOT REMOVE/CHANGE

    public class SeedSearcherPatches
    {
        // To create a patch, you need to declare either a prefix or a postfix. 
        // Prefixes are executed before the original code, postfixes are executed after
        // Then you need to tell Harmony which method to patch.

        // public static 

        // #pragma warning disable Harmony003 // Harmony non-ref patch parameters modified

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
            // string seed2 = "3ASMHBK";
            // string shop = "rubychest";
            // string node = "aqua_20";
            // ListInfoFromSeed(seed2,shop,node);
            // LogAllItems();
            // FindSeedWithItems();
            // CheckSingleSeed("QB2WCZW");
                        
            
            // LogDebug(SearchCaravansForEpicPairs.Value.ToString());
            // if(SearchCaravansForEpicPairs.Value)
            bool f = false;

            // if (f)
            // {
            //     List<(string, string)> l = [
            //                             ("holyhammerrare","justicarring"),
            //                             ];
            //     // int nSeeds = NumberOfSeeds.Value;
            //     int nSeeds = 2_000_000;
            //     string seed = DoubleCaravanEpics(l, nSeeds);
            //     LogDebug($"Seed meeting conditions: {seed}");
            // }
            if (!f)
            {
                Dictionary<string, string> itemsMappedToShop = new() {
                    {"piggybank","chappel"},
                    {"piggybank2","towntier0_b"},                    
                    // {"smallchest2","voidtwins"},
                    // {"smallchest3","voidtsnemo"},

                };
                LogDebug("dict init");

                int nSeeds = 100_000; 
                List<string> seedInfo = CheckSeeds(itemsMappedToShop, nSeeds, madness: 1, corruptorCount: 0);
                LogDebug($"List of Seeds with good things: \n {string.Join(", ", seedInfo)}");
            }
            
            List<(string,string,string)> thingsToSearch =
            [                
                ("bloodblobpetrare","blobbleed","sen_29"),
                ("bloodblobpetrare","blobbleed","faen_41"),
                ("bloodblobpetrare","blobsphys","voidlow_28"),
            ];
            // LogSeedsNodeSpecified(thingsToSearch, nSeeds: 1_000_000);

            List<(string,string)> eventsToFind =
            [
                ("sen_29", "e_sen29_a"),
                // ("bloodblobpetrare","blobbleed","sen_29"),
                // ("bloodblobpetrare","blobbleed","faen_41"),
                // ("bloodblobpetrare","blobsphys","voidlow_28"),
            ];

            
            
        }



    }
}