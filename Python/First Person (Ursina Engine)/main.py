from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
 
app = Ursina()
 
ground = Entity( model='plane', collider='box', scale=(25, 1, 25) )
 
player = FirstPersonController( position=(0, 10) )
 
app.run()
