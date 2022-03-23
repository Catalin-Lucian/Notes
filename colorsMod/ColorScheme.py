import json


class ColorScheme(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ColorScheme, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.colors = {}
        with open(f'colorsMod/color_scheme.json') as json_file:
            self.colors = json.load(json_file)
