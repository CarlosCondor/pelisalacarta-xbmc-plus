# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para filesmonster.com
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os,sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

#from pelisalacarta import buscador

__channel__ = "filesmonster_catalogue"
__category__ = "D"
__type__ = "generic"
__title__ = "filesmonster_catalogue"
__language__ = "ES"

DEBUG = config.get_setting("debug")

IMAGES_PATH = os.path.join( config.get_runtime_path(), 'resources' , 'images' , 'filesmonster_catalogue' )

def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)
    
def isGeneric():
    return True

def mainlist(item):
    logger.info("[filesmonster_catalogue.py] mainlist")

    itemlist = []
    itemlist.append( Item(channel=__channel__, action="hetero"  ,  title="Categorías porno hetero" , thumbnail="http://photosex.biz/imager/w_400/h_500/e48337cd95bbb6c2c372ffa6e71441ac.jpg"))    
    itemlist.append( Item(channel=__channel__, action="gay"  ,  title="Categorías porno gay - lesbian" , thumbnail="http://photosex.biz/imager/w_400/h_500/93df13c85224d428c195ea6581e7cdb3.jpg"))   
    itemlist.append( Item(channel=__channel__, action="bisex"  , title="Categorías porno bisex, trans y otras" , thumbnail="http://photosex.biz/imager/w_400/9dbaf07ad77788fd3d1f2f533bb25544.jpg"))     
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="Listado global" ,  url="http://filesmonster.filesdl.net/index.php",  thumbnail="http://photosex.biz/imager/w_400/h_400/9f869c6cb63e12f61b58ffac2da822c9.jpg"))         
    itemlist.append( Item(channel=__channel__, title="Búsqueda global"     , action="search") )
    return itemlist




def hetero(item):
    logger.info("[filesmonster_catalogue.py] mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero películas completas" ,  url="http://filesmonster.filesdl.net/index.php?cat=Full-length+films",  thumbnail="http://photosex.biz/imager/w_400/h_500/1325b1c8b815adc9284102d794264452.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero comic 3D" ,  url="http://filesmonster.filesdl.net/index.php?cat=3D+Porno",  thumbnail="http://photosex.biz/imager/w_400/h_500/941ebaa6185e37357c6156f602413ada.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero amateurish" ,  url="http://filesmonster.filesdl.net/index.php?cat=Amateurish",  thumbnail="http://photosex.biz/imager/w_400/h_500/a91255afe5b24291371049d92c9cdab5.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero anal" ,  url="http://filesmonster.filesdl.net/index.php?cat=Anal",  thumbnail="http://photosex.biz/imager/w_400/h_500/0a23d1fe93f54d82f2d28024861520a4.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero anime & hentai" ,  url="http://filesmonster.filesdl.net/index.php?cat=Anime+and+Hentai",  thumbnail="http://photosex.biz/imager/w_400/h_500/af4fb300f92b1105df4c07ad9696f766.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero BBW" ,  url="http://filesmonster.filesdl.net/index.php?cat=BBW",  thumbnail="http://photosex.biz/imager/w_400/h_500/6bcfac1425b8de6a58ee286b46258748.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Big boobs" ,  url="http://filesmonster.filesdl.net/index.php?cat=Big+boobs",  thumbnail="http://photosex.biz/imager/w_400/h_500/9191bc193317636437a4cf455ec965fe.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Black" ,  url="http://filesmonster.filesdl.net/index.php?cat=Black",  thumbnail="http://photosex.biz/imager/w_400/h_500/0623dffa59ef4fe0e0a1d33aa9ab29bd.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Blondes" ,  url="http://filesmonster.filesdl.net/index.php?cat=Blondes",  thumbnail="http://photosex.biz/imager/w_400/h_500/034bee14caa0e900c89ae398fcbf3b84.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Bukkake" ,  url="http://filesmonster.filesdl.net/index.php?cat=Bukkake",  thumbnail="http://photosex.biz/imager/w_400/h_500/816de59d8bdc8d53c44389358497a653.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Classic sex" ,  url="http://filesmonster.filesdl.net/index.php?cat=Classic+Sex",  thumbnail="http://photosex.biz/imager/w_400/h_500/4bc7e7d2dc93151d5a57d7104c9147fd.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Erotic & Softcore" ,  url="http://filesmonster.filesdl.net/index.php?cat=Erotic+and+Softcore",  thumbnail="http://photosex.biz/imager/w_400/h_500/90007536f2c2b512814f8769bb111f3e.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Erotic games" ,  url="http://filesmonster.filesdl.net/index.php?cat=Erotic+games",  thumbnail="http://photosex.biz/imager/w_400/h_500/94c6115340d1a8ae59dacd2a77764f11.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Extremals" ,  url="http://filesmonster.filesdl.net/index.php?cat=Extremals",  thumbnail="http://photosex.biz/imager/w_400/h_500/04d7dc6ffec80a5f62b1a177bdd654f9.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Fisting and dildos" ,  url="http://filesmonster.filesdl.net/index.php?cat=Fisting+and+Dildo",  thumbnail="http://photosex.biz/imager/w_400/h_500/219460b181092604f5def92218438b49.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero HD Clips" ,  url="http://filesmonster.filesdl.net/index.php?cat=HD+Clips",  thumbnail="http://photosex.biz/imager/w_400/h_500/f686c6debbd6ae955759dd4a19b01dd2.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Hairy" ,  url="http://filesmonster.filesdl.net/index.php?cat=Hairy",  thumbnail="http://photosex.biz/imager/w_400/h_500/635c8d55149d7e605266d13b44c0878d.jpg"))        
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Hidden Camera" ,  url="http://filesmonster.filesdl.net/index.php?cat=Hidden+camera",  thumbnail="http://photosex.biz/imager/w_400/h_500/e6917ab0a62ec31a731d6f25e463e40a.jpg"))        
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Incest" ,  url="http://filesmonster.filesdl.net/index.php?cat=Incest",  thumbnail="http://photosex.biz/imager/w_400/h_500/2c4d105d75997341fc6e0afd57eef356.jpg"))        
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Interracial" ,  url="http://filesmonster.filesdl.net/index.php?cat=Interracial",  thumbnail="http://photosex.biz/imager/w_400/h_500/4fde1e749b6d61873df92f0e3abe92ed.jpg"))        
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Latino" ,  url="http://filesmonster.filesdl.net/index.php?cat=Latino",  thumbnail="http://photosex.biz/imager/w_400/h_500/813b0664b0fe11428cb8c2f8b009ac7b.jpg"))        
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Masturbation" ,  url="http://filesmonster.filesdl.net/index.php?cat=Masturbation",  thumbnail="http://photosex.biz/imager/w_400/h_500/712dcd4f440eb1d0e1b133d871043110.jpg"))        
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Mature MILF" ,  url="http://filesmonster.filesdl.net/index.php?cat=Mature%2C+MILF",  thumbnail="http://photosex.biz/imager/w_400/h_500/b7880db52c6e2e37d67b4a2e6f460af6.jpg"))   
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Oral" ,  url="http://filesmonster.filesdl.net/index.php?cat=Oral",  thumbnail="http://photosex.biz/imager/w_400/h_500/ba52125bd04ed774ebb7595a0442e573.jpg"))   
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Orgies" ,  url="http://filesmonster.filesdl.net/index.php?cat=Orgies",  thumbnail="http://photosex.biz/imager/w_400/h_500/77c340bcca3e8b8004b74e8fa7bea399.jpg"))   
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Public sex" ,  url="http://filesmonster.filesdl.net/index.php?cat=Public+sex",  thumbnail="http://photosex.biz/imager/w_400/h_500/4a84ad103e455207c6c5b802059ae403.jpg"))         
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Retro" ,  url="http://filesmonster.filesdl.net/index.php?cat=Retro",  thumbnail="http://photosex.biz/imager/w_400/h_500/746e0d35e98a08e78f55fc3e563e207c.jpg"))   
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Russian" ,  url="http://filesmonster.filesdl.net/index.php?cat=Russian",  thumbnail="http://photosex.biz/imager/w_400/h_500/7accc2b596dd5585cfacba1075151b72.jpg"))   
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Teens" ,  url="http://filesmonster.filesdl.net/index.php?cat=Teens",  thumbnail="http://photosex.biz/imager/w_400/h_500/a3461fcab14e6afb675a7baf6fb322bc.jpg"))   
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero Uncensored asian" ,  url="http://filesmonster.filesdl.net/index.php?cat=Uncensored+asian",  thumbnail="http://photosex.biz/imager/w_400/h_500/25a5c2c40cdc625dae96075423a6f2d4.jpg"))  
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="hetero bdsm" ,  url="http://filesmonster.filesdl.net/index.php?cat=bdsm",  thumbnail="http://photosex.biz/imager/w_400/h_500/6cc50717b64cf66960fff840e19810bd.jpg"))  
                                                
    return itemlist
    
    


def gay(item):
    logger.info("[filesmonster_catalogue.py] mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="gay películas completas" ,  url="http://filesmonster.filesdl.net/index.php?cat=Gay+Full-length+films",  thumbnail="http://photosex.biz/imager/w_400/h_500/a1acc8a1f273ac8bfae2130802e21188.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="gays todos" ,  url="http://filesmonster.filesdl.net/index.php?cat=Gays",  thumbnail="http://photosex.biz/imager/w_400/h_500/296f152596d45be35c23b14a54271735.jpg"))        
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="gay 3D stereo" ,  url="http://filesmonster.filesdl.net/index.php?cat=Gay+3D+stereo",  thumbnail="http://photosex.biz/imager/w_400/h_500/bbf39e2cfc6d773ee5aaa9d99be8a090.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="gay asian" ,  url="http://filesmonster.filesdl.net/index.php?cat=Gay+Asian",  thumbnail="http://photosex.biz/imager/w_400/h_500/b6fcd3980304cc67bd7d794c46ef7200.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="gay BDSM" ,  url="http://filesmonster.filesdl.net/index.php?cat=Gay+BDSM",  thumbnail="http://photosex.biz/imager/w_400/h_500/db31625ff8b6055d406405ff9abdcbf9.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="lesbians" ,  url="http://filesmonster.filesdl.net/index.php?cat=Lesbians",  thumbnail="http://photosex.biz/imager/w_400/h_500/769c05b9ae6bfa6c082924a759d66bc3.jpg"))    
                
    return itemlist
    

    
    
    
def bisex(item):
    logger.info("[filesmonster_catalogue.py] mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="Documentaries" ,  url="http://filesmonster.filesdl.net/index.php?cat=Documentaries",  thumbnail="http://photosex.biz/imager/w_400/h_500/2ef8ef74124d37d1bec9865bf9b0ad1f.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="Transsexual" ,  url="http://filesmonster.filesdl.net/index.php?cat=Transsexual",  thumbnail="http://photosex.biz/imager/w_400/h_500/6edcad5b6475cb2bf09fe6eeb912d4d4.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="Other" ,  url="http://filesmonster.filesdl.net/index.php?cat=Other",  thumbnail="http://photosex.biz/imager/w_400/h_500/5854a2da100a8e69ae6c54296bdcf79a.jpg"))    
    itemlist.append( Item(channel=__channel__, action="lista_categoria"  ,  title="Bisexual" ,  url="http://filesmonster.filesdl.net/index.php?cat=Bisexual",  thumbnail="http://photosex.biz/imager/w_400/h_500/9b0fdf1b9b29d816694740867a39de10.jpg"))    
  
     
    return itemlist

    


def lista_categoria(item):
    logger.info("[filesmonster_catalogue.py] lista")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.downloadpageGzip(item.url)
    #logger.info(data)

    
    # Extrae las entradas (carpetas)
    patronvideos ='<h1 class="product_title"><a href="([^"]+)">([^<]+).*?</a>.*?<img src="([^"]+)".*?'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        scrapedtitle = match[1]
        scrapedtitle = scrapedtitle.replace("&#8211;","-")
        scrapedtitle = scrapedtitle.replace("&#8217;","'")
        scrapedurl= "http://filesmonster.filesdl.net/"+match[0]
        scrapedthumbnail = match[2]
        imagen = ""
        scrapedplot = match[0]  
        tipo = match[2]
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        scrapedplot=strip_tags(scrapedplot)
        itemlist.append( Item(channel=__channel__, action="detail_1", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail ,  plot=scrapedplot , folder=True) )
 
 
  # Extrae la marca de siguiente página
    patronvideos ='<a href="([^"]+)">Next</a>([^"]+).*?<div class="product_content">'
    matches2 = re.compile(patronvideos,re.DOTALL).findall(data)

    for match2 in matches2:
        scrapedtitle = ">> página siguiente"
        scrapedurl = "http://filesmonster.filesdl.net/index.php"+match2[0]
        scrapedthumbnail = ""
        imagen = ""
        scrapedplot = match2[0]  
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="lista_categoria", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
 

    itemlist.append( Item(channel=__channel__, action="mainlist", title="<< volver al inicio",  folder=True) )
  

    return itemlist







def lista(item):
    logger.info("[filesmonster_catalogue.py] lista")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.downloadpageGzip(item.url)
    #logger.info(data)

    
    # Extrae las entradas (carpetas)
    patronvideos ='<h1 class="product_title"><a href="([^"]+)">([^<]+).*?</a>.*?<img src="([^"]+)"'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        scrapedtitle = match[1]
        scrapedtitle = scrapedtitle.replace("&#8211;","-")
        scrapedtitle = scrapedtitle.replace("&#8217;","'")
        scrapedurl= "http://filesmonster.filesdl.net/"+match[0]
        scrapedthumbnail = match[2]
        imagen = ""
        scrapedplot = match[0]  
        tipo = match[2]
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        scrapedplot=strip_tags(scrapedplot)
        itemlist.append( Item(channel=__channel__, action="detail_1", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
 
 
  # Extrae la marca de siguiente página
    patronvideos ='<a href="([^"]+)">Next</a>([^"]+).*?<div class="product_content">'
    matches2 = re.compile(patronvideos,re.DOTALL).findall(data)

    for match2 in matches2:
        scrapedtitle = ">> página siguiente"
        scrapedurl = "http://filesmonster.filesdl.net/search.php"+match2[0]
        scrapedthumbnail = ""
        imagen = ""
        scrapedplot = match2[0]  
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="lista", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
 
 
    itemlist.append( Item(channel=__channel__, action="mainlist", title="<< volver al inicio",  folder=True) )

    return itemlist







def search(item,texto):
    logger.info("[filesmonster_catalogue.py] search")
    itemlist = []

    # descarga la pagina
    data=scrapertools.downloadpageGzip("http://filesmonster.filesdl.net/search.php?q="+texto)

    
    # Extrae las entradas (carpetas)
    patronvideos ='<h1 class="product_title"><a href="([^"]+)">([^<]+)</a>.*?<img src="([^"]+)"'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        scrapedtitle = match[1]
        scrapedtitle = scrapedtitle.replace("&#8211;","-")
        scrapedtitle = scrapedtitle.replace("&#8217;","'")
        scrapedurl= "http://filesmonster.filesdl.net/"+match[0]
        scrapedthumbnail = match[2]
        imagen = ""
        scrapedplot = match[0]  
        tipo = match[2]
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        scrapedplot=strip_tags(scrapedplot)
        itemlist.append( Item(channel=__channel__, action="detail_1", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
 

 
  # Extrae la marca de siguiente página
    patronvideos ='<a href="([^"]+)">Next</a>([^"]+).*?<div class="product_content">'
    matches2 = re.compile(patronvideos,re.DOTALL).findall(data)

    for match2 in matches2:
        scrapedtitle = ">> página siguiente"
        scrapedurl = "http://filesmonster.filesdl.net/search.php"+match2[0]
        scrapedthumbnail = ""
        imagen = ""
        scrapedplot = match2[0]  
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="lista", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
 
    itemlist.append( Item(channel=__channel__, action="mainlist", title="<< volver al inicio",  folder=True) )

    return itemlist




def detail_1(item):
    logger.info("[filesmonster_catalogue.py] detail_1")
    itemlist = []

    # descarga la pagina
    data=scrapertools.downloadpageGzip(item.url)

    
    # Extrae las entradas (carpetas)
    patronvideos ='class="product_link"><a href="([^"]+)".*?<img src="([^"]+)"'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        scrapedtitle ="Pulsa ok para generar el enlace"
        scrapedurl= "http://filesmonster.filesdl.net/"+match[0]
        scrapedthumbnail ="http://filesmonster.filesdl.net/"+match[1]
        imagen = ""
        scrapedplot = match[0]  
        tipo = match[1]
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        scrapedplot=strip_tags(scrapedplot)
        itemlist.append( Item(channel=__channel__, action="detail", title=scrapedtitle , url=scrapedurl , thumbnail=item.thumbnail , plot=scrapedplot , folder=True) )

    return itemlist








def detail(item):
    logger.info("[filesmonster_catalogue.py] detail")
    itemlist = []

	 # descarga la pagina
    data2=scrapertools.downloadpageGzip(item.url)
    # descubre la url
    patronvideos2 ='window.location.href = "([^"]+)"([^"]+)'
    matches2 = re.compile(patronvideos2,re.DOTALL).findall(data2)
    for match2 in matches2:
        scrapedurl2 =match2[0]
        scrapedtitle2 ="ver película ->"+ match2[0]
        itemlist.append( Item(channel=__channel__ , action="play" , server="filesmonster", title="ver en filesmonster",url=scrapedurl2, thumbnail=item.thumbnail, folder=False))


    return itemlist
    
    
