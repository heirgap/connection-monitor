from win10toast import ToastNotifier
from pythonping import ping
from infi.systray import SysTrayIcon
from PIL import Image, ImageDraw,ImageFont


hostname = '8.8.8.8'

pings_per_cycle = 5
image = "systray.ico"
i = 1
drop_count = 0

while True:
    try: 
        response = ping(hostname,timeout = 1, size=1, count=pings_per_cycle, verbose=False,interval=2)
        formatted_response = "{:.0f}".format(response.rtt_avg_ms)

        # initializes the notification object and sets conditions in which it is triggered
        notify = ToastNotifier()
        if response.success() == False:
                print('timeout')
                notify.show_toast('Connection Alert', 'Connection to {} is down'.format(hostname))
                drop_count += 1
        else:
            print('success', response.rtt_avg_ms)

    # catch Windows errors and notifies user
    except OSError as error: 
            notify.show_toast('Connection Alert', 'Connection to {} is down'.format(hostname))
            print(error)
            drop_count += 1 
    

    # create image
    img = Image.new('RGBA', (50, 50), color = (0, 0, 0, 0))  # color background =  white  with transparency
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (50, 50)], fill=(255, 255, 255, 0), outline=None)

     # scale text size based on number of characters
    if len(formatted_response) <= 2:
        font_size = 45
        padding = (5,5)
    elif len(formatted_response) >= 4:
        font_size = 30
        padding = (0,5)
    else:
        font_size = 32
        padding = (0,10)

    # add text to image
    font_type  = ImageFont.truetype('calibrib.ttf', font_size)
    d.text((padding), formatted_response, fill=(255,255,255), font = font_type)
    img.save(image)
    
    # display image in systray 
    formatted_hover_text = formatted_response + ' ms to ' + hostname
    
    if i == 1:
        total_pings = pings_per_cycle
        systray = SysTrayIcon(image, hover_text = formatted_hover_text + '\n' + str(drop_count) + ' connection drops today.' + '\n' + str(total_pings) + ' total pings sent')
        systray.start()
    else:
        total_pings = i * pings_per_cycle
        systray.update(icon=image, hover_text = formatted_hover_text +  '\n' +  str(drop_count) +  ' connection drops today.' + '\n' + str(total_pings) + ' total pings sent')
    i += 1
    
    







