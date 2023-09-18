"""
Items are in camel case and a-Z
Comp from https://app.mobalytics.gg/tft/comps-guide/challengers-2Qnyf4oMpJ0P8r6K2ZL5jDoAlAO
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
"""

COMP = {
    "Kalista": {
        "board_position": 6,
        "best_in_slot": ["JeweledGauntlet", "GuinsoosRageblade", "HandofJustice"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Yasuo": {
        "board_position": 23,
        "best_in_slot": ["TitansResolve", "Bloodthirster"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Shen": {
        "board_position": 24,
        "best_in_slot": ["Redemption", "BrambleVest"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Gwen": {
        "board_position": 25,
        "best_in_slot": ["WarmogsArmor", "BlueBuff", "ChallengerEmblem"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Warwick": {
        "board_position": 22,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Irelia": {
        "board_position": 26,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "KaiSa": {
        "board_position": 0,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Samira": {
        "board_position": 3,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Kassadin": {
        "board_position": 23,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Maokai": {
        "board_position": 24,
        "best_in_slot": ["WarmogsArmor"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
PRIMARY_AUGMENTS: list[str] = [
    "Battle Ready I",
    "Bronze Ticket",
    "Challenger Heart",
    "Cybernetic Bulk I",
    "Cybernetic Leech I",
    "Gotta Go Fast!!! I",
    "Healing Orbs I",
    "Jeweled Lotus I",
    "Money!",
    "Pandora's Items",
    "Partial Ascension",
    "Pumping Up I",
    "Red Buff",
    "Social Distancing I",
    "Tiny Titans",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Big Grab Bag",
    "Buried Treasures II",
    "Caretaker's Favor",
    "Challenger Crest"
    "Cybernetic Bulk II",
    "Cybernetic Leech II",
    "Defensive Dash"
    "Early Education",
    "Endurance Training",
    "Final Grab Bag II",
    "Gifts from the Fallen",
    "Gotta Go Fast!!! II",
    "Healing Orbs II",
    "Idealism",
    "Infusion",
    "Item Grab Bag II",
    "It Pays to Learn II",
    "Jeweled Lotus",
    "Knowledge Download II",
    "Know Your Enemy",
    "Last Stand",
    "Magic Wand"
    "Martyr",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Salvage Bin",
    "Salvage Bin+",
    "Scrappy Inventions",
    "Social Distancing II",
    "Sorcerer Crest",
    "Tactical Superiority",
    "Tiny Power II",
    "Tons of Stats!",
    "Unified Resistance II",
    "Vampiric Blades",
    "What Doesn't Kill You",
    "You Have My Bow",

    "Ancient Archives II",
    "Balanced Budget III",
    "Battle Ready III",
    "Blinding Speed",
    "Buried Treasures III",
    "Challenger Crown",
    "Cybernetic Bulk III",
    "Cybernetic Leech III",
    "Final Ascension",
    "Final Reserves",
    "Freljord Soul",
    "Giant Grab Bag",
    "Gifts From Above",
    "Golden Ticket",
    "Gotta Go Fast!!! III",
    "Harmacist III",
    "Hedge Fund",
    "Hedge Fund+",
    "Hedge Fund++",
    "High End Sector",
    "Impenetrable Bulwak",
    "Item Grab Bag III",
    "It Pays to Learn III",
    "Jeweled Lotus III",
    "Knowledge Download III",
    "Large Forge",
    "Level Up!",
    "Living Forge",
    "Lucky Gloves",
    "Masterful Job",
    "Money Money Money!",
    "Pandora's Box",
    "Parting Gifts",
    "Phreaky Friday",
    "Phreaky Friday+",
    "Pumping Up III",
    "Rolling for Days III",
    "Roll The Dice",
    "Shopping Spree",
    "Social Distancing III",
    "Spoils of War III",
    "Tactician's Tools",
    "Tiniest Titan",
    "Tiny Power III",
    "Transfusion III",
    "Unified Resistance III",
    "Unleashed Arcana",
    "Wandering Trainer"
    "Well-Earned Comforts III",
    "Wellness Trust",
]