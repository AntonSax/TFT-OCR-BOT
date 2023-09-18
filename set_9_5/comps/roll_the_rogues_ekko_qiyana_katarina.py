"""
Arcane Domain - S Tier
Comp from https://app.mobalytics.gg/tft/comps-guide/piltovers-pride-2VG56xmI0csHVkF4qX6Uo0443fa
Set: 9.5
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
Legend: Twisted Fate
Don't level up at stage 2-1.
Items are in camel case and a-Z
"""

NAME = "Roll the Rogues"

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Rogue", "Ixtal", "Zaun", "Bastion", "Sorcerer"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Bilgewater", "Gunner", "Invoker", "Noxus", "Piltover", "Slayer", "Targon"]

RECOMMENDED_LEGEND = "Twisted Fate"

COMP = {
    "Qiyana": {
        "board_position": 26,
        "items_to_build": ["HandofJustice", "InfinityEdge", "SteraksGage"],
        "completed_items_to_accept": ["Deathblade", "Bloodthirster", "HandofJustice", "InfinityEdge", "SteraksGage", "TitansResolve"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Ekko": {
        "board_position": 22,
        "items_to_build": ["HandofJustice", "JeweledGauntlet", "HandofJustice"],
        "completed_items_to_accept": ["Crownguard", "HandofJustice", "RabadonsDeathcap"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["SlayerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["HextechExoskeleton", "ShimmerInjector", "UnstableChemtech", "VirulentBioware"],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Katarina": {
        "board_position": 24,
        "items_to_build": ["IonicSpark", "NightHarvester"],
        "completed_items_to_accept": ["Crownguard", "IonicSpark", "NightHarvester", "RabadonsDeathcap"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["SlayerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Silco": {
        "board_position": 0,
        "items_to_build": [],
        "completed_items_to_accept": ["BlueBuff", "Morellonomicon", "RabadonsDeathcap"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["RogueEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "VirulentBioware"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Taric": {
        "board_position": 23,
        "items_to_build": [],
        "completed_items_to_accept": ["BrambleVest", "DragonsClaw", "IonicSpark", "Redemption", "SunfireCape"],
        "support_items_to_accept": ["ChaliceofPower", "LocketoftheIronSolari", "VirtueoftheMartyr", "ZzRotPortal"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Neeko": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Graves": {
        "board_position": 14,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Milio": {
        "board_position": 6,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["NeedlesslyBigGem"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "RekSai": {
        "board_position": 19,
        "items_to_build": ["HandofJustice"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["RogueEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Warwick": {
        "board_position": 15,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["RogueEmblem", "SlayerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "HextechExoskeleton", "RoboticArm", "ShimmerInjector", "UnstableChemtech"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Swain": {
        "board_position": 27,
        "items_to_build": ["Redemption"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["RogueEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Kassadin": {
        "board_position": 16,
        "items_to_build": ["HandofJustice", "HandofJustice", "JeweledGauntlet"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Soraka": {
        "board_position": 2,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Illaoi": {
        "board_position": 21,
        "items_to_build": ["SteraksGage"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["SlayerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Kayle": {
        "board_position": 4,
        "items_to_build": ["InfinityEdge"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["SlayerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
PRIMARY_AUGMENTS: list[str] = [
    "Cybernetic Leech I",
    "Pandora's Items I",
    "Rogue Heart",

    "Idealism",
    "Pandora's Items II",
    "Vampiric Blades",

    "Golden Ticket",
    "Pandora's Items III",
    "Rogue Crown"
]

SECONDARY_AUGMENTS: list[str] = [
    "Battle Ready I",
    "Consistency",
    "Money!",
    "Tiny Power I",
    "Unified Resistance I",

    "Balanced Budget II",
    "Battle Ready II",
    "Ixtal Heart",
    "Last Stand",
    "Money Money!",
    "Patient Study",
    "Pumping Up II",
    "Tiny Power II",
    "Unified Resistance II"

    "Battle Ready III",
    "Lucky Gloves",
    "Money Money Money!",
    "Tiny Power III",
    "Training Reward III",
    "Unified Resistance III",
]