from DLAuto import Auto
import time

duel_count = 10


for i in range (0, duel_count):
    print(f"Duel Count: {i + 1}")
    duel = Auto()
    
    # Modifier is added to skip some event like Capsule Event, etc.
    duel.clickCenterUntilFind("Images/duel_button.png", 0.6, 30, modifier=[300, 0])
    
    duel.clickCenterUntilFind("Images/duel_button.png", 0.8, 20)

    while True:
        print(duel.win)
        if duel.win is True:
            break

        print("Checking main phase...")
        duel.clickCenterUntilFind("Images/main_phase.png", 0.7, 50)

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

    # Modifier is added to prevent level up pop up
    duel.clickCenter(6, duration=1, modifier = [0, -500])
    
    print("Next button...")
    duel.clickCenterUntilFind("Images/next_button.png", 0.8, 10)
    print("Next BUtton (2)")
    time.sleep(2)
    duel.clickCenterUntilFind("Images/next_button.png", 0.8, 10)