#!/bin/bash

# MySQL root user credentials
MYSQL_USER="root"
MYSQL_PASSWORD="root"

# Running MySQL command
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "SHOW DATABASES;"
