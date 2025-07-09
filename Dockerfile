FROM jenkins/jenkins:lts

USER root

# Instala Python 3, pip y pandas (forzando instalación segura)
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    python3 -m pip install --break-system-packages pandas && \
    apt-get clean

USER jenkins