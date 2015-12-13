__author__ = 'Jo'

from pico2d import *

class Ui:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.firewood_num = 0
        self.attack_num = 0
        self.font = load_font("ConsolaMalgun.TTF", 17)

    def draw(self):
        self.font.draw(self.x - 20, self.y+90, "장작:%d" % self.firewood_num, (1000, 1000, 1000))
        self.font.draw(self.x - 20, self.y+70, "능력:%d" % self.attack_num, (1000, 1000, 1000))


    def update(self, x, y, ability):
        self.x = x
        self.y = y
        self.attack_num = ability
        pass


def test_ui():
    open_canvas()

    ui = Ui()
    for i in range(100):
        clear_canvas()
        ui.score = i
        ui.update(0, 0, 0) # dummy frame time for interfacing to scroll_state
        ui.draw()
        update_canvas()
        delay(0.01)

    delay(2)
    close_canvas()

if __name__ == "__main__":
    test_ui()