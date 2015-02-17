# update and install essentials
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip curl -y

# install NginX, uWSGI and Redis
#sudo apt-get install nginx-full uwsgi uwsgi-plugin-python redis-server -y

# install MySQL
export DEBIAN_FRONTEND=noninteractive
sudo -E apt-get -q -y install mysql-server
mysqladmin -u root password h4305
sudo sed -i 's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf
mysql -u root -ph4305 < /vagrant/conf/user.sql
mysql -u root -ph4305 < /vagrant/conf/structure.sql


# install flask
sudo pip install flask
# install sqlalchemy
sudo apt-get install libmysqlclient-dev python-mysqldb -y
sudo pip install mysql-python
sudo pip install Flask-SQLAlchemy
sudo pip install Flask-Mail
sudo pip install Flask-WTF

export PYTHONPATH=/app/mouvinsa/
echo 'export PYTHONPATH=/app/mouvinsa/' >> ~/.bashrc
python -c "import sys; sys.path.append('/app'); from mouvinsa import models; from mouvinsa.models import db; db.create_all()"
sudo easy_install supervisor
sudo cp /vagrant/conf/supervisord.sh /etc/init.d/supervisord
sudo sed -i 's/\r//g' /etc/init.d/supervisord
sudo chmod +x /etc/init.d/supervisord
sudo update-rc.d supervisord defaults

# configure uWSGI
#touch /tmp/uwsgi.sock
#sudo chown www-data /tmp/uwsgi.sock
#sudo ln -s /vagrant/conf/app.uwsgi /etc/uwsgi/apps-available/app.ini
#sudo ln -s /etc/uwsgi/apps-available/app.ini /etc/uwsgi/apps-enabled/app.ini

# configure NginX
#sudo rm /etc/nginx/sites-enabled/default
#sudo rm /etc/nginx/sites-available/default
#sudo ln -s /vagrant/conf/app.nginx /etc/nginx/sites-available/app
#sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

# configure Redis
#sudo cp /vagrant/conf/app.redis /etc/redis/redis.conf
#sudo ln -s /vagrant/conf/app.redis /etc/redis/redis.conf

# install lynx browser for testing
sudo apt-get install lynx

# install WTforms
sudo pip install Flask-WTF

#install Werkzeug
sudo pip install Werkzeug

#setup the BDD
echo "That's all folks!"