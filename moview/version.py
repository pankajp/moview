__version_info__ = (0,1)
__version__ = '.'.join(str(i) for i in __version_info__)
is_released = False
if not is_released:
    __version__ += '.dev0'
    __version_info__ += (-1, )
