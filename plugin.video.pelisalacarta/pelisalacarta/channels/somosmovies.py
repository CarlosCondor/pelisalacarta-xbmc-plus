# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para somosmovies
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "somosmovies"
__category__ = "F,S,D,A"
__type__ = "generic"
__title__ = "Somosmovies"
__language__ = "ES"

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("[somosmovies.py] mainlist")

    itemlist = []
    itemlist.append( Item(channel=__channel__, title="Películas"    , action="listado", url="http://www.somosmovies.com"))
    itemlist.append( Item(channel=__channel__, title="Series"       , action="listado", url="http://www.somosmovies.com/search/label/Series?max-results=12"))
    itemlist.append( Item(channel=__channel__, title="Anime"        , action="listado", url="http://www.somosmovies.com/search/label/Anime?max-results=12"))
    
    return itemlist

def listado(item):
    logger.info("[somosmovies.py] listado")
    itemlist=[]

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    logger.info("data="+data)

    # Extrae las entradas
    '''
    <article CLASS='post crp'>
    <header><h3 CLASS='post-title entry-title item_name'>
    <a href='http://www.somosmovies.com/2013/09/guerra-mundial-z-2013.html' title='Guerra Mundial Z (2013)'>Guerra Mundial Z (2013)</a>
    </h3>
    </header>
    <section CLASS='post-body entry-content clearfix'>
    <a href='http://www.somosmovies.com/2013/09/guerra-mundial-z-2013.html' title='Guerra Mundial Z (2013)'><center>
    <img border="0" src="http://2.bp.blogspot.com/-u89RQDpP3kk/UiYWrGIM9kI/AAAAAAAADQw/RVI_sadottc/s1600/poster.jpg" style="display: block; height: 400px; width: 312px;">
    </center>
    </a>
    <div CLASS='es-LAT'></div>
    '''
    patron = "<article(.*?)</article>"
    matches = re.compile(patron,re.DOTALL).findall(data)

    for match in matches:
        logger.info("match="+match)
        scrapedtitle = scrapertools.get_match(match,"<a href='[^']+' title='([^']+)'")
        scrapedurl = urlparse.urljoin(item.url, scrapertools.get_match(match,"<a href='([^']+)' title='[^']+'") )
        scrapedplot = ""
        scrapedthumbnail = urlparse.urljoin(item.url, scrapertools.get_match(match,'<img border="0" src="([^"]+)"') )
        try:
            idioma = scrapertools.get_match(match,"</center[^<]+</a[^<]+<div CLASS='([^']+)'></div>")
            scrapedtitle = scrapedtitle + " ("+idioma.upper()+")"
        except:
            pass
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")

        # Añade al listado de XBMC
        itemlist.append( Item(channel=__channel__, action="findvideos", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )

    # Extrae el paginador
    #<a CLASS='blog-pager-older-link' href='http://www.somosmovies.com/search?updated-max=2012-08-22T23:10:00-05:00&amp;max-results=16' id='Blog1_blog-pager-older-link' title='Siguiente Película'>Siguiente &#187;</a>
    patronvideos  = "<a CLASS='blog-pager-older-link' href='([^']+)' id='Blog1_blog-pager-older-link' title='Siguiente"
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        #http://www.somosmovies.com/search/label/Peliculas?updated-max=2010-12-20T08%3A27%3A00-06%3A00&max-results=12
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        scrapedurl = scrapedurl.replace("%3A",":")
        itemlist.append( Item(channel=__channel__, action="listado", title=">> Página siguiente" , url=scrapedurl , folder=True) )

    return itemlist

def findvideos(item):
    logger.info("[somosmovies.py] findvideos")
    itemlist = []
    
    data = scrapertools.cachePage(item.url)
    
    '''
    <fieldset id="enlaces">
    <legend>Enlaces</legend><br />
    <div class="clearfix uno">
    <div class="dos"><b>1 LINK</b></div>
    <div class="tres">
    <a href="http://goo.gl/5l89YA" target="_blank">MEGA</a> <b class="sep">|</b> <a href="http://bit.ly/17KEYve" target="_blank">1Fichier</a> <b class="sep">|</b> <a href="http://bit.ly/1ebJqnZ" target="_blank">PutLocker</a> <b class="sep">|</b> <a href="http://bit.ly/17CpCFv" target="_blank">DepositFiles</a> <b class="sep">|</b> <a href="http://bit.ly/1dDVI9U" target="_blank">180upload</a> <b class="sep">|</b> <a href="http://bit.ly/19fLsQi" target="_blank">TurboBit</a><br />
    </div>
    </div>
    </fieldset>
    '''
    '''
    <fieldset id="enlaces">
    <legend>Enlaces</legend><br />
    <div class="clearfix uno">
    <div class="dos"><b> Capítulo 1</b>: Pilot</div><div class="tres"><a href="http://bit.ly/15w2hna" target="_blank">MEGA</a> <b class="sep">|</b> <a href="http://bit.ly/15xqoHo" target="_blank">1Fichier</a> <b class="sep">|</b> <a href="http://bit.ly/16MaoML" target="_blank">PutLocker</a> <b class="sep">|</b> <a href="http://bit.ly/16Mat2R" target="_blank">SockShare</a> <b class="sep">|</b> <a href="http://goo.gl/Amu9in" target="_blank">TurboBit</a> <b class="sep">|</b> <a href="http://bit.ly/19CBYxV" target="_blank">FreakShare</a></div>
    </div>
    </fieldset>
    '''
    # Se queda con la caja de enlaces
    data = scrapertools.get_match(data,'<fieldset id="enlaces"[^<]+<legend>Enlaces</legend>(.*?)</fieldset>')
    
    try:
        # Se queda con los enlaces 1 LINK
        data = scrapertools.get_match(data,'<div class="clearfix uno"[^<]+<div class="dos"><b>1 LINK</b></div[^<]+<div class="tres">(.*?)</div[^<]+</div>')
        patron = '<a href="([^"]+)"[^>]+>([^<]+)</a>'
        matches = re.compile(patron,re.DOTALL).findall(data)
        for url,title in matches:
            itemlist.append( Item(channel=__channel__, action="play" , title=title , url=url, thumbnail=item.thumbnail, plot=item.plot, server="", folder=False))
    except:
        import traceback
        logger.info(traceback.format_exc())

    if len(itemlist)==0:
        data = scrapertools.get_match(data,'<div class="clearfix uno"[^<]+<div class="dos">(.*?)</div[^<]+</div>')
        patron = '<a href="([^"]+)"[^>]+>([^<]+)</a>'
        matches = re.compile(patron,re.DOTALL).findall(data)
        for url,title in matches:
            itemlist.append( Item(channel=__channel__, action="play" , title=title , url=url, thumbnail=item.thumbnail, plot=item.plot, server="", folder=False))

    return itemlist

def play(item):
    logger.info("[somosmovies.py] play(item.url="+item.url+")")
    itemlist=[]

    if "goo.gl" in item.url:
        logger.info("Acortador goo.gl")
        location = scrapertools.get_header_from_response(item.url,header_to_get="location")
        item.url = location
        return play(item)
    
    #adf.ly
    elif "j.gs" in item.url:
        logger.info("Acortador j.gs (adfly)")
        from servers import adfly
        location = adfly.get_long_url(item.url)
        item.url = location
        return play(item)

    else:
        from servers import servertools
        itemlist=servertools.find_video_items(data=item.url)
        for videoitem in itemlist:
            videoitem.channel=__channel__
            videoitem.folder=False

    return itemlist

# Verificación automática de canales: Esta función debe devolver "True" si todo está ok en el canal.
def test():
    bien = True

    # mainlist
    mainlist_items = mainlist(Item())
    peliculas_items = listado(mainlist_items[0])
    if len(peliculas_items)==0:
        print "No salen películas"
        return False
    
    for pelicula_item in peliculas_items:
        mirrors = findvideos(pelicula_item)
        if len(mirrors)>0:
            return True

    print "No hay ningún vídeo en la sección de películas"
    return False