FROM ubuntu:18.04
MAINTAINER Pyae Phyo Hein "pyaephyohien.info.3326@gmail.com"
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev 
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3 -m pip install requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]