import json

class JsonKeySelector:
    CATEGORY = "json"
    RETURN_TYPES = ("FLOAT", "INT", "STRING",)
    RETURN_NAMES = ("float","int","string" )
    FUNCTION = "select_key"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
               "json_data": (("JSON"),),
               "key": ("STRING",),
            },
        }

    def select_key(self, json_data, key):
        print(f"select_key: {json_data}, {json_data[key]}")
        value = json_data[key]
        if isinstance(value, float):
            return (value, int(value), str(value))
        if isinstance(value, int):
            return (float(value), value, str(value) )
        if isinstance(value, str):
            return (0, 0, value)
        return (0, 0, "")
