from ursina import *

app=Ursina()

#Block Class
def Block(x_coord,y_coord):
    grass = Entity(model='quad',x=x_coord,y=y_coord)

Block(x_coord=1,y_coord=1)

app.run()