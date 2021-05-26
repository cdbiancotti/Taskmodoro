
import os
import ctypes

path_user = os.path.expanduser('~')
directory = r'Pictures'
name_of_file = '1143.jpg'
imagePath = os.path.join(path_user, directory, name_of_file)


def is_64_windows():
    """Find out how many bits is OS. """
    return 'PROGRAMFILES(X86)' in os.environ


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper(imagePath):
    SPI_SETDESKWALLPAPER = 20
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, imagePath, 0)
    if not r:
        print(ctypes.WinError())


change_wallpaper(imagePath)
