# Smart-Badge
Group 2 - Smart Badge Firmware

## Filestructure
```
smart_badge/
  display/
    display.py (display driver)
  settings.json
  apps/
    name.py
    ...
  sensors/
    accelerometer.py
    ...
README.md
dev/
  (any development files not to be loaded onto the MCU)
```

### Notes
- Files and directories should be named with underscores i.e. smart\_badge.
- `/smart_badge/` should *only* contain files for the MCU
