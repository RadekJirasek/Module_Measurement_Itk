from PIL import Image, ImageTk
import pyautogui as pag
import datetime


class Com:
    path = ""

    @classmethod
    def set_path(cls, _path):
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
            # write initial text to log
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
            # log

    def click(self, x_offset=0, y_offset=0):
        pag.click((self.position[0] + x_offset, self.position[1] + y_offset))

    def find_pos(self, grayscale=True):
        self.position = self.if_exist(grayscale)
        self.x_range = pag.size()[0] - self.position[0]
        self.y_range = pag.size()[1] - self.position[1]

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

    def wait(self, control_picture):
        if not control_picture.if_exist():
            self.finding_height_attempt += 1
            return True
        else:
            return False

    def set_height(self, low, high, height):
        pag.alert("s00")
        if self.end:
            pag.alert("s0")
            return 0
        pag.alert("s1")
        low.find_pos()
        pag.alert("s2")
        high.find_pos()
        pag.alert("s3")

        while self.wait(height):
            pag.alert("sW")
            if not self.finding_change_indexes:
                self.save_log("\n" + datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                              + "| Can not be set correct height of station in %s sesion." % self.name)
                self.__del__()
            if self.finding_height_attempt in self.finding_change_indexes:
                self.finding_height_dir = not self.finding_height_dir
                for i in range(0, self.finding_change_indexes[0]):
                    if self.finding_height_dir:
                        low.click()
                    else:
                        high.click()
                    self.delay(500)
                self.finding_change_indexes = self.finding_change_indexes[1:]

            if self.finding_height_dir:
                low.click()
            else:
                high.click()

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

    def end_sesion(self):
        self.end = True
        # things for end sesion after measuring (reset, ...)
        pass

    # doplnit
