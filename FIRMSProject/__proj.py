import yaml

class _PROJECTREADING(object):
    def __new__(cls,filedir:str):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,filedir:str):
        self.__dir = filedir
    def __str__(self):
        return "YAML READING - USE FOR THAT PURPOSE"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _READFILE(self):
        ymdoc = yaml.safe_load(open(self.__dir,"r"))
        return ymdoc
    def _RETURNINIT(self,params:str):
        yl = self._READFILE()
        return yl[params]
    def _GET_COUNTRIES(self):
        return self._RETURNINIT("places")
    def _GET_AREAS(self):
        return self._RETURNINIT("area")
    def _GETINFO(self):
        fr = ""
        dd = self._READFILE()
        yl = list(self._READFILE().keys())
        for xl in yl:
            idn = dd[xl]
            try:
                for xx in list(idn.keys()):
                    ifn = idn[xx]
                    fr += f"> [{str(xx).upper()}]"+"\n"
                    fr += f"{str(ifn)}"+"\n\n"
            except:
                fr += f"> [{str(xl).upper()}]"+"\n"
                fr += f"{str(idn)}"+"\n\n"
        return fr
    def _GET_KEY(self):
        fr = []
        dd = self._READFILE()
        yl = list(self._READFILE().keys())
        for xl in yl:
            idn = dd[xl]
            if len(list(idn.keys())) > 0:
                try:
                    for xx in list(idn.keys()):
                        ifn = idn[xx]
                        if str(xx).upper() == "KY_ONE" or str(xx).upper() == "KY_TWO"\
                            or str(xx).upper() == "KY_THR" or str(xx).upper() == "KY_FOR":
                                fr.append(ifn)  
                except:
                    if str(xx).upper() == "KY_ONE" or str(xx).upper() == "KY_TWO"\
                        or str(xx).upper() == "KY_THR" or str(xx).upper() == "KY_FOR":
                            fr.append(idn)
            else:
                raise TypeError("EMPTY KEY DICTIONARY - ERROR")
        return fr
    def __repr__(self):
        pp = self._GETINFO()
        return pp

