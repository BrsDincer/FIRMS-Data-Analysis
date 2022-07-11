class _NUMERICRESULT(object):
    def __new__(cls,datainit,params:str):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,datainit,params:str):
        self.__dat = datainit
        self.__prm = params
    def __str__(self):
        return "NUMERIC RESULTS - USE FOR THAT PURPOSE"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _GET_MAX(self):
        return self.__dat[self.__prm].max()
    def _GET_MIN(self):
        return self.__dat[self.__prm].min()
    def _GET_MEAN(self):
        return self.__dat[self.__prm].mean()
    def _GET_ALL(self):
        yield self._GET_MAX()
        yield self._GET_MIN()
        yield self._GET_MEAN()
    def __repr__(self):
        mlst = list(self._GET_ALL())
        return f"""
    
MAXIMUM:            {mlst[0]}
MINIMUM:            {mlst[1]}
MEAN   :            {mlst[2]}
    
    
    
    
    """
        