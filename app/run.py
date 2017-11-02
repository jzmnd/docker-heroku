# -*- coding: utf-8 -*-
import os
from app import app

# Use run.py to run manually i.e. not on heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(port=port, debug=True)
