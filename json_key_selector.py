import json

class JsonKeySelector:
    CATEGORY = "json"
    RETURN_TYPES = ("JSON", "FLOAT", "INT", "STRING", "LENGTH")
    RETURN_NAMES = ("json", "float", "int", "string", "length")
    FUNCTION = "select_key"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_data": (("JSON"),),
                "key": ("STRING", {"default": "key"})
            },
        }

    def select_key(self, json_data, key):
        try:
            # Ensure the input is a valid dictionary
            if not isinstance(json_data, dict):
                raise ValueError("Input is not a valid JSON object.")

            # Extract the value for the specified key
            value = json_data.get(key)

            if value is None:
                print(f"Key '{key}' not found in the JSON.")
                return (None, None, None, None, None)

            # Compute length if applicable
            length = len(value) if isinstance(value, (list, str)) else None

            # Return based on the type of value
            if isinstance(value, dict):
                return (value, None, None, None, None)
            if isinstance(value, list):
                return (None, None, None, value, length)
            if isinstance(value, str):
                return (None, None, None, value, length)
            if isinstance(value, float):
                return (None, value, int(value), str(value), None)
            if isinstance(value, int):
                return (None, float(value), value, str(value), None)

            # Handle unexpected types
            print(f"Unexpected type for key '{key}': {type(value)}")
            return (None, None, None, None, None)

        except Exception as e:
            print(f"Error in select_key: {e}")
            return (None, None, None, None, None)
