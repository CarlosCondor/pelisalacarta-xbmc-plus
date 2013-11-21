# -*- coding: iso-8859-1 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para cine-adicto.com by Bandavi
# Actualización Carles Carmona 15/08/2011
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os
import sys

from core import scrapertools
from core import config
from core import logger
from core.item import Item
from pelisalacarta import buscador
from servers import servertools

__channel__ = "teledocumentales"
__category__ = "D"
__type__ = "generic"
__title__ = "Teledocumentales"
__language__ = "ES"
__creationdate__ = "20111019"


DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("[teledocumentales.py] mainlist")

    itemlist = []
    itemlist.append( Item(channel=__channel__ , action="ultimo"        , title="Últimos Documentales"    , url="http://www.teledocumentales.com/"))
    itemlist.append( Item(channel=__channel__ , action="ListaCat"          , title="Listado por Genero"            , url="http://www.teledocumentales.com/"))
    itemlist.append( Item(channel=__channel__, title="Buscar", action="search") )
    
    return itemlist

def ultimo(item):
    logger.info("[telecodocumentales.py] Ultimos")

    url = item.url
                  
    data = scrapertools.cachePage(url)

    # Extrae las entradas (carpetas)
    
    #<div class="slidethumb">
    #<a href="http://www.cine-adicto.com/transformers-dark-of-the-moon.html"><img src="http://www.cine-adicto.com/wp-content/uploads/2011/09/Transformers-Dark-of-the-moon-wallpaper.jpg" width="638" alt="Transformers: Dark of the Moon 2011" /></a>
    #</div>

    patron = '<div class="imagen">(.*?)<div class="lista_videos_fecha">'
    matches = re.compile(patron,re.DOTALL).findall(data)
    logger.info("hay %d matches" % len(matches))
    

    itemlist = []
    for match in matches:
        data2 = match
        patron  = '<img src="(.*?)" alt=".*?'
        patron  += '<a href="(.*?)">(.*?)</a>'
        matches2 = re.compile(patron,re.DOTALL).findall(data2)
        logger.info("hay %d matches2" % len(matches2))

        for match2 in matches2:
            scrapedtitle = match2[2].replace("&#8211;","-").strip()
            scrapedurl = match2[1]
            scrapedthumbnail = match2[0].replace(" ","%20")
            scrapedplot = ""
            
            itemlist.append( Item(channel=item.channel , action="detail"  , title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail, plot=scrapedplot , fanart=scrapedthumbnail ))

    #Extrae la marca de siguiente p�gina
    #<span class='current'>1</span><a href='http://delatv.com/page/2' class='page'>2</a>
    patronvideos = '<div class="navigation">.*?<a href="([^"]+)" class="next">.*?'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)
    
    
    if len(matches)>0:
        scrapedtitle = "Página siguiente"
        scrapedurl = matches[0]#matches[0]
        scrapedthumbnail = ""
        scrapedplot = ""
        itemlist.append( Item(channel=item.channel , action="ultimo"  , title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail, plot=scrapedplot ))

    return itemlist

def search(item,texto):
    logger.info("[teledocumentales.py] search")
    item.url = "http://www.teledocumentales.com/?s="+texto
    itemlist = []
    itemlist.extend(ultimo(item))
    return itemlist

def detail(item):
    logger.info("[cineadicto.py] detail")

    title = item.title
    thumbnail = item.thumbnail
    plot = item.plot
    scrapedurl = ""
    url = item.url

    itemlist = []

    # Descarga la p�gina
    data = scrapertools.cachePage(url)
    
    # Usa findvideos    
    listavideos = servertools.findvideos(data)
    
    itemlist = []
    
    for video in listavideos:
        server = video[2]
        scrapedtitle = item.title + " [" + server + "]"
        scrapedurl = video[1]
        
        itemlist.append( Item(channel=__channel__, action="play" , title=scrapedtitle , url=scrapedurl, thumbnail=item.thumbnail, plot=item.plot, server=server, folder=False))



    return itemlist

def ListaCat(item):
    logger.info("[telecodocumentales.py] Ultimos")

    url = item.url
                  
    data = scrapertools.cachePage(url)

    # Extrae las entradas (carpetas)
    
    #<div class="slidethumb">
    #<a href="http://www.cine-adicto.com/transformers-dark-of-the-moon.html"><img src="http://www.cine-adicto.com/wp-content/uploads/2011/09/Transformers-Dark-of-the-moon-wallpaper.jpg" width="638" alt="Transformers: Dark of the Moon 2011" /></a>
    #</div>

    patron = '<div id="menu_horizontal">(.*?)<div class="cuerpo">'
    matches = re.compile(patron,re.DOTALL).findall(data)
    logger.info("hay %d matches" % len(matches))
    

    itemlist = []
    for match in matches:
        data2 = match
        patron  = '<li class="cat-item cat-item-.*?<a href="(.*?)".*?>(.*?)</a>.*?</li>'
        matches2 = re.compile(patron,re.DOTALL).findall(data2)
        logger.info("hay %d matches2" % len(matches2))

        for match2 in matches2:
            scrapedtitle = match2[1].replace("&#8211;","-").replace("&amp;","&").strip()
            scrapedurl = match2[0]
            scrapedthumbnail = match2[0].replace(" ","%20")
            scrapedplot = ""
            
            itemlist.append( Item(channel=item.channel , action="ultimo"  , title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail, plot=scrapedplot , fanart=scrapedthumbnail ))

    return itemlist

# Verificación automática de canales: Esta función debe devolver "True" si todo está ok en el canal.
def test():
    # mainlist
    mainlist_items = mainlist(Item())
    
    # Da por bueno el canal si alguno de los vídeos de "Ultimos videos" devuelve mirrors
    ultimos_items = ultimo(mainlist_items[0])
    
    bien = False
    for ultimo_item in ultimos_items:
        play_items = detail(ultimo_item)
        if len(play_items)>0:
            return True
    
    return False