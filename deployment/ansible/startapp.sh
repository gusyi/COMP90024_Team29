#!/bin/bash

cd /home/ubuntu/backend
source myenv/bin/activate

sudo ln -s /etc/nginx/sites-available/backend /etc/nginx/sites-enabled;

echo "== Test Nginx config for syntax error =="
sudo nginx -t;

echo "== Restart Nginx =="
sudo systemctl restart nginx

echo "== Close port 8000 =="
sudo ufw delete allow 8000;

echo "== Open up firewall for normal traffic on port 80 =="
sudo ufw allow 'Nginx Full';

gunicorn backend.wsgi

echo "== Start server =="
python3 manage.py runserver;

# deactivate;