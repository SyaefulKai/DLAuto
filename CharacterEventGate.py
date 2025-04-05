from DLAuto import Auto
import time

def run():
    count = 15

    for i in range(0, count):
        duel = Auto()
        duel.clickCenterUntilFind("Images/duel_button.png", 0.6, 20, modifier=[300, 0])
        duel.clickCenterUntilFind("Images/auto_duel.png")
        duel.clickCenterUntilFind("Images/ok_button.png", 0.7, 100)
        print("Next button...")
        duel.clickCenterUntilFind("Images/next_button.png", 0.8, 10)
        time.sleep(2)
        print("Next BUtton (2)")
        duel.clickCenterUntilFind("Images/next_button.png", 0.8, 10)
