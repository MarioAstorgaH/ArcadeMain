import arcade
global xPlayer
global yPlayer
Ancho=
Alto=
xPlayer=Ancho//2
class GameVieW(arcade.View):
    def __init__(self):
        super().__init__()
        self.list_ladrillos=None
        self.player_list=arcade.SpriteList()
        self.player_sprite=arcade.Sprite("assets/MiniPekka.png")
        self.player_sprite.center_x=xPlayer
        self.velocidad=5
        self.