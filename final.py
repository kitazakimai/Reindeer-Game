
import pyxel

field_size = 150

class Ball:
    speed = 5

    def __init__(self, img_id):
        self.x = pyxel.rndi(0, 199)
        self.y = 0
        angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)
        self.image_id = img_id #画像の識別子を保持

    def update(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy * Ball.speed


class Pad:
    def __init__(self):
        self.x = field_size / 2
        self.size = field_size / 5

    def catch(self, ball):
        if ball.y >= 195 and self.x - 20 <= ball.x and ball.x <= self.x + 20:
            return True
        else:
            return False

class App:

    def __init__(self):
        pyxel.init(200, 200)
        self.s = 0
        self.fail = 0
        #異なる果物に異なるimg_idを割りてる
        self.balls = [Ball(0), Ball(1)]  # ボールを2個生成し、リストに追加
        self.pad = Pad()

        #画像を読み込む
        pyxel.load("final.py.pyxres")
        # 引数なしでpyxel.run()を呼び出す
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        for i in self.balls:
            i.update()
            self.pad.x = pyxel.mouse_x

            if i.x >= 200 or i.x < 0:
              i.vx *= -1

            if i.y >= 200:
                i.y = 0
                i.x = pyxel.rndi(0, 199)
                i.angle = pyxel.rndi(30, 150)
                i.vx = pyxel.cos(i.angle)
                i.vy = pyxel.sin(i.angle)
                self.fail += 1
                
            if self.pad.catch(i):
                i.y = 0
                i.x = pyxel.rndi(0, 199)
                i.angle = pyxel.rndi(30, 150)
                i.vx = pyxel.cos(i.angle)
                i.vy = pyxel.sin(i.angle)
                Ball.speed += 0.2

                if self.s % 10 == 0 and self.s != 0:
                    self.balls.append(Ball(pyxel.rndiz(0, 1)))
                    Ball.speed = 2
                self.s += 1    

    def draw(self):
        if self.fail >= 10:
            pyxel.text(10, 30, 'game over', 2)
        else:
            pyxel.cls(7)
            pyxel.text(10, 10, 'score:' + str(self.s), 2)
            for i in self.balls:
                pyxel.blt(i.x, i.y, i.image_id, 0, 0, 16, 16, 7)
            pyxel.rect(self.pad.x - 20, 195, 40, 5, 14)

App()
