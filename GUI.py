from main import*
import tkinter
from tkinter import*

# ↓ settings for GUI
MM = tkinter.Tk()
MM.title("Module ITk measurement")
MM.resizable(0, 0)
Com.set_gui(MM)
# ↓ variables for sesions
checkCoordinate = IntVar()
checkPosHybrid = IntVar()
checkPosBoard = IntVar()
checkGlueT = IntVar()
checkSurfaceBoard = IntVar()
checkModuleBow = IntVar()


# ↓ functions for GUI
def start():
    sesions = []
    if CheckCoordinate.var.get():
        sesions.append(Sesion("coordinate", sesion_coordinate_lp, sesion_coordinate_hp))
    if CheckPosHybrid.var.get():
        sesions.append(Sesion("posHybrid", sesion_posHybird_lp, sesion_posHybrid_hp))
    if CheckPosBoard.var.get():
        sesions.append(Sesion("posBoard", sesion_posBoard_lp, sesion_posBoard_hp))
    if CheckGlueT.var.get():
        sesions.append(Sesion("glueT", sesion_glueT_lp, sesion_glueT_hp))
    if CheckSurfaceBoard.var.get():
        sesions.append(Sesion("faceBoard", sesion_surfaceBoard_lp, sesion_serfaceBoard_hp))
    if CheckModuleBow.var.get():
        sesions.append(Sesion("moduleBow", sesion_moduleBow_lp, sesion_moduleBow_hp))
    main(sesions)


# ↓ Set properties of window and objects(buttons, menu, etc...).
TypeMenu = tkinter.Menubutton(MM, text="Select type of module", relief=SUNKEN,
                              bg="light gray", activebackground="gray", activeforeground="white")

TypeMenu.grid()
TypeMenu.menu = Menu(TypeMenu, tearoff=1)
TypeMenu["menu"] = TypeMenu.menu
TypeMenu.menu.add_command(command=Com.set_type("R0"))  # , image=R0.get_img()
TypeMenu.menu.add_command(command=Com.set_type("R1"))
TypeMenu.menu.add_command(command=Com.set_type("R2"))
TypeMenu.menu.add_command(command=Com.set_type("R3"))
TypeMenu.menu.add_command(command=Com.set_type("R4"))
TypeMenu.menu.add_command(command=Com.set_type("R5"))

frameTop = tkinter.Frame(MM)
frameDown = tkinter.Frame(MM)

frameTopT = tkinter.Frame(frameTop)
frameTopTT = tkinter.Frame(frameTopT)
frameTopTB = tkinter.Frame(frameTopT)

frameTopB = tkinter.Frame(frameTop)
frameTopBT = tkinter.Frame(frameTopB)
frameTopBB = tkinter.Frame(frameTopB)

frameDownT = tkinter.Frame(frameDown)
frameDownTT = tkinter.Frame(frameDownT)
frameDownTB = tkinter.Frame(frameDownT)

frameDownB = tkinter.Frame(frameDown)
frameDownBT = tkinter.Frame(frameDownB)
frameDownBB = tkinter.Frame(frameDownB)

LSerialNumber = tkinter.Label(frameTopTT, text="Serial number: ", height=1, width=20)
SerialNumber = tkinter.Entry(frameTopTT, bd=3, width=41)
frameTBBB = tkinter.Frame(frameTopTB, bg="light gray", height=7, width=500)

CheckCoordinate = tkinter.Checkbutton(frameTopBB, text="Coordinate system  ", width=30, variable=checkCoordinate)
CheckCoordinate.var = checkCoordinate
CheckPosHybrid = tkinter.Checkbutton(frameTopBB, text="Position of hybrid", width=30, variable=checkPosHybrid)
CheckPosHybrid.var = checkPosHybrid
CheckPosBoard = tkinter.Checkbutton(frameDownTT, text="Position of power board", width=34, variable=checkPosBoard)
CheckPosBoard.var = checkPosBoard
CheckGlueT = tkinter.Checkbutton(frameDownTT, text="Glue thickness", width=33, variable=checkGlueT)
CheckGlueT.var = checkGlueT
CheckSurfaceBoard = tkinter.Checkbutton(frameDownTB, text="Power board surface", width=31, variable=checkSurfaceBoard)
CheckSurfaceBoard.var = checkSurfaceBoard
CheckModuleBow = tkinter.Checkbutton(frameDownTB, text="Module bow", width=34, variable=checkModuleBow)
CheckModuleBow.var = checkModuleBow
frameTBTB = tkinter.Frame(frameDownBT, bg="light gray", height=7, width=500)
ButtonStart = tkinter.Button(frameDownBB, text="Start measuring", bg="light gray", command=start,
                             activebackground="dark red", activeforeground="white")

# ↓ Set position of objects.
TypeMenu.pack(side=TOP, fill=BOTH)
frameTop.pack(side=TOP, fill=BOTH)
frameDown.pack(side=BOTTOM, fill=BOTH)
frameTopT.pack(side=TOP, fill=BOTH)
frameTopTT.pack(side=TOP, fill=BOTH)
frameTopTB.pack(side=BOTTOM, fill=BOTH)
frameTopB.pack(side=BOTTOM, fill=BOTH)
frameTopBT.pack(side=TOP, fill=BOTH)
frameTopBB.pack(side=BOTTOM, fill=BOTH)
frameDownT.pack(side=TOP, fill=BOTH)
frameDownTT.pack(side=TOP, fill=BOTH)
frameDownTB.pack(side=BOTTOM, fill=BOTH)
frameDownB.pack(side=BOTTOM, fill=BOTH)
frameDownBT.pack(side=TOP, fill=BOTH)
frameDownBB.pack(side=BOTTOM, fill=BOTH)
LSerialNumber.pack(side=LEFT, fill=BOTH)
SerialNumber.pack(side=RIGHT, fill=BOTH)
frameTBBB.pack(side=TOP, fill=BOTH)
CheckCoordinate.pack(side=LEFT, fill=BOTH)
CheckPosHybrid.pack(side=RIGHT, fill=BOTH)
CheckPosBoard.pack(side=LEFT, fill=BOTH)
CheckGlueT.pack(side=RIGHT, fill=BOTH)
CheckSurfaceBoard.pack(side=LEFT, fill=BOTH)
CheckModuleBow.pack(side=RIGHT, fill=BOTH)
frameTBTB.pack(side=BOTTOM, fill=BOTH)
ButtonStart.pack(side=BOTTOM, fill=BOTH)

# ↓ Set options of GUI.
CheckCoordinate.select()
CheckPosHybrid.select()
CheckPosBoard.select()
CheckGlueT.select()
CheckSurfaceBoard.select()
CheckModuleBow.select()
try:
    pass
    # MM.iconbitmap("")
except tkinter.TclError:
    pass  # It doesn't matter, if program can't import icon.


# SMS.protocol("WM_DELETE_WINDOW", on_closing)
MM.mainloop()
# ↑ Loop of GUI. It maintains window opened.
