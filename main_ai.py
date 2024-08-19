import subprocess
import sys

python = sys.executable

command = [
    python, "ai_model/detect.py",
    "--source", "0",
    "--weight", "weight/yolov9-t-converted.pt",
    "--classes", "0",
]

subprocess.run(command)
