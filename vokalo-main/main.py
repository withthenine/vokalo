# Importere library til at forbinde til adafruit.io
import umqtt_robust2
from machine import Pin
from time import sleep_ms, sleep , ticks_ms
# fra gps main 
import GPSfunk
import lyd
import led 
# ATGM336H-5N <--> ESP32 
# GPS til ESP32 kredsløb
# GPS VCC --> ESP32 3v3
# GPS GND --> ESP32 GND
# GPS TX  --> ESP32 GPIO 16

#knap som instantieres til et Pin objekt på Pin 32 
knap = Pin(32,Pin.IN)

interval = 5000 # 5esk == 5000milli sek 
previousTime = 0


lib = umqtt_robust2
# fra gps main
# opret en ny feed kaldet map_gps indo på io.adafruit
mapFeed = bytes('{:s}/feeds/{:s}'.format(b'sebastian9', b'mapfeed/csv'), 'utf-8')

# opret en ny feed kaldet speed_gps indo på io.adafruit
speedFeed = bytes('{:s}/feeds/{:s}'.format(b'DIT ADAFRUIT BRUGERNAVN HER!!', b'speedfeed/csv'), 'utf-8')




while True:
    current_time = ticks_ms()

    sleep_ms(500)
    besked = lib.besked
    # haandtere fejl i forbindelsen og hvor ofte den skal forbinde igen
    
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            # hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
            lib.c.reconnect()
        else:
            lib.c.resubscribe()
    try:
        # Det er primært herinde at i skal tilfoeje kode
        if (current_time - previousTime > interval) :
            lib.c.publish(topic=mapFeed, msg=GPSfunk.main())
            previousTime = current_time

            print("sender gps data")
        #speed = GPSfunk.main()
        #speed = speed[:4]
        #print("speed: ",speed)
        #lib.c.publish(topic=speedFeed, msg=speed) 
    
        if knap.value() != 0 :
            led.Green_color()
            sleep(3)
            
        else:
            led.red_color()
        
  
        if besked == "offensive":
            print("modtaget")
            lyd.offensive()
            lib.besked = ""
            
        if besked == "defensive":
            print("modtaget")
            lyd.defensive()
            lib.besked = ""
            
#         if besked == "ledig":
#             print("modtaget")
#             led.Green_color()
#             lib.besked = ""
        

    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print("Ctrl-C pressed...exiting")
        lib.client.disconnect()
        # fram main gps 
        lib.wifi.active(False)
        lib.sys.exit()
    except OSError as e:
        print("Failed to read sensor.")
        #fram main gps 
    except NameError as e:
        print('NameError')
    except TypeError as e:
        print('TypeError')

    lib.c.check_msg()  # needed when publish(qos=1), ping(), subscribe()
    lib.c.send_queue()  # needed when using the caching capabilities for unsent messages
lib.c.disconnect()
