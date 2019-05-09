import os
import sys
import tkinter as tk
from tkinter import filedialog
import random
import pathlib

print("Fire Emblem 5 Randomizer By NNadnerd")

###DEFINITIONS
root = tk.Tk()
root.withdraw()
red_growths_player = "0"
first_skill = [0x8, 0x10]
second_skill = [0x1, 0x2, 0x8, 0x10, 0x20, 0x40, 0x80]
third_skill = [0x1, 0x2, 0x4, 0x8, 0x10]
uec = open("unit_exec_class.txt", "r")
unit_exec_class = uec.readlines()
uec.close()
uecb = open("unit_exec_class_boss.txt", "r")
unit_exec_class_boss = uec.readlines()
uecb.close()
uci = open("unit_config_index.txt", "r")
unit_config_index = uci.readlines()
uci.close()

unp = open("unpromo_index.txt", "r")
unpromoted_classes = unp.readlines()
unp.close()
unpromoted = []
for x in range(0, 1000):
    uclass = random.choice(unpromoted_classes)
    unpromoted.append(int(uclass.split(" ")[0]))

pro = open("promo_index.txt", "r")
promoted_classes = pro.readlines()
pro.close()
promoted = []
for x in range(0, 1000):
    uclass = random.choice(promoted_classes)
    promoted.append(int(uclass.split(" ")[0]))
    
skillz = []
for x in range(0, 1000):
    cha = random.randint(1, 80)
    modif = dict()
    if cha > 70:
        modif.update({"first" : random.sample(first_skill, random.randint(0, 2))})
    elif cha > 60:
        modif.update({"second" : random.sample(second_skill, random.randint(0, 7))})
    elif cha > 50:
        modif.update({"third" : random.sample(third_skill, random.randint(0, 5))})
    elif cha > 40:
        modif.update({"third" : random.choice(third_skill)})
        modif.update({"second" : random.choice(second_skill)})
    first = 0x0
    second = 0x0
    third = 0x0
    try:
        first = sum(modif["first"])
    except:
        try:
            second = sum(modif["second"])
            third = sum(modif["third"])
        except:
            try:
                second = sum(modif["second"])
            except:
                try:
                    third = sum(modif["third"])
                except:
                    first = 0x0
    skillz.append([first, second, third])

promo = []
for x in range(0, 50):
    prom = random.choice(promoted_classes)
    promo.append(int(prom.split(" ")[0]))

class Unit:
    def __init__(self, rom, m):
        self.hp = rom[0x31A2D + (48 * m) + 0]
        self.stg = rom[0x31A2D + (48 * m) + 1]
        self.mag = rom[0x31A2D + (48 * m) + 2]
        self.skl = rom[0x31A2D + (48 * m) + 3]
        self.spd = rom[0x31A2D + (48 * m) + 4]
        self.dfc = rom[0x31A2D + (48 * m) + 5]
        self.con = rom[0x31A2D + (48 * m) + 6]
        self.lck = rom[0x31A2D + (48 * m) + 7]
        self.mov = rom[0x31A2D + (48 * m) + 8]
        self.move_stars = rom[0x31A2D + (48 * m) + 9]
        self.pcc = rom[0x31A2D + (48 * m) + 10]
        self.hp_growth = rom[0x31A2D + (48 * m) + 11]
        self.stg_growth = rom[0x31A2D + (48 * m) + 12]
        self.mag_growth = rom[0x31A2D + (48 * m) + 13]
        self.skl_growth = rom[0x31A2D + (48 * m) + 14]
        self.spd_growth = rom[0x31A2D + (48 * m) + 15]
        self.dfc_growth = rom[0x31A2D + (48 * m) + 16]
        self.con_growth = rom[0x31A2D + (48 * m) + 17]
        self.lck_growth = rom[0x31A2D + (48 * m) + 18]
        self.mov_growth = rom[0x31A2D + (48 * m) + 19]
        self.sword = rom[0x31A2D + (48 * m) + 20]
        self.lance = rom[0x31A2D + (48 * m) + 21]
        self.axe = rom[0x31A2D + (48 * m) + 22]
        self.bow = rom[0x31A2D + (48 * m) + 23]
        self.staff = rom[0x31A2D + (48 * m) + 24]
        self.fire = rom[0x31A2D + (48 * m) + 25]
        self.thunder = rom[0x31A2D + (48 * m) + 26]
        self.wind = rom[0x31A2D + (48 * m) + 27]
        self.light = rom[0x31A2D + (48 * m) + 28]
        self.dark = rom[0x31A2D + (48 * m) + 29]
        self.gender = rom[0x31A2D + (48 * m) + 40]
        self.skill_one = rom[0x31A2D + (48 * m) + 41]
        self.skill_two = rom[0x31A2D + (48 * m) + 42]
        self.skill_three = rom[0x31A2D + (48 * m) + 43]
        self.uclass = rom[0x31A2D + (48 * m) + 44]
        self.lead_stars = rom[0x31A2D + (48 * m) + 45]
        self.map_sprite = rom[0x31A2D + (48 * m) + 46]
        self.portrait = rom[0x31A2D + (48 * m) + 47]
    def writable(self):
        formated = bytearray()
        formated.append(self.hp)
        formated.append(self.stg)
        formated.append(self.mag)
        formated.append(self.skl)
        formated.append(self.spd)
        formated.append(self.dfc)
        formated.append(self.con)
        formated.append(self.lck)
        formated.append(self.mov)
        formated.append(self.move_stars)
        formated.append(self.pcc)
        formated.append(self.hp_growth)
        formated.append(self.stg_growth)
        formated.append(self.mag_growth)
        formated.append(self.skl_growth)
        formated.append(self.spd_growth)
        formated.append(self.dfc_growth)
        formated.append(self.con_growth)
        formated.append(self.lck_growth)
        formated.append(self.mov_growth)
        formated.append(self.sword)
        formated.append(self.lance)
        formated.append(self.axe)
        formated.append(self.bow)
        formated.append(self.staff)
        formated.append(self.fire)
        formated.append(self.thunder)
        formated.append(self.wind)
        formated.append(self.light)
        formated.append(self.dark)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(0x64)
        formated.append(self.gender)
        formated.append(self.skill_one)
        formated.append(self.skill_two)
        formated.append(self.skill_three)
        formated.append(self.uclass)
        formated.append(self.lead_stars)
        formated.append(self.map_sprite)
        formated.append(self.portrait)
        return formated
###

###FUNCTIONS
def find_preset():
    try:
        preset_path = filedialog.askopenfilename()
        f = open(preset_path, "r")
        f.close()
    except:
        print(">Invalid file")
        find_preset()
    return preset_path

def randolog(tolog):
    print(">%s" % tolog)

def promolinker(unprom):
    if unprom == 0x42:
        return 0x4B
    elif unprom == 0x43:
        return 0x49
    elif unprom == 0x44:
        return 0x4D
    elif unprom == 0x45:
        return 0x4F
    elif unprom == 0x46:
        return 0x4E
    elif unprom == 0x47:
        return 0x4C
    elif unprom == 0x50:
        return 0x51
    elif unprom == 0x52:
        return 0x53
    elif unprom == 0x15:
        return 0x18
    elif unprom == 0x16:
        return 0x17
    elif unprom == 0x1D:
        return 0x1A
    elif unprom == 0x1E:
        return 0x1A
    elif unprom == 0x1F:
        return 0x1A
    elif unprom == 0x20:
        return 0x1A
    elif unprom == 0x22:
        return 0x24
    elif unprom == 0x25:
        return 0x24
    elif unprom == 0x26:
        return 0x21
    elif unprom == 0x29:
        return 0x2A
    elif unprom == 0x2E:
        return 0x33
    elif unprom == 0x30:
        return 0x38
    elif unprom == 0x31:
        return 0x28
    elif unprom == 0x2F:
        return 0x35
    elif unprom == 0x36:
        return 0x35
    elif unprom == 0x37:
        return 0x35
    elif unprom == 0x3A:
        return 0x3B
    elif unprom == 0x41:
        return 0x71
###

### INIT
print("Select File To Randomize")
file_path = filedialog.askopenfilename()
try:
    f = open(file_path, "r")
    f.close()
except:
    randolog("Invalid File!")
    sys.exit(1)
randolog("Randomizer will randomize the file %s" % file_path)
print("Type 1 for yes and anything else for no to answer all questions.")
preset = input("Would you like to use file of preset settings for this randomization?")
###

### OPTIONS
if preset == "1":
    print("Select Preset File")
    preset_path = find_preset()
    f = open(preset_path, "r")
    exec(f.read())
    f.close()
else:
    print("You will now be asked a series of questions about how you want to randomize the rom.")
    character_classes = input("Randomize Character Classes?\n")
    if character_classes == "1":
        promotions = input("Randomize Promotions?\n")
        leif_class = input("Randomize Leif?\n")
        player_class = input("Randomize Player?\n")
        boss_class = input("Randomize Bosses?\n")
    growths_player = input("Randomize Character Growths?\n")
    if growths_player == "1":
        growths_min = int(input("The Minimum Value Per Growth:"))
        growths_max = int(input("The Maximum Value Per Growth:"))
    else:
        red_growths_player = input("Redistribute Character Growths?\n")
    increase_enemy = input("Increase Enemy Growths?\n")
    if increase_enemy == "1":
        enemy_growth_varient = int(input("Increase Growths By:"))
    bases_player = input("Randomize Player Bases?\n")
    bases_enemy = input("Randomize Enemy Bases?\n")
    if bases_enemy == "1" or bases_player == "1":
        bases_min = int(input("The Minimum Value Per Base:"))
        bases_max = int(input("The Maximum Value Per Base:"))
    skills_player = input("Randomize Player Skills?\n")
    skills_bosses = input("Randomize Enemy Skills?\n")
    movement_stars_player = input("Randomize Player Movement Stars?\n")
    movement_stars_bosses = input("Randomize Enemy Movement Stars?\n")
    if movement_stars_bosses == "1" or movement_stars_player == "1":
        movement_stars_min = int(input("The Minimum Value Per Star:"))
        movement_stars_max = int(input("The Maximum Value Per Star:"))
    leadership_stars_player = input("Randomize Player Leadership Stars?\n")
    leadership_stars_bosses = input("Randomize Enemy Leadership Stars?\n")
    if leadership_stars_bosses == "1" or leadership_stars_player == "1":
        leadership_stars_min = int(input("The Minimum Value Per Star:"))
        leadership_stars_max = int(input("The Maximum Value Per Star:"))
    pcc_player = input("Randomize Player PCC?\n")
    pcc_boss = input("Randomize Enemy PCC?\n")
    if pcc_boss == "1" or pcc_player == "1":
        pcc_min = int(input("The Minimum Value Per Coefficient:"))
        pcc_max = int(input("The Maximum Value Per Coefficient:"))
    crusader_scrolls = input("Randomize Crusader Scrolls?\n")
    if crusader_scrolls == "1":
        crusader_scrolls_min = int(input("The Minimum Value Per Growth Increase:"))
        crusader_scrolls_max = int(input("The Maximum Value Per Growth Increase:"))
    fow = input("Randomize Fog Of War?\n")
    if fow == "1":
        fow_min = int(input("The Minimum For Vision Range (0 for infinite):"))
        fow_max = int(input("The Maximum For Vision Range (0 for infinite):"))
    items = input("Randomize Weapons?\n")
    item_effects = input("Randomize Weapon Effects?")
    remove_weapon_locks = input("Remove Weapon Locks?\n")
    export = input("Export Preset?\n")
    if export == "1":
        export_name = input("Name the preset (this will overwrite any file of the same name in the same directory as your rom):")
        try:
            os.remove("%s.rpst" % export_name)
        except:
            print(">")
        entries = []
        entries.append("character_classes = \"%s\"\n" % character_classes)
        entries.append("promotions = \"%s\"\n" % promotions)
        entries.append("leif_class = \"%s\"\n" % leif_class)
        entries.append("player_class = \"%s\"\n" % player_class)
        entries.append("boss_class = \"%s\"\n" % boss_class)
        entries.append("growths_player = \"%s\"\n" % growths_player)
        entries.append("red_growths_player = \"%s\"\n" % red_growths_player)
        entries.append("increase_enemy = \"%s\"\n" % increase_enemy)
        entries.append("enemy_growth_varient = %s\n" % enemy_growth_varient)
        entries.append("growths_min = %s\n" % growths_min)
        entries.append("growths_max = %s\n" % growths_max)
        entries.append("bases_player = \"%s\"\n" % bases_player)
        entries.append("bases_enemy = \"%s\"\n" % bases_enemy)
        entries.append("bases_min = %s\n" % bases_min)
        entries.append("bases_max = %s\n" % bases_max)
        entries.append("skills_player = \"%s\"\n" % skills_player)
        entries.append("skills_bosses = \"%s\"\n" % skills_bosses)
        entries.append("movement_stars_player = \"%s\"\n" % movement_stars_player)
        entries.append("movement_stars_enemy = \"%s\"\n" % movement_stars_bosses)
        entries.append("movement_stars_min = %s\n" % movement_stars_min)
        entries.append("movement_stars_max = %s\n" % movement_stars_max)
        entries.append("leadership_stars_player = \"%s\"\n" % leadership_stars_player)
        entries.append("leadership_stars_bosses = \"%s\"\n" % leadership_stars_bosses)
        entries.append("leadership_stars_min = %s\n" % leadership_stars_min)
        entries.append("leadership_stars_max = %s\n" % leadership_stars_max)
        entries.append("pcc_player = \"%s\"\n" % pcc_player)
        entries.append("pcc_boss = \"%s\"\n" % pcc_boss)
        entries.append("pcc_min = %s\n" % pcc_min)
        entries.append("pcc_max = %s\n" % pcc_max)
        entries.append("crusader_scrolls = \"%s\"\n" % crusader_scrolls)
        entries.append("crusader_scrolls_min = %s\n" % crusader_scrolls_min)
        entries.append("crusader_scrolls_max = %s\n" % crusader_scrolls_max)
        entries.append("fow = \"%s\"\n" % fow)
        entries.append("fow_min = %s\n" % fow_min)
        entries.append("fow_max = %s\n" % fow_max)
        entries.append("remove_weapon_locks = \"%s\"\n" % remove_weapon_locks)
        entries.append("item_effects = \"%s\"\n" % item_effects)
        entries.append("items = \"%s\"\n" % items)
        prst = open("%s.rpst" % export_name, "w")
        prst.writelines(entries)
        prst.close()
###

### ROM DATA EXTRACTION
rom = pathlib.Path(file_path).read_bytes()
#unit objects
leif = Unit(rom, 0)
finn = Unit(rom, 1)
orsin = Unit(rom, 2)
halvan = Unit(rom, 3)
eyvel = Unit(rom, 4)
dagdar = Unit(rom, 5)
ralph = Unit(rom, 6)
marty = Unit(rom, 7)
ronan = Unit(rom, 8)
miranda = Unit(rom, 9)
safy = Unit(rom, 10)
lara = Unit(rom, 11)
brighton = Unit(rom, 12)
fergus = Unit(rom, 13)
eda = Unit(rom, 14)
asvel = Unit(rom, 15)
matria = Unit(rom, 16)
hicks = Unit(rom, 17)
nanna = Unit(rom, 18)
selphina = Unit(rom, 19)
dalson = Unit(rom, 20)
callion = Unit(rom, 21)
shiva = Unit(rom, 22)
pahn = Unit(rom, 23)
glade = Unit(rom, 24)
kane = Unit(rom, 25)
alba = Unit(rom, 26)
robert = Unit(rom, 27)
fred = Unit(rom, 28)
olwen = Unit(rom, 29)
ced = Unit(rom, 30)
lifis = Unit(rom, 31)
karen = Unit(rom, 32)
dean = Unit(rom, 33)
shanam = Unit(rom, 34)
trude = Unit(rom, 35)
tanya = Unit(rom, 36)
linoan = Unit(rom, 37)
mischa = Unit(rom, 38)
salem = Unit(rom, 39)
seluf = Unit(rom, 40)
mareeta = Unit(rom, 41)
tina = Unit(rom, 42)
amalda = Unit(rom, 44)
conomore = Unit(rom, 45)
homer = Unit(rom, 46)
dermott = Unit(rom, 47)
sara = Unit(rom, 48)
saias = Unit(rom, 49)
galzus = Unit(rom, 0x49)
eyrios = Unit(rom, 0xD3)
xavier = Unit(rom, 0xEC)
redric = Unit(rom, 0x142)
berdo = Unit(rom, 0x34)
weisman = Unit(rom, 0x35)
balist = Unit(rom, 0x37)
lobos = Unit(rom, 0x3C)
bandol = Unit(rom, 0xB6)
truman = Unit(rom, 0xB8)
eisenhowe = Unit(rom, 0x54)
gomes = Unit(rom, 0x5B)
merloc = Unit(rom, 0x5C)
largo = Unit(rom, 0x62)
kempf = Unit(rom, 0x65)
oltof = Unit(rom, 0x67)
rist = Unit(rom, 0x6B)
paul = Unit(rom, 0x6C)
baldack = Unit(rom, 0x6D)
codha = Unit(rom, 0x73)
rumaigh = Unit(rom, 0x5A)
colho = Unit(rom, 0x6A)
brooks = Unit(rom, 0x7D)
nicolav = Unit(rom, 0x7F)
moore = Unit(rom, 0x80)
mueller = Unit(rom, 0x81)
reincock = Unit(rom, 0x82)
palman = Unit(rom, 0x83)
gustav = Unit(rom, 0x85)
barat = Unit(rom, 0x102)
wolfe = Unit(rom, 0x156)
dvorak = Unit(rom, 0xc2)
zile = Unit(rom, 0xcf)
eichman = Unit(rom, 0xce)
flavus = Unit(rom, 0x89)
seimtore = Unit(rom, 0x8a)
zaum = Unit(rom, 0x8b)
cohen = Unit(rom, 0x8c)
alphan = Unit(rom, 0x8d)
farden = Unit(rom, 0x8f)
coulter = Unit(rom, 0x90)
reinhardt = Unit(rom, 0x91)
mus = Unit(rom, 0x132)
tigris = Unit(rom, 0x133)
tigris_dagdar = Unit(rom, 0x134)
canis = Unit(rom, 0x135)
canis_sara = Unit(rom, 0x136)
bovis = Unit(rom, 0x137)
bovis_galzus = Unit(rom, 0x138)
porcus = Unit(rom, 0x139)
porcus_lifis = Unit(rom, 0x13A)
draco = Unit(rom, 0x13B)
draco_eyvel = Unit(rom, 0x13C)
#scroll objects
#chapter objects
###

### ACTUAL RANDOMIZATION
if character_classes == "1":
    if leif_class == "1":
        leif.uclass = unpromoted[random.randint(1, 9999)]
    if player_class == "1":
        for x in range(0, 34):
            exec("%s.uclass = unpromoted[random.randint(0, 9999)]" % unit_exec_class[x + 1])
        for x in range(0, 17):
            exec("%s.uclass = promoted[random.randint(0, 9999)]" % unit_exec_class[x + 35])
    if boss_class == "1":
        weisman.uclass = unpromoted[random.randint(1, 9999)]
        for x in range(0, 49):
            exec("%s.uclass = promoted[random.randint(0, 9999)]" % unit_exec_class_boss[x + 1])
if growths_player == "1":
    for x in range(0, 52):
        exec("%s.hp_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.stg_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.mag_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.skl_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.spd_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.dfc_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.con_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.lck_growth = random.randint(growths_min, growths_max)" % unit_exec_class[x])
        exec("%s.mov_growth = random.randint(0, 5)" % unit_exec_class[x])
if red_growths_player == "1":
    leif_div = int(leif.hp_growth) + int(leif.stg_growth) + int(leif.mag_growth) + int(leif.skl_growth) + int(leif.spd_growth) + int(leif.dfc_growth) + int(leif.con_growth) + int(leif.lck_growth)
if bases_player == "1":
    for x in range(0, 52):
        exec("%s.hp = random.randint(bases_min, bases_max)" % unit_exec_class[x])
        exec("%s.stg = random.randint(bases_min, bases_max)" % unit_exec_class[x])
        exec("%s.mag = random.randint(bases_min, bases_max)" % unit_exec_class[x])
        exec("%s.skl = random.randint(bases_min, bases_max)" % unit_exec_class[x])
        exec("%s.spd = random.randint(bases_min, bases_max)" % unit_exec_class[x])
        exec("%s.dfc = random.randint(bases_min, bases_max)" % unit_exec_class[x])
        exec("%s.con = random.randint(bases_min, bases_max)" % unit_exec_class[x])
        exec("%s.lck = random.randint(bases_min, bases_max)" % unit_exec_class[x])
if bases_enemy == "1":
    for x in range(0, 50):
        exec("%s.hp = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.stg = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.mag = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.skl = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.spd = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.dfc = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.con = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.lck = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
        exec("%s.mov = random.randint(bases_min, bases_max)" % unit_exec_class_boss[x])
if skills_player == "1":
    for x in range(0, 52):
        exec("%s.skill_one = skillz[random.randint(0, 149)][0]" % unit_exec_class[x])
        exec("%s.skill_two = skillz[random.randint(0, 149)][1]" % unit_exec_class[x])
        exec("%s.skill_three = skillz[random.randint(0, 149)][2]" % unit_exec_class[x])
if skills_bosses == "1":
    for x in range(0, 50):
        exec("%s.skill_one = skillz[random.randint(0, 149)][0]" % unit_exec_class_boss[x])
        exec("%s.skill_two = skillz[random.randint(0, 149)][1]" % unit_exec_class_boss[x])
        exec("%s.skill_three = skillz[random.randint(0, 149)][2]" % unit_exec_class_boss[x])
if movement_stars_player == "1":
    for x in range(0, 52):
        exec("%s.move_stars = random.randint(movement_stars_min, movement_stars_max)" % unit_exec_class[x])
if movement_stars_bosses == "1":
    for x in range(0, 50):
        exec("%s.move_stars = random.randint(movement_stars_min, movement_stars_max)" % unit_exec_class_boss[x])
if leadership_stars_player == "1":
    for x in range(0, 52):
        exec("%s.lead_stars = random.randint(leadership_stars_min, leadership_stars_max)" % unit_exec_class[x])
if leadership_stars_bosses == "1":
    for x in range(0, 50):
        exec("%s.lead_stars = random.randint(leadership_stars_min, leadership_stars_max)" % unit_exec_class_boss[x])
if pcc_player == "1":
    for x in range(0, 52):
        exec("%s.pcc = random.randint(pcc_min, pcc_max)" % unit_exec_class[x])
if pcc_boss == "1":
    for x in range(0, 50):
        exec("%s.pcc = random.randint(pcc_min, pcc_max)" % unit_exec_class_boss[x])
#if crusader_scrolls == "1":
#if fow == "1":
#if items == "1":
#if item_effects == "1":
#if remove_weapon_locks == "1":
###

### VALUE WRITING
#open ROM
romhand = open(file_path, "wb")
#unit writing
romhand.seek((48 * 0) + 0x31A2D)
romhand.write(leif.writable())
romhand.seek((48 * 1) + 0x31A2D)
romhand.write(finn.writable())
romhand.seek((48 * 2) + 0x31A2D)
romhand.write(orsin.writable())
romhand.seek((48 * 3) + 0x31A2D)
romhand.write(halvan.writable())
romhand.seek((48 * 4) + 0x31A2D)
romhand.write(eyvel.writable())
romhand.seek((48 * 5) + 0x31A2D)
romhand.write(dagdar.writable())
romhand.seek((48 * 6) + 0x31A2D)
romhand.write(ralph.writable())
romhand.seek((48 * 7) + 0x31A2D)
romhand.write(marty.writable())
romhand.seek((48 * 8) + 0x31A2D)
romhand.write(ronan.writable())
romhand.seek((48 * 9) + 0x31A2D)
romhand.write(miranda.writable())
romhand.seek((48 * 10) + 0x31A2D)
romhand.write(safy.writable())
romhand.seek((48 * 11) + 0x31A2D)
romhand.write(lara.writable())
#promo writing/correcting
if promotions == "1":
    romhand.seek(0x402F3 + (3 * 0))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 1))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 2))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 3))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 4))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 5))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 6))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 7))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 8))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 9))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 10))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 11))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 12))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 13))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 14))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 15))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 16))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 17))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 18))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 19))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 20))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 21))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 22))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 23))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 24))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 25))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 26))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 27))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 28))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 29))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 30))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 31))
    romhand.write(promo[random.randint(0, 50)])
    romhand.seek(0x402F3 + (3 * 32))
    romhand.write(promo[random.randint(0, 50)])
else:
    romhand.seek(0x402F3 + (3 * 0))
    romhand.write(promolinker(finn.uclass))
    romhand.seek(0x402F3 + (3 * 1))
    romhand.write(promolinker(orsin.uclass))
    romhand.seek(0x402F3 + (3 * 2))
    romhand.write(promolinker(halvan.uclass))
    romhand.seek(0x402F3 + (3 * 3))
    romhand.write(promolinker(ralph.uclass))
    romhand.seek(0x402F3 + (3 * 4))
    romhand.write(promolinker(marty.uclass))
    romhand.seek(0x402F3 + (3 * 5))
    romhand.write(promolinker(ronan.uclass))
    romhand.seek(0x402F3 + (3 * 6))
    romhand.write(promolinker(miranda.uclass))
    romhand.seek(0x402F3 + (3 * 7))
    romhand.write(promolinker(safy.uclass))
    romhand.seek(0x402F3 + (3 * 8))
    romhand.write(promolinker(lara.uclass))
    romhand.seek(0x402F3 + (3 * 9))
    romhand.write(promolinker(brighton.uclass))
    romhand.seek(0x402F3 + (3 * 10))
    romhand.write(promolinker(fergus.uclass))
    romhand.seek(0x402F3 + (3 * 11))
    romhand.write(promolinker(eda.uclass))
    romhand.seek(0x402F3 + (3 * 12))
    romhand.write(promolinker(asvel.uclass))
    romhand.seek(0x402F3 + (3 * 13))
    romhand.write(promolinker(matria.uclass))
    romhand.seek(0x402F3 + (3 * 14))
    romhand.write(promolinker(hicks.uclass))
    romhand.seek(0x402F3 + (3 * 15))
    romhand.write(promolinker(nanna.uclass))
    romhand.seek(0x402F3 + (3 * 16))
    romhand.write(promolinker(selphina.uclass))
    romhand.seek(0x402F3 + (3 * 17))
    romhand.write(promolinker(dalson.uclass))
    romhand.seek(0x402F3 + (3 * 18))
    romhand.write(promolinker(callion.uclass))
    romhand.seek(0x402F3 + (3 * 19))
    romhand.write(promolinker(shiva.uclass))
    romhand.seek(0x402F3 + (3 * 20))
    romhand.write(promolinker(kane.uclass))
    romhand.seek(0x402F3 + (3 * 21))
    romhand.write(promolinker(alba.uclass))
    romhand.seek(0x402F3 + (3 * 22))
    romhand.write(promolinker(robert.uclass))
    romhand.seek(0x402F3 + (3 * 23))
    romhand.write(promolinker(lifis.uclass))
    romhand.seek(0x402F3 + (3 * 24))
    romhand.write(promolinker(karen.uclass))
    romhand.seek(0x402F3 + (3 * 25))
    romhand.write(promolinker(trude.uclass))
    romhand.seek(0x402F3 + (3 * 26))
    romhand.write(promolinker(tanya.uclass))
    romhand.seek(0x402F3 + (3 * 27))
    romhand.write(promolinker(salem.uclass))
    romhand.seek(0x402F3 + (3 * 28))
    romhand.write(promolinker(seluf.uclass))
    romhand.seek(0x402F3 + (3 * 29))
    romhand.write(promolinker(mareeta.uclass))
    romhand.seek(0x402F3 + (3 * 30))
    romhand.write(promolinker(tina.uclass))
    romhand.seek(0x402F3 + (3 * 31))
    romhand.write(promolinker(homer.uclass))
    romhand.seek(0x402F3 + (3 * 32))
    romhand.write(promolinker(sara.uclass))
#class writing

#scroll writing

#increase enemy growths
if increase_enemy == "1":
    untouchables = []
    for x in range(0, 184):
        untouchables.append(int(unit_config_index[x]) - 1)
    unit = 0
    if enemy_growth_varient > 127:
        enemy_growth_varient = 127
    while unit < 0x156:
        if unit in untouchables:
            unit = unit + 1
        else:
            romhand.seek(0x31A2D + 11 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 11 + (unit * 48)]) + enemy_growth_varient)
            romhand.seek(0x31A2D + 12 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 12 + (unit * 48)]) + enemy_growth_varient)
            romhand.seek(0x31A2D + 13 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 13 + (unit * 48)]) + enemy_growth_varient)
            romhand.seek(0x31A2D + 14 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 14 + (unit * 48)]) + enemy_growth_varient)
            romhand.seek(0x31A2D + 15 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 15 + (unit * 48)]) + enemy_growth_varient)
            romhand.seek(0x31A2D + 16 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 16 + (unit * 48)]) + enemy_growth_varient)
            romhand.seek(0x31A2D + 17 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 17 + (unit * 48)]) + enemy_growth_varient)
            romhand.seek(0x31A2D + 18 + (unit * 48))
            romhand.write(int(rom[0x31A2D + 18 + (unit * 48)]) + enemy_growth_varient)
            unit = unit + 1
#close ROM
romhand.close()
###