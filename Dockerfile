FROM python:3.10-slim

RUN useradd -ms /bin/bash dude
RUN echo 'root:root' | chpasswd
RUN echo 'dude:dude' | chpasswd
RUN adduser dude sudo
RUN chown -R dude.dude /home/dude/

WORKDIR /home/dude/
COPY  requirements.in /home/dude/

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.in

USER dude
WORKDIR /home/dude/app/

EXPOSE 8501

ENTRYPOINT ["bash", "entrypoint.sh"]
