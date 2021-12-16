from header import *
from initialize import*


def control(sesion, wait_object, catch_object):
    while sesion.wait(wait_object):
        # waiting for end of sesion
        if not sesion.wait(catch_object):
            # condition for error message
            sesion.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                            + "| Program detect error screen in %s sesion." % sesion.name)
            sesion.end_sesion()
            break
    else:
        sesion.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                        + "| %s has been successfully done." % sesion.name)


def main(sesions):
    for sesion in sesions:
        if not program_icon.if_exist():
            pag.alert("Info 1")
            program_start.find_pos()
            pag.alert("Info 2")
            program_start.click()
            control(sesion, program_icon, error_screen)
            pag.alert("Info 3")

        pag.alert("Info 3.5")

        sesion.set_height(b_Lower, b_Higher, sesion.screen_lr)
        # Set height roughly

        pag.alert("Info 4")

        control(sesion, height_good_screen, error_screen)

        pag.alert("Info 5")

        sesion.set_height(b_lower, b_higher, sesion.screen_hr)
        # Set height with more precision
        control(sesion, height_good_screen, error_screen)

        pag.alert("Info 7")

        sesion.open_sesion(b_sesion)
        # open new sesion
        control(sesion, opend_sesion_screen, error_screen)
        sesion.start_sesion(b_start_session)
        # start the sesion
        control(sesion, end_screen, error_screen)

        # CHYBI: restart programu, uvedeni programu do puvodni pozice
