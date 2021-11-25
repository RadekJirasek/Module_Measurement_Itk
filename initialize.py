from header import Object
import tkinter

# define gui object
MM = tkinter.Tk()
# ↓ settings for GUI
MM.title("Module ITk measurement")
MM.resizable(0, 0)

# Define objects:

program_icon = Object("program_icon.png")
program_start = Object("program_start.png")
MM_icon = Object("icon.png")

b_Lower = Object("Llower_height.png")  # object to button for lower position
b_Higher = Object("Hhigher_height.png")
b_lower = Object("lower_height.png")
b_higher = Object("higher_height.png")
b_load_sesion = Object("load_sesion.png")

sesion_coordinate_lp = Object("sesion_coordinate_lr.png")  # object for photo of height pos. - 1. sesion, low resolution
sesion_coordinate_hp = Object("sesion_coordinate_hr.png")
end_screen = Object("end_screen.png")
error_screen = Object("error_screen.png")
height_good_screen = Object("height_good_screen.png")


R0 = Object("R0.png")
R1 = Object("R1.png")
R2 = Object("R2.png")
R3 = Object("R3.png")
R4 = Object("R4.png")
R5 = Object("R5.png")

# load image for objects:
program_icon.load_img()
program_start.load_img()

b_Lower.load_img()
b_Higher.load_img()
b_lower.load_img()
b_higher.load_img()
b_load_sesion.load_img()

sesion_coordinate_lp.load_img()
sesion_coordinate_hp.load_img()
end_screen.load_img()
error_screen.load_img()
height_good_screen.load_img()

R0.load_img()
R1.load_img()
R2.load_img()
R3.load_img()
R4.load_img()
R5.load_img()

# log o inicializaci
