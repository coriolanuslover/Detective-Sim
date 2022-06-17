# Who-Dun-It Game using Lists and Loops
# List suspects and use inputs to assign break and continue functions, narrowing the list each pass
# Final and correct suspect will print good job string
# If wrong, print bad job string
# Design Outline - Plot Mystery Narrative, List Suspects, Design Inputs, Have Dialog print, Move back and forth between dialogs
# TODO- Add plot and dialog, Add Input options for Details Testimony and Solve

suspects = ["Red", "Blake", "Harbin", "Rob", "Raija", "Sav", "Lani", "Shilpa"]

innocentsuspects = ["Red", "Blake", "Harbin", "Rob", "Raija", "Sav", "Shilpa"]

details = """Andrew MacFadyen was found dead on Tuesday June 21st. Cause Of Death: Blood Loss. 
Cause Of Cause Of Death: A dog, AKA Wednesday, ate the neck and carotid artery of Andrew.
The severity of the wound indicates that Wednesday had been eating Andrew for at least a few minutes
before being discovered. No defensive wounds or signs of resistance were found. This was probably on account
of the massive amount of quaaludes, notable sedative used recreationally throughout the 80's, found in Andrew's system.
Regarding Wednesday's state, she was found a bloody mess dripping with gore and anatomical particulate. 
Oddly enough, deep within her mouth, behind the gore, was also a sizable amount of peanut butter. 
"""

Harb = """I had gotten some based quaaludes from my pog cousin and gave to two to everyone.
Andrew didn't want any at first but eventually put them in their pocket. I had taken mine and fell asleep
on the couch a little after I gave Andrew his. I don't know if he ever actually took them or not.
I woke back up when Raija came back and told us about finding Andrew after Wednesday had...
After Wednesday had...   Damn that dog!!!
"""

Red = """Harb came in with some methaqualone, which I didn't think you could get anymore and started handing them out to everyone. 
Very sweet. Harb took there's and passed out onthe couch. I only took one of the two and was very mellowed out so I just stayed 
on the couch and watched [REDACTED], my favorite anime ever. A bit into it, Raija came in and asked if Wednesday was around. 
I think I saw someone let her out but I can't be sure as [REDACTED] was simply too interesting. I saw Raija go outside for a bit 
and very shortly after she came back in. She started to tell us, extremely panicked, abot what she saw. I still can't believe it.
"""
## Missing During Incident, Death Threats Towards Andy, In Truck Smoking During Incident
Rob = """"""

## Witness Blake Wash Dishes, Notice Lani Come Downstairs
Shilpa = """Witness Blake wash dishes, Notice Lani come downstairs"""

## Washes Dishes Thus Empty Sink, Hangs In Living Room, Leaves Early, Witness Rob In Truck
Blake = """Washes dishes thus empty sink. Hangs in living room. Leaves early. Witness Rob in truck"""

## Witness Lani Washing Hands And Go Back Upstairs. And Clean Knife In Sink. Witness Raija Make Kong. Goes in Living Room
Sav = """Witness Lani washing hands and knife in sink. Witness Raija make kong and go outside. Goes in to living room to talk to Red"""

## Comes Downstairs To Make Food. Washes Dishes And Outs In Sink. Heads Back Upstairs.
Lani = """TDB Wait until all testimonies are written"""

print("On the night of Tuesday June 21st, Andrew P. MacFadyen was murdered.")
print("Ten people roamed Simp City that night and one of them committed the most heinous of acts")
print("Who killed Andy? As crack detective P.R. Ivateinvestigator, you've been tasked with solving this crime.")
a = input("Enter Details or Testimony to get started: ")

def options(q):
    if q == "Details":
        print(details)
    else q == "Testimony":

options(a)

def murderer(y):
    if y == "Lani":
        print("The murder of Andrew MacFadyen has been solved. Never again shall the evil intellect of Lani Polanco be used to harm another")
        print("Another case closed by P.R. Ivateinvestigator")
    elif y in innocentsuspects:
        print("Another soul off to the dog house. I can't help shake the feeling that " + z + " has taken the fall for someone else. Either way, Case Clsoed")
    else:
        print(z + ", a cook at the diner downtown, has been apprehended and is awaiting trial. While they certainly didn't do it, they did however put onions on a burger of mine when I specificaly asked them not to, so fuck 'em. Case Closed.")

z = input("Who is the murderer? ")
murderer(z)