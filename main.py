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


def main(sessions):
    for session in sessions:
        if not program_icon.if_exist():
            program_start.find_pos()
            program_start.click()
            control(session, program_icon, error_screen)

        session.set_height(b_Lower, b_Higher, session.screen_lr)
        # Set height roughly
        # control(session, height_good_screen, error_screen)
        # control height (not necessary)
        session.set_height(b_lower, b_higher, session.screen_hr)
        # Set height with more precision
        # control(session, height_good_screen, error_screen)
        # control height (not necessary)
        session.open_sesion(b_sesion)
        # open new session
        control(session, opend_sesion_screen, error_screen)
        # control if session has been opened actually successfully
        session.start_sesion(b_start_session)
        # start the session
        control(session, end_screen, error_screen)
        # control if session has been started actually successfully
        session.end_sesion()
        # end session and restart program
