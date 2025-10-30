import arcade
import time 
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
        self.player_sprite=arcade.Sprite("Assets/thelost.png",1.5)
        self.player_sprite.center_x=xPlayer
        self.player_sprite.center_y=yPlayer
        self.player_list.append(self.player_sprite)

        # lista de disparos (tears)
        self.lagrimas_list=arcade.SpriteList()

        # tiempos y velocidades para el cronómetro y disparo
        self.tiempo=0.0
        self.velocidad=5*60

        # flags de movimiento
        self.izquierda=False
        self.derecha=False
        self.arriba=False
        self.abajo=False

        # flags de disparo por dirección
        self.disparo=False
        self.disparoArriba=False
        self.disparoAbajo=False
        self.disparoDerecha=False
        self.disparoIzquierda=False

        # control de cadencia y velocidad de tear (segundos entre disparos)
        self.tear_rate = 0.25      # segundos entre disparos cuando mantienes tecla
        self.time_since_last_shot = 0.0
        self.tear_speed = 500.0    # píxeles por segundo
        self.tear_scale = 2    # escala del sprite de la lágrima

        self.texto="hola"
        self.LagrimasDisparadas=0

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
        self.clear()
        minutos:int = self.tiempo//60
        segundos=self.tiempo%60
        segundos=round(segundos,1)
        Tears=self.LagrimasDisparadas
        str1=f"tiempo: "+str(minutos)+":"+str(segundos)
        str2=f"Lagrimas disparadas:"+str(Tears)
        self.lista_ladrillos.draw()
        arcade.draw_text("Mario Astorga Hernandez",180,530,arcade.color.YELLOW,24,anchor_x="center")
        arcade.draw_text("23050015",700,530,arcade.color.YELLOW,24,anchor_x="center")
        arcade.draw_text(str1,700,0,arcade.color.YELLOW,24,anchor_x="center")
        arcade.draw_text(str2,150,0,arcade.color.YELLOW,24,anchor_x="center")
        self.player_list.draw()
        self.lista_dineros.draw()
        self.lagrimas_list.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol==arcade.key.A:
            self.izquierda=True
        elif symbol==arcade.key.W:
            self.arriba=True
        elif symbol==arcade.key.S:
            self.abajo=True
        elif symbol==arcade.key.D:
            self.derecha=True
        elif symbol==arcade.key.UP:
            self.disparo=True
            self.disparoArriba=True
        elif symbol==arcade.key.DOWN:
            self.disparo=True
            self.disparoAbajo=True
        elif symbol==arcade.key.RIGHT:
            self.disparo=True
            self.disparoDerecha=True
        elif symbol==arcade.key.LEFT:
            self.disparo=True
            self.disparoIzquierda=True

    def on_key_release(self, symbol, modifiers):
        if symbol==arcade.key.A:
            self.izquierda=False
        elif symbol==arcade.key.W:
            self.arriba=False
        elif symbol==arcade.key.S:
            self.abajo=False
        elif symbol==arcade.key.D:
            self.derecha=False    
        elif symbol==arcade.key.UP:
            self.disparo=False
            self.disparoArriba=False
        elif symbol==arcade.key.DOWN:
            self.disparo=False
            self.disparoAbajo=False
        elif symbol==arcade.key.RIGHT:
            self.disparo=False
            self.disparoDerecha=False
        elif symbol==arcade.key.LEFT:
            self.disparo=False
            self.disparoIzquierda=False

    def spawn_tear(self, dir_x:float, dir_y:float):
        """Crear una lágrima en la posición del jugador con dirección (dir_x, dir_y) normalizada."""
        tear = arcade.Sprite("assets/Lagrima.png", scale=self.tear_scale)
        tear.center_x = self.player_sprite.center_x
        tear.center_y = self.player_sprite.center_y
        # guardar velocidad en píxeles/segundo en change_x/change_y
        tear.change_x = dir_x * self.tear_speed
        tear.change_y = dir_y * self.tear_speed
        self.lagrimas_list.append(tear)

    def on_update(self,delta_time):
        # cronómetro
        self.tiempo += delta_time

        # movimiento del player
        dx=0
        dy=0
        if self.izquierda:
            dx -= self.velocidad*delta_time
        if self.derecha:
            dx += self.velocidad*delta_time
        if self.arriba:
            dy += self.velocidad*delta_time
        if self.abajo:
            dy -= self.velocidad*delta_time
        self.player_sprite.center_x += dx
        self.player_sprite.center_y += dy
        halfW=self.player_sprite.width/2
        halfH=self.player_sprite.height/2
        self.player_sprite.center_x = min(max(64, self.player_sprite.center_x), Ancho- 64)
        self.player_sprite.center_y = min(max(80, self.player_sprite.center_y), Alto - 64)

        # control de cadencia de disparo
        self.time_since_last_shot += delta_time
        if self.disparo and self.time_since_last_shot >= self.tear_rate:
            # disparar en la(s) dirección(es) activas (solo una en tu diseño)
            if self.disparoArriba:
                self.spawn_tear(0, 1)
                self.LagrimasDisparadas+=1
            elif self.disparoAbajo:
                self.spawn_tear(0, -1)
                self.LagrimasDisparadas+=1
            elif self.disparoDerecha:
                self.spawn_tear(1, 0)
                self.LagrimasDisparadas+=1
            elif self.disparoIzquierda:
                self.spawn_tear(-1, 0)
                self.LagrimasDisparadas+=1
            # resetear timer
            self.time_since_last_shot = 0.0

        # actualizar posición de todas las lágrimas (usando delta_time)
        for tear in list(self.lagrimas_list):  # copiar lista para poder eliminar dentro del bucle
            tear.center_x += getattr(tear, "change_x", 0) * delta_time
            tear.center_y += getattr(tear, "change_y", 0) * delta_time
            # borrar si sale de la pantalla
            if (tear.center_x < -50 or tear.center_x > Ancho + 50 or
                tear.center_y < -50 or tear.center_y > Alto + 50):
                tear.remove_from_sprite_lists()
        if self.disparo:
            self.LagrimasDisparadas+1
def main():
    Window=arcade.Window(Ancho,Alto,Titulo)

    game=GameView()
    game.setup()
    Window.show_view(game)
    arcade.run()


if __name__=="__main__":
    main()