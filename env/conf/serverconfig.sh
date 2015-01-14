CREATE USER 'h4305DBmaster'@'localhost' IDENTIFIED BY '1603c45f1036cbbff74a77a8218541af';
GRANT ALL PRIVILEGES ON *.* TO 'h4305DBmaster'@'localhost' WITH GRANT OPTION;
CREATE USER 'h4305DBmaster'@'%' IDENTIFIED BY '1603c45f1036cbbff74a77a8218541af';
GRANT ALL PRIVILEGES ON *.* TO 'h4305DBmaster'@'%' WITH GRANT OPTION;

mysql user: h4305DBmaster
mysql password: 1603c45f1036cbbff74a77a8218541af

/srv/
  |
  |- www
      |
      |- mouvinsa
            |
            |- logs
            |   |
            |   |- nginx
            |   |- mysql
            |   |- uwsgi
            |
            |- static
            |
            |- app
                |
                |- controller
                |- model
                |- templates
                |- view