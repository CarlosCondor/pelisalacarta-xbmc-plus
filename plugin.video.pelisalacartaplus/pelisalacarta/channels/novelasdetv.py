# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para novelasdetv
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

DEBUG = config.get_setting("debug")

__category__ = "A"
__type__ = "generic"
__title__ = "Novelas de TV"
__channel__ = "novelasdetv"
__language__ = "ES"
__creationdate__ = "20121112"

def isGeneric():
    return True

def mainlist(item):
    logger.info("[novelasdetv.py] mainlist")
    return series(Item(url="http://www.novelasdetv.com", channel=__channel__))

def series(item):
    logger.info("[novelasdetv.py] series")
    itemlist = []
    
    data = scrapertools.cache_page(item.url)

    data = scrapertools.get_match(data,'<div class="accordion" id="accordion2">(.*?)</aside>')
    '''
    <div class="accordion-group">
    <div class="accordion-heading">
    <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseTwo">
    Mas novelas
    </a>
    </div>
    <div id="collapseTwo" class="accordion-body collapse">
    <div class="accordion-inner">
    <ul class="nav nav-list">
    <li><a href=" http://www.novelasdetv.com/2012/01/capitulos-de-abismo-de-pasion-completos-online.html">Abismo de Pasion</a></li>
    <li><a href="http://www.novelasdetv.com/2012/11/capitulos-de-te-presento-a-valentin-completos-online.html">Te presento a Valentin</a></li>
    <li><a href='http://www.novelasdetv.com/2012/08/capitulos-de-quien-quiere-casarse-con.html'>&#191;Quién quiere casarse con mi hijo?</a></li>
    </ul>
    </div>
    </div>
    '''

    patron = "<li><a href=([^>]+)>([^<]+)</a></li>"
    matches = re.compile(patron,re.DOTALL).findall(data)    

    for scrapedurl,scrapedtitle in matches:
        title = scrapedtitle
        url = urlparse.urljoin(item.url,scrapedurl.strip()[1:-1].strip())
        thumbnail = ""
        plot = ""
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"]")

        itemlist.append( Item(channel=__channel__, action="episodios" , title=title , url=url, thumbnail=thumbnail, plot=plot))        

    itemlist = sorted(itemlist, key=lambda item: item.title.lower())

    return itemlist

def episodios(item):
    logger.info("[novelasdetv.py] episodios")

    # Descarga la pagina

    data = scrapertools.cache_page(item.url)
    data = scrapertools.get_match(data,'<section class="redes-sociales".*?</section>(.*?)<aside')
    logger.info("data="+data)

    #<a href="http://www.novelasdetv.com/2012/11/escobar-el-patron-del-mal-capitulo-109.html" target="_blank">Escobar Capitulo 109 Online</a><br />
    patron = '<a href="([^"]+)[^>]+>([^<]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    itemlist = []
    
    for scrapedurl,scrapedtitle in matches:
        title = scrapedtitle.strip()
        url = urlparse.urljoin(item.url,scrapedurl)
        thumbnail = ""
        plot = ""
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"]")

        if "Cabalas para este " not in title:
            itemlist.append( Item(channel=__channel__, action="findvideos" , title=title , url=url, thumbnail=thumbnail, fanart=thumbnail, plot=plot, viewmode="movie_with_plot"))

    if len(itemlist)==0:
        itemlist.append( Item(channel=__channel__, action="" , title="No hay episodios de esta serie en la web"))
    
    return itemlist

def findvideos(item):
    data = scrapertools.cache_page(item.url)
    itemlist = []
    logger.info("data="+data)
    
    #http://content2.catalog.video.msn.com/e2/ds/09d8b24e-203e-4a3a-b374-e920eb78a081.mp4
    #http://content4.catalog.video.msn.com/e2/ds/69c13d8c-913e-42d7-bf43-fa157e16e97d.mp4& 
    patron='(http:\//[a-z0-9\.]+msn.com/[a-z0-9\/\-]+\.mp4)'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl in matches:
        logger.info("patron 1="+scrapedurl)
        itemlist.append( Item(channel=__channel__, action="play" , server="directo", title="Video en msn.com" , url=scrapedurl, folder=False))

    #http://content4.catalog.video.msn.com/e2/ds/69c13d8c-913e-42d7-bf43-fa157e16e97d.flv& 
    patron='(http:\//[a-z0-9\.]+msn.com/[a-z0-9\/\-]+\.flv)'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl in matches:
        logger.info("patron 2="+scrapedurl)
        itemlist.append( Item(channel=__channel__, action="play" , server="directo", title="Video en msn.com" , url=scrapedurl, folder=False))

    #<param name="flashvars" value="file=http://gbs04.esmas.com/m4v/boh/poamo/fda5ed7787b1f6fddcbfc296778fa8d9/b1f6fddcbf-480.mp4&
    patron='(http:\//[a-z0-9\.]+esmas.com/[a-z0-9\/\-]+\.mp4)'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl in matches:
        logger.info("patron 3="+scrapedurl)
        itemlist.append( Item(channel=__channel__, action="play" , server="directo", title="Video en esmas.com" , url=scrapedurl, folder=False))

    #http://capitulosdenovela.net/refugio-c001.mp4
    patron='(http://capitulosdenovela.net/[a-z0-9A-Z\/\-]+\.mp4)'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl in matches:
        logger.info("patron 3="+scrapedurl)
        itemlist.append( Item(channel=__channel__, action="play" , server="directo", title="Video en capitulosdenovela.net" , url=scrapedurl, folder=False))

    #http://cinechulo.com/series/el_capo2/capitulo73.html
    patron  = '(http://cinechulo.com/[A-Z0-9a-z\-\_\/]+.html)'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl in matches:
        logger.info("patron 4="+scrapedurl)
        itemlist.append( Item(channel=__channel__, action="play" , server="directo", title="Video en cinechulo.com" , url=scrapedurl, extra = item.url, folder=False))

    listavideos = servertools.findvideos(data=data)
    for video in listavideos:
        scrapedurl = video[1]
        server = video[2]
        scrapedtitle = "Ver en "+server
        
        itemlist.append( Item(channel=item.channel, title=scrapedtitle , action="play" , server=server, url=scrapedurl, folder=False) )

    return itemlist

def play(item):

    itemlist = []

    if "cinechulo" in item.url:
        headers = []
        headers.append(['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14'])
        headers.append(['Referer',item.extra])
        data = scrapertools.cache_page( item.url , headers=headers )
        logger.info("data="+data)
        
        # Sigue los pasos
        form_action = scrapertools.get_match(data,'form action="([^"]+)"')
        data = scrapertools.cache_page( form_action , headers=headers , post="url="+item.extra )
        logger.info("data="+data)
        
        location = scrapertools.get_match(data,"file=(.*?)&")

        itemlist.append( Item(channel=__channel__, action="play" , server="directo", title=item.title , url=location, folder=False))

    else:
        itemlist.append( Item(channel=__channel__, action="play" , server="directo", title=item.title , url=item.url, folder=False))

    return itemlist

# Verificación automática de canales: Esta función debe devolver "True" si todo está ok en el canal.
def test():
    bien = True
    
    # mainlist
    serie_itemlist = mainlist(Item())
    
    # Comprueba que todas las opciones tengan algo (excepto el buscador)
    for serie_item in serie_itemlist:
        episodio_itemlist = episodios(serie_item)

        for episodio_item in episodio_itemlist:
            mirrors = findvideos(item=episodio_item)
            if len(mirrors)>0:
                return True

    return False