import os

script_path = os.getenv('WALLPAPER_CHANGER_SCRIPT')
cmd = r'SCHTASKS /CREATE /SC DAILY /TN "WallpaperRotationTask" /TR ' + \
    f'"{script_path}"' + r' /ST 19:00'

returned_value = os.system(cmd)
