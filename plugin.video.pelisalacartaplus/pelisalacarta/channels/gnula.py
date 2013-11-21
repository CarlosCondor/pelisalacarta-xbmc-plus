# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para Shurweb
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os,sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "gnula"
__category__ = "F"
__type__ = "generic"
__title__ = "Gnula"
__language__ = "ES"

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("[gnula.py] getmainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="A-Z"       , action="letras"    , url="http://gnula.biz/"))
    itemlist.append( Item(channel=__channel__, title="Años"      , action="anyos"     , url="http://gnula.biz/"))
    itemlist.append( Item(channel=__channel__, title="Generos"   , action="generos"   , url="http://gnula.biz/"))
    #itemlist.append( Item(channel=__channel__, title="Buscar"    , action="search"))
    return itemlist

def generos(item):
    logger.info("[gnula.py] letras")
    itemlist = []
    
    data = scrapertools.cache_page(item.url)
    data = scrapertools.get_match(data,'<select onchange="[^"]+" id="gen_ini">(.*?)/select')
    patron = '<option value="([^"]+)">([^<]+)</option>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    if DEBUG: scrapertools.printMatches(matches)
    for url,genero in matches:
        scrapedtitle =  scrapertools.htmlclean(genero)
        scrapedplot = ""
        scrapedurl = "http://gnula.biz/"+url
        scrapedthumbnail = ""
        if DEBUG: logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action='peliculas', title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , extra=scrapedtitle) )
    
    return itemlist

def letras(item):
    logger.info("[gnula.py] letras")
    itemlist = []
    
    data = scrapertools.cache_page(item.url)
    data = scrapertools.get_match(data,'<select onchange="[^"]+" id="alf_ini">(.*?)/select')
    patron = '<option value="([^"]+)">([^<]+)</option>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    if DEBUG: scrapertools.printMatches(matches)
    for url,letra in matches:
        scrapedtitle =  letra
        scrapedplot = ""
        scrapedurl = "http://gnula.biz/"+url
        scrapedthumbnail = ""
        if DEBUG: logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action='peliculas', title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , extra=scrapedtitle) )
    
    return itemlist

def anyos(item):
    logger.info("[gnula.py] letras")
    itemlist = []
    
    data = scrapertools.cache_page(item.url)
    data = scrapertools.get_match(data,'<select onchange="[^"]+" id="emi_ini">(.*?)/select')
    patron = '<option value="([^"]+)">([^<]+)</option>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    #if DEBUG: scrapertools.printMatches(matches)
    for url,letra in matches:
        scrapedtitle =  letra
        scrapedplot = ""
        scrapedurl = "http://gnula.biz/"+url
        scrapedthumbnail = ""
        if DEBUG: logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action='peliculas', title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , extra=scrapedtitle) )
    
    return itemlist


def paises(item):
    logger.info("[gnula.py] letras")
    itemlist = []
    
    data = scrapertools.cache_page(item.url)
    data = scrapertools.get_match(data,'<select name="pais"(.*?)/select')
    patron = '<option value="([^"]+)">([^<]+)</option>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    if DEBUG: scrapertools.printMatches(matches)
    for url,pais in matches:
        scrapedtitle =  pais
        scrapedplot = ""
        scrapedurl = "http://gnula.biz/ano/"+pais
        scrapedthumbnail = ""
        if DEBUG: logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action='peliculas', title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , extra=scrapedtitle) )
    
    return itemlist

def peliculas(item,paginacion=True):
    logger.info("[gnula.py] peliculas")
    url = item.url

    '''
    <div class="boxes" style="width: 123px;">
    <a href="doc-mcstuffins-time-for-your-check-up.html">
    <span>
    <div style="height: 180px; overflow: hidden;">
    <img class="reflect rheight18 ropacity25" title="Doc McStuffins Time For Your Check Up" src="http://t3.gstatic.com/images?q=tbn:ANd9GcQd7e36SLqanfSqYOIG2cp0hQlSmdB5mdkov3Qtvcri21x04RhJkg" style="display: block;">
    '''
    # Descarga la página
    data = scrapertools.cachePage(url)
    patron  = '<div class="boxes"[^<]+'
    patron += '<a href="([^"]+)"[^<]+'
    patron += '<span[^<]+'
    patron += '<div style="[^"]+"[^<]+'
    patron += '<img class="[^"]+" title="([^"]+)" src="([^"]+)"'
    matches = re.compile(patron,re.DOTALL).findall(data)
    if DEBUG: scrapertools.printMatches(matches)
    itemlist = []
    for url,title,thumbnail in matches:
        scrapedtitle=unicode( title, "iso-8859-1" , errors="replace" ).encode("utf-8")

        fulltitle = scrapedtitle
        scrapedplot = ""
        scrapedurl = urlparse.urljoin("http://gnula.biz",url)
        scrapedthumbnail = thumbnail
        if DEBUG: logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action='findvideos', title=scrapedtitle , fulltitle=fulltitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , viewmode="movie", extra=scrapedtitle) )

    patron = "<span \"\">[^<]+</span><a href='([^']+)'>"
    matches = re.compile(patron,re.DOTALL).findall(data)
    if DEBUG: scrapertools.printMatches(matches)
    for match in matches:
        itemlist.append( Item(channel=__channel__, action='peliculas', title=">> Página siguiente" , url=urlparse.urljoin(item.url,match)) )

    return itemlist

def findvideos(item):
    logger.info("[gnula.py] findvideos")
    
    data = scrapertools.cache_page(item.url)
    itemlist = servertools.find_video_items(data=data)
    i=1
    for videoitem in itemlist:
        videoitem.title = "Ver en "+videoitem.server
        videoitem.fulltitle = item.fulltitle
        videoitem.channel=channel=__channel__
        i=i+1

    try:
        data = scrapertools.get_match(data,'<TABLE class="episodes"(.*?)</TABLE>')
        
        '''
        <TABLE class="episodes" width="900" align="center">
        <THEAD> 
        <TR> 
        <TH class="episode-title-chapter" width="135">Enlace</TH>
        <TH class="episode-server-img" width="158" align="center">Servidor</TH>
        <TH width="8" align="center"></TH>
        <TH class="center" width="87" align="center">&nbsp;</TH>
        <TH class="center" width="110" align="center">Enlaces</TH>
        <TH class="center" width="199" align="center">Compartir</TH>
        <TH class="episode-subtitle" width="171" align="center">Suscribite</TH>
        </TR> 
        </THEAD>
        <TBODY>
        <TR bgColor="#e6e3e3">
        <TD align="left"><A style="text-decoration: none;" title="Wonder Pets Ollies Slumber Party" 
        href="pelicula/wonder-pets-ollies-slumber-party.html" target="_blank"><IMG 
        src="http://www.terra.com/img/ico2006/i_video.gif" width="26" height="22"><B><FONT color="#555555">Opcion 1</FONT></B></A></TD> 
        <TD align="center"><B>Vk</B></TD> 
        <TD align="left"></TD> 
        <TD class="center" align="center"></TD> 
        <TD class="center" align="center"><A class="verLink" title="Wonder Pets Ollies Slumber Party" 
        href="pelicula/wonder-pets-ollies-slumber-party.html" target="_blank"><IMG 
        align="middle" src="http://2.bp.blogspot.com/-jsypRsEs_0s/UI3Pxb29dEI/AAAAAAAAABQ/R7-uEPFFYpA/s1600/ver.jpg" width="100" height="26"></A>    </TD> 
        <TD class="episode-uploader" align="center">
        <div class="fb-like" data-href="http://gnula.biz/wonder-pets-ollies-slumber-party.html" data-send="true" data-layout="button_count" data-width="450" data-show-faces="true"></div>
        </TD> 
        <TD style="overflow: hidden;" class="center" align="center">  <div class="fb-subscribe" data-href="http://www.facebook.com/inf.stork" data-layout="button_count" data-show-faces="true" data-width="450"></div></TD> 
        </TR></TBODY>
        </TABLE> <BR></DIV>
        <TABLE border="0" cellSpacing="0" cellPadding="6" width="960">
        <TBODY>
        '''
        
        patron  = '<TR[^<]+'
        patron += '<TD[^<]+<A.*?href="([^"]+)"[^<]+<IMG\s+src="([^"]+)"[^<]+<B><FONT[^>]+>([^<]+)</FONT></B></A></TD>[^<]+'
        patron += '<TD[^<]+<B>([^<]+)<'
        matches = re.compile(patron,re.DOTALL).findall(data)
        if DEBUG: scrapertools.printMatches(matches)

        for url,thumbnail,title,servidor in matches:
            scrapedtitle = "Ver en "+servidor.lower()+" ("+title.lower()+")"
            scrapedplot = ""
            scrapedurl = urlparse.urljoin(item.url,url)
            scrapedthumbnail = thumbnail
            if DEBUG: logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
            itemlist.append( Item(channel=__channel__, action='play', title=scrapedtitle , fulltitle=item.title , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=False) )
    except:
        pass

    return itemlist

'''
def play(item):
    logger.info("[gnula.py] play")

    itemlist=[]
    data = scrapertools.cachePage(item.url)
    logger.info("data="+data)
    itemlist = servertools.find_video_items(data=data)
    i=1
    for videoitem in itemlist:
        videoitem.title = "Mirror %d%s" % (i,videoitem.title)
        videoitem.fulltitle = item.fulltitle
        videoitem.channel=channel=__channel__
        i=i+1

    return itemlist
'''

# Verificación automática de canales: Esta función debe devolver "True" si está ok el canal.
def test():
    from servers import servertools
    # mainlist
    mainlist_items = mainlist(Item())
    # Da por bueno el canal si alguno de los vídeos de "Novedades" devuelve mirrors
    peliculas_items = peliculas(mainlist_items[0])
    bien = False
    for pelicula_item in peliculas_items:
        mirrors = servertools.find_video_items( item=pelicula_item )
        if len(mirrors)>0:
            bien = True
            break

    return bien