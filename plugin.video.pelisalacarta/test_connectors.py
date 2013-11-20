# -*- coding: utf-8 -*-
#------------------------------------------------------------
# tvalacarta
# tester
# http://blog.tvalacarta.info/plugin-xbmc/tvalacarta/
#------------------------------------------------------------

import re,urllib,urllib2,sys
sys.path.append ("lib")

from core import platform_name
platform_name.PLATFORM_NAME="developer"

from core import config
config.set_setting("debug","true")

from core import scrapertools
from core.item import Item
from servers import servertools

def test_connectors(connectorid):
    #print test_one_connector("safelinking")
    #return

    if connectorid!="":
        resultado = test_one_connector(connectorid)
        print "Resultado: " , resultado
    else:

        funcionan = []
        no_funcionan = []
        no_probados = []
        para_probar = []

        para_probar.append("adfly")
        para_probar.append("adnstream")
        no_probados.append(["allbox4","Fuera de servicio"])
        para_probar.append("allmyvideos")
        no_probados.append(["bayfiles","Solo premium"])
        no_probados.append(["cramit","Solo premium"])
        #HACER para_probar.append("bayfiles")
        no_probados.append(["bitshare","Solo premium"])
        #HACER para_probar.append("bliptv")
        no_probados.append(["cineraculo","Fuera de servicio"])
        #HACER para_probar.append("cramit")
        para_probar.append("dailymotion")
        no_probados.append(["depositfiles","Solo premium"])
        para_probar.append("divxstage")
        no_probados.append(["downupload","Fuera de servicio"])
        no_probados.append(["extabit","Solo premium"])
        no_probados.append(["facebook","No hay ejemplos"])
        no_probados.append(["fiberupload","Solo premium"])
        para_probar.append("filebox")
        no_probados.append(["filefactory","Solo premium"])
        para_probar.append("fileflyer")
        no_probados.append(["filejungle","Fuera de servicio"])
        no_probados.append(["filereactor","Fuera de servicio"])
        no_probados.append(["fileserve","Fuera de servicio"])
        no_probados.append(["filesonic","Fuera de servicio"])
        para_probar.append("flashx")
        no_probados.append(["fooget","Solo premium"])
        para_probar.append("fourshared")
        no_probados.append(["freakshare","Fuera de servicio"])
        no_probados.append(["gigabyteupload","Sin ejemplos"])
        no_probados.append(["gigasize","Solo premium"])
        no_probados.append(["googlevideo","Fuera de servicio"])
        no_probados.append(["hdplay","Fuera de servicio"])
        no_probados.append(["hotfile","Fuera de servicio"])
        para_probar.append("hulkshare")
        no_probados.append(["jumbofiles","Fuera de servicio"])
        #HACER para_probar.append("justintv")
        para_probar.append("letitbit")
        para_probar.append("linkbucks")
        no_probados.append(["lumfile","Solo premium"])

        no_probados.append(["modovideo","Fuera de servicio"])
        para_probar.append("moevideos")
        para_probar.append("movshare")
        para_probar.append("nosvideo")
        para_probar.append("novamov")
        para_probar.append("nowvideo")
        para_probar.append("one80upload")
        para_probar.append("playedto")
        para_probar.append("putlocker")
        no_probados.append(["rutube","Solo premium"])
        para_probar.append("sockshare")
        para_probar.append("streamcloud")
        para_probar.append("tutv")
        para_probar.append("twitvid")
        para_probar.append("videobam")
        para_probar.append("videopremium")
        para_probar.append("videoweed")
        no_probados.append(["vidxden","Solo premium (en free requiere captcha)"])
        para_probar.append("vk")
        para_probar.append("youtube")
        para_probar.append("zinwa")
        no_probados.append(["zippyshare","Solo premium"])

        '''
        para_probar.append(["twitvid","http://www.telly.com/KN995?fromtwitvid=1"])
        para_probar.append(["twitvid","http://www.telly.com/666IK?fromtwitvid=1"])
        para_probar.append(["videoweed","http://embed.videoweed.es/embed.php?v=jgos3ftj8a1zg"])
        para_probar.append(["videoweed","http://embed.videoweed.es/embed.php?v=76ev085tmn0m6"])
        para_probar.append(["novamov","http://www.novamov.com/video/tb6ira2dj029b"])
        para_probar.append(["novamov","http://www.novamov.com/video/yqesmw0th1ad9"])
        para_probar.append(["adfly","http://adf.ly/Fp6BF"])
        para_probar.append(["moevideos","http://moevideo.net/swf/letplayerflx3.swf?file=23885.2b0a98945f7aa37acd1d6a0e9713"])
        para_probar.append(["moevideos","http://www.moevideos.net/online/106249"])
        para_probar.append(["mediafire","http://www.mediafire.com/?aol88b96gm2rteb"])
        para_probar.append(["dailymotion","http://www.dailymotion.com/video/xrf96h"])
        '''
        
        '''
        para_probar.append(["videobam","http://videobam.com/FSxJO"])
        para_probar.append(["youtube","http://www.youtube.com/watch?v=nL-ww-XHtaY"])
        para_probar.append(["filebox","http://www.filebox.com/owif1u0k7ntq"])
        para_probar.append(["streamcloud","http://streamcloud.eu/neuj4jw5w261"])
        para_probar.append(["movshare","http://www.movshare.net/video/tk2uynzhbbio5"])
        para_probar.append(["divxstage","http://www.divxstage.net/video/27wnoxhgtvmff"])
        '''

        # Verifica los conectores
        for server in para_probar:
            try:
                resultado = test_one_connector(server)
                if resultado:
                    funcionan.append([server,0,0])
                else:
                    no_funcionan.append([server,0,0,""])
            except:
                no_funcionan.append([server,0,0,"Excepción"])
        
        print "------------------------------------"
        print " no probados: %d" % len(no_probados)
        for server,motivo in no_probados:
            print "   %s (%s)" % (server,motivo)

        print " funcionan: %d" % len(funcionan)
        for server,ok,nok in funcionan:
            print "   %s [%d/%d]" % (server,ok,nok)

        print " no funcionan: %d" % len(no_funcionan)
        for server,ok,nok,detalle in no_funcionan:
            print "   %s [%d/%d] %s" % (server,ok,nok,detalle)    

def test_one_connector(server):

    exec "from servers import "+server+" as serverconnector"
    return serverconnector.test()

if __name__ == "__main__":
    import getopt
    options, arguments = getopt.getopt(sys.argv[1:], "", ["connector="])
    connector = ""
    
    print options,arguments
    
    for option, argument in options:
        print option,argument
        if option == "--connector":
            connector = argument

    test_connectors(connector)
