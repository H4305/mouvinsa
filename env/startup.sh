#restart servers
#sudo service nginx restart
#sudo service uwsgi restart
sudo service supervisord start
sudo pip install sqlalchemy-migrate

cat /vagrant/conf/mouvinsa
