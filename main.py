from header import *
from initialize import*


def control(sesion, wait_object, catch_object):
    while sesion.wait(wait_object):
        # waiting for end of sesion
        if sesion.wait(catch_object):
            # condition for error message
            sesion.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                            + "| Program detect error screen in %s sesion." % sesion.name)
            break
    else:
        sesion.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                        + "| %s has been successfully done." % sesion.name)


def main(sesions):
    for sesion in sesions:
        if not program_icon.if_exist():
            program_start.find_pos()
            program_start.click(2, 2)
            sesion.delay(1000)

        sesion.set_height(b_Lower, b_Higher, sesion.screen_lr)
        # Set height roughly
        control(sesion, height_good_screen, error_screen)
        sesion.set_height(b_lower, b_higher, sesion.screen_hr)
        # Set height with more precision
        control(sesion, height_good_screen, error_screen)
        sesion.start()
        # start the sesion
        control(sesion, end_screen, error_screen)

        # CHYBI: restart programu, uvedeni programu do puvodni pozice
