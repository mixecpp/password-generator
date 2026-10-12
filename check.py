import json
import urllib.request

VERSION = "1.0"

def check_for_update():
    url = "https://api.github.com/repos/mixecpp/password-generator/releases/latest"
    try:
        with urllib.request.urlopen(url, timeout=3) as response:
            latest = json.load(response)["tag_name"]
        if latest != VERSION:
            print(f"New version available: {latest} (you have {VERSION})")
            print("Download: https://github.com/mixecpp/password-generator/releases/latest")
            print()
    except Exception:
        pass

check_for_update()