"""
Title: Heart of the Cards v2 - A Tier
Comp: https://app.mobalytics.gg/tft/comps-guide/heart-of-the-cards-2UiFaH0he2Q79A36gooRYd56OYY
Set: 9.5
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
Legend: Lee Sin
"""

NAME = "Heart of the Cards v2"

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Multicaster", "Strategist", "Demacia", "Sorcerer", "Shurima"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Bilgewater", "Invoker", "Noxus", "Void"]

RECOMMENDED_LEGEND = "Lee Sin"

HEALTH_TO_START_PLACING_ITEMS_ON_UNITS_RANDOMLY = 16

COMP = {
    "Twisted Fate": {
        "board_position": 1,
        "best_in_slot": ["BlueBuff", "HextechGunblade", "JeweledGauntlet"],
        "secondary_items": ["BlueBuff", "GiantSlayer", "RabadonsDeathcap"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": ["DeathfireGrasp", "InfinityForce", "SnipersFocus"],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Swain": {
        "board_position": 24,
        "best_in_slot": ["DragonsClaw", "GargoyleStoneplate", "IonicSpark"],
        "secondary_items": ["ArchangelsStaff", "Redemption", "SunfireCape", "TitansResolve"],
        "support_items_to_accept": ["LocketoftheIronSolari"],
        "trait_items_to_accept": ["JuggernautEmblem"],
        "ornn_items_to_accept": ["AnimaVisage", "BlacksmithsGloves", "DeathsDefiance", "EternalWinter", "Hullcrusher", "TrickstersGlass", "ZzRotPortal"],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Jarvan IV": {
        "board_position": 22,
        "best_in_slot": ["ProtectorsVow", "WarmogsArmor"],
        "secondary_items": ["BrambleVest", "DragonsClaw", "SunfireCape"],
        "support_items_to_accept": ["AegisoftheLegion", "VirtueoftheMartyr"],
        "trait_items_to_accept": ["MulticasterEmblem"],
        "ornn_items_to_accept": ["ZhonyasParadox"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 2,
        "final_comp": True
    },
    "Azir": {
        "board_position": 6,
        "best_in_slot": [],
        "secondary_items": ["Guardbreaker", "SpearofShojin", "GuinsoosRageblade", "HextechGunblade", "StatikkShiv"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["DemaciaEmblem", "MulticasterEmblem"],
        "ornn_items_to_accept": ["Muramana", "SnipersFocus"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Galio": {
        "board_position": 26,
        "best_in_slot": [],
        "secondary_items": ["Redemption", "DragonsClaw", "BrambleVest", "GargoyleStoneplate", "IonicSpark", "SunfireCape"],
        "support_items_to_accept": ["VirtueoftheMartyr"],
        "trait_items_to_accept": ["NoxusEmblem", "StrategistEmblem", "VoidEmblem"],
        "ornn_items_to_accept": ["EternalWinter", "TrickstersGlass"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 2,
        "final_comp": True
    },
    "Sona": {
        "board_position": 0,
        "best_in_slot": [],
        "secondary_items": ["StatikkShiv"],
        "support_items_to_accept": ["ChaliceofPower", "ShroudofStillness", "ZekesHerald", "Zephyr"],
        "trait_items_to_accept": ["BilgewaterEmblem", "SorcererEmblem", "StrategistEmblem"],
        "ornn_items_to_accept": ["ObsidianCleaver"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Taliyah": {
        "board_position": 2,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["ChaliceofPower", "ZekesHerald"],
        "trait_items_to_accept": ["BilgewaterEmblem", "DemaciaEmblem"],
        "ornn_items_to_accept": ["RocketPropelledFist"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "VelKoz": {
        "board_position": 5,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem", "DemaciaEmblem", "VanquisherEmblem", "NoxusEmblem", "InvokerEmblem"],
        "ornn_items_to_accept": ["BlacksmithsGloves", "GoldCollector", "GoldmancersStaff", "SnipersFocus"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "ChoGath": {
        "board_position": 23,
        "best_in_slot": ["IonicSpark", "WarmogsArmor"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Renekton": {
        "board_position": 25,
        "best_in_slot": ["DragonsClaw", "GargoyleStoneplate"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
# Picks these augments 100% of the time.
PRIMARY_AUGMENTS: list[str] = [
    # "AFK",
    "Money!",
    "On a Roll",
    "Training Reward I",

    "Money Money!",
    "Perfected Repetition",
    "Strategist Heart",
    "Training Reward II",

    "Golden Ticket",
    "Money Money Money!",
    "Shopping Spree",
    "Strategist Soul",
    "Training Reward III",
]

# Picks these augments when there are no primary augments to pick from after re-rolling augments in neither list.
SECONDARY_AUGMENTS: list[str] = [
    "Balanced Budget",
    "Battle Ready I",
    "Bronze Ticket",
    "Pandora's Items I",
    "Partial Ascension",
    "Sorcerer Heart",
    "Tiny Power I",
    "Tiny Titans",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Demacia Heart",
    "Last Stand",
    "Metabolic Accelerator",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Sorcerer Crest",
    "Support Cache",
    "Teaming Up II",
    "Tiny Power II",
    "Trade Sector",
    "Unified Resistance II",
    "You Have My Bow",

    "Battle Ready III",
    "Balanced Budget III",
    "Demacia Crown",
    "Final Ascension",
    "Impenetrable Bulwark",
    "Lucky Gloves",
    "Multicaster Soul",
    "Pandora's Items III",
    "Sorcerer Crown",
    "Teaming Up III",
    "Tiniest Titan",
    "Tiny Power III",
    "Unified Resistance III",
]