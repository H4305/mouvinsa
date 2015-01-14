# update and install essentials
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip -y

# install NginX, uWSGI and Redis
sudo apt-get install nginx-full uwsgi uwsgi-plugin-python redis-server -y

# install MySQL
export DEBIAN_FRONTEND=noninteractive
sudo -E apt-get -q -y install mysql-server
mysqladmin -u root password h4305
sudo sed -i 's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf
mysql -u root -ph4305 < /vagrant/user.sql
mysql -u root -ph4305 < /vagrant/structure.sql


# install flask
sudo pip install flask
# install sqlalchemy
sudo apt-get install libmysqlclient-dev python-mysqldb -y
sudo pip install mysql-python
sudo pip install Flask-SQLAlchemy
sudo pip install Flask-Mail

# configure uWSGI
touch /tmp/uwsgi.sock
sudo chown www-data /tmp/uwsgi.sock
#sudo cp /vagrant/app.uwsgi /etc/uwsgi/apps-available/app.ini
sudo ln -s /vagrant/app.uwsgi /etc/uwsgi/apps-available/app.ini
sudo ln -s /etc/uwsgi/apps-available/app.ini /etc/uwsgi/apps-enabled/app.ini

# configure NginX
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/default
sudo ln -s /vagrant/app.nginx /etc/nginx/sites-available/app
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

# configure Redis
#sudo cp /vagrant/app.redis /etc/redis/redis.conf
sudo ln -s /vagrant/app.redis /etc/redis/redis.conf

# install lynx browser for testing
sudo apt-get install lynx

# install WTforms
sudo pip install Flask-WTF

#setup the BDD

cat /vagrant/antho
echo "That's all folks!"