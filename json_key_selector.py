import json

class JsonKeySelector:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON", "FLOAT", "INT", "STRING",)
    RETURN_NAMES = ("json","float","int","string" )
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
        print(f"select_key: {json}, {json[key]}")
        value = json[key]
        if isinstance(value, dict): return (value, None, None, None)
        if isinstance(value, list): return (None, None, None, value)
        if isinstance(value, str): return (None,None,None,value)
        if isinstance(value, float): return (None, value, int(value), str(value))
        if isinstance(value, int): return (None, float(value), value, str(value))
        print("JSON selector: wtf is this?", value)
        return (None, None, None, None)
