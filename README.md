GhostHunt
=========

A simple projekt in order to make a box with a RPI a motion sensor, a battery pack and a speaker to scare the kids on the ghost hunt. 

Connect USB speakers and follow this tutorial 

  http://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876

Do a git clone into /home/pi

To enable autostart:
  
  copy GhostHunt.sh to /etc/init.d
  run:  update-rc.d GhostHunt.sh defaults
        update-rc.d GhostHunt.sh enable
  
Connect PIR motion sensor signal cable to port 23. Connect voltage to motion sensor. 

  http://cdn.shopify.com/s/files/1/0254/2677/products/pi5_1024x1024.png?v=1384622988

Connect battery pack and put everthing in a whaterproof case. 
