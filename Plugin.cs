// These are your imports, mostly you'll be needing these 5 for every plugin. Some will need more.

using BepInEx;
using BepInEx.Logging;
using BepInEx.Configuration;
using HarmonyLib;
// using static Obeliskial_Essentials.Essentials;
using System;
using System.Collections.Generic;
using System.Linq;


namespace SeedSearcher{

    // If you have other dependencies, such as obeliskial content, make sure to include them here.
    [BepInPlugin(PluginInfo.PLUGIN_GUID, PluginInfo.PLUGIN_NAME, PluginInfo.PLUGIN_VERSION)]
    // [BepInDependency("com.stiffmeds.obeliskialessentials")] // this is the name of the .dll in the !libs folder.
    [BepInProcess("AcrossTheObelisk.exe")] //Don't change this

    public class Plugin : BaseUnityPlugin
    {
        
        
        public static ConfigEntry<bool> RunSeedSearcher { get; set; }
        public static ConfigEntry<bool> SearchCaravansForEpicPairs { get; set; }
        public static ConfigEntry<int> NumberOfSeeds { get; set; }
        internal int ModDate = int.Parse(DateTime.Today.ToString("yyyyMMdd"));
        private readonly Harmony harmony = new(PluginInfo.PLUGIN_GUID);
        internal static ManualLogSource Log;

        public static string debugBase = $"{PluginInfo.PLUGIN_GUID} ";

        private void Awake()
        {

            // The Logger will allow you to print things to the LogOutput (found in the BepInEx directory)
            Log = Logger;
            Log.LogInfo($"{PluginInfo.PLUGIN_GUID} {PluginInfo.PLUGIN_VERSION} has loaded!");
            
            // Sets the title, default values, and descriptions
            RunSeedSearcher = Config.Bind(new ConfigDefinition("SeedSearcher", "RunSeedSearcher"), true, new ConfigDescription("If false, disables the mod. Restart the game upon changing this setting."));
            SearchCaravansForEpicPairs = Config.Bind(new ConfigDefinition("SeedSearcher", "SearchCaravansForEpicPairs"), false, new ConfigDescription("Has the game search through seeds on startup for a predefined list of epic pairs. Pairs are stored in the LogOutput.log file. Do not reload the game. To run this, set this value to true and then restart your game. "));
            NumberOfSeeds = Config.Bind(new ConfigDefinition("SeedSearcher", "Seeds to Search"), 2000000, new ConfigDescription("Number of seeds to search through (I believe it takes around 10 minutes to search through 1 millions seeds)"));
            
            // Register with Obeliskial Essentials, delete this if you don't need it.
            // RegisterMod(
            //     _name: PluginInfo.PLUGIN_NAME,
            //     _author: "binbin",
            //     _description: "Sample Plugin",
            //     _version: PluginInfo.PLUGIN_VERSION,
            //     _date: ModDate,
            //     _link: @"https://github.com/binbinmods/SampleCSharpWorkspace"
            // );

            LogDebug($"Pre-Log Items {RunSeedSearcher.Value}");

            // apply patches
            if(RunSeedSearcher.Value){
                LogDebug("Patching");
                harmony.PatchAll();
                // SeedSearcher.LogAllItems();
                
            }
            LogDebug($"Post-Log Items {RunSeedSearcher.Value}");
        }

        internal static void LogDebug(string msg)
        {
            Log.LogDebug(debugBase + msg);
        }
        internal static void LogInfo(string msg)
        {
            Log.LogInfo(debugBase + msg);
        }
        internal static void LogError(string msg)
        {
            Log.LogError(debugBase + msg);
        }

        public static string DictToString(Dictionary<string, List<string>> dict)
        {
            if (dict == null)
                throw new ArgumentNullException(nameof(dict));

            var sb = new System.Text.StringBuilder();
            sb.Append('{');

            var sortedKeys = dict.Keys.OrderBy(k => k).ToList();

            for (int i = 0; i < sortedKeys.Count; i++)
            {
                string key = sortedKeys[i];
                List<string> values = dict[key];

                sb.Append($"\"{key}\":[");

                for (int j = 0; j < values.Count; j++)
                {
                    sb.Append($"\"{values[j]}\"");
                    if (j < values.Count - 1)
                        sb.Append(',');
                }

                sb.Append(']');

                if (i < sortedKeys.Count - 1)
                    sb.Append(',');
            }

            sb.Append('}');
            return sb.ToString();
        }

    }
}