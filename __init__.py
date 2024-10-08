from .json_loader import JsonLoader
from .json_key_selector import JsonKeySelector

NODE_CLASS_MAPPINGS = {
  "Json Loader" : JsonLoader,
  "Json Key Selector" : JsonKeySelector,
}

__all__ = ['NODE_CLASS_MAPPINGS']
