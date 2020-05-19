sudo apt update
sudo apt install python3-pip python3-dev libpq-dev nginx curl 
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

cd ~/backend
source myenv/bin/activate

sudo ufw allow 8000

deactivate

