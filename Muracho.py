import arcade

EscalaSprite=0.5
Ancho=832
Alto=576
Titulo="Curso de albañileria express"
Velocidad=5
global xPlayer
global yPlayer
xPlayer=Ancho//2
yPlayer=Alto//2
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.lista_ladrillos=None
        self.lista_dineros=None
        self.player_list=arcade.SpriteList()
        self.player_sprite=arcade.Sprite("Assets/thelost.png",1)
        self.player_sprite.center_x=xPlayer
        self.player_sprite.center_y=yPlayer
        self.player_list.append(self.player_sprite)
        self.tiempo=0.0
        self.velocidad=5*60
        self.texto="hola"
        self.izquierda=False
        self.derecha=False
        self.arriba=False
        self.abajo=False
    def setup(self):
        self.background_color=arcade.color.AMAZON
        self.lista_ladrillos=arcade.SpriteList()
        self.lista_dineros=arcade.SpriteList()
        for x in range(32,Ancho,64):
            for y in (32, Alto-32):
                wall=arcade.Sprite(":resources:images/tiles/brickBrown.png",scale=EscalaSprite)
                wall.center_x=x
                wall.center_y=y
                self.lista_ladrillos.append(wall)

        for y in range(96,Alto,64):
            for x in (32,Ancho-32):
                wall=arcade.Sprite(":resources:images/tiles/brickBrown.png",scale=EscalaSprite)
                wall.center_x=x
                wall.center_y=y
                self.lista_ladrillos.append(wall)
    def on_draw(self):
        minutos:int =self.tiempo//60
        segundos=self.tiempo%60
        segundos=round(segundos,2)
        str1=f"tiempo: "+str(minutos)+":"+str(segundos)
        self.clear()
        self.lista_ladrillos.draw()
        arcade.draw_text(str1,700,0,arcade.color.YELLOW,24,anchor_x="center")
        
        self.player_list.draw()
        self.lista_dineros.draw()
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
        self.tiempo+=delta_time
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
        self.player_sprite.center_x = min(max(64, self.player_sprite.center_x), Ancho- 64)
        self.player_sprite.center_y= min(max(64, self.player_sprite.center_y), Alto - 64)

def main():
    Window=arcade.Window(Ancho,Alto,Titulo)

    game=GameView()
    game.setup()
    Window.show_view(game)
    arcade.run()



if __name__=="__main__":
    main()