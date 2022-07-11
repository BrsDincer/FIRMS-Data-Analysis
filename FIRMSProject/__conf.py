from configparser import ConfigParser

class _CONFIGREQUESTS(object):
    def __new__(cls,confdir:str,keyinit:str,dayinit:str,placeinit:str,tarinit:str):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,confdir:str,keyinit:str,dayinit:str,placeinit:str,tarinit:str):
        self.__con = ConfigParser()
        self.__dir = confdir
        self.__key = keyinit
        self.__day = dayinit
        self.__plc = placeinit
        self.__trg = tarinit
        self.__con.read(self.__dir)
    def __str__(self):
        return "CONFIGURATION FOR REQUESTS - USE FOR THAT PURPOSE"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _GET_SECTIONS(self):
        return self.__con.sections()
    def _SET_KEY(self):
        self.__con.set("DATA","def_kys",str(self.__key))
    def _SET_DAY(self):
        if 0 < int(self.__day) <= 10:
            self.__con.set("DATA","def_day",str(self.__day))
        else:
            self.__day = self.__con.get("DATA","def_day")
            self.__con.set("DATA","def_day",str(self.__day))
    def _SET_PLACE(self):
        self.__con.set("DATA","def_plc",str(self.__plc))
    def _SET_AREA(self):
        self.__con.set("DATA","def_tar",str(self.__trg))
    def _GET_SITE(self,sectionname:str):
        self._SET_KEY()
        self._SET_DAY()
        self._SET_PLACE()
        self._SET_AREA()
        sec = self._GET_SECTIONS()
        dicd = {}
        if len(sec) > 0:
            for xi in sec:
                if xi == sectionname:
                    itm = self.__con.items(xi)
                    ltm = len(itm)
                    while ltm > 0:
                        for xn in itm:
                            if xn[0] != "def_kys" and xn[0] != "def_day" and\
                                xn[0] != "def_plc" and xn[0] != "def_are":
                                    dicd[xn[0]] = xn[1]
                        ltm -= 1
        else:
            raise UserWarning("INI FAILED - ERROR / CHECK FILE")
        return dicd
    def __repr__(self):
        sec = self._GET_SECTIONS()
        frf = ""
        if len(sec) > 0:
            for xi in sec:
                itm = self.__con.items(xi)
                for xn in itm:
                    frf += f"""
{"---"*7}
{xn[0]}:         {xn[1]}
                        
                    """
        return frf