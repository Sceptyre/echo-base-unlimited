#!/usr/bin/env python3

import shutil
import os
import sys
import string

# PREP
BUILD_VERSION = "devel"
if len(sys.argv) > 1: BUILD_VERSION = f"v{sys.argv[1]}"

BUILD_DIR = "./build"

if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)

os.makedirs(BUILD_DIR, exist_ok=True)

with open("manifest.json", "r") as f:
    t = string.Template(f.read())
    manifest_formatted = t.substitute({
        "BUILD_VERSION": BUILD_VERSION
    })

with open(os.path.join(BUILD_DIR, "manifest.json"), "w+") as f:
    f.write(manifest_formatted)

copy_list = [
    "overrides",
    "icon.ico"
]

for src in copy_list:
    dst = os.path.join(BUILD_DIR, src)

    is_dir = os.path.isdir(src)
    
    if is_dir:
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)

shutil.make_archive(f"build", "zip", root_dir=BUILD_DIR)
