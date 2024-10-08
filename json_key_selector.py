import json

class JsonKeySelector:
    CATEGORY = "example"
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "pick_value"
    @classmethod
    def INPUT_TYPES(s):
        return { "required":  { "path": ("STRING",),
                                "key": ("STRING",)} }

    def pick_value(self, path, key):
        print("pick_value", path, key)
        with open(path, 'r') as file:
            data = json.load(file)
        print("pick_value data[key]", data[key])
        return (data[key],)
