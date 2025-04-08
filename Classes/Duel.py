import pyautogui as gui
from Classes.Finder import Finder
import time
from Classes.Clicker import Clicker
from pynput import keyboard

class Duel(Clicker, Finder):

    def __init__(self):
        super().__init__()
        self.monster_count = 0
        
        # Based on 1920x1080
        self.main_monster_zone = [[836, 610], [961, 609], [1084, 610]]
        
        # self.opponent_monster_zone = [[842, 375], [958, 379], [1076, 382]]
        self.first_card_selection_coordinate = [703, 849]
        
        self.is_first_turn = False
        
        self.win = False
        
        # Adjust the duration of the clicks
        self.global_duration = 0.5
        
    def dinamic_coor(self):
        width = self.screenSize.width()
        height = self.screenSize.height()
        base_width = 1920
        base_height = 1080

        self.main_monster_zone = [
            [int(x / base_width * width), int(y / base_height * height)]
            for x, y in self.main_monster_zone
        ]
        
        x, y = self.first_card_selection_coordinate
        self.first_card_selection_coordinate = [
            int(x / base_width * width),
            int(y / base_height * height)
        ]

    def attack(self):
        """Attack the opponent's monster and check for win condition."""
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
            
            # Check ok button to confirm the win
            if self.clickCenterUntilFind("Images/ok_button.png", max_attempt=5) is not None:
                self.win = True
                return True

    def summon(self):
        """Summon a monster to the field."""
        if self.monster_count > 2:
            return
        
        # Click on the summon button and select the monster
        rect = self.getWindow().rectangle()
        # Click on the bottom of the screen to choose the monster
        gui.click([(rect.width() // 2) - 10, rect.height() - 75], duration=self.global_duration)
        
        while True:
            x = self.find("Images/normal_summon.png", 0.6)
            if x is not None:
                gui.click(x)
                break
            
        gui.click(self.main_monster_zone[self.monster_count], duration=self.global_duration)
        self.monster_count += 1

    def toBattlePhase(self):
        """Change the phase to Battle Phase."""
        gui.click(self.find("Images/change_phase.png", 0.7), duration=self.global_duration)
        gui.click(self.find("Images/battle_phase_button.png"), duration=self.global_duration)
        time.sleep(2)

    def toEndPhase(self):
        """Change the phase to End Phase."""
        gui.click(self.find("Images/change_phase.png", 0.7), duration=self.global_duration)
        gui.click(self.find("Images/end_phase_button.png"), duration=self.global_duration)

    def winCheck(self):
        """Check if the win condition is met."""
        check = self.clickCenterUntilFind("Images/ok_button.png", 0.8, 7)
        if check is not None:
            self.win = True
            return True

    def firstTurnCheck(self):
        """Check if it's the first turn."""
        if self.find("Images/first_turn.png") is not None:
            return True