import json

class JsonLoader:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON", "FLOAT", "INT", "STRING")
    RETURN_NAMES = ("json_data", "float", "int", "string"   )
    FUNCTION = "load_json"

    @classmethod
    def INPUT_TYPES(s):
        print("JsonLoader.INPUT_TYPES")
        return {
            "required": {
                "file_path": ("STRING", {"default": ""}),
            },
        }

    def load_json(self, file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, list): return (data, None, None, None)
            if isinstance(data, dict): return (data, None, None, None)
            if isinstance(data, float): return (None,data,int(data),str(data))
            if isinstance(data, int): return (None,float(data),data,str(data))
            if isinstance(data, str): return (None,None,None,data)
            return (None,None,None,None)
