#!/bin/bash

clear
email="topgear35rus@ya.ru"
uname="racer-prog"
upass="246810Retracker$&"
git init
git config --global user.email $email
git config --global user.name $uname
git config --global user.password $upass
git add .
git commit -m "commit from script" $1
git push --all
