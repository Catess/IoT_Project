## connect to wifi at boot time.


def connect():
    import network
    import uping

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Honor9', 'iot12345')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    if wlan.isconnected():
        uping.ping('192.168.43.79')
    else:
        print('No network')    
    
def no_debug():
    import esp
    # you can run this from the REPL as well
    esp.osdebug(None)

no_debug()
connect()
