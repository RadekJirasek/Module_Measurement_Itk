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
                        + "| One of the control of %s session has been successfully done." % sesion.name)


def main(sessions):
    for session in sessions:
        # open the measuring program
        if not program_icon.if_exist():
            program_start.find_pos()
            program_start.click()
            control(session, program_icon, error_screen)
        if probe_indicators2.if_exist():
            probe_indicators2.find_pos()
            probe_indicators2.click()
            pag.move(500, 0)
            session.delay(500)
        if not probe_indicators3.if_exist():
            probe_indicators1.find_pos()
            probe_indicators1.click(double=True)
            session.delay(1000)
        if program_icon.if_exist():
            probe_indicators3.find_pos()
            probe_indicators3.click(double=True)
        session.delay(1000)

        session.set_height(b_Lower, b_Higher, session.screen_lr.img_address, min_height)
        # Set height roughly
        control(session, height_good_screen, error_screen)
        # control height (not necessary)
        session.set_height(b_lower, b_higher, session.screen_hr.img_address, min_height)
        # Set height with more precision
        control(session, height_good_screen, error_screen)
        # control height (not necessary)

        pag.click(pag.size()[0]-5, 5)
        control(session, program_icon, error_screen)
        session.delay(2000)

        session.open_sesion(b_sesion1, b_sesion2, b_sesion3)
        # open new session
        control(session, opend_sesion_screen, error_screen)
        # control if session has been opened actually successfully

        while not b_start_session.if_exist():
            session.delay(2000)
        session.start_sesion(b_start_session)
        # start the session
        session.delay(10000)

        while not end_of_measuring.if_exist():
            session.delay(2000)
        """while session.wait_log("Scan finished.", "Closing Log File."):
            pag.alert("Not found")
            session.delay(1000)"""
        # wait to end of session.

        session.end_sesion()
        # end session and restart program
