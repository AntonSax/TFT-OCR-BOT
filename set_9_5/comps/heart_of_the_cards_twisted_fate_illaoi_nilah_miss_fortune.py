"""
Title: Heart of the Cards - A Tier
Comp: https://app.mobalytics.gg/tft/comps-guide/heart-of-the-cards-2UiFaH0he2Q79A36gooRYd56OYY
Set: 9.5
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
Legend: Lee Sin
"""

NAME = "Heart of the Cards"

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Bilgewater", "Bastion", "Multicaster"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Demacia", "Juggernaut", "Strategist", "Vanquisher"]

RECOMMENDED_LEGEND = "Lee Sin"

HEALTH_TO_START_PLACING_ITEMS_ON_UNITS_RANDOMLY = 16

COMP = {
    "Twisted Fate": {
        "board_position": 1,
        "best_in_slot": ["BlueBuff", "HextechGunblade", "JeweledGauntlet"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 23,
        "best_in_slot": ["DragonsClaw", "Redemption", "WarmogsArmor"],
        "secondary_items": ["Evenshroud", "SteraksGage", "TitansResolve"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Nilah": {
        "board_position": 16,
        "best_in_slot": ["TitansResolve", "Bloodthirster", "RapidFirecannon"],
        "secondary_items": ["Deathblade", "GiantSlayer", "SteraksGage"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Miss Fortune": {
        "board_position": 3,
        "best_in_slot": ["Guardbreaker", "SpearofShojin"],
        "secondary_items": ["JeweledGauntlet", "BlueBuff", "HextechGunblade"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["MulticasterEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Nautilus": {
        "board_position": 24,
        "best_in_slot": [],
        "secondary_items": ["Redemption", "DragonsClaw", "BrambleVest", "GargoyleStoneplate", "IonicSpark", "SunfireCape"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Poppy": {
        "board_position": 25,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem", "JuggernautEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Sona": {
        "board_position": 0,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem", "StrategistEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Taliyah": {
        "board_position": 2,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Swain": {
        "board_position": 22,
        "best_in_slot": ["Redemption", "TitansResolve", "WarmogsArmor"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem"],
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
    "AFK",
    "Money!",
    "On a Roll",

    "Money Money!",
    "Perfected Repetition",
    "Strategist Heart",

    "Golden Ticket",
    "Money Money Money!",
    "Strategist Soul"
]

# Picks these augments when there are no primary augments to pick from after re-rolling augments in neither list.
SECONDARY_AUGMENTS: list[str] = [
    "Balanced Budget",
    "Battle Ready I",
    "Pandora's Items I",
    "Partial Ascension",
    "Tiny Power I",
    "Tiny Titans",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Last Stand",
    "Metabolic Accelerator",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Support Cache",
    "Teaming Up II",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",

    "Battle Ready III",
    "Balanced Budget III",
    "Final Ascension",
    "Impenetrable Bulwark",
    "Lucky Gloves",
    "Pandora's Items III",
    "Teaming Up III",
    "Tiniest Titan",
    "Tiny Power III",
    "Unified Resistance III",
]