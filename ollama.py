import subprocess
import atexit
import time
import os

ollama_path = r"C:\Users\Berna\AppData\Local\Programs\Ollama\ollama.exe"


def start_ollama():
    if not os.path.exists(ollama_path):
        raise FileNotFoundError(f"Ollama not found at {ollama_path}. Please install Ollama first.")

    process = subprocess.Popen(
        [ollama_path, "serve"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    time.sleep(3)

    atexit.register(process.kill)
    return process


ollama_process = start_ollama()

print("ollama is running")
print(f"Process ID: {ollama_process.pid}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
