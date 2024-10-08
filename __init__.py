from .json_loader import JsonLoader
from .json_key_selector import JsonKeySelector
from .json_index_selector import JsonIndexSelector

NODE_CLASS_MAPPINGS = {
  "Json Loader" : JsonLoader,
  "Json Key Selector" : JsonKeySelector,
  "Json Index Selector" : JsonIndexSelector,
}

__all__ = ['NODE_CLASS_MAPPINGS']
