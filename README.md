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

Then Ctrl + X, Y, Enter

systemctl --user enable bot
systemctl --user enable bot
systemctl --user start bot
Contact:

Email: thangsmhome@gmail.com
