# update and install essentials
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip -y

# install flask
sudo pip install flask

# install NginX and uWSGI
sudo apt-get install nginx uwsgi uwsgi-plugin-python -y

# install MySQL
export DEBIAN_FRONTEND=noninteractive
sudo -E apt-get -q -y install mysql-server
mysqladmin -u root password h4305
sudo sed -i 's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf
mysql -u root -ph4305 < /vagrant/structure.sql
mysql -u root -ph4305 < /vagrant/structure.sql


# install peewee
sudo pip install peewee

# configure uWSGI
touch /tmp/uwsgi.sock
sudo chown www-data /tmp/uwsgi.sock
sudo cp /vagrant/app.uwsgi /etc/uwsgi/apps-available/app.ini
sudo ln -s /etc/uwsgi/apps-available/app.ini /etc/uwsgi/apps-enabled/app.ini

# configure NginX
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/default
sudo cp /vagrant/app.nginx /etc/nginx/sites-available/app
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

# install and configure redis
#sudo apt-get install tcl-dev
#wget http://download.redis.io/redis-stable.tar.gz
#wget http://download.redis.io/redis-stable.tar.gz
#tar xvzf redis-stable.tar.gz
#cd redis-stable
#make
#sudo make install

# install lynx browser for testing
sudo apt-get install lynx


cat /vagrant/antho
echo "That's all folks!"