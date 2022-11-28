# MPPL KELOMPOK 1

# Deployments

## Install Docker

```bash
$ sudo apt update
$ sudo apt install apt-transport-https curl gnupg-agent ca-certificates software-properties-common -y
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
$ sudo apt install docker-ce
$ sudo apt install docker-compose
$ sudo usermod -aG docker $USER
```

## Build Docker

```bash
$ docker-compose up -d --build
```

## Without Docker
```bash
Note: Change db.py host from "mysql" to "localhost", and change the password also.
$ pip3 install -r requirements.txt
$ python3 main.py
```