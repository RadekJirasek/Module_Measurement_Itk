from PIL import Image, ImageTk
import pyautogui as pag
import datetime


class Com:
    path = ""

    @classmethod
    def set_path(cls, _path):
        if _path[-1] != "\\":
            _path += "\\"
        cls.path = _path

    @classmethod
    def set_gui(cls, _gui):
        # method for defining graphical user interface for editing it (waiting etc...)
        cls.gui = _gui

    @classmethod
    def set_type(cls, _type):
        # method for define type of module
        cls.type = _type

    @classmethod
    def set_log(cls):
        cls.log_file = "logs\\" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M") + ".txt"
        with open(cls.path + cls.log_file, 'w') as file:
            file.close()

    def save_log(self, message):
        with open(self.path + self.log_file, 'a') as file:
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
        self.load_img()  # ? musi byt jiz loadnuty v find_pos

    def pos(self):
        return self.position

    def if_exist(self, grayscale=True):
        return pag.locateCenterOnScreen(self._image, grayscale=grayscale,
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
        self.name = name
        self.screen_lr = screen_lr
        self.screen_hr = screen_hr
        self.finding_change_indexes = _finding_change_indexes
        self.finding_height_dir = _finding_height_dir

    def __del__(self):
        self.save_log()

    def wait(self, control_picture):
        if not control_picture.if_exist():
            self.finding_height_attempt += 1
            return True
        else:
            return False

    def set_height(self, low, high, height):
        low.find_pos()
        high.find_pos()
        height.find_pos()

        while self.wait(height):
            if self.finding_change_indexes:
                self.save_log()
                self.__del__()
            if self.finding_height_attempt in self.finding_change_indexes:
                self.finding_height_dir = not self.finding_height_dir
                for i in range(0, self.finding_change_indexes[0]):
                    if self.finding_height_dir:
                        low.click()
                    else:
                        high.click()
                    self.gui.after(500)
                self.finding_change_indexes = self.finding_change_indexes[1:]

            if self.finding_height_dir:
                low.click()
            else:
                high.click()

    @staticmethod
    def start(load_sesion):
        load_sesion.find_pos()
        load_sesion.click(2, 2)
        # doplnit
