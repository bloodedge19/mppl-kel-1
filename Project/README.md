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