sudo apt update
sudo apt install python3-pip python3-dev libpq-dev nginx curl
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

cd ~/backend
virtualenv myenv
source myenv/bin/activate

pip install django gunicorn 
python manage.py collectstatic
sudo ufw allow 8000
gunicorn --bind 0.0.0.0:8000 backend.wsgi

deactivate

