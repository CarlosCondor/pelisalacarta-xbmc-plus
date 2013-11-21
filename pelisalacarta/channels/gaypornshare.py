# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para gaypornshare.com
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os,sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

#from pelisalacarta import buscador

__channel__ = "gaypornshare"
__category__ = "D"
__type__ = "generic"
__title__ = "gaypornshare"
__language__ = "ES"

DEBUG = config.get_setting("debug")

IMAGES_PATH = os.path.join( config.get_runtime_path(), 'resources' , 'images' , 'gaypornshare' )

def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)
    
def isGeneric():
    return True

def mainlist(item):
    logger.info("[gaypornshare.py] mainlist")

    itemlist = []
    itemlist.append( Item(channel=__channel__, action="lista"  , title="Todas las Películas" , url="http://gaypornshare.org/page/1/",thumbnail="http://t1.pixhost.org/thumbs/3282/12031567_a152063_xlb.jpg"))    
    itemlist.append( Item(channel=__channel__, title="Buscar"     , action="search") )
    return itemlist







def lista(item):
    logger.info("[gaypornshare.py] lista")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.downloadpageGzip(item.url)
    #logger.info(data)



    # Extrae las entradas (carpetas)
 #<div class="post" id="post-xxx> <a href="http://gaypornshare.org/a-toy-story-2013/" title="A Toy Story (2013)"><img width="240" height="170" src="http://gaypornshare.org/wp-content/uploads/2013/07/18132279_a168223_xlb-300x213.jpg" class="attachment-240x180 wp-post-image" alt="A Toy Story (2013)" title="" /></a>
                        
    patronvideos ='<div class="post" id="post-.*?<a href="([^"]+)".*?<img.*?src="([^"]+)".*?alt="([^"]+)".*?</a>'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        scrapedtitle = match[2]
        scrapedtitle = scrapedtitle.replace("&#8211;","-")
        scrapedtitle = scrapedtitle.replace("&#8217;","'")
        scrapedurl = match[0]
        scrapedthumbnail = match[1]
        imagen = ""
        scrapedplot = match[0]  
        tipo = match[1]
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        scrapedplot=strip_tags(scrapedplot)
        itemlist.append( Item(channel=__channel__, action="detail", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
 
 
  
  # Extrae la marca de siguiente página
#<span class="current">3</span><a href='http://gaypornshare.org/page/4/' class="inactive">
    patronvideos ="<span.*?current.*?</span><a href='([^']+)' class=\"inactive\">([^']+)</a>"
    matches2 = re.compile(patronvideos,re.DOTALL).findall(data)

    for match2 in matches2:
        scrapedtitle = ">> página "+match2[1]
        scrapedurl = match2[0]
        scrapedthumbnail = ""
        imagen = ""
        scrapedplot = match2[0]  
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="lista", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
    itemlist.append( Item(channel=__channel__, action="mainlist", title="<< volver al inicio",  folder=True) )
 
    return itemlist







def search(item,texto):
    logger.info("[gaypornshare.py] search")
    itemlist = []

    # descarga la pagina
    data=scrapertools.downloadpageGzip("http://gaypornshare.org/?s="+texto)

    
    # Extrae las entradas (carpetas)
    #<div class="post" id="post-xxx><a href="http://gaypornshare.org/navigaytor-2007/" title="NaviGayTor (2007)"><img width="240" height="170" src="http://gaypornshare.org/wp-content/uploads/2013/07/18130228_a114299_xlb-300x213.jpg" class="attachment-240x180 wp-post-image" alt="NaviGayTor (2007)" title="" /></a>
            
    patronvideos ='<div class="post" id="post-.*?<a href="([^"]+)".*?<img.*?src="([^"]+)".*?alt="([^"]+)".*?</a>'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        scrapedtitle = match[2]
        scrapedtitle = scrapedtitle.replace("&#8211;","-")
        scrapedtitle = scrapedtitle.replace("&#8217;","'")
        scrapedurl = match[0]
        scrapedthumbnail = match[1]
        imagen = ""
        scrapedplot = match[0]  
        tipo = match[1]
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        scrapedplot=strip_tags(scrapedplot)
        itemlist.append( Item(channel=__channel__, action="detail", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
 

   
  # Extrae la marca de siguiente página
    patronvideos ="<span.*?current.*?</span><a href='([^']+)' class=\"inactive\">([^']+)</a>"
    matches2 = re.compile(patronvideos,re.DOTALL).findall(data)

    for match2 in matches2:
        scrapedtitle = ">> página"+match2[1]
        scrapedurl = match2[0]
        scrapedthumbnail = ""
        imagen = ""
        scrapedplot = match2[0]  
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="lista", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
    itemlist.append( Item(channel=__channel__, action="mainlist", title="<< volver al inicio",  folder=True) )
 

    return itemlist







def detail(item):
    logger.info("[gaypornshare.py] detail")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.downloadpageGzip(item.url)
    
    #busca los adf.ly
    #<a href="http://adf.ly/S72Kc">TheFarm.avi 1.4 GB</a>
    patron = '<a href="http.//adf.ly/([^"]+)">([^>]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    
    for match in matches:
        titulo="[con adf.ly] "+match[1]
        enlace="http://adf.ly/"+match[0]
        itemlist.append( Item(channel=__channel__ , action="getadfly" ,  server="adfly",  title=titulo, url=enlace, thumbnail=item.thumbnail, plot=item.plot, folder=False))


    # Busca los enlaces a los videos de los servidores
    video_itemlist = servertools.find_video_items(data=data)
    for video_item in video_itemlist:
        itemlist.append( Item(channel=__channel__ , action="play" , server=video_item.server, title=item.title+video_item.title, url=video_item.url, thumbnail=item.thumbnail, plot=item.plot, folder=False))

    return itemlist
    
    

 
def getadfly(item):
    logger.info("[gaypornshare.py] play")
    itemlist=[]

    location = item.url
    if item.server=="adfly":

    
        # Extrae la URL de saltar el anuncio en adf.ly
        if location.startswith("http://adf"):
            # Averigua el enlace
            from servers import adfly
            location = adfly.get_long_url(location)
            logger.info("location="+location)

        from servers import servertools
        itemlist=servertools.find_video_items(data=location)
        for videoitem in itemlist:
            videoitem.channel=__channel__
            videoitem.folder=False

    else:
        itemlist.append(item)

    return itemlist

