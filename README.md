# RadiSpawn
A simple, customizable script for launching applications and scripts using a radial menu

# Installation
The is on PyPI, so it can be installed by running:
```
$ pip install radispawn
```

# Running
```
radispawn cfg_file.json
```
The cfg_file.json argument can be located in either:
- The present working directory 
- ~/.config/radispawn/

# Basic config file
```json
{
    "wedges": [
        {"name": "Firefox", "call": "firefox", "color": [255, 128, 0]},
        {"name": "Discord", "call": "/opt/discord/Discord", "color": [0, 128, 255]},
        {"name": "PCManFM", "call": "pcmanfm", "color": [255, 255, 255]}
    ]
}
```
