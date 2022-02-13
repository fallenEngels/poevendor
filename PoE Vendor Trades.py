import tkinter as tk
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")


### Window and canvas setup
root = tk.Tk()
root.title("Vendor Trades")
canvas = tk.Canvas(root, width = 237, height = 218, bg = config["Interface"]["bg_col"])
canvas.pack()

### Options
# Checkbox to display window always on top (default off)
aotvar = tk.IntVar() # logs state
def fnAotSwitch():
	if (aotvar.get() == 1):
		root.attributes('-topmost',True)
	else:
		root.attributes('-topmost',False)

AotText = tk.Label(root, text = "Always on Top", font = ("helvetica", 12), bg = config["Interface"]["bg_col"], fg = config["Interface"]["tx_col"])
AotCheck = tk.Checkbutton(variable=aotvar, onvalue=1, offvalue=0, command=fnAotSwitch, bg = config["Interface"]["bg_col"])
AotCheck.pack()

canvas.create_window(65, 207, window = AotCheck)
canvas.create_window(130, 207, window = AotText)

### Variables and functions
# define vars
sets = tk.IntVar()

head = tk.IntVar()
chst = tk.IntVar()
weap = tk.IntVar()
hand = tk.IntVar()
feet = tk.IntVar()
amul = tk.IntVar()
ring = tk.IntVar()
belt = tk.IntVar()

# load saved values
sets.set(config["SavedVars"]["sets"])

head.set(config["SavedVars"]["head"])
chst.set(config["SavedVars"]["chst"])
weap.set(config["SavedVars"]["weap"])
hand.set(config["SavedVars"]["hand"])
feet.set(config["SavedVars"]["feet"])
amul.set(config["SavedVars"]["amul"])
ring.set(config["SavedVars"]["ring"])
belt.set(config["SavedVars"]["belt"])

# updating completed sets
def fnSetMinus():
	global sets
	sets.set(max(sets.get() - 1, 0))

def fnSetPlus():
	global sets, head, chst, weap, hand, feet, amul, ring, belt
	sets.set(sets.get() + 1)
	head.set(max(head.get() - 1, 0))
	chst.set(max(chst.get() - 1, 0))
	weap.set(max(weap.get() - 2, 0))
	hand.set(max(hand.get() - 1, 0))
	feet.set(max(feet.get() - 1, 0))
	amul.set(max(amul.get() - 1, 0))
	ring.set(max(ring.get() - 2, 0))
	belt.set(max(belt.get() - 1, 0))
	fnUpdCollection()

SetText = tk.Label(root, text = "Completed Sets", font = ("helvetica", 15), bg = config["Interface"]["bg_col"], fg = config["Interface"]["tx_col"])
SetLabel = tk.Label(root, textvariable = sets, font = ('helvetica', 15), bg = config["Interface"]["bg_col"], fg = config["Interface"]["tx_col"])
MinusSet = tk.Button(root, text = "-", command = fnSetMinus)
MinusSet.pack()
PlusSet = tk.Button(root, text = "+", command = fnSetPlus)
PlusSet.pack()

canvas.create_window(90, 17, window = SetText)
canvas.create_window(180, 17, window = MinusSet)
canvas.create_window(199, 17, window = SetLabel)
canvas.create_window(220, 17, window = PlusSet)

### Collection status and colouration
coll_stat = [config["Interface"]["cl_low"]] * 8
def fnUpdCollection():
	item_coll = [head.get() * 2, chst.get() * 2, weap.get(), hand.get() * 2, feet.get() * 2, amul.get() * 2, ring.get(), belt.get() * 2]
	# get values from all items (* 2) to counteract need for double weapons and decimal points
	for i in [0,1,2,3,4,5,6,7]: # update coll_stat for each slot if 0 = 2, some = 3, max = 4
		if item_coll[i] <= 1:
			coll_stat[i] = config["Interface"]["cl_low"]
		elif item_coll[i] == max(item_coll):
			coll_stat[i] = config["Interface"]["cl_hig"]
		else:
			coll_stat[i] = config["Interface"]["cl_mid"]
	HeadLabel.configure(bg = coll_stat[0])
	ChstLabel.configure(bg = coll_stat[1])
	WeapLabel.configure(bg = coll_stat[2])
	HandLabel.configure(bg = coll_stat[3])
	FeetLabel.configure(bg = coll_stat[4])
	AmulLabel.configure(bg = coll_stat[5])
	RingLabel.configure(bg = coll_stat[6])
	BeltLabel.configure(bg = coll_stat[7])


# Haven't found a way to package all in one function yet, so for now it's every variable individually - update item slots
def fnHeadMinus():
	global head
	head.set(max(head.get() - 1, 0))
	fnUpdCollection()
def fnHeadPlus():
	global head
	head.set(head.get() + 1)
	fnUpdCollection()
	
def fnChstMinus():
	global chest
	chst.set(max(chst.get() - 1, 0))
	fnUpdCollection()
def fnChstPlus():
	global chest
	chst.set(chst.get() + 1)
	fnUpdCollection()

def fnWeapMinus():
	global weap
	weap.set(max(weap.get() - 1, 0))
	fnUpdCollection()
def fnWeapPlus():
	global weap
	weap.set(weap.get() + 1)
	fnUpdCollection()
def fnWeapMinus2():
	global weap
	weap.set(max(weap.get() - 2, 0))
	fnUpdCollection()
def fnWeapPlus2():
	global weap
	weap.set(weap.get() + 2)
	fnUpdCollection()

def fnHandMinus():
	global hand
	hand.set(max(hand.get() - 1, 0))
	fnUpdCollection()
def fnHandPlus():
	global hand
	hand.set(hand.get() + 1)
	fnUpdCollection()
	
def fnFeetMinus():
	global Feet
	feet.set(max(feet.get() - 1, 0))
	fnUpdCollection()
def fnFeetPlus():
	global feet
	feet.set(feet.get() + 1)
	fnUpdCollection()

def fnAmulMinus():
	global amul
	amul.set(max(amul.get() - 1, 0))
	fnUpdCollection()
def fnAmulPlus():
	global amul
	amul.set(amul.get() + 1)
	fnUpdCollection()

def fnRingMinus():
	global ring
	ring.set(max(ring.get() - 1, 0))
	fnUpdCollection()
def fnRingPlus():
	global ring
	ring.set(ring.get() + 1)
	fnUpdCollection()

def fnBeltMinus():
	global belt
	belt.set(max(belt.get() - 1, 0))
	fnUpdCollection()
def fnBeltPlus():
	global belt
	belt.set(belt.get() + 1)
	fnUpdCollection()

### Item Canvas Setup
# Head Canvas
HeadText = tk.Label(root, text = "Head", font = ("helvetica", 12), width = 7, bg = config["Slots"]["head_c"], fg = config["Slots"]["head_t"])
HeadLabel = tk.Label(root, textvariable = head, font = ('helvetica', 12, "bold"))
MinusHead = tk.Button(root, text = "-", command = fnHeadMinus)
MinusHead.pack()
PlusHead = tk.Button(root, text = "+", command = fnHeadPlus)
PlusHead.pack()
canvas.create_window(120, 100, window = HeadText)
canvas.create_window(119, 127, window = HeadLabel)
canvas.create_window(100, 127, window = MinusHead)
canvas.create_window(140, 127, window = PlusHead)

# Chest Canvas
ChstText = tk.Label(root, text = "Chest", font = ("helvetica", 12), width = 7, bg = config["Slots"]["chst_c"], fg = config["Slots"]["chst_t"])
ChstLabel = tk.Label(root, textvariable = chst, font = ('helvetica', 12, "bold"))
MinusChst = tk.Button(root, text = "-", command = fnChstMinus)
MinusChst.pack()
PlusChst = tk.Button(root, text = "+", command = fnChstPlus)
PlusChst.pack()
canvas.create_window(120, 155, window = ChstText)
canvas.create_window(119, 182, window = ChstLabel)
canvas.create_window(100, 182, window = MinusChst)
canvas.create_window(140, 182, window = PlusChst)

# Weapon Canvas
WeapText = tk.Label(root, text = "Weapons", font = ("helvetica", 12), width = 8, bg = config["Slots"]["weap_c"], fg = config["Slots"]["weap_t"])
WeapLabel = tk.Label(root, textvariable = weap, font = ('helvetica', 12, "bold"))
MinusWeap = tk.Button(root, text = "-", command = fnWeapMinus)
MinusWeap.pack()
MinusWeap2 = tk.Button(root, text = "--", command = fnWeapMinus2)
MinusWeap2.pack()
PlusWeap = tk.Button(root, text = "+", command = fnWeapPlus)
PlusWeap.pack()
PlusWeap2 = tk.Button(root, text = "++", command = fnWeapPlus2)
PlusWeap2.pack()
canvas.create_window(80, 45, window = WeapText)
canvas.create_window(79, 72, window = WeapLabel)
canvas.create_window(60, 72, window = MinusWeap)
canvas.create_window(40, 72, window = MinusWeap2)
canvas.create_window(100, 72, window = PlusWeap)
canvas.create_window(124, 72, window = PlusWeap2)

# Hands Canvas
HandText = tk.Label(root, text = "Hands", font = ("helvetica", 12), width = 7, bg = config["Slots"]["hand_c"], fg = config["Slots"]["hand_t"])
HandLabel = tk.Label(root, textvariable = hand, font = ('helvetica', 12, "bold"))
MinusHand = tk.Button(root, text = "-", command = fnHandMinus)
MinusHand.pack()
PlusHand = tk.Button(root, text = "+", command = fnHandPlus)
PlusHand.pack()
canvas.create_window(40, 100, window = HandText)
canvas.create_window(39, 127, window = HandLabel)
canvas.create_window(20, 127, window = MinusHand)
canvas.create_window(60, 127, window = PlusHand)

# Feet Canvas
FeetText = tk.Label(root, text = "Feet", font = ("helvetica", 12), width = 7, bg = config["Slots"]["feet_c"], fg = config["Slots"]["feet_t"])
FeetLabel = tk.Label(root, textvariable = feet, font = ('helvetica', 12, "bold"))
MinusFeet = tk.Button(root, text = "-", command = fnFeetMinus)
MinusFeet.pack()
PlusFeet = tk.Button(root, text = "+", command = fnFeetPlus)
PlusFeet.pack()
canvas.create_window(40, 155, window = FeetText)
canvas.create_window(39, 182, window = FeetLabel)
canvas.create_window(20, 182, window = MinusFeet)
canvas.create_window(60, 182, window = PlusFeet)

# Amulet Canvas
AmulText = tk.Label(root, text = "Amulet", font = ("helvetica", 12), width = 7, bg = config["Slots"]["amul_c"], fg = config["Slots"]["amul_t"])
AmulLabel = tk.Label(root, textvariable = amul, font = ('helvetica', 12, "bold"))
MinusAmul = tk.Button(root, text = "-", command = fnAmulMinus)
MinusAmul.pack()
PlusAmul = tk.Button(root, text = "+", command = fnAmulPlus)
PlusAmul.pack()
canvas.create_window(200, 45, window = AmulText)
canvas.create_window(199, 72, window = AmulLabel)
canvas.create_window(180, 72, window = MinusAmul)
canvas.create_window(220, 72, window = PlusAmul)

# Ring Canvas
RingText = tk.Label(root, text = "Rings", font = ("helvetica", 12), width = 7, bg = config["Slots"]["ring_c"], fg = config["Slots"]["ring_t"])
RingLabel = tk.Label(root, textvariable = ring, font = ('helvetica', 12, "bold"))
MinusRing = tk.Button(root, text = "-", command = fnRingMinus)
MinusRing.pack()
PlusRing = tk.Button(root, text = "+", command = fnRingPlus)
PlusRing.pack()
canvas.create_window(200, 100, window = RingText)
canvas.create_window(199, 127, window = RingLabel)
canvas.create_window(180, 127, window = MinusRing)
canvas.create_window(220, 127, window = PlusRing)

# Belt Canvas
BeltText = tk.Label(root, text = "Belt", font = ("helvetica", 12), width = 7, bg = config["Slots"]["belt_c"], fg = config["Slots"]["belt_t"])
BeltLabel = tk.Label(root, textvariable =  belt, font = ('helvetica', 12, "bold"))
MinusBelt = tk.Button(root, text = "-", command = fnBeltMinus)
MinusBelt.pack()
PlusBelt = tk.Button(root, text = "+", command = fnBeltPlus)
PlusBelt.pack()
canvas.create_window(200, 155, window = BeltText)
canvas.create_window(199, 182, window = BeltLabel)
canvas.create_window(180, 182, window = MinusBelt)
canvas.create_window(220, 182, window = PlusBelt)

### Saving changes on program exit
def fnSaveItems():
	f = open("settings.ini", "w+")
	config.set("SavedVars", "sets", str(sets.get()))
	config.set("SavedVars", "head", str(head.get()))
	config.set("SavedVars", "chst", str(chst.get()))
	config.set("SavedVars", "weap", str(weap.get()))
	config.set("SavedVars", "hand", str(hand.get()))
	config.set("SavedVars", "feet", str(feet.get()))
	config.set("SavedVars", "amul", str(amul.get()))
	config.set("SavedVars", "ring", str(ring.get()))
	config.set("SavedVars", "belt", str(belt.get()))
	config.write(f)
	f.close()
	root.destroy()

### Starting program
fnUpdCollection()

root.protocol("WM_DELETE_WINDOW", fnSaveItems)

root.mainloop()