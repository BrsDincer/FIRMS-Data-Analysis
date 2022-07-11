class LAUNCHTEMP(object):
    def __init__(self,filetar:str):
        self.file = filetar
        self.fb = None
    def __str__(self):
        return "LOGGING AND CREATING - USE FOR THAT PURPOSE"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _WRITE(self,textinit):
        self.fb.write(textinit)
    def __enter__(self):
        self.fb = open(self.file,"w")
        return self    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.fb.close()

class _HTMLTEMP(object):
    def __new__(cls,tardir:str,savedir:str):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,tardir:str,savedir:str):
        self.__tar = tardir
        self.__sve = savedir
    def __str__(self):
        return "HTML RESULTS - USE FOR THAT PURPOSE"
    def __call__(self):
        return 
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _GET_TEMP(self):
        hmltmp = open(self.__tar,"r")
        hmltrd = hmltmp.read()
        hmltmp.close()
        return hmltrd
    def _DESIGN_TEMP_VAL(self,
                         csstar,
                         namevalone,
                         maxvalone,
                         minvalone,
                         meanvalone,
                         namevaltwo,
                         maxvaltwo,
                         minvaltwo,
                         meanvaltwo,
                         namevalthree,
                         maxvalthree,
                         minvalthree,
                         meanvalthree):
        tmph = self._GET_TEMP()
        tmph = tmph.format(css_tar=csstar,
                           one_name=namevalone.upper(),
                           max_one_data=maxvalone,
                           min_one_data=minvalone,
                           mean_one_data=meanvalone,
                           two_name=namevaltwo,
                           max_two_data=maxvaltwo,
                           min_two_data=minvaltwo,
                           mean_two_data=meanvaltwo,
                           three_name=namevalthree,
                           max_three_data=maxvalthree,
                           min_three_data=minvalthree,
                           mean_three_data=meanvalthree)
        return tmph
    def _WRITE_TEMP(self,
                    csstar,
                    namevalone,
                    maxvalone,
                    minvalone,
                    meanvalone,
                    namevaltwo,
                    maxvaltwo,
                    minvaltwo,
                    meanvaltwo,
                    namevalthree,
                    maxvalthree,
                    minvalthree,
                    meanvalthree):
        tmph = self._DESIGN_TEMP_VAL(csstar,
                                    namevalone,
                                    maxvalone,
                                    minvalone,
                                    meanvalone,
                                    namevaltwo,
                                    maxvaltwo,
                                    minvaltwo,
                                    meanvaltwo,
                                    namevalthree,
                                    maxvalthree,
                                    minvalthree,
                                    meanvalthree)
        with LAUNCHTEMP(self.__sve) as LCH:
            LCH._WRITE(tmph)
        print("\n"+f"LAST RESULT SAVED - SUCCESS / CHECK --> [ {self.__sve} ]")