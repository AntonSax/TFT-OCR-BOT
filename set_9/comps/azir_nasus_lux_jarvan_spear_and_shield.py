"""
Items are in camel case and a-Z
Comp from https://app.mobalytics.gg/tft/comps-guide/spear-and-shield-2RvLjaeufrqyrIRRsJFTqDm5riI
Strategy: Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
Difficulty: Medium
"""

COMP = {
    "Azir": {
        "board_position": 6,
        "best_in_slot": ["GuinsoosRageblade", "HextechGunblade", "StatikkShiv", "RapidFirecannon", "Guardbreaker",
                           "GiantSlayer"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Nasus": {
        "board_position": 24,
        "best_in_slot": ["Redemption", "DragonsClaw", "BrambleVest", "GargoyleStoneplate", "WarmogsArmor"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Jarvan IV": {
        "board_position": 26,
        "best_in_slot": ["ProtectorsVow"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "KSante": {
        "board_position": 9,
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
    "Taliyah": {
        "board_position": 9,
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
    "Teemo": {
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
    "Swain": {
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
    "Garen": {
        "board_position": 23,
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
    "Lux": {
        "board_position": 0,
        "best_in_slot": ["BlueBuff", "JeweledGauntlet"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Renekton": {
        "board_position": 16,
        "best_in_slot": ["BrambleVest", "DragonsClaw"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Vi": {
        "board_position": 14,
        "best_in_slot": ["BrambleVest", "DragonsClaw"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Cassiopeia": {
        "board_position": 7,
        "best_in_slot": ["GuinsoosRageblade", "HextechGunblade", "JeweledGauntlet"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Sona": {
        "board_position": 8,
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
    "Orianna": {
        "board_position": 2,
        "best_in_slot": ["StatikkShiv", "BlueBuff"],
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
PRIMARY_AUGMENTS: list[str] = [
    "Battle Ready I",
    "Money!",
    "Pandora's Items I",
    "Partial Ascension",
    "Tiny Power I",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Last Stand",
    "Magic Wand"
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Shurima Crest",
    "Shurima's Legacy",
    "Strategist Heart",
    "Tactical Superiority",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",

    "Battle Ready III",
    "Final Ascension",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
    "Strategist Soul",
    "Tiny Power III",
    "Unified Resistance III",
]

"""
    "Bronze Ticket",
    "Cybernetic Bulk I",
    "Cybernetic Leech I",
    "Gotta Go Fast!!! I",
    "Healing Orbs I",
    "Pumping Up I",
    "Red Buff",
    "Social Distancing I",
    
    
    "Big Grab Bag",
    "Buried Treasures II",
    "Caretaker's Favor",
    "Cybernetic Bulk II",
    "Cybernetic Leech II",
    "Early Education",
    "Endurance Training",
    "Final Grab Bag II",
    "Gifts from the Fallen",
    "Gotta Go Fast!!! II",
    "Healing Orbs II",
    "Infusion",
    "Item Grab Bag II",
    "It Pays to Learn II",
    "Jeweled Lotus",
    "Knowledge Download II",
    "Know Your Enemy",
    "Martyr",
    "Salvage Bin",
    "Salvage Bin+",
    "Scrappy Inventions",
    "Social Distancing II",
    "Sorcerer Crest",
    "Tons of Stats!",
    "What Doesn't Kill You",
    
    "Ancient Archives II",
    "Balanced Budget III",
    "Blinding Speed",
    "Buried Treasures III",
    "Cybernetic Bulk III",
    "Cybernetic Leech III",
    "Final Reserves",
    "Giant Grab Bag",
    "Gifts From Above",
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
    "Masterful Job",
    "Multicaster Soul",
    "Parting Gifts",
    "Phreaky Friday",
    "Phreaky Friday+",
    "Pumping Up III",
    "Rolling for Days III",
    "Roll The Dice",
    "Shopping Spree",
    "Shurima Crown",
    "Social Distancing III",
    "Spoils of War III",
    "Tactician's Tools",
    "Tiniest Titan",
    "Transfusion III",
    "Unleashed Arcana",
    "Wandering Trainer"
    "Well-Earned Comforts III",
    "Wellness Trust",
"""