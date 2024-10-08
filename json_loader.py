import json

class JsonLoader:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON",)
    RETURN_NAMES = ("json_data",)
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
            return (data,)
