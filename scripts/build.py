#!/usr/bin/env python3

import shutil
import os
import sys

BUILD_DIR = "./build"

if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)

os.makedirs(BUILD_DIR, exist_ok=True)

copy_list = [
    "overrides",
    "manifest.json",
    "icon.ico"
]

for src in copy_list:
    dst = os.path.join(BUILD_DIR, src)

    is_dir = os.path.isdir(src)
    
    if is_dir:
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)

shutil.make_archive(f"Base Echo's Unlimited {sys.argv[1]}", "zip", root_dir=BUILD_DIR)
