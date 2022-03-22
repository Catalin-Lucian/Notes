import json


class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class ColorScheme(SingletonClass):
    def __init__(self):
        self.colors = {
            "primary_color_lite": "",
            "primary_color_light": "",
            "primary_color": "",
            "primary_color_dark": "",
            "primary_color_darker": "",

            "secondary_color_lite": "",
            "secondary_color_light": "",
            "secondary_color": "",
            "secondary_color_dark": "",
            "secondary_color_darker": "",

            "accent_color_lite": "",
            "accent_color_light": "",
            "accent_color": "",
            "accent_color_dark": "",
            "accent_color_darker": ""
        }
        with open(f'colorsMod/color_scheme.json') as json_file:
            self.colors = json.load(json_file)
