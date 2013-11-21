# -*- coding: iso-8859-1 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para Movshare
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
# Credits:
# Unwise, jsunpack and main algorithm taken from Eldorado url resolver
# https://github.com/Eldorados/script.module.urlresolver/blob/master/lib/urlresolver/plugins/movshare.py

import urlparse,urllib2,urllib,re
import os

from core import scrapertools
from core import logger
from core import config
from core import unwise
from core import jsunpack

def test_video_exists( page_url ):
    logger.info("[movshare.py] test_video_exists(page_url='%s')" % page_url)

    data = scrapertools.cache_page(page_url)
    
    if "This file no longer exists on our servers" in data:
        return False,"El fichero ha sido borrado de movshare"

    return True,""

# Returns an array of possible video url's from the page_url
def get_video_url( page_url , premium = False , user="" , password="" , video_password="" ):
    logger.info("[movshare.py] get_video_url(page_url='%s')" % page_url)

    videoid = scrapertools.get_match(page_url,"http://www.movshare.net/video/([a-z0-9]+)")
    video_urls = []

    # Descarga la página
    headers = [ ['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'],['Referer','http://www.movshare.net/'] ]
    html = scrapertools.cache_page(page_url , headers = headers)
    
    # La vuelve a descargar, como si hubieras hecho click en el botón
    html = scrapertools.cache_page(page_url , headers = headers)

    """
    movshare can do both flv and avi. There is no way I know before hand
    if the url going to be a flv or avi. So the first regex tries to find 
    the avi file, if nothing is present, it will check for the flv file.
    "param name="src" is for avi
    "flashvars.file=" is for flv
    """
    r = re.search('<param name="src" value="(.+?)"', html)

    if not r:
        html = unwise.unwise_process(html)
        html = re.compile(r'eval\(function\(p,a,c,k,e,(?:d|r)\).+?\.split\(\'\|\'\).*?\)\)').search(html).group()
        html = jsunpack.unpack(html)
        filekey = unwise.resolve_var(html, "flashvars.filekey")
        
        #get stream url from api
        api = 'http://www.movshare.net/api/player.api.php?key=%s&file=%s' % (filekey, videoid)
        html = scrapertools.cache_page(api)
        logger.info("html="+html)
        r = re.search('url=(.+?)&title', html)
    if r:
        stream_url = r.group(1)
        video_urls.append( [ scrapertools.get_filename_from_url(stream_url)[-4:]+" [movshare]" , stream_url ] )

    for video_url in video_urls:
        logger.info("[movshare.py] %s - %s" % (video_url[0],video_url[1]))

    return video_urls

# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    #http://www.movshare.net/video/deg0ofnrnm8nq
    patronvideos  = 'movshare.net/video/([a-z0-9]+)'
    logger.info("[movshare.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[movshare]"
        url = "http://www.movshare.net/video/"+match

        if url not in encontrados:
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'movshare' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    #
    patronvideos  = "movshare.net/embed/([a-z0-9]+)"
    logger.info("[movshare.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[movshare]"
        url = "http://www.movshare.net/video/"+match

        if url not in encontrados:
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'movshare' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    #http://embed.movshare.net/embed.php?v=xepscujccuor7&width=1000&height=450
    patronvideos  = "movshare.net/embed.php\?v\=([a-z0-9]+)"
    logger.info("[movshare.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[movshare]"
        url = "http://www.movshare.net/video/"+match

        if url not in encontrados:
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'movshare' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    return devuelve

def test():
    #http://www.movshare.net/video/6090de0821098
    video_urls = get_video_url("http://www.movshare.net/video/6090de0821098")

    return len(video_urls)>0