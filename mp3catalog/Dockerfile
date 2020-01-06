
FROM python:3.6

#RUN apt-get update && apt-get upgrade

# Installs eyeD3
RUN pip install eyed3

# Installs mpck
# From https://github.com/Sjord/checkmate

# Installs mp3val
# From http://mp3val.sourceforge.net/download.shtml

# Installs PyMongo
RUN pip install pymongo

RUN mkdir /mp3_catalog

ADD ./src/ /mp3_catalog/

WORKDIR /mp3_catalog

CMD python
