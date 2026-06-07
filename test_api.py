import os
import requests
import json

URL = "https://ollama.com/api/generate"
MODEL = "gpt-oss:120b"
KEY = os.environ.get("BIGMODEL_API_KEY", "")

headers = {
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": MODEL,
    "prompt": "Say hello",
    "stream": False
}

try:
    print(f"Connecting to {URL}...")
    response = requests.post(URL, json=data, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}")
except Exception as e:
    print(f"Error: {e}")
