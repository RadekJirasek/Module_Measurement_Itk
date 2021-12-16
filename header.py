from PIL import Image, ImageTk
import pyautogui as pag
import datetime
from psutil import virtual_memory
from shutil import disk_usage


def memory(memory_type):
    free_size = 0
    if memory_type == "RAM":
        free_size = virtual_memory()[4] / (2**20)
    else:
        free_size = disk_usage(memory_type)[2] / (2**30)

    return round(free_size, 3)


def w(im, reg, session):
    if not pag.locateCenterOnScreen(im.img_address, grayscale=True, region=reg, confidence=0.9):
        session.finding_height_attempt += 1
        return True
    else:
        return False


class Com:
    path = ""

    @classmethod
    def set_path(cls, _path):
        # method for set path of program folder
        _path += "\\"
        cls.path = _path

    @classmethod
    def set_gui(cls, _gui):
        # method for defining graphical user interface for editing it (waiting etc...)
        cls.gui = _gui

    @classmethod
    def set_type(cls, _type, __menu):
        # method for define type of module
        cls.type = _type
        __menu["text"] = "Selected type of module - %s" % cls.type

    @classmethod
    def set_log(cls):
        cls.log_file = "C:\\Users\\student\\Documents\\" \
                       + "logs\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + ".txt"
        with open(cls.log_file, 'w+') as file:
            file.write("\n\nSTART OF MEASURING: " + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                       + "\nFree data size on DISK: " + str(memory(cls.path[0:2]))
                       + " GB\n_________________________________________")
            file.close()

    @classmethod
    def set_serial_number(cls, _serial_number):
        cls.serial_number = _serial_number

    def save_log(self, message):
        with open(self.log_file, 'a') as file:
            file.write(message)

    def delay(self, time_ms):
        self.gui.after(time_ms)


class Object(Com):
    x_range = pag.size()[0]
    y_range = pag.size()[1]
    position = (None, None)
    img_format = ''
    img_address = ""

    def __init__(self, img_address, x=0, y=0, img_format='L'):
        self.position = (x, y)
        self.img_address = self.path + "screens\\" + img_address
        self.img_format = img_format
        self.x_range = pag.size()[0] - x
        self.y_range = pag.size()[1] - y

    def pos(self):
        return self.position

    def if_exist(self, grayscale=True):
        return pag.locateCenterOnScreen(self.img_address, grayscale=grayscale,
                                        region=(self.position[0], self.position[1], self.x_range, self.y_range))

    def load_img(self):
        try:
            self._image = ImageTk.PhotoImage(Image.open(self.img_address))
        except OSError:
            raise AssertionError("Not found '%s' screenshot." % self.img_address)

    def click(self, x_offset=0, y_offset=0):
        pag.click((self.position[0] + x_offset, self.position[1] + y_offset))

    def find_pos(self, grayscale=True):
        _position = self.if_exist(grayscale)
        if _position:
            self.position = _position
            self.x_range = pag.size()[0] - self.position[0]
            self.y_range = pag.size()[1] - self.position[1]
        else:
            self.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                          + "| Position of screen from %s has not been found." % self.img_address)

    def get_img(self):
        return self._image


class Sesion(Com):
    finding_height_attempt = 0

    def __init__(self, name, screen_lr, screen_hr, _finding_change_indexes=(3, 5, 8, 13), _finding_height_dir=True):
        self.end = False
        self.name = name
        self.screen_lr = screen_lr
        self.screen_hr = screen_hr
        self.finding_change_indexes = _finding_change_indexes
        self.finding_height_dir = _finding_height_dir

    def __del__(self):
        self.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                      + "| Sesion %s has been end." % self.name)

    @staticmethod
    def wait(control_picture):
        if not control_picture.if_exist():
            return True
        else:
            return False

    def set_height(self, low, high, height):
        if self.end:
            return 0
        low.find_pos()
        high.find_pos()

        height.position = high.pos()
        height.x_range = 100
        height.y_range = 80

        while w(height, (high.pos()[0], high.pos()[1], 100, 80), self):
            pag.alert("sW")
            if not self.finding_change_indexes:
                self.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                              + "| Can not be set correct height of station in %s sesion." % self.name)
                break

            if self.finding_height_attempt in self.finding_change_indexes:
                self.finding_height_dir = not self.finding_height_dir
                for i in range(0, self.finding_change_indexes[0]):
                    if self.finding_height_dir:
                        low.click()
                    else:
                        high.click()
                    self.delay(1000)
                self.finding_change_indexes = self.finding_change_indexes[1:]

            if self.finding_height_dir:
                low.click()
            else:
                high.click()
            self.delay(1500)

    def open_sesion(self, load_sesion):
        if self.end:
            return 0
        load_sesion.find_pos()
        load_sesion.click(2, 2)
        self.delay(2000)
        pag.hotkey("alt", "d")
        self.delay(500)
        pag.typewrite(self.path + "Sessions\\")
        pag.hotkey("alt", "n")
        self.delay(500)
        pag.typewrite(self.name + ".Session")

        self.delay(1000)
        pag.typewrite(["enter"])
        self.delay(1000)
        pag.typewrite(["enter"])

    def start_sesion(self, start_ses):
        if self.end:
            return 0
        start_ses.find_pos()
        start_ses.click(2, 2)
        # next things ..?

    def end_sesion(self):
        self.end = True
        # things for end sesion after measuring (reset, ...)
        pass
