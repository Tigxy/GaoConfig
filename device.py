class Device:
    def __init__(self):
        self.description = ""
        self.location = ""
        self.buttons = []

    def load(self, file):
        """
        Loads the settings from the specified file
        :param file: The file that contains the settings
        """
        pass

    def save(self, file):
        """
        Stores the settings in the specified file, note that the file will be overwritten
        :param file: The file to store the settings in
        """
        pass

    def reconfigure(self):
        """
        Configures the device by using the DIGImend driver
        """
        pass


class Tablet(Device):
    def __init__(self):
        super().__init__()
        self.drawing_size = None
        self.drawing_offset = None
        self.app = None
        self.on_app = None


class Pen(Device):
    def __init__(self):
        super().__init__()
        self.pressure_curve = None
        self.constant_pressure = None
        self.use_constant_pressure = None


def find_devices():
    pass


