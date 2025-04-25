
import os
import json
import hashlib

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# 

def _get_cache_path(prefix, key):
    hashed_key = hashlib.md5(key.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{prefix}_{hashed_key}.json")

def save_to_cache(prefix, key, data):
    path = _get_cache_path(prefix, key)
    with open(path, "w") as f:
        json.dump(data, f)

def load_from_cache(prefix, key):
    path = _get_cache_path(prefix, key)
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None
