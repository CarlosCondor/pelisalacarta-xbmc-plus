# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para vidspot
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os

from core import scrapertools
from core import logger
from core import config
from core import unpackerjs,unpackerjs3

def get_video_url( page_url , premium = False , user="" , password="", video_password="" ):
    logger.info("[vidspot.py] url="+page_url)

    # Normaliza la URL
    try:
        if not page_url.startswith("http://vidspot.net/embed-"):
            videoid = scrapertools.get_match(page_url,"vidspot.net/([a-z0-9A-Z]+)")
            page_url = "http://vidspot.net/embed-"+videoid+".html"
    except:
        import traceback
        logger.info(traceback.format_exc())    

    # Lo pide una vez
    headers = [['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14']]
    data = scrapertools.cache_page( page_url , headers=headers )
    logger.info("data="+data)
    
    try:
        '''
        <input type="hidden" name="op" value="download1">
        <input type="hidden" name="usr_login" value="">
        <input type="hidden" name="id" value="d6fefkzvjc1z">
        <input type="hidden" name="fname" value="coriolanus.dvdr.mp4">
        <input type="hidden" name="referer" value="">
        <input type="hidden" name="method_free" value="1">
        <input type="image"  id="submitButton" src="/images/continue-to-video.png" value="method_free" />
        '''
        '''
        <Form name="F1" method="POST" action=''>
        <input type="hidden" name="op" value="download1">
        <input type="hidden" name="usr_login" value="">
        <input type="hidden" name="id" value="lqwa0bh2aw0n">
        <input type="hidden" name="fname" value="Cupu1x01.mp4">
        <input type="hidden" name="referer" value="">
        <input type="hidden" name="method_free" value="1">
        <input type="image"  id="submitButton" src="/images/continue-to-video.png" value="method_free" />
        <!-- <input name="confirm" type="submit" value="Continue as Free User" disabled="disabled" id="submitButton" class="confirm_button" style="width:190px;"> -->
           
        </form>
        '''
        op = scrapertools.get_match(data,'<input type="hidden" name="op" value="([^"]+)"')
        usr_login = ""
        id = scrapertools.get_match(data,'<input type="hidden" name="id" value="([^"]+)"')
        fname = scrapertools.get_match(data,'<input type="hidden" name="fname" value="([^"]+)"')
        referer = scrapertools.get_match(data,'<input type="hidden" name="referer" value="([^"]*)"')
        method_free = scrapertools.get_match(data,'<input type="hidden" name="method_free" value="([^"]*)"')
        submitbutton = scrapertools.get_match(data,'<input type="image"  id="submitButton".*?value="([^"]+)"').replace(" ","+")
        
        import time
        time.sleep(10)
        
        # Lo pide una segunda vez, como si hubieras hecho click en el banner
        #op=download1&usr_login=&id=d6fefkzvjc1z&fname=coriolanus.dvdr.mp4&referer=&method_free=1&x=109&y=17
        post = "op="+op+"&usr_login="+usr_login+"&id="+id+"&fname="+fname+"&referer="+referer+"&method_free="+method_free+"&x=109&y=17"
        headers.append(["Referer",page_url])
        data = scrapertools.cache_page( page_url , post=post, headers=headers )
        logger.info("data="+data)
    except:
        pass
    
    # Extrae la URL
    media_url = scrapertools.get_match( data , '"file"\s*\:\s*"([^"]+)"' )+"?start=0"
    
    video_urls = []
    video_urls.append( [ scrapertools.get_filename_from_url(media_url)[-4:]+" [vidspot]",media_url])

    for video_url in video_urls:
        logger.info("[vidspot.py] %s - %s" % (video_url[0],video_url[1]))

    return video_urls

# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    # http://vidspot.net/embed-d6fefkzvjc1z.html 
    patronvideos  = 'vidspot.net/embed-([a-z0-9]+)\.html'
    logger.info("[vidspot.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[vidspot]"
        url = "http://vidspot.net/embed-"+match+".html"
        if url not in encontrados and match!="embed":
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'vidspot' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    # http://vidspot.net/6lgjjav5cymi
    patronvideos  = 'vidspot.net/([a-z0-9]+)'
    logger.info("[vidspot.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[vidspot]"
        url = "http://vidspot.net/embed-"+match+".html"
        if url not in encontrados and match!="embed":
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'vidspot' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    #http://www.cinetux.org/video/vidspot.php?id=gntpo9m3mifj
    patronvideos  = 'vidspot.php\?id\=([a-z0-9]+)'
    logger.info("[vidspot.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[vidspot]"
        url = "http://vidspot.net/embed-"+match+".html"
        if url not in encontrados and match!="embed":
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'vidspot' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)


    return devuelve

def test():

    video_urls = get_video_url("http://vidspot.net/embed-5349gu9u9pkn.html")

    return len(video_urls)>0