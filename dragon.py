import random
import time

def displayIntro():
        print('You are in a land full of dragons. In front of you,')
        print('you see tow caves. In one cave, the dragon is friendly')
        print('and will share his treasure with you. The other dragon')
        print('is greedy and hungry, and will eat you on sight')

def choseCave():
        cave = ''
        while cave != '1' and cave !='2':
                print('Which cave will you go into? (1 or 2)')
                cave = input()

        return cave

def checkCave(chosenCave):
        print('You approach the cave...')
        time.sleep(2)
        print('It is dark and spooky...')
        time.sleep(2)
        print('A large dragon jumps out in front of you! He opens his jows and...')
        print()
        time.sleep(2)

        friendlyCave = random.randint(1, 2)

        if chosenCave == str(friendlyCave):
                print('Give you his treasure!')
                time.sleep(1)
                print('⟢⟣♦♢♢◈♦💍💎💠💍💎💠♢◈♦◈♦♢◈⟣')
        else:
                print('Gobbles you down in one bite')
                time.sleep(1)
                print(
              '''                             ______________
                        ,===:'.,            `-._
                            `:.`---.__         `-._
                     `:.     `--.         `.
                                 ..        `.         `.
                         (,,(,    ..         `.   ____,-`.,
                      (,'     `,   ..   ,--.___`.'
                  ,  ,'  ,--.  `,   ..;'         `
                   `{S, {    .  :    .;
                     I,,'    /  /    ,,
                     ;;    /  ,' ,-,,.    ,---.      ,
                     .;'   /  ,' /  _  . /  _  .   ,'/
                           .   `'  / .  `'  / .  `.' /
                            `.___,'   `.__,'   `.__,'
              ''')
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

        displayIntro()

        caveNumber = choseCave()
        checkCave(caveNumber)
        print('Do you want to play again? (yes or no)')
        playAgain = input()
