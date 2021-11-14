from header import Object
import os

path = ""  # path to folder with files and screens.

# inicializace (vytvoreni objektu a stazeni veci, kontrly)
# log o inicializaci

program_icon = Object(path + "program_icon.png")
program_start = Object(path + "program_start.png")

b_Lower = Object(path + "Lower_height.png")  # object to button for lower position
b_Higher = Object(path + "Higher_height.png")
b_lower = Object(path + "lower_height.png")
b_higher = Object(path + "higher_height.png")
b_load_sesion = Object(path + "load_sesion.png")

sesion_coordinate_lp = Object(path + "sesion_coordinate_lr.png")  # object for photo of height position - 1. sesion, low resolution
sesion_coordinate_hp = Object(path + "sesion_coordinate_hr.png")
end_screen = Object(path + "end_screen.png")
error_screen = Object(path + "error_screen.png")
height_good_screen = Object(path + "height_good_screen.png")

R0 = Object(path + "R0.png")
R1 = Object(path + "R1.png")
R2 = Object(path + "R2.png")
R3 = Object(path + "R3.png")
R4 = Object(path + "R4.png")
R5 = Object(path + "R5.png")
