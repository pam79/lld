# copy this file as `config.py`

import os

# EDIT
USERNAME = ''
PASSWORD = ''
COURSES = [
'course-slug-here',
'course-slug-here'
]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None
