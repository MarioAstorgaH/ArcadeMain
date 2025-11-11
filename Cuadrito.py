import arcade
global xPlayer
global yPlayer
Titulo="Cuadritos de Colores"
Ancho=832
Alto=576
xPlayer=Ancho//2
yPlayer=Alto//2
class GameView(arcade.View):
    def __init__(self):
        super.__init__()
        self.player=Jugador()
        
    def setup():
        pass
    def on_draw():
        pass
    def on_key_press():
        pass
    def on_update():
        pass
    def on_key_release():
        pass
    def on_update():
        pass
class Jugador(arcade.Sprite):
    def __init__(self):
        super().__init__(xPlayer,yPlayer)
        self.sprite=arcade.draw_rect_filled((10,10,10,10))
        self.velocidad=5
        self.vida=1
        self.color={"rojo":(255,0,0),"azul":(0,0,255),"verde":(0,255,0)}
        self.center_x=xPlayer
        self.center_y=yPlayer
    
def main():
    Window=arcade.Window(Ancho,Alto,Titulo)
    game=GameView()
    game.setup()
    Window.show_view(game)
    arcade.run()

