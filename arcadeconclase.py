#Mario Astorga Hernandez 23050015
import arcade
Ancho= 800
Alto=600
Titulo="Mi ventana"
global xPlayer
xPlayer=Ancho//2
global yPlayer
yPlayer=Alto//2
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_list=arcade.SpriteList()
        self.player_sprite=arcade.Sprite("Assets/thelost.png",1)
        self.player_sprite.center_x=xPlayer
        self.player_sprite.center_y=yPlayer
        self.player_list.append(self.player_sprite)
        self.velocidad=5*60
        self.texto="hola"
        self.izquierda=False
        self.derecha=False
        self.arriba=False
        self.abajo=False
    def on_draw(self):
        self.clear()
        arcade.draw_text(self.texto,
                        Ancho//2,
                        Alto//2,
                        arcade.color.YELLOW,
                        24,
                        anchor_x="center")
        self.player_list.draw()
    def on_key_press(self, symbol, modifiers):
        if symbol==arcade.key.A:
            self.izquierda=True
        elif symbol==arcade.key.W:
            self.arriba=True
        elif symbol==arcade.key.S:
            self.abajo=True
        elif symbol==arcade.key.D:
            self.derecha=True
    def on_key_release(self, symbol, modifiers):
        if symbol==arcade.key.A:
            self.izquierda=False
        elif symbol==arcade.key.W:
            self.arriba=False
        elif symbol==arcade.key.S:
            self.abajo=False
        elif symbol==arcade.key.D:
            self.derecha=False    
    def on_update(self,delta_time):
        dx=0
        dy=0
        if self.izquierda==True:
            dx-=self.velocidad*delta_time
        if self.derecha==True:
            dx+=self.velocidad*delta_time
        if self.arriba==True:
            dy+=self.velocidad*delta_time
        if self.abajo==True:
            dy-=self.velocidad*delta_time
        self.player_sprite.center_x+=dx
        self.player_sprite.center_y+=dy
        halfW=self.player_sprite.width/2
        halfH=self.player_sprite.height/2
        self.player_sprite.center_x = min(max(halfW, self.player_sprite.center_x), Ancho - halfW)
        self.player_sprite.center_y= min(max(halfH, self.player_sprite.center_y), Alto - halfH)
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)
class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)
    def on_draw(self):
        self.clear()
        arcade.draw_text("Pulsa ENTER para jugar",Ancho//2,Alto//2,arcade.color.YELLOW,24,anchor_x="center")
    def on_key_press(self, symbol, modifiers):
        if symbol==arcade.key.ENTER:
            ventana.show_view(GameView())
if __name__ =="__main__":
    ventana=arcade.Window(Ancho,Alto,Titulo)
    ventana.show_view(MenuView())
    arcade.run()
