"""
A CI/CD for my resume.
"""

import os.path
from pathlib import Path
import logging
import sys


pythonpath = os.getenv("PYTHON_PATH")
sys.path.append(pythonpath)

# pylint: disable=C0413
import re  # noqa: E402
from fsevents import Observer, Stream  # noqa: E402


logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

pattern = re.compile("Rick Zhang Resume.*pdf$")
src_directory = Path(os.getenv("RESUME_SRC"))
src_directory = src_directory.expanduser().resolve()

dest_directory = Path(os.getenv("RESUME_DEST"))
dest_directory = str(dest_directory.expanduser().resolve())
counter = 0


def move_file(event):
    global counter
    search_result = re.search(pattern, event.name)
    if search_result is not None:
        file_name = search_result.group()
        file_name = file_name.replace(" ", "\\ ")
        file_name = file_name.replace("(", "\\(")
        file_name = file_name.replace(")", "\\)")
        exit_status = os.system(
            f"mv {src_directory}/{file_name}  {dest_directory}"
        )  # noqa
        if exit_status == 0:
            counter += 1
            logger.info(
                "moved %s into %s. %d manual resume moves saved.",
                file_name,
                dest_directory,
                counter,
            )


logger.info("file pipeline starting...")
observer = Observer()
stream = Stream(move_file, str(src_directory), file_events=True)
observer.schedule(stream)
logger.info("waiting for file downloads...")
observer.run()
