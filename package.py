#!/usr/bin/env python3

import os.path
from os import path

import json

projects = {
    "deauther": [
        "esp8266",
    ],
    "wifiduck": [
        "esp8266",
        "avr",
        "samd",
    ]
}

index_json = {
    "packages": []
}

for i, project in enumerate(projects):
    # Meta data
    project_json = {
        "name": project,
        "maintainer": "Spacehuhn Technologies",
        "websiteURL": "https://spacehuhn.tech",
        "email": "support@spacehuhn.tech",
        "help": {
            "online": f"https://github.com/spacehuhntech/arduino{project}",
        },
        "platforms": [],
        "tools": [],
    }
    
    # Platforms
    for package in projects[project]:
        platform_file = f"{project}/{package}-platform.json"
        
        if path.exists(platform_file):
            with open(platform_file) as f:
                project_json["platforms"].append(json.load(f))

    # Tools
    tools_file = f"{project}/{package}/tools.json"
    with open(tools_file) as f:
        project_json["tools"] = json.load(f)

    index_json["packages"].append(project_json)

with open("package_spacehuhn_index.json", "w") as f:
    f.write(json.dumps(index_json, indent=4))