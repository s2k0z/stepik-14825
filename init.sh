sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/boxweb
sudo /etc/init.d/nginx restart
