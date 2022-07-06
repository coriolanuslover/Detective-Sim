# Who-Dun-It Game using Lists and Loops
# List suspects and use inputs to assign break and continue functions, narrowing the list each pass
# Final and correct suspect will print good job string
# If wrong, print bad job string
# Design Outline - Plot Mystery Narrative, List Suspects, Design Inputs, Have Dialog print, Move back and forth between dialogs
# TODO- Add plot and dialog, Add Input options for Details Testimony and Solve, Finish Testimonies

from AndyThing import *

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

harbt = """I had gotten some based quaaludes from my pog cousin and gave to two to everyone.
Andrew didn't want any at first but eventually put them in their pocket. I had taken mine and fell asleep
on the couch a little after I gave Andrew his. I don't know if he ever actually took them or not.
I woke back up when Raija came back and told us about finding Andrew after Wednesday had...
After Wednesday had...   Damn that dog!!!
"""

redt = """Harb came in with some methaqualone, which I didn't think you could get anymore and started handing them out to everyone. 
Very sweet. Harb took theirs and passed out on the couch. I only took one of the two and was very mellowed so I just stayed 
on the couch and watched [REDACTED], my favorite anime ever. A bit into it, Raija came in and asked if Wednesday was around. 
I think I saw someone let her out but I can't be sure as [REDACTED] was simply too interesting. I saw Raija go outside for a bit 
and very shortly after she came back in. She started to tell us, extremely panicked, abot what she saw. I still can't believe it.
"""
## Missing During Incident, Death Threats Towards Andy, In Truck Smoking During Incident
robt = """I swear on my dead father Robby Ott former youth pastor and man of God that I did not kill Andrew.
Sure I said I'd kill him tonight. Sure I said, in writing, that I'd kill him tonight. And in typewriter. And in text message.
And with a week's notice. But I didn't do it! I was just being sweet! I got my ludes from Harb and went to my truck to smoke! 
Then all that bullshit inside happened and I wasn't anywhere near it! Ask Blake. He left early and saw me in the truck!"""

## Witness Blake Wash Dishes, Notice Lani Come Downstairs
shilpat = """I get off from my job where I save lives daily and Andrew has to make the night all about him. Harbin passed out quaaludes, 
Blake put all the dishes in the washer, Lani hung around for a little while.
Everything was fine until Andrew wanted to get away from the noise and go out into the shed. He must have taken more than his share 
of quaaludes. I know I saw some on the counter that disappeared. And then I saw some residue in a glass Andrew was drinking out of.
Not sure why he didn't take them normally like the rest of the group. Anyways, we're all in the living room when Raija comes back in
and then it all went to shit"""

## Washes Dishes Thus Empty Sink, Hangs In Living Room, Leaves Early, Witness Rob In Truck
blaket = """(Blake Cameron could not be reached for questioning however a note with his testimony
was left at his residence) Dear Coppers, I did not do it. I wasn't even there to do it, I didn't even know
it happened until Raija called and told me. But by then I was already at my house packing. I popped in. 
Popped some ludes. Did the literally all the dishes thank you very much. Then left because I was 
over stimmied. Rob saw me leave ask them. Off to Bolivia for a bit don't wait up. GN. Disregards, Blake."""

## Witness Lani Washing Hands And Go Back Upstairs. And Clean Knife In Sink. Witness Raija Make Kong. Goes in Living Room
savt = """Can't believe that Wednesday would devour Andrew's neck like that. I suppose even Wednesday became tired of his
antics. I didn't see it personally but Raija came in and told us what had happened. Everything was going so normally.
Most everyone was downstairs watching some horrific anime Red put on. I had stepped into the kitchen as it was a little
overwhelming. I saw Lani doing some dishes and decided to talk to her. She said she just ate and was about to go back upstairs.
I stayed in there for a bit longer before Raija came in to fix Wednesday her kong. Only a minute later did she come back in
with the news of what had happened."""

## Got knife out of sink to prep Kong with, Left Ludes somewhere, Finds Andrew
raijat = """I think Andrew got what was coming to him. All of those special little questions finally caught up to the 
bastard. Last thing I did before I found him was make Wednesday's kong for her. I got a knife out of the sink as usual
but I noticed Wednesday's peanut butter had less in it than I remember. Either way I prepped the kong and called for her.
I went into the living room anf asked if anyone had seen her and Red told they thought she was outside. I go outside and
I see the shed door open. I figured Wednesday had gotten in there somehow. I walk in and there they were. Eater and Eatee
I went back inside immediately and told everyone what I saw."""

## Comes Downstairs To Make Food. Washes Dishes And Outs In Sink. Heads Back Upstairs.
lanit = """Since everyone was doing qualuudes I decided that tonight wasn't really my scene. I went to my room and did 
Lani Stuff TM. I got hungry so I went downstairs and made myself a sandwich. As I was washing the dishes I used Sav
popped in to talk to me before I went back upstairs. A bit later I noticed some commotion downstairs and went to see
what was going on. And that's when I learned Rob was my new landlord."""

print_out("On the night of Tuesday June 21st, Andrew P. MacFadyen was murdered.")
print()
print_out("Ten people roamed Simp City that night and one of them committed the most heinous of acts")
print()
print_out("Who killed Andy? As crack detective P.R. Ivateinvestigator, you've been tasked with solving this crime.")
print()
print_out("Enter Details or Testimonies to get started: ")
a = input()

def options(q):
    if q == "Details":
        print_out(details)
    elif q == "Testimonies":
        print_out("Whose testimony would you like to hear? ")
        fbnj = input()
        def testimonies(sub):
            if sub == "Harb":
                print_out(harbt)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Red":
                print_out(redt)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Shilpa":
                print_out(shilpat)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Blake":
                print_out(blaket)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Sav":
                print_out(savt)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Raija":
                print_out(raijat)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Lani":
                print_out(lanit)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Rob":
                print_out(robt)
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
            elif sub == "Done":
                print("DONE")
            else:
                print("Try Again")
                print_out("\nWhose testimony would you like to hear? ")
                fbjn = input()
                testimonies(fbjn)
        testimonies(fbnj)
    else:
        print_out("Wrong")
options(a)

def murderer(y):
    if y == "Lani":
        print_out("The murder of Andrew MacFadyen has been solved. Never again shall the evil intellect of Lani Polanco be used to harm another")
        print()
        print_out("Another case closed by P.R. Ivateinvestigator")
    elif y in innocentsuspects:
        print_out("Another soul off to the dog house. I can't help shake the feeling that " + z + " has taken the fall for someone else. Either way, Case Closed")
    elif y == "Options":
        options(a)
    else:
        print_out(z + ", a cook at the diner downtown, has been apprehended and is awaiting trial. While they certainly didn't do it, they did however put onions on a burger of mine when I specificaly asked them not to, so fuck 'em. Case Closed.")
print_out("Who is the murderer? ")
z = input()
murderer(z)