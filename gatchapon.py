#!/usr/bin/env python
import sys
from playsound import playsound
import pandas as pd
import textwrap

# initializes the items and description DataFrames, along with his voice
items = pd.read_csv('data/items.csv')
items = items.drop(columns='Description')
descriptions = pd.read_csv('data/descriptions.csv')
descriptions = descriptions.drop(columns='Repeatable?')

# wow how pretty
print('                                                                                    ')
print('                              Welcome to Fantasy Gatchapon Systems!                        ')
print("                                 I'm Figis, twist my shoulder!")
print('                                                                                    ')
print('                   Oh please, oh please! I do love it so when people do that')
print('                                                                                    ')
print('                                           @@@@@@@                                  ')
print('                                       @@@@@     @@@@@                              ')
print('                                     @@@@           @@@@                            ')
print('                                    @@                 @@                           ')
print('                                   @@                   @@                          ')
print('                                   @@                   @@                          ')
print('                                    @@                 @@                           ')
print('                                     @@               @@                            ')
print('                                       @@            @@                             ')
print('                                         @@@      @@@                               ')
print('                                            @@@@@@              ___                 ')
print('                                            @    @             /   \                ')
print('                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@  \   /                ')
print('                                 @@   ____          ____   @@   | |                 ')
print('                                 @@  |   x|        |x   |  @@   | |                 ')
print('                                 @@                        @@   | |                 ')
print('                                 @@      /@@@@@@@@@@\      @@   | |                 ')
print('                                 @@      @   ____   @      @@___| |_                ')
print('                                 @@      @          @      @@_______|               ')
print('                                 @@      @  |____|  @      @@_______|               ')
print('                                 @@      @          @      @@                       ')
print('                                 @@      \@@@@@@@@@@/      @@                       ')
print('                                 @@                        @@                       ')
print('                                 @@@@@@@@@    | |   @@@@@@@@@                       ')
print('                                  @@@@@@@@@@@@@@@@@@@@@@@@@@                        ')
print('                                                                                    ')
print('                                         Insert a coin?                             ')
print('                                           yes / no')
print('------------------------------------------------------------------------------------------------------')
playsound("sounds/figisintro.wav")

# I am bad at using input()
yes = 'yes'
Yes = 'yes'
no = 'no'
No = 'no'
try:
    choice = str(input())

    if choice == 'yes':
        print('------------------------------------------------------------------------------------------------------')
        print('Figis: Oh wait, what class are you again? (Example: I am Figis and my class is a: "Robot")')
        print('------------------------------------------------------------------------------------------------------')
        playsound("sounds/figisclass.wav")

        # Oh yea still bad at it
        Fighter = 'Fighter'
        Bard = 'Bard'
        Cleric = 'Cleric'
        Druid = 'Druid'
        Monk = 'Monk'
        Paladain = 'Paladin'
        Ranger = 'Ranger'
        Rogue = 'Rogue'
        Sorcerer = 'Sorcerer'
        Warlock = 'Warlock'
        Wizard = 'Wizard'

        try:
            random_class = input("Enter class: ")

            # selects the class and grabs a random item from the correct classes table
            if random_class:
                random_item_df = items[items['Class'].str.contains(random_class) == True]
                random_item = random_item_df.sample(n=1)
                random_item_name = random_item['Item'].item()
            else:
                random_class = items['Class'].sample(n=1).item()
                random_item_name = items['Class'] == random_class
                random_item_df = items[random_item_name]
                random_item = random_item_df.sample(n=1)
                random_item_name = random_item['Item'].item()

        except:
            print('------------------------------------------------------------------------------------------------------')
            print('You probably entered your class in wrong. You fat fingered troll!')
            print('------------------------------------------------------------------------------------------------------')
            playsound("sounds/figiswrong1.wav")
            sys.exit(1)

        # selecting the various features of the randomly chosen item
        find_item = descriptions['Name'] == random_item_name
        item = descriptions[find_item].drop(columns='Class')
        item_type = item['Type'].item()
        item_name = item['Name'].item()
        pill_shape = item['Pill Shape'].item()
        item_size = item['Size'].item()
        item_description = item['Description'].item()
        disclaimer = "Disclaimer: Joanne's Fantasy Gambling Systems" + u"\u2122" + " is not responsible if the Fantasy Gatchapon System (FGS) fails to produce a complete rhyme everytime."

        print('------------------------------------------------------------------------------------------------------')
        print('                      Figis:  With a thunk and a spin of the top             ')
        print('                              Out comes a ' + pill_shape + ' pill with a plop')
        print('                              Its quite ' + item_size + ' in size            ')
        print('                              And much to your surprise!                     ')
        print("                              Congradlation, its an 'ol                      ")
        print('------------------------------------------------------------------------------------------------------')
        print('Item name: ' + item_name + '                               ')
        print('------------------------------------------------------------------------------------------------------')
        print('This ' + item_type +  ' is a...')
        print('\n'.join(textwrap.wrap(item_description, 100, break_long_words=False)))
        print('')
        print('')
        print('')
        print('\n'.join(textwrap.wrap(disclaimer, 100, break_long_words=False)))
        playsound("sounds/figisfin.wav")

    else:
        print('------------------------------------------------------------------------------------------------------')
        print("Figis: Huh, probably don't even have any coins, do you? Buzz off!")
        print('------------------------------------------------------------------------------------------------------')
        playsound("sounds/figisbuzz.wav")
        sys.exit(1)
except:
    print('------------------------------------------------------------------------------------------------------')
    print("Siiiigh, lets try that again one more time shall we?")
    playsound("sounds/figissigh.wav")
    sys.exit(1)

