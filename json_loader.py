import json
import os

class JsonLoader:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON", "FLOAT", "INT", "STRING", "INT")
    RETURN_NAMES = ("json", "float", "int", "string", "length")
    FUNCTION = "load_json"

    @classmethod
    def INPUT_TYPES(s):
        default_path = os.path.join(os.path.dirname(__file__), "example.json")
        return {
            "required": {
                "file_path": ("STRING", {"default": default_path}),
            },
        }

    def load_json(self, file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, list): return (data, None, None, None, len(data))
            if isinstance(data, dict): return (data, None, None, None, len(data))
            if isinstance(data, float): return (None,data,int(data),str(data),0)
            if isinstance(data, int): return (None,float(data),data,str(data),0)
            if isinstance(data, str): return (None,None,None,data,0)
            return (None,None,None,None,0)
