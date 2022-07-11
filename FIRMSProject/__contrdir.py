import os

class _CONTROLDIRECTORY(object):
    def __new__(cls,dirtar:str):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,dirtar:str):
        self.__tar = dirtar
    def __str__(self):
        return "DIRECTORY CONTROL - USE FOR THAT PURPOSE"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _DIR_CONTROL(self):
        if os.path.exists(self.__tar):
            pass
        else:
            os.makedirs("www")
    