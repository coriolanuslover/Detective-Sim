# Who-Dun-It Game using Lists and Loops
# List suspects and use inputs to assign break and continue functions, narrowing the list each pass
# Final and correct suspect will print good job string
# If wrong, print bad job string
# Design Outline - Plot Mystery Narrative, List Suspects, Design Inputs, Have Dialog print, Move back and forth between dialogs
# TODO- Add plot and dialog, Add Input options for Details Testimony and Solve, Finish Testimonies

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

print("On the night of Tuesday June 21st, Andrew P. MacFadyen was murdered.")
print("Ten people roamed Simp City that night and one of them committed the most heinous of acts")
print("Who killed Andy? As crack detective P.R. Ivateinvestigator, you've been tasked with solving this crime.")
a = input("Enter Details to get started: ")

def options(q):
    if q == "Details":
        print(details)
    else:
        print("Wrong")
options(a)

def murderer(y):
    if y == "Lani":
        print("The murder of Andrew MacFadyen has been solved. Never again shall the evil intellect of Lani Polanco be used to harm another")
        print("Another case closed by P.R. Ivateinvestigator")
    elif y in innocentsuspects:
        print("Another soul off to the dog house. I can't help shake the feeling that " + z + " has taken the fall for someone else. Either way, Case Closed")
    elif y == "Options":
        options(a)
    else:
        print(z + ", a cook at the diner downtown, has been apprehended and is awaiting trial. While they certainly didn't do it, they did however put onions on a burger of mine when I specificaly asked them not to, so fuck 'em. Case Closed.")
z = input("Who is the murderer? ")
murderer(z)