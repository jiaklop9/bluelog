#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from bluelog import create_app  # noqa

app = create_app('development')