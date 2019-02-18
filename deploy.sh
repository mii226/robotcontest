#!bin/bash
sudo su
cd /home/ubuntu
rm -rf robotcontest
git clone https://github.com/mii226/robotcontest.git
chmod 777 robotcontest
chmod 777 robotcontest/db.sqlite3
systemctrl restart httpd
cat /var/log/apache2/access_robot.log
