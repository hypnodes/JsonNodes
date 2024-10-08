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
        print(f"select_index: {json_data}, {json_data[index]}")
        if index >= len(json_data):
            raise IndexError(f"Array index {index} is out of range. The array has {len(json_data)} elements.")
        value = json_data[index]
        if isinstance(value, dict):  return (value, None, None, None)
        if isinstance(value, list):  return (value, None, None, None)
        if isinstance(value, float): return (None, value, int(value), str(value))
        if isinstance(value, int): return (None, float(value), value, str(value))
        if isinstance(value, str): return (None, None, None, value)
        print("JSON selector: wtf is this?", value)
        return (None, None, None, None)
