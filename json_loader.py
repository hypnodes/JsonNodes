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
                "index": ("INT", {"default": 0, "min": 0, "step": 1}),
            },
        }

    def load_json(self, file_path, index):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        if not isinstance(data, list):
            raise ValueError("The JSON file does not contain an array at the root level")

        if index >= len(data):
            raise IndexError(f"Array index {index} is out of range. The array has {len(data)} elements.")

        item = data[index]

        # Convert values to float where possible, otherwise keep as string
        json_data = {}
        for k, v in item.items():
            try:
                json_data[str(k)] = float(v)
            except ValueError:
                try:
                    json_data[str(k)] = int(v)
                except ValueError:
                    json_data[str(k)] = str(v)

        return (json_data,)
