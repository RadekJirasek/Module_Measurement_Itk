from header import Object
import tkinter
from pyautogui import size as sz

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

sesion_coordinate_lp = Object("sesion_coordinate_lr.png")  # object for photo of height pos. - 1. sesion, low resolution
sesion_coordinate_hp = Object("sesion_coordinate_hr.png")
sesion_posHybird_lp = Object("sesion_posHybrid_lr.png")
sesion_posHybrid_hp = Object("sesion_posHybrid_hr.png")

end_screen = Object("end_screen.png")
end_screen.position = (int(sz()[0]/2), int(sz()[1]/2))
error_screen = Object("error_screen.png")
height_good_screen = Object("height_good_screen.png")
b_sesion1 = Object("b_sesion1.png")
b_sesion2 = Object("b_sesion2.png")
b_sesion3 = Object("b_sesion3.png")
opend_sesion_screen = Object("opend_sesion_screen.png")
b_start_session = Object("b_start_session.png")
probe_indicators1 = Object("probe1.png")
probe_indicators2 = Object("probe2.png")
probe_indicators3 = Object("probe3.png")
#probe_indicators1.x_range = 400
#probe_indicators1.y_range = 100
#probe_indicators2.x_range = 400
#probe_indicators2.y_range = 100
end_of_measuring = Object("end.png")
min_height = Object("min_height.png")

# R0 = Object("R0.png")
# R1 = Object("R1.png")
R2 = Object("R2.png")
# R3 = Object("R3.png")
R4_M1 = Object("R4_M1.png")
R4_M2 = Object("R4_M2.png")
# R5 = Object("R5.png")

# load image for objects:
program_icon.load_img()
program_start.load_img()

b_Lower.load_img()
b_Higher.load_img()
b_lower.load_img()
b_higher.load_img()

sesion_coordinate_lp.load_img()
sesion_coordinate_hp.load_img()
end_screen.load_img()
error_screen.load_img()
height_good_screen.load_img()
b_sesion1.load_img()
b_sesion2.load_img()
b_sesion3.load_img()
b_start_session.load_img()
opend_sesion_screen.load_img()
probe_indicators1.load_img()
probe_indicators2.load_img()
end_of_measuring.load_img()
min_height.load_img()

# R0.load_img()
# R1.load_img()
R2.load_img()
# R3.load_img()
R4_M1.load_img()
R4_M2.load_img()
# R5.load_img()

# log o inicializaci
