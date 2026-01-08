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
using TMPro;

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
        [HarmonyPatch(typeof(HeroSelectionManager), "Start")]
        public static void HeroSelectionManagerStartPrefix(ref HeroSelectionManager __instance, TMP_Text ___gameSeedTxt)
        {
            // LogInfo("BeginAdventurePrefix - Start");
            if (SaveSeedToGame.Value)
            {
                AtOManager.Instance?.SetGameId(GetSavedSeed());
                ___gameSeedTxt.text = GetSavedSeed();
            }
            // LogInfo($"BeginAdventurePrefix - GameID - {__state}");
        }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(AtOManager), nameof(AtOManager.BeginAdventure))]
        public static void BeginAdventurePrefix(ref AtOManager __instance)
        {
            // LogInfo("BeginAdventurePostfix - Start");
            if (SaveSeedToGame.Value || BypassMadnessRandomization.Value)
            {
                SavedSeed = __instance.GetGameId();
            }
            // LogInfo($"BeginAdventurePostfix - GameID - {__instance.GetGameId()}");
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(AtOManager), nameof(AtOManager.BeginAdventure))]
        public static void BeginAdventurePostfix(ref AtOManager __instance)
        {
            // LogInfo("BeginAdventurePostfix - Start");
            if (SaveSeedToGame.Value || BypassMadnessRandomization.Value)
            {
                LogDebug($"BeginAdventurePostfix - Setting GameID to {GetSavedSeed()}");
                __instance.SetGameId(GetSavedSeed());
            }
            // LogInfo($"BeginAdventurePostfix - GameID - {__instance.GetGameId()}");
        }


        [HarmonyPostfix]
        [HarmonyPatch(typeof(Globals), nameof(Globals.CreateGameContent))]
        public static void CreateGameContentPostfix(ref Globals __instance)
        {
            // Needs to be called here since the game content needs to exist to properly search through it.
            LogInfo("CreateGameContentPostfix - Start");
            // string seed2 = "539ZX6M";
            // string shop = "caravanshop";//caravanshop
            // string node = "sen_44";
            // LogSingleShop(shop, seed2, node);
            // LogAllItems();
            // FindSeedWithItems();
            // CheckSingleSeed("QB2WCZW");


            // LogDebug(SearchCaravansForEpicPairs.Value.ToString());

            // WriteItemsToText();


            if (SearchForItemsOnStartup.Value)
            {
                ExecuteSearch();
            }



            bool f = false;
            if (f)
            {
                List<(string, string, string)> thingsToSearch =
            [
                ("heartofthornsrare","caravanshop","sen_44"),
                // ("bloodblobpetrare","blobsphys","voidlow_28"),
            ];
                // LogSeedsNodeSpecified(thingsToSearch, nSeeds: 5_000);

                List<(string, string)> eventsToFind =
                [
                    ("sen_29", "e_sen29_a"),
                // ("bloodblobpetrare","blobbleed","sen_29"),
                // ("bloodblobpetrare","blobbleed","faen_41"),
                // ("bloodblobpetrare","blobsphys","voidlow_28"),
            ];

            }


        }


    }
}