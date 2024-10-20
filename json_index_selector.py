import json

class JsonIndexSelector:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON", "FLOAT", "INT", "STRING")
    RETURN_NAMES = ("json", "float", "int", "string" )
    FUNCTION = "select_index"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
               "json_data": (("JSON"),),
               "index": ("INT",),
            },
        }

    def select_index(self, json_data, index):
        if index >= len(json_data):
            raise IndexError(f"Array index {index} is out of range. The array has {len(json_data)} elements.")
        value = json_data[index]
        length = len(value) if isinstance(value, (list, str)) else None
        if isinstance(value, dict):  return (value, None, None, None, None)
        if isinstance(value, list):  return (value, None, None, None, length)
        if isinstance(value, float): return (None, value, int(value), str(value), None)
        if isinstance(value, int): return (None, float(value), value, str(value), None)
        if isinstance(value, str): return (None, None, None, value, length)
        return (None, None, None, None, None)
