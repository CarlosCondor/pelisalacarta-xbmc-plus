# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Script for downloading files from any server supported on pelisalacarta
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#-------------------------------------------------------------------------

import re,urllib,urllib2,sys,os
sys.path.append ("lib")

from core import platform_name
platform_name.PLATFORM_NAME="developer"

from core import config
config.set_setting("debug","true")

from core import scrapertools
from core import downloadtools
from core.item import Item
from servers import servertools

def download_url(url,titulo):

    url = url.replace("\\","")

    print "Analizando enlace "+url

    # Averigua el servidor
    itemlist = servertools.find_video_items(data=url)
    if len(itemlist)==0:
        print "No se puede identificar el enlace"
        return

    item = itemlist[0]
    print "Es un enlace en "+item.server

    # Obtiene las URL de descarga
    video_urls, puedes, motivo = servertools.resolve_video_urls_for_playing(item.server,url)
    if len(video_urls)==0:
        print "No se ha encontrado nada para descargar"
        return

    # Descarga el de mejor calidad, como hace pelisalacarta
    print video_urls
    devuelve = downloadtools.downloadbest(video_urls,titulo,continuar=False)

if __name__ == "__main__":
    url = sys.argv[1]
    title = sys.argv[2]

    if title.startswith("http://") or title.startswith("https://"):
        url = sys.argv[2]
        title = sys.argv[1]

    download_url(url,title)
