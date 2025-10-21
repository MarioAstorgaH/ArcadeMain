#Mario Astorga Hernandez 23050015
import arcade
Ancho= 800
Alto=600
Titulo="Mi ventana"

class MiVentana(arcade.Window):
    def __init__(self):
        super().__init__(Ancho, Alto, Titulo)
        arcade.set_background_color((255,255,255))
        self.recAnc=150
        self.recAlt=150
        self.recY=50
        self.recX=300
        self.velocidad=5*60
        self.texto="hola"

        self.izquierda=False
        self.derecha=False
        self.arriba=False
        self.abajo=False
    def on_draw(self):
        arcade.draw_text(self.texto,
                         Ancho//2,
                         Alto//2,
                         arcade.color.BLACK,
                         24,
                         anchor_x="center")
        self.clear()
        arcade.draw_lbwh_rectangle_filled(self.recX,self.recY,self.recAnc,self.recAlt,(90,132,23))
        
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
        self.recX+=dx
        self.recY+=dy
        self.recX = min(max(0, self.recX), Ancho - self.recAnc)
        self.recY = min(max(0, self.recY), Alto - self.recAlt)

            
        
if __name__ =="__main__":
    ventana=MiVentana()
    arcade.run()
