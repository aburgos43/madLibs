import random

def monkeyKingMadLib():
    print("Monkey King Mad Lib")
    monkeyBlanks = {
    'blank1' : input("Give me a verb: "),'blank2' : input("Give me some plural for body parts: "),'blank3' : input("Give me some sense of the body: "),'blank4' : input("Give me a paste tense verb: "),
    'blank5' : input("Give me the name of a fruit: "),'blank6' : input("Give me an amount of time: "),'blank7' :input("Give me a sort of push force, in its past tense: ") ,'blank8' : input("Give me the name of a teacher: "),
    'blank9' :input("Give me some athletic equipment: ") ,'blank10' : input("Give me a noun: "),'blank11' : input("Give me an adjective: "),'blank12' : input("Give me an adverb: ")
    }


    print("The day I saw the Monkey King %r. It was one of the most interesting days of the year. I cannot believe my %r. I had the %r running through my body for over a week." % (monkeyBlanks['blank1'], monkeyBlanks['blank2'], monkeyBlanks['blank3'] ))

    print("The Monkey King %r one of the largest %r I had seen in %r. The funniest thing was when he %r %r in a huge pile of %r" % (monkeyBlanks['blank4'], monkeyBlanks['blank5'], monkeyBlanks['blank6'], monkeyBlanks['blank7'], monkeyBlanks['blank8'], monkeyBlanks['blank9']))

    print("After he did that, the king played chess on his brother's %r and then combed his %r hair with a comb made out of old fish bones." % (monkeyBlanks['blank10'], monkeyBlanks['blank11']))

    print("Later, that same day, I saw the Monkey King dance %r in front of an audience of kangaroos and wombats." % (monkeyBlanks['blank12']))

def bikeRidingMadLib():
    print("Bike Riding Mad Lib")


    bikeBlanks = {
    'blank1' : input("Give me a verb that ends in ing: "),'blank2' : input("Give me an adjective: "),'blank3' : input("Give me a verb that ends in ing: "),'blank4' : input("Give me a part of the body: "),
    'blank5' : input("Give me an adverb: "),'blank6' : input("Give me a part of the body: "),'blank7' :input("Give me a plural noun: ") ,'blank8' : input("Give me a verb: "),
    'blank9' :input("Give me a plural noun for an animal (flamingos): ") ,'blank10' : input("Give me a noun: "),'blank11' : input("Give me a verb: "),'blank12' : input("Give me an adjective: "), 'blank13' :input("Give me a color: ")
    }

    print("%r is a/an %r form of exercise." % (bikeBlanks['blank1'], bikeBlanks['blank2']))
    print("%r a bicycle enables you to develop your %r muscles as well as %r" % (bikeBlanks['blank3'], bikeBlanks['blank4'], bikeBlanks['blank5']))
    print(" increase the rate of your %r beat. More %r" % (bikeBlanks['blank6'], bikeBlanks['blank7']))
    print(" around the world %r bicycles than drive %r. No matter what kind of %r" % (bikeBlanks['blank8'], bikeBlanks['blank9'], bikeBlanks['blank10']))
    print(" you %r, always be sure to wear a/an %r helmet. Make sure to have %r reflectors too!" % (bikeBlanks['blank11'], bikeBlanks['blank12'], bikeBlanks['blank13'], ))

def valentinesMadLib():
    print("Valentines Mad Lib")

    valentineBlanks = {
    'blank1' : input("Give me a noun: "),'blank2' : input("Give me an ing verb: "),'blank3' : input("Give me a noun: "),'blank4' : input("Give me an adjective: "),
    'blank5' : input("Give me a noun: "),'blank6' : input("Give me a noun: "),'blank7' :input("Give me an emotion: ") ,'blank8' : input("Give me an action: "),
    'blank9' :input("Give me a noun: ") ,'blank10' : input("Give me a noun: "),'blank11' : input("Give me the name of a friend: "),'blank12' : input("Give me the name of the friend again: "), 'blank13' :input("Give me a noun: ") }

    print("One Valentine's %r, I was %r when I looked in my %r " % (valentineBlanks['blank1'], valentineBlanks['blank2'], valentineBlanks['blank3']))
    print("and saw a %r %r! It said, 'Will you be my %r?'"% (valentineBlanks['blank4'], valentineBlanks['blank5'], valentineBlanks['blank6']))
    print("I was so %r! I %r to see who it was from , but there was no %r. " %(valentineBlanks['blank7'], valentineBlanks['blank8'], valentineBlanks['blank9']))
    print("So, at %r, I asked for clues, but %r didn't know about it. Finally, someone told me that %r gave me the %r." %(valentineBlanks['blank10'], valentineBlanks['blank11'], valentineBlanks['blank12'], valentineBlanks['blank13']))

def excusedMadLib():
    print("Excused Mad Lib")

    exBlanks = {'blank1' : input("Give me a date: "),'blank2' : input("Give me a name: "),'blank3' : input("Give me an adjective: "),'blank4' : input("Give me a noun: "),
    'blank5' : input("Give me a name: ")}

    print("Date: %r" % (exBlanks['blank1']))
    print("Please excuse %r who is far too %r to attend %r class." % (exBlanks['blank2'], exBlanks['blank3'], exBlanks['blank4']))
    print("Signed: %r" %(exBlanks['blank5']))

def sickExcuseMadLib():
    sickBlanks = {
    'blank1' : input("Give me a date: "), 'blank2' : input("Give me a name: "), 'blank3' : input("Give me a part of the body: "),
    'blank4' : input("Give me a type of liquid: "), 'blank5' : input("Give me a substance: "), 'blank6' : input("Give me a name: ")
    }
    print("Date: %r" % sickBlanks['blank1'])
    print("%r is sick with the %r flu. Drink more %r and take %r as needed." % (sickBlanks['blank2'], sickBlanks['blank3'], sickBlanks['blank4'], sickBlanks['blank5']))
    print("Signed: %r" % (sickBlanks['blank6']))

def hallPassMadLib():
    print("Hallpass Mad Lib")
    hallBlanks = {
    'blank1' : input("Give me a date: "), 'blank2' : input("Give me a name: "), 'blank3' : input("Give me a place: "),
    'blank4' : input("Give me a noun: "), 'blank5' : input("Give me a name: ")
    }

    print("Date: %r" % (hallBlanks['blank1']))
    print("%r is authorized to be at %r instead of %r class." % (hallBlanks['blank2'], hallBlanks['blank3'], hallBlanks['blank4']))
    print("Signed: %r" % (hallBlanks['blank5']))

def coolHallPassMadLib():
    print("Cool Hallpass Mad Lib ")
    coolBlanks = {
    'blank1' : input("Give me a date: "), 'blank2' : input("Give me a name: "), 'blank3' : input("Give me a noun: "),
    'blank4' : input("Give me a event: "), 'blank5' : input("Give me a name: ")
    }

    print("Date: %r" % (coolBlanks['blank1']))
    print("%r is too cool for %r class. Instead, she/he will be attending the %r class." %(coolBlanks['blank2'], coolBlanks['blank3'], coolBlanks['blank4']))
    print("Signed: %r" % (coolBlanks['blank5']))

def FFWinterMadLib():
    print("Fun Facts about Winter Mad Lib")

    FFblanks = {
    'blank1' : input("Give me a number: "),'blank2' : input("Give me an adjective: "),'blank3' : input("Give me a noun: "),'blank4' : input("Give me a noun: "),
    'blank5' : input("Give me a noun: "),'blank6' : input("Give me an adjective: "),'blank7' :input("Give me a noun: ") ,'blank8' : input("Give me an ing verb: "),
    'blank9' :input("Give me an ing verb: ") ,'blank10' : input("Give me an ing verb: "),'blank11' : input("Give me a beverage: "),'blank12' : input("Give me a food: ")
    }


    print("Winter is one of %r seasons of the year. The other seasons are %r, %r, and %r." % (FFblanks['blank1'], FFblanks['blank2'], FFblanks['blank3'], FFblanks['blank4']))
    print("Winter is the time of year when the %r is furthest from earth. The weather tends to be %r in winter, with %r fall and cold temperatures." %(FFblanks['blank5'], FFblanks['blank6'], FFblanks['blank7']))
    print("Some winter sports include %r, %r, and %r . Hot %r with %r on top is a popular winter drink." % (FFblanks['blank8'], FFblanks['blank9'], FFblanks['blank10'], FFblanks['blank11'], FFblanks['blank12']))

def LunchRoomMadLib():
    print("Lunch Room Mad Lib")

    lunchBlanks = {
    'blank1' : input("Give me a container: "),'blank2' : input("Give me an adjective: "),'blank3' : input("Give me an adjective: "),'blank4' : input("Give me a noun: "),
    'blank5' : input("Give me an animal: "),'blank6' : input("Give me a vegetable: "),'blank7' :input("Give me a vegetable: ") ,'blank8' : input("Give me a color: "),
    'blank9' :input("Give me an adjective: ")
    }


    print("Make sure your unch %r is filled with nutritious %r food." % (lunchBlanks['blank1'], lunchBlanks['blank2']))
    print("Do not go to the %r food stand across the street from school." % (lunchBlanks['blank3']))
    print("The hamburgers they serve are fried in %r and are made of %r meat." %(lunchBlanks['blank4'], lunchBlanks['blank5']))
    print("So take a sandwich made of %r or %r, it's much healthier! Drink %r milk instead of %r colas." % (lunchBlanks['blank6'], lunchBlanks['blank7'], lunchBlanks['blank8'], lunchBlanks['blank9']))

def ParkTripMadLib():
    print("Trip to the Park! Mad Lib")

    parkBlanks = {
    'blank1' : input("Give me a person: "),'blank2' : input("Give me an adjective: "),'blank3' : input("Give me an adjective: "),'blank4' : input("Give me a noun: "),
    'blank5' : input("Give me an adjective: "),'blank6' : input("Give me a noun: "),'blank7' :input("Give me an adjective: ") ,'blank8' : input("Give me an adjective: "),
    'blank9' :input("Give me a verb: ") ,'blank10' : input("Give me a verb: "),'blank11' : input("Give me a person: "),'blank12' : input("Give me a verb: "),
    'blank13' :input("Give me an adjective: "), 'blank14' : input("Give me a verb: ")
    }

    print("Yesterday, %r and I went to the park. On our way to the %r park, we saw a %r %r on a bike." % (parkBlanks['blank1'], parkBlanks['blank2'], parkBlanks['blank3'], parkBlanks['blank4']))
    print("We also saw big %r balloons tied to a %r." % (parkBlanks['blank5'], parkBlanks['blank6']))
    print("Once we got to the %r park, the sky turned %r. It started to %r and %r." % (parkBlanks['blank7'], parkBlanks['blank8'], parkBlanks['blank9'], parkBlanks['blank10']))
    print("%r and I %r all the way home. Tomorrow, we will go to the %r park again and hope it doesn't %r." % (parkBlanks['blank11'], parkBlanks['blank12'], parkBlanks['blank13'], parkBlanks['blank14']))

madLibList = [ParkTripMadLib, LunchRoomMadLib, FFWinterMadLib, coolHallPassMadLib, hallPassMadLib,
sickExcuseMadLib, excusedMadLib, valentinesMadLib, bikeRidingMadLib, monkeyKingMadLib]

madLibChoice = random.choice(madLibList)()
