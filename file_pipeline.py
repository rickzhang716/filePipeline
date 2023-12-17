"""
A CI/CD for my resume.
"""

import os
import os.path
import time
from pathlib import Path


file_path = Path(os.getenv("RESUME_PATH"))
file_path = file_path.expanduser().resolve()


while True:
    if os.path.exists(file_path):
        os.system(f'mv {os.getenv("RESUME_SRC")} {os.getenv("RESUME_DEST")}') # noqa
    time.sleep(30)
