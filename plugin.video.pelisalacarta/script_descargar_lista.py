# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Pelisalacarta script
# Descargar lista
# http://blog.tvalacarta.info/plugin-xbmc/tvalacarta/
#------------------------------------------------------------

import re,urllib,urllib2,sys,os
sys.path.append ("/root/scripts-pelisalacarta/pelisalacarta")

from core import platform_name
platform_name.PLATFORM_NAME="developer"

from core import config
config.set_setting("debug","true")

from core import scrapertools
from core.item import Item
from servers import servertools

config.set_setting("downloadlistpath","/root/scripts-pelisalacarta/documaniatv/list")
config.set_setting("downloadpath","/root/scripts-pelisalacarta/documaniatv/downloads")
from core import descargas
descargas.downloadall(None)
