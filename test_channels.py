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

def test_one_channel(channelid):
    try:
        exec "from pelisalacarta.channels import "+channelid+" as channelmodule"
        resultado = channelmodule.test()
    except:
        import traceback
        from pprint import pprint
        exc_type, exc_value, exc_tb = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_tb)
        for line in lines:
            line_splits = line.split("\n")
            for line_split in line_splits:
                print line_split

        resultado = False

    return resultado

def test_channels(channelid):

    if channelid!="":
        print test_one_channel(channelid)
        return

    else:
        # importa la lista de canales
        import channelselector
        channels_itemlist = channelselector.channels_list()

        # Construye la lista para probar, y la lista de no probados, teniendo en cuenta algunas excepciones (util para sacar un canal del test temporalmente)
        para_probar = []
        no_probados = []
        excepciones = ['stormtv']

        for channel_item in channels_itemlist:

            # Importa el canal
            try:
                exec "from pelisalacarta.channels import "+channel_item.channel+" as channel_module"

                # Si tiene método test, es un canal para probar
                if channel_item.channel not in excepciones and hasattr(channel_module, 'test'):
                    para_probar.append(channel_item.channel)
                else:
                    no_probados.append(channel_item.channel)
            except:
                no_probados.append(channel_item.channel)

        # Ahora procede con las pruebas para sacar la lista de los que funcionan y los que no funcionan
        funcionan = []
        no_funcionan = []
        
        # Verifica los canales
        for canal in para_probar:
            resultado = test_one_channel(canal)
            if resultado:
                funcionan.append(canal)
            else:
                no_funcionan.append(canal)
        
        print "------------------------------------"
        print " no probados: %d" % len(no_probados)
        for canal in no_probados:
            print "   %s" % canal
        print " funcionan: %d" % len(funcionan)
        for canal in funcionan:
            print "   %s" % canal
        print " no funcionan: %d" % len(no_funcionan)
        for canal in no_funcionan:
            print "   %s" % canal

if __name__ == "__main__":
    import getopt
    options, arguments = getopt.getopt(sys.argv[1:], "", ["channel="])
    channel = ""
    
    print options,arguments
    
    for option, argument in options:
        print option,argument
        if option == "--channel":
            channel = argument

    test_channels(channel)
