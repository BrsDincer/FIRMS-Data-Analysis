import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode,plot
import matplotlib.pyplot as plt
import pandas as pd

class _PLOTGRAPH(object):
    init_notebook_mode()
    def __new__(cls,datainit):
        retobj = object.__new__(cls)
        return retobj
    def __init__(self,datainit):
        self.__dat = datainit
        self.__prj = "orthographic"
    def _LINE(self,pone,ptwo,title:str):
        fg = px.line(x=self.__dat[pone],y=self.__dat[ptwo],title=title)
        fg.write_html("www/lineplot.html")
    def _GEO(self,lon,lat,dat,title):
        lon = self.__dat[lon]
        lat = self.__dat[lat]
        dat = self.__dat[dat]
        fig = go.Figure(data=go.Scattergeo(lon=lon,
                                           lat=lat,
                                           mode="markers",
                                           marker_color=dat))
        fig.update_layout(title=title,
                          geo=go.layout.Geo(projection_type=self.__prj))
        fig.update_geos(resolution=50,
                        showcoastlines=True,
                        showland=True,
                        showcountries=True,
                        lataxis_showgrid=True,
                        lonaxis_showgrid=True,
                        landcolor="#000000",
                        oceancolor="#0000ff",
                        coastlinecolor="#FF0000")
        fig.write_html("www/geoplot.html")
    def _HEAT(self,lon,lat,dat,title,animate:str="on",dayt:str="time"):
        if animate.lower() == "on":
            if dayt.lower() == "time":
                fig = px.density_mapbox(self.__dat,
                                        lat=lat,
                                        lon=lon,
                                        z=dat,
                                        radius=17,
                                        center=(dict(lat=38.96,lon=35.24)),
                                        zoom=4,
                                        mapbox_style="stamen-terrain",
                                        color_continuous_scale=px.colors.sequential.Hot,
                                        animation_frame='acq_time')
                fig.update_layout(title=title)
                fig.write_html("www/heat.html")
            elif dayt.lower() == "day":
                fig = px.density_mapbox(self.__dat,
                                        lat=lat,
                                        lon=lon,
                                        z=dat,
                                        radius=17,
                                        center=(dict(lat=38.96,lon=35.24)),
                                        zoom=4,
                                        mapbox_style="stamen-terrain",
                                        color_continuous_scale=px.colors.sequential.Hot,
                                        animation_frame='acq_date')
                fig.update_layout(title=title)
                fig.write_html("www/heat.html")
            else:
                raise UserWarning("USE ONLY TIME/DAY") 
        elif animate.lower() == "off":
            fig = px.density_mapbox(self.__dat,
                                    lat=lat,
                                    lon=lon,
                                    z=dat,
                                    radius=17,
                                    center=(dict(lat=38.96,lon=35.24)),
                                    zoom=4,
                                    mapbox_style="stamen-terrain",
                                    color_continuous_scale=px.colors.sequential.Hot)
            fig.update_layout(title=title)
            fig.write_html("www/heat.html")
    def _BAR(self,dato,datt,dath,none,ntwo,nthr,dayt:str="time"):
        dato = self.__dat[dato]
        datt = self.__dat[datt]
        dath = self.__dat[dath]
        fig = go.Figure()
        if dayt.lower() == "time":
            fig.add_trace(go.Bar(name=none,x=self.__dat["acq_time"],y=dato))
            fig.add_trace(go.Bar(name=ntwo,x=self.__dat["acq_time"],y=datt))
            fig.add_trace(go.Bar(name=nthr,x=self.__dat["acq_time"],y=dath))
            fig.update_layout(title=f"{none}-{ntwo}-{nthr}")
            fig.write_html("www/barplot.html")
        elif dayt.lower() == "day":
            fig.add_trace(go.Bar(name=none,x=self.__dat["acq_date"],y=dato))
            fig.add_trace(go.Bar(name=ntwo,x=self.__dat["acq_date"],y=datt))
            fig.add_trace(go.Bar(name=nthr,x=self.__dat["acq_date"],y=dath))
            fig.update_layout(title=f"{none}-{ntwo}-{nthr}")
            fig.write_html("www/barplot.html")
        else:
            raise UserWarning("USE ONLY TIME/DAY")
    def _MULTI_LINE(self,
                    onex,
                    onet,
                    twox,
                    twot,
                    thrx,
                    thrt,
                    dayt:str="time"):
        fgy = make_subplots(rows=1,cols=3,subplot_titles=(onet,twot,thrt))
        if dayt.lower() == "time":
            fgy.add_trace(go.Scatter(x=self.__dat["acq_time"],
                                     y=self.__dat[onex],
                                     name=onet,
                                     mode="lines"),
                          row=1,col=1)
            fgy.add_trace(go.Scatter(x=self.__dat["acq_time"],
                                     y=self.__dat[twox],
                                     name=twot,
                                     mode="lines"),
                          row=1,col=2)
            fgy.add_trace(go.Scatter(x=self.__dat["acq_time"],
                                     y=self.__dat[thrx],
                                     name=thrt,
                                     mode="lines"),
                          row=1,col=3)
            fgy.update_layout(title=f"{onet}-{twot}-{thrt}",
                              legend=dict(font_size=12),
                              xaxis_title="TIME",
                              yaxis_title="VALUE",
                              xaxis=dict(showline=True,
                                         showgrid=False,
                                         showticklabels=True,
                                         linewidth=2),
                              yaxis=dict(showline=True,
                                         showgrid=False,
                                         showticklabels=True,
                                         linewidth=2))
            fgy.write_html("www/multiline.html")
        elif dayt.lower() == "day":
            fgy.add_trace(go.Scatter(x=self.__dat["acq_date"],
                                     y=self.__dat[onex],
                                     name=onet,
                                     mode="lines"),
                          row=1,col=1)
            fgy.add_trace(go.Scatter(x=self.__dat["acq_date"],
                                     y=self.__dat[twox],
                                     name=twot,
                                     mode="lines"),
                          row=1,col=2)
            fgy.add_trace(go.Scatter(x=self.__dat["acq_date"],
                                     y=self.__dat[thrx],
                                     name=thrt,
                                     mode="lines"),
                          row=1,col=3)
            fgy.update_layout(title=f"{onet}-{twot}-{thrt}",
                              legend=dict(font_size=12),
                              xaxis_title="DATE",
                              yaxis_title="VALUE",
                              xaxis=dict(showline=True,
                                         showgrid=False,
                                         showticklabels=True,
                                         linewidth=2),
                              yaxis=dict(showline=True,
                                         showgrid=False,
                                         showticklabels=True,
                                         linewidth=2))
            fgy.write_html("www/multiline.html")
        else:
            raise UserWarning("USE ONLY TIME/DAY")
    def _MULTI_MAP(self,
                    lat,
                    lon,
                    oned,
                    twod,
                    thrd,
                    onet,
                    twot,
                    thrt):
        lon = self.__dat[lon]
        lat = self.__dat[lat]
        dato = self.__dat[oned]
        datt =self.__dat[twod]
        dath =self.__dat[thrd]
        fig = go.Figure(data=go.Scattergeo(lon=lon,
                                           lat=lat,
                                           mode="markers",
                                           marker_color=dato,
                                           name=onet))
        
        fig.add_trace(go.Scattergeo(lon=lon,
                                    lat=lat,
                                    mode="markers",
                                    marker_color=datt,
                                    name=twot))
        fig.add_trace(go.Scattergeo(lon=lon,
                                    lat=lat,
                                    mode="markers",
                                    marker_color=dath,
                                    name=thrt))
        fig.update_layout(title=f"{onet}-{twot}-{thrt}")
        fig.update_geos(resolution=50,
                        showcoastlines=True,
                        lataxis_showgrid=True,
                        lonaxis_showgrid=True)
        fig.write_html("www/multimap.html")