import configparser
config = configparser.ConfigParser()

config["Interface"] = {
    'bg_col': "#1E1E1E",
    'tx_col': "white",
    'cl_low': "red",
    'cl_mid': "yellow",
    'cl_hig': "green"
}

# As there seems to be no way to include comments in the ini-writing of configparser, have a dumb workaround:
config["Slot Colours"] = {
    "readme": "Equipment slot colours - baseline values are based on filterblade's standard colorations - Caution: Filterblade only provides rgb values, while tkinter only accepts hex values and/or colour names (ie black, yellow, ...). Convert with a free program of your choosing or use something like https://www.rgbtohex.net/. Find these values in your filterblade-filters under Customize > Endgame > Add custom Show/Hide rule > Highlight rares by item slot. Use _c to modify background colour and _t to modify text colour of respective slot"
}

config["Slots"] = {
    'weap_c': "#FF5D00", 'weap_t': "black",
    'hand_c': "#533E93", 'hand_t': "black",
    'feet_c': "#3E7B93", 'feet_t': "black",
    'head_c': "#BA3B8A", 'head_t': "black",
    'chst_c': "#256C1A", 'chst_t': "black",
    'amul_c': "#FFFFFF", 'amul_t': "black",
    'ring_c': "#FFFFFF", 'ring_t': "black",
    'belt_c': "#FFFFFF", 'belt_t': "black"
}

config["SavedVars"] = {
    'sets': "0",
    'head': "0", 'chst': "0",
    'weap': "0", 'hand': "0",
    'feet': "0", 'amul': "0",
    'ring': "0", 'belt': "0",
}
with open('settings.ini', 'w') as configfile:
    config.write(configfile)