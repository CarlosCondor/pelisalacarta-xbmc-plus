# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para mejortorrent
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "mejortorrent"
__category__ = "F,S,D"
__type__ = "generic"
__title__ = "Mejor Torrent"
__language__ = "ES"

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("[mejortorrent.py] mainlist")

    itemlist = []
    itemlist.append( Item(channel=__channel__, title="Películas"    , action="peliculas"   , url="http://www.mejortorrent.com/torrents-de-peliculas.html"))
    itemlist.append( Item(channel=__channel__, title="Series"       , action="series"      , url="http://www.mejortorrent.com/torrents-de-series.html"))
    itemlist.append( Item(channel=__channel__, title="Documentales" , action="documentales", url="http://www.mejortorrent.com/torrents-de-documentales.html"))

    return itemlist

def peliculas(item):
    logger.info("[mejortorrent.py] peliculas")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    patron  = '<a href="(/peli-descargar-torrent[^"]+)">[^<]+'
    patron += '<img src="([^"]+)"[^<]+</a>'

    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedthumbnail in matches:
        title = scrapertools.get_match(scrapedurl,"/peli-descargar-torrent-\d+-(.*?)\.html")
        title = title.replace("-"," ")
        url = urlparse.urljoin(item.url,scrapedurl)
        thumbnail = urlparse.urljoin(item.url,scrapedthumbnail)
        plot = ""
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="play", title=title , url=url , thumbnail=thumbnail , plot=plot , folder=False) )


    # Extrae el paginador
    patronvideos  = "<a href='([^']+)' class='paginar'> Siguiente >>"
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=__channel__, action="peliculas", title="Página siguiente >>" , url=scrapedurl , folder=True) )

    return itemlist

def series(item):
    logger.info("[mejortorrent.py] series")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    #<a href="/serie-descargar-torrents-11589-11590-Ahora-o-nunca-4-Temporada.html">
    #<img src="/uploads/imagenes/series/Ahora o nunca4.jpg" border="1"></a>  
    patron  = '<a href="(/serie-descargar-torrent[^"]+)">[^<]+'
    patron += '<img src="([^"]+)"[^<]+</a>'

    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedthumbnail in matches:
        title = scrapertools.get_match(scrapedurl,"/serie-descargar-torrents-\d+-\d+-(.*?)\.html")
        title = title.replace("-"," ")
        url = urlparse.urljoin(item.url,scrapedurl)
        thumbnail = urlparse.urljoin(item.url,scrapedthumbnail)
        plot = ""
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="episodios", title=title , url=url , thumbnail=thumbnail , plot=plot , folder=True) )


    # Extrae el paginador
    patronvideos  = "<a href='([^']+)' class='paginar'> Siguiente >>"
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=__channel__, action="series", title="Página siguiente >>" , url=scrapedurl , folder=True) )

    return itemlist

def episodios(item):
    logger.info("[mejortorrent.py] episodios")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    
    total_capis = scrapertools.get_match(data,"<input type='hidden' name='total_capis' value='(\d+)'>")
    tabla = scrapertools.get_match(data,"<input type='hidden' name='tabla' value='([^']+)'>")
    titulo = scrapertools.get_match(data,"<input type='hidden' name='titulo' value='([^']+)'>")
    
    #<form name='episodios' action='secciones.php?sec=descargas&ap=contar_varios' method='post'>
    data = scrapertools.get_match(data,"<form name='episodios' action='secciones.php\?sec=descargas\&ap=contar_varios' method='post'>(.*?)</form>")
    '''
    <td bgcolor='#C8DAC8' style='border-bottom:1px solid black;'>2x05 -</td>
    <td width='120' bgcolor='#C8DAC8' align='right' style='border-right:1px solid black; border-bottom:1px solid black;'><div style='color:#666666; font-size:9px; margin-right:5px;'>Fecha: 2012-08-26</div></td>
    <td width='60' bgcolor='#F1F1F1' align='center' style='border-bottom:1px solid black;'>
    <input type='checkbox' name='episodios[4]' value='11815'>
    '''
                   
    patron  = "<td bgcolor[^>]+>([^<]+)</td>[^<]+"
    patron += "<td[^<]+<div[^>]+>Fecha. ([^<]+)</div></td>[^<]+"
    patron += "<td[^<]+"
    patron += "<input type='checkbox' name='([^']+)' value='([^']+)'"

    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle,fecha,name,value in matches:
        title = scrapedtitle.strip()+" ("+fecha+")"
        url = "http://www.mejortorrent.com/secciones.php?sec=descargas&ap=contar_varios"
        #"episodios%5B1%5D=11744&total_capis=5&tabla=series&titulo=Sea+Patrol+-+2%AA+Temporada"
        post = urllib.urlencode( { name:value , "total_capis":total_capis , "tabla":tabla , "titulo":titulo } )
        logger.info("post="+post)
        thumbnail = item.thumbnail
        plot = item.plot
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="play", title=title , url=url , thumbnail=thumbnail , plot=plot , extra=post, folder=False) )

    return itemlist

def play(item):
    logger.info("[mejortorrent.py] play")
    itemlist = []

    if item.extra=="":
        data = scrapertools.cache_page(item.url)
        logger.info("data="+data)
        patron  = "<a href='(secciones.php\?sec\=descargas[^']+)'"
        matches = re.compile(patron,re.DOTALL).findall(data)
        scrapertools.printMatches(matches)
    
        for scrapedurl in matches:
            title = item.title
            url = urlparse.urljoin(item.url,scrapedurl)
            thumbnail = item.thumbnail
            plot = ""
            if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"]")
            
            torrent_data = scrapertools.cache_page(url)
            logger.info("torrent_data="+torrent_data)
            #<a href='/uploads/torrents/peliculas/los-juegos-del-hambre-brrip.torrent'>
            link = scrapertools.get_match(torrent_data,"<a href='(/uploads/torrents/peliculas/.*?\.torrent)'>")
            link = urlparse.urljoin(url,link)
    
            logger.info("link="+link)
            
            itemlist.append( Item(channel=__channel__, action="play", server="torrent", title=title , url=link , thumbnail=thumbnail , plot=plot , folder=False) )

    else:
        data = scrapertools.cache_page(item.url, post=item.extra)
        logger.info("data="+data)
        #<a href="http://www.mejortorrent.com/uploads/torrents/series/falling-skies-2-01_02.torrent"
        #<a href="http://www.mejortorrent.com/uploads/torrents/series/falling-skies-2-03.torrent"
        link = scrapertools.get_match(data,'<a href="(http.//www.mejortorrent.com/uploads/torrents/series/.*?\.torrent)"')

        logger.info("link="+link)
        
        itemlist.append( Item(channel=__channel__, action="play", server="torrent", title=item.title , url=link , thumbnail=item.thumbnail , plot=item.plot , folder=False) )

    
    return itemlist

# Verificación automática de canales: Esta función debe devolver "True" si todo está ok en el canal.
def test():
    bien = True
    
    # mainlist
    mainlist_items = mainlist(Item())
    peliculas_items = peliculas(mainlist_items[0])
    play_items = play(peliculas_items[0])
    
    if len(play_items)>0:
        return True

    return False