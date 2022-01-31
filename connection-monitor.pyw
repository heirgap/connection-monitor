from win10toast import ToastNotifier
import time
from pythonping import ping
from infi.systray import SysTrayIcon
from PIL import Image, ImageDraw,ImageFont


hostname = "8.8.8.8"
count = 5
image= "systray.ico"
n=1
while True:

    response = ping(hostname,timeout = 1, size=1, count=count, verbose=False, interval=.2)

    try: 
        print('')  
    except OSError as error: 
            print(error) 
     
    notify = ToastNotifier()
    if response.success() == False:
            print('timeout')
            notify.show_toast('Connection Alert', 'Connection to {} is down'.format(hostname))
    else:
        print('success', response.rtt_avg_ms)

    formatted_response = "{:.0f}".format(response.rtt_avg_ms)

    # create image
    img = Image.new('RGBA', (50, 50), color = (255, 255, 255, 0))  # color background =  white  with transparency
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (50, 50)], fill=(255, 255, 255, 0), outline=None)

     # add scaled text to image
    if len(formatted_response) <= 2:
        font_size = 45
        padding = (5,5)
    if len(formatted_response) >= 4:
        font_size = 30
        padding = (0,5)
    elif len(formatted_response) == 3:
        font_size = 32
        padding = (0,10)

    font_type  = ImageFont.truetype('calibrib.ttf', font_size)
    d.text((padding), formatted_response, fill=(255,255,255), font = font_type)
    img.save(image)
    time.sleep(4)
    # display image in systray 
    if n==1:
        systray = SysTrayIcon(image, formatted_response + 'ms')
        systray.start()
    else:
        systray.update(icon=image)
    n+=1
    







