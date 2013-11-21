# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para elitetorrent
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "elitetorrent"
__category__ = "F,S,D"
__type__ = "generic"
__title__ = "Elite Torrent"
__language__ = "ES"

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("[elitetorrent.py] mainlist")

    itemlist = []
    itemlist.append( Item(channel=__channel__, title="Docus y TV"     , action="peliculas", url="http://www.elitetorrent.net/categoria/6/docus-y-tv"))
    itemlist.append( Item(channel=__channel__, title="Estrenos"       , action="peliculas", url="http://www.elitetorrent.net/categoria/1/estrenos"))
    itemlist.append( Item(channel=__channel__, title="Películas"      , action="peliculas", url="http://www.elitetorrent.net/categoria/2/peliculas"))
    itemlist.append( Item(channel=__channel__, title="Peliculas HDRip", action="peliculas", url="http://www.elitetorrent.net/categoria/13/peliculas-hdrip"))
    itemlist.append( Item(channel=__channel__, title="Peliculas VOSE" , action="peliculas", url="http://www.elitetorrent.net/categoria/14/peliculas-vose"))
    itemlist.append( Item(channel=__channel__, title="Series"         , action="peliculas", url="http://www.elitetorrent.net/categoria/4/series"))
    itemlist.append( Item(channel=__channel__, title="Series VOSE"    , action="peliculas", url="http://www.elitetorrent.net/categoria/16/series-vose"))

    return itemlist

def peliculas(item):
    logger.info("[elitetorrent.py] peliculas")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    '''
    <div class="ficha ficha2">
    <a href="/torrent/17907/las-voces-del-11s-docu"><img src="thumb_fichas/17907.jpg" width="120px" border="0" alt="Imagen "/></a>
    <br/><br/>
    <a href="/torrent/17907/las-voces-del-11s-docu">Las voces del 11S (Docu)</a><hr/>
    <span class="categoria">Docus y TV</span><br/>
    <span class="popularidad">Popularidad: 0 ptos</span><br/>
    <span class="fecha">13-09-2012</span></div>
    '''
    patron = '<div class="ficha ficha2">[^<]+'
    patron += '<a[^<]+<img src="([^"]+)"[^<]+</a>[^<]+'
    patron += '<br/><br/>[^<]+'
    patron += '<a href="([^"]+)">([^<]+)</a>'

    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedthumbnail,scrapedurl,scrapedtitle in matches:
        title = scrapedtitle.strip()
        url = urlparse.urljoin(item.url,scrapedurl)
        thumbnail = urlparse.urljoin(item.url,scrapedthumbnail)
        plot = ""
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="play", title=title , url=url , thumbnail=thumbnail , plot=plot , folder=False) )

    # Extrae el paginador
    patronvideos  = '<a href="([^"]+)" class="pagina pag_sig">Siguiente \&raquo\;</a>'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=__channel__, action="peliculas", title="Página siguiente >>" , url=scrapedurl , folder=True) )

    return itemlist

def play(item):
    logger.info("[elitetorrent.py] play")
    itemlist = []

    data = scrapertools.cache_page(item.url)
    logger.info("data="+data)
    #<a href="magnet:?xt=urn:btih:d6wtseg33iisp7jexpl44wfcqh7zzjuh&amp;dn=Abraham+Lincoln+Cazador+de+vampiros+%28HDRip%29+%28EliteTorrent.net%29&amp;tr=http://tracker.torrentbay.to:6969/announce" class="enlace_torrent degradado1">Descargar por magnet link</a> 
    link = scrapertools.get_match(data,'<a href="(magnet[^"]+)" class="enlace_torrent[^>]+>Descargar por magnet link</a>')
    link = urlparse.urljoin(item.url,link)
    logger.info("link="+link)

    itemlist.append( Item(channel=__channel__, action="play", server="torrent", title=item.title , url=link , thumbnail=item.thumbnail , plot=item.plot , folder=False) )

    return itemlist