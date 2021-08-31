#Universidad del Valle de Guatemala
#Graficas por Computadoras
#Fernando Jose Garavito Ovando 18071
#Lab 2: Shaders
# Programa principal
from gl import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(0,0,-1)

rend.active_texture = Texture('models/Moon1.bmp')
rend.normal_map = Texture('models/Moon2.bmp')

rend.active_shader = normalMap
rend.glLoadModel("models/model.obj",
                 translate = V3(-3, 0, -10),
                 scale = V3(1,1,1))

rend.active_shader = normalMapp
rend.glLoadModel("models/model.obj",
                 translate = V3(-3, 2, -10),
                 scale = V3(1,1,1))

rend.active_shader = phong
rend.glLoadModel("models/model.obj",
                 translate = V3(3, 0, -10),
                 scale = V3(1,1,1))

rend.active_shader = phongg
rend.glLoadModel("models/model.obj",
                 translate = V3(3, 2, -10),
                 scale = V3(1,1,1))

rend.glFinish("Human.bmp")


