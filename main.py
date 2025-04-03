from Classes.Duel import Duel
from Classes.Clicker import Clicker
from Classes.Finder import Finder
import time

duel_count = 10
capsule_event = False

clicker = Clicker()

for i in range (0, duel_count):

    duel = Duel()
    clicker.clickCenterUntilFind("Images/duel_button.png", 0.6, 20)
    clicker.clickCenterUntilFind("Images/duel_button.png", 0.8, 10)

    while True:
        print(duel.win)
        if duel.win is True:
            break

        print("Checking main phase...")
        clicker.clickCenterUntilFind("Images/main_phase.png", 0.7, 50)

        print("Summoning")
        duel.summon()

        time.sleep(1)

        if duel.firstTurnCheck() is True:
            duel.toEndPhase()
            continue

        time.sleep(2)

        print("To battle phase")
        duel.toBattlePhase()

        print("Attacking..")
        if duel.attack() is True:
            continue

        print("WINCHECK...")
        if duel.winCheck() is True:
            continue

        print("End Phase")
        duel.toEndPhase()
        
        print("WINCHECK...")
        duel.winCheck()

    clicker.clickCenter(6, duration=1, modifier = [0, 500])
    print("Next button...")
    clicker.clickCenterUntilFind("Images/next_button.png", 0.8, 10)
    print("Next BUtton (2)")
    time.sleep(2)
    clicker.clickCenterUntilFind("Images/next_button.png", 0.8, 10)
    if capsule_event is True:
        clicker.clickCenterUntilFind("Images/ok_button.png", 0.6, 20)