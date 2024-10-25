import pyxel


class App:
    def __init__(self) -> None:
        pyxel.init(160, 120)
        self.x = 0  # 四角形の左上のx座標

    def update(self) -> None:
        """フレームの更新処理"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.x = (self.x + 1) % pyxel.width  # 画面の端まで行ったら戻る

    def draw(self) -> None:
        """フレームの描画処理"""
        pyxel.cls(0)  # 画面をクリア
        pyxel.rect(self.x, 10, 20, 20, 11)  # 四角形の描画


if __name__ == "__main__":
    app = App()
    pyxel.run(app.update, app.draw)
