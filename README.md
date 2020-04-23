To install

    cd ~
    git clone https://github.com/thangnd85/vinahome.git
    cd vinahome
    python3 st_env.py


To make bot autostart with pi
    
    cd ~
    mkdir .config
    mkdir .config/systemd
    mkdir .config/systemd/user
    nano .config/systemd/user/bot.service

Paste following line:
    
    [Unit]
    Description=Bot
    After=syslog.target network.target
    [Service]
    Type=simple
    WorkingDirectory=/home/pi/vinahome
    ExecStart=/bin/bash -lc '. bot.sh'
    RestartSec=1
    Restart=on-failure
    StandardOutput=syslog
    StandardError=syslog
    SyslogIdentifier=vinahome
    [Install]
    WantedBy=multi-user.target

Then Ctrl + X, Y, Enter

    systemctl --user enable bot
    systemctl --user enable bot
    systemctl --user start bot

To start manualy:
   
     cd ~
     cd vinahome
     . bot.sh
     
Contact:

    Email: thangsmhome@gmail.com

Donate Momo / Airpay / ViettelPay
![alt text](https://dummyimage.com/160x40/000/fff&text=0985435685)
