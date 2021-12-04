from test.utils import Colour


class Config:
    def __init__(self):
        self.verbose = False
        self.python = None

    def log(self, text):
        if self.verbose:
            Colour.YELLOW.print(text)
