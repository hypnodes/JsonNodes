import json

class JsonKeySelector:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON", "FLOAT", "INT", "STRING", "INT")
    RETURN_NAMES = ("json", "float", "int", "string", "length")
    FUNCTION = "select_key"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
               "json": (("JSON"),),
               "key": ("STRING",),
            },
        }

    def select_key(self, json, key):
        value = json[key]
        length = len(value) if isinstance(value, (list, str)) else None

        if isinstance(value, dict):
            return (value, None, None, None, None)
        if isinstance(value, list):
            return (None, None, None, value, length)
        if isinstance(value, str):
            return (None, None, None, value, length)
        if isinstance(value, float):
            return (None, value, int(value), str(value), None)
        if isinstance(value, int):
            return (None, float(value), value, str(value), None)

        print("JSON selector: wtf is this?", value)
        return (None, None, None, None, None)
