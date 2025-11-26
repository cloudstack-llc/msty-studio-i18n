import json
import re

with open('zh_CN.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def check_spaces(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            check_spaces(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, str):
        # Look for Space+{ or }+Space or Space+@ or @+Space
        # But exclude cases where it might be legitimate (like English words around it, though this is zh_CN)
        if re.search(r' [{@]', obj) or re.search(r'[}@] ', obj):
            print(f"{path}: {obj}")

check_spaces(data)
