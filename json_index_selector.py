import json

class JsonIndexSelector:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON",)
    RETURN_NAMES = ("json_data",)
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
        return (value,)
