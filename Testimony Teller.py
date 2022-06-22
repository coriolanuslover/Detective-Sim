import time, sys

# Put this at the beginning of both files
def print_out(text):
    i = 0
    while i < len(text):
        print(text[i], end="")
        # time is in seconds. This is pretty fast, feel free to adjust
        time.sleep(0.01)
        i += 1
        sys.stdout.flush()

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

fbnj = input("Who's testimony would you like to hear? ")
def testimonies(sub):
    if sub == "Harb":
        print(harbt)
    elif sub == "Red":
        print(redt)
    elif sub == "Shilpa":
        print(shilpat)
    elif sub == "Blake":
        print(blaket)
    elif sub == "Sav":
        print(savt)
    elif sub == "Raija":
        print(raijat)
    elif sub == "Lani":
        print(lanit)
    elif sub == "Rob":
        print(robt)
    else:
        print("Try Again")
testimonies(fbnj)