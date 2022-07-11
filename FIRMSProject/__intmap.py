import folium
from folium import plugins
from collections import defaultdict, OrderedDict
import yaml
import pandas as pd

def YAMLREADING(dirtar:str):
    rf = yaml.safe_load(open(dirtar,"r"))
    return rf


class _MAPWMSTILE(object):
    def __new__(cls,datainit):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,datainit):
        self.__dat = datainit
        self.__ytl = YAMLREADING("__yaml/__tilelayers.yaml")["tiles"]
        self.__dtl = "/MapServer/tile/{z}/{y}/{x}"
        self.__bse = "https://firms.modaps.eosdis.nasa.gov/map"
    def __str__(self):
        return "MAP CONTROL - USE FOR THAT PURPOSE"
    def __call__(self):
        return
    def __getstate__(self):
        raise TypeError("PICKLED - DENIED")
    def _GET_COORDINATE(self):
        lsc = list(zip(self.__dat.latitude,self.__dat.longitude))
        return lsc
    def _GET_FOR_ANIMATED(self,dayt:str="time"):
        dat = defaultdict(list)
        for rx in self.__dat.itertuples():
            if dayt.lower() == "time":
                dat[rx.acq_time].append([rx.latitude,rx.longitude])
            elif dayt.lower() == "date":
                dat[rx.acq_date].append([rx.latitude,rx.longitude])
            else:
                raise UserWarning("USE ONLY TIME/DATE")
        dat = OrderedDict(sorted(dat.items(),key=lambda xl: xl[0]))  
        return dat
    def _GET_MAP_BASE(self,tle:str="Stamen Terrain",wdth:int=1220,hght:int=550,loc:list=[36,42],zst:int=2):
        mf = folium.Map(tiles=tle,
                        width=wdth,
                        height=hght,
                        location=loc,
                        zoom_start=zst,
                        attr=f"<a href={self.__bse}>NASA FIRMS</a>")
        return mf
    def _GET_SIMPLE_MAP(self,savf:str="www/simpleMAP.html"):
        mf = self._GET_MAP_BASE()
        for xn,xu in self.__ytl.items():
            xu += self.__dtl
            folium.TileLayer(tiles=xu,
                             name=xn,
                             attr=f"<a href={self.__bse}>NASA</a>").add_to(mf)
        folium.LayerControl().add_to(mf)
        mf.save(savf)
    def _GET_DATA_MAP(self,savf:str="www/resultMAP.html",tyvs:str="norm",anm:str="off",dayt:str="time"):
        mf = self._GET_MAP_BASE()
        cr = self._GET_COORDINATE()
        plugins.MiniMap().add_to(mf)
        if tyvs.lower() == "norm":
            plugins.MarkerCluster(cr).add_to(mf)
            for xn,xu in self.__ytl.items():
                xu += self.__dtl
                folium.TileLayer(tiles=xu,
                                 name=xn,
                                 attr=f"<a href={self.__bse}>NASA</a>").add_to(mf)
            folium.LayerControl().add_to(mf)
            mf.save(savf)
            print("\n"+f"MAP / SAVED - SUCCESS / CHECK --> [ {savf} ]")
        elif tyvs.lower() == "heat":
            if anm.lower() == "off":
                plugins.HeatMap(cr).add_to(mf)
                for xn,xu in self.__ytl.items():
                    xu += self.__dtl
                    folium.TileLayer(tiles=xu,
                                     name=xn,
                                     attr=f"<a href={self.__bse}>NASA</a>").add_to(mf)
                folium.LayerControl().add_to(mf)
                mf.save(savf)
                print("\n"+f"MAP / SAVED - SUCCESS / CHECK --> {savf}")
            elif anm.lower() == "on" and dayt.lower() == "time":
                timedta = self._GET_FOR_ANIMATED(dayt="time")
                plugins.HeatMapWithTime(data=list(timedta.values()),
                                        index=list(timedta.keys()),
                                        radius=7,
                                        auto_play=True,
                                        max_opacity=0.5).add_to(mf)
                for xn,xu in self.__ytl.items():
                    xu += self.__dtl
                    folium.TileLayer(tiles=xu,
                                     name=xn,
                                     attr=f"<a href={self.__bse}>NASA</a>").add_to(mf)
                folium.LayerControl().add_to(mf)
                mf.save(savf)
                print("\n"+f"MAP / SAVED - SUCCESS / CHECK --> {savf}")
            elif anm.lower() == "on" and dayt.lower() == "date":
                datedta = self._GET_FOR_ANIMATED(dayt="date")
                plugins.HeatMapWithTime(data=list(datedta.values()),
                                        index=list(datedta.keys()),
                                        radius=7,
                                        auto_play=True,
                                        max_opacity=0.5).add_to(mf)
                for xn,xu in self.__ytl.items():
                    xu += self.__dtl
                    folium.TileLayer(tiles=xu,
                                     name=xn,
                                     attr=f"<a href={self.__bse}>NASA</a>").add_to(mf)
                folium.LayerControl().add_to(mf)
                mf.save(savf)
                print("\n"+f"MAP / SAVED - SUCCESS / CHECK --> {savf}")
            else:
                raise UserWarning("PARAMETERS - ERROR / DEFINE DAY/TIME")
        else:
            raise UserWarning("ONLY USE NORM/HEAT")