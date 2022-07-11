import pandas as pd
import random as rd
import os
from __proj import _PROJECTREADING
from __conf import _CONFIGREQUESTS
from __graph import _PLOTGRAPH
from __intmap import _MAPWMSTILE
from __numeric import _NUMERICRESULT
from __returnhtml import _HTMLTEMP
from __contrdir import _CONTROLDIRECTORY

class FIRMSAnalysis(object):
    def __init__(self):
        self.__keys = _PROJECTREADING("__yaml/__project.yaml")._GET_KEY()
        self.__ini = "__con/req.ini"
    def __str__(self):
        return "FIRMS ANALYSIS - HOTPOINTS"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _READ_CSV(self,sitetar:str):
        return pd.read_csv(sitetar)
    def _GET_KEY(self):
        ky = rd.choice(self.__keys)
        return ky
    def _GET_COUNTRIES_AREAS(self):
        rpr = ""
        apr = ""
        clnt = _PROJECTREADING("__yaml/__project.yaml")._GET_COUNTRIES()
        arnt = _PROJECTREADING("__yaml/__project.yaml")._GET_AREAS()
        for xn,xl in clnt.items():
            rpr += f"{xn} : {xl}"+"\n"
        for xn,xl in arnt.items():
            apr += f"{xn} : {xl}"+"\n"
        return rpr,apr
    def _GET_SITE_ATTRIBUTES(self,daytar,plctar,tarinit):
        ky = self._GET_KEY()
        dsite = _CONFIGREQUESTS(self.__ini,str(ky),daytar,plctar,tarinit)._GET_SITE("DATA")
        kyd = dsite.keys()
        kyv = dsite.values()
        return kyd,kyv
    def _GET_DICT(self,daytar,plctar,tarinit):
        ndic = {}
        kyd,kyv = self._GET_SITE_ATTRIBUTES(daytar,plctar,tarinit)
        for xd,xv in zip(kyd,kyv):
            ndic[xd] = xv
        return ndic
    def _DOWNLOAD_CSV(self,daytar:str,typedata:str,plctar:str,tarinit:str):
        kyd = self._GET_DICT(daytar,plctar,tarinit)
        if tarinit.lower() == "area":
            datusr = input("[>>] SPECIAL DATE [YYYY-MM-DD]: ")
            std = kyd[typedata.lower()]+"/"+str(datusr)
        elif tarinit.lower() == "country":
            std = kyd[typedata.lower()]
        else:
            raise UserWarning("USE ONLY AREA/COUNTRY")
        rcsv = self._READ_CSV(std)
        dname = f"DAT_{daytar}_{str(typedata)}.csv"
        rcsv.to_csv(dname)
        print("\n"+f"DOWNLOAD - OK / SUCCESS: [ {dname} ]")
        return dname
    def _CHECK_DATA(self,dirdata:str):
        if os.path.exists(dirdata):
            rcsv = self._READ_CSV(dirdata)
            try:
                rcsv.drop(["Unnamed: 0"],axis=1,inplace=True)
            except:
                pass
            try:
                rcsv["daynight"].replace({"D":"DAY","N":"NIGHT"},inplace=True)
            except:
                pass
            return rcsv
        else:
            raise UserWarning("FILE DOES NOT EXIST - ERROR / CHECK CONNECTION OR SCRIPT PATH")
    def _GET_NUMERIC(self,dirdata:str,params:str,ops:str):
        rcsv = self._CHECK_DATA(dirdata)
        nmrc = _NUMERICRESULT(rcsv,params)
        if ops.lower() == "max":
            print(f"MAXIMUM {params.upper()}: "+str(nmrc._GET_MAX()))
        elif ops.lower() == "min":
            print(f"MINIMUM {params.upper()}: "+str(nmrc._GET_MIN()))
        elif ops.lower() == "all":
            print(nmrc.__repr__())
        else:
            raise UserWarning("USE ONLY MAX/MIN/ALL")
    def _VISUALIZATION_SINGLE(self,dirdata:str,datparams:str,dayt:str,anm:str="off"):
        rcsv = self._CHECK_DATA(dirdata)
        pltr = _PLOTGRAPH(rcsv)
        pltr._GEO("longitude","latitude",datparams,datparams.upper())
        if anm == "off":
            pltr._HEAT("longitude","latitude",datparams,datparams.upper(),anm,dayt)
        elif anm == "on":
            pltr._HEAT("longitude","latitude",datparams,datparams.upper(),anm,dayt)
        else:
            raise UserWarning("ONLY USE ON/OFF")
    def _SINGLE_LINE(self,dirdata:str,paramsone:str,paramstwo:str,title:str):
        rcsv = self._CHECK_DATA(dirdata)
        pltr = _PLOTGRAPH(rcsv)
        try:
            pltr._LINE(pone=paramsone,ptwo=paramstwo,title=title)
        except Exception as err:
            print(str(err))
            raise UserWarning("FAILED - LINE PLOT")
    def _VISUALIZATION_ALL(self,dirdata:str,dayt:str):
        rcsv = self._CHECK_DATA(dirdata)
        pltr = _PLOTGRAPH(rcsv)
        if "VIIRS_SNPP_NRT" in dirdata.upper() or\
                "VIIRS_NOAA20_NRT" in dirdata.upper() or "VIIRS_SNPP_SP" in dirdata.upper():
                    pltr._MULTI_LINE("frp",
                                     "FRP",
                                     "bright_ti4",
                                     "BRIGHTNESS T4",
                                     "bright_ti5",
                                     "BRIGHTNESS T5",
                                     dayt)
        else:
                pltr._MULTI_LINE("frp",
                                 "FRP",
                                 "brightness",
                                 "BRIGHTNESS",
                                 "bright_t31",
                                 "BRIGHTNESS T31",
                                 dayt)
        if "VIIRS_SNPP_NRT" in dirdata.upper() or\
                "VIIRS_NOAA20_NRT" in dirdata.upper() or "VIIRS_SNPP_SP" in dirdata.upper():
                    pltr._MULTI_MAP("latitude",
                                    "longitude",
                                    "frp",
                                    "bright_ti4",
                                    "bright_ti5",
                                    "FRP",
                                    "BRIGHTNESS T4",
                                    "BRIGHTNESS T5")
        else:
                pltr._MULTI_MAP("latitude",
                                "longitude",
                                "frp",
                                "brightness",
                                "bright_t31",
                                "FRP",
                                "BRIGHTNESS",
                                "BRIGHTNESS T31")
        if "VIIRS_SNPP_NRT" in dirdata.upper() or\
                "VIIRS_NOAA20_NRT" in dirdata.upper() or "VIIRS_SNPP_SP" in dirdata.upper():
                    pltr._BAR("frp",
                              "bright_ti4",
                              "bright_ti5",
                              "FRP",
                              "BRIGHTNESS T4",
                              "BRIGHTNESS T5",
                              dayt)
        else:
                pltr._BAR("frp",
                          "brightness",
                          "bright_t31",
                          "FRP",
                          "BRIGHTNESS",
                          "BRIGHTNESS T31",
                          dayt)
    def _INTERACT_MAP(self,dirdata:str,vistype:str,anm:str="off",dayt:str="time"):
        rcsv = self._CHECK_DATA(dirdata)
        try:
            _MAPWMSTILE(rcsv)._GET_DATA_MAP(tyvs=vistype,anm=anm,dayt=dayt)
        except:
            raise UserWarning("FAILED - MAP SAVING")
    def _GET_ALL(self):
        _CONTROLDIRECTORY("www")._DIR_CONTROL()
        clnt,arnt = self._GET_COUNTRIES_AREAS()
        msf = """
        
        SELECTION:
            
            
        1) MODIS_NRT
        2) MODIS_SP
        3) VIIRS_NOAA20_NRT
        4) VIIRS_SNPP_NRT
        5) VIIRS_SNPP_SP
        
        """
        print(msf)
        typusr = input("[>>] SELECT DATA: ")
        trtusr = input("[>>] SELECT PLACE RANGE [COUNTRY/AREA]: ")
        if trtusr.lower() == "country":
            print(clnt)
            plcusr = input("[>>] SELECT COUNTRY: ")
            try:
                if plcusr.upper() in _PROJECTREADING("__yaml/__project.yaml")._GET_COUNTRIES().keys():
                    plcusr = plcusr.upper()
                else:
                    print("THE COUNTRY PARAMETER YOU SELECTED IS NOT CORRECT - ERROR")
                    print("[>>] AUTOMATICALLY ADJUSTED: USA")
                    plcusr = "USA"
            except:
                print("SOMETHING IS WRONG - ERROR")
                print("[>>] AUTOMATICALLY ADJUSTED: USA")
                plcusr = "USA"
        elif trtusr.lower() == "area":
            print("\n"+arnt)
            plcusr = input("[>>] SELECT AREA: ")
            try:
                if plcusr.upper() in _PROJECTREADING("__yaml/__project.yaml")._GET_AREAS().keys():
                    plcusr = plcusr.lower()
                else:
                   print("THE AREA PARAMETER YOU SELECTED IS NOT CORRECT - ERROR")
                   print("[>>] AUTOMATICALLY ADJUSTED: WORLD")
            except:
                print("SOMETHING IS WRONG - ERROR")
                print("[>>] AUTOMATICALLY ADJUSTED: USA")
                plcusr = "world"
        dayusr = input("[>>] SELECT DAY RANGE [1-10]: ")
        visusr = input("[>>] SELECT VISUALIZATION [TIME/DATE]: ")
        print("\n"+"---"*7+"\n"+"SET THE VISUALIZATION PARAMETERS")
        anmusr = input("[>>] ANIMATION [ON/OFF]: ")
        ddmusr = input("[>>] RANGE [TIME/DAY]: ")
        xlmusr = input("[>>] DATA FOR LINE PLOT [X]: ")
        ylmusr = input("[>>] DATA FOR LINE PLOT [Y]: ")
        vlmusr = input("[>>] SPECIFIC VALUE: ")
        pdat = self._DOWNLOAD_CSV(str(dayusr),typusr.upper(),plcusr,trtusr)
        rcsv = self._CHECK_DATA(pdat)
        self._SINGLE_LINE(pdat,xlmusr,ylmusr,f"{xlmusr.upper()}-{ylmusr.upper()}")
        self._VISUALIZATION_SINGLE(pdat,vlmusr,ddmusr)
        self._VISUALIZATION_ALL(pdat,ddmusr)
        if visusr.lower() == "time":
            self._INTERACT_MAP(pdat,"heat",anmusr,"time")
        elif visusr.lower() == "date":
            self._INTERACT_MAP(pdat,"heat",anmusr,"date")
        else:
            raise UserWarning("USE ONLY TIME/DATE")
        allvalfrp = list(_NUMERICRESULT(rcsv,"frp")._GET_ALL())
        if "VIIRS_SNPP_NRT" in pdat.upper() or\
            "VIIRS_NOAA20_NRT" in pdat.upper() or "VIIRS_SNPP_SP" in pdat.upper():
                btiname = "bright_ti4"
                btmname = "bright_ti5"
                allvalbrightnesstm = list(_NUMERICRESULT(rcsv,btiname)._GET_ALL())
                allvalbrightnessti = list(_NUMERICRESULT(rcsv,btmname)._GET_ALL())
        else:
            btiname = "brightness"
            btmname = "bright_t31"
            allvalbrightnesstm = list(_NUMERICRESULT(rcsv,btiname)._GET_ALL())
            allvalbrightnessti = list(_NUMERICRESULT(rcsv,btmname)._GET_ALL())
        _HTMLTEMP("firmstemp.html.tpl","FIRMSresultMAP.html")._WRITE_TEMP("stylefirm.css",
                                                                        "frp",
                                                                        allvalfrp[0],
                                                                        allvalfrp[1],
                                                                        allvalfrp[2],
                                                                        btiname,
                                                                        allvalbrightnesstm[0],
                                                                        allvalbrightnesstm[1],
                                                                        allvalbrightnesstm[2],
                                                                        btmname,
                                                                        allvalbrightnessti[0],
                                                                        allvalbrightnessti[1],
                                                                        allvalbrightnessti[2])
    def _RETURN_COLUMN(self,dirdata):
        rcsv = self._CHECK_DATA(dirdata)
        return list(rcsv.columns)
    def __repr__(self):
        frr = "OPTIONS"+"\n"
        kyd,kyv = self._GET_SITE_ATTRIBUTES()
        for xd,xv in zip(kyd,kyv):
            frr += f"""
{xd}:  {xv}
            
            """
        return frr

if __name__ == "__main__":
    FIRMSAnalysis()._GET_ALL()