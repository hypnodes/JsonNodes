import json

class JsonKeySelector:
    CATEGORY = "example"
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "pick_value"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "path": ("STRING",),
                "index": ("INT", {"default": 0, "min": 0, "step": 1}),
                "key": ("STRING",)
            }
        }

    def pick_value(self, path, index, key):
        print(f"pick_value: path={path}, index={index}, key={key}")
        with open(path, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("The JSON file does not contain an array at the root level")

        if index >= len(data):
            raise IndexError(f"Array index {index} is out of range. The array has {len(data)} elements.")

        selected_element = data[index]

        if key not in selected_element:
            raise KeyError(f"The key '{key}' is not present in the selected array element")

        value = selected_element[key]

        if not isinstance(value, (int, float)):
            raise ValueError(f"The value for key '{key}' is not a number")

        print(f"pick_value: selected value = {value}")
        return (float(value),)
