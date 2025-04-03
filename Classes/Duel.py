import pyautogui as gui
from Classes.Finder import Finder
import time
from Classes.Clicker import Clicker

class Duel(Clicker, Finder):

    monster_count = 0

    main_monster_zone = [[836, 610], [961, 609], [1084, 610]]
    opponent_monster_zone = [[842, 375], [958, 379], [1076, 382]]
    first_card_selection_coordinate = [703, 849]

    is_first_turn = False

    win = False

    global_duration = 0.5

    def attack(self):
        for i in range(0, self.monster_count):
            time.sleep(1)
            gui.click(self.main_monster_zone[i], duration=self.global_duration)
            time.sleep(1)
            gui.click(self.find("Images/battle_button.png", 0.6), duration=self.global_duration)
            time.sleep(1)
            gui.click(self.first_card_selection_coordinate)
            time.sleep(1)
            gui.click(self.find("Images/confirm_button.png"), duration=self.global_duration)
            time.sleep(1)
            if self.clickCenterUntilFind("Images/ok_button.png", max_attempt=5) is not None:
                self.win = True
                return True

    def summon(self):
        if self.monster_count > 2:
            return
        rect = self.getWindow().rectangle()
        gui.click([(rect.width() // 2) - 10, rect.height() - 75], duration=self.global_duration)
        gui.click(self.find("Images/normal_summon.png", 0.6), duration=self.global_duration)
        gui.click(self.main_monster_zone[self.monster_count], duration=self.global_duration)
        self.monster_count += 1

    def toBattlePhase(self):
        gui.click(self.find("Images/change_phase.png", 0.7), duration=self.global_duration)
        gui.click(self.find("Images/battle_phase_button.png"), duration=self.global_duration)
        time.sleep(2)

    def toEndPhase(self):
        gui.click(self.find("Images/change_phase.png", 0.7), duration=self.global_duration)
        gui.click(self.find("Images/end_phase_button.png"), duration=self.global_duration)

    def winCheck(self):
        check = self.clickCenterUntilFind("Images/ok_button.png", 0.8, 7)
        if check is not None:
            self.win = True
            return True
        
    def firstTurnCheck(self):
        if self.find("Images/first_turn.png") is not None:
            return True