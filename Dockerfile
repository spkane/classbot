FROM jfloff/alpine-python:recent-slim

COPY scripts/entrypoint.sh /entrypoint.sh

RUN /entrypoint.sh \
  -p pipenv \
  -p https://github.com/errbotio/errbot/archive/master.zip \
  -p sleekxmpp \
  -p pyasn1 \
  -p pyasn1-modules \
  -p irc \
  -p hypchat \
  -p https://github.com/slackhq/python-slackclient/archive/master.zip \
  -p python-telegram-bot \
  -b build-base \
  -b libressl-dev \
  -b libffi-dev \
  -a curl \
  -a vim \
  -a git \
  -a sudo \
  -a ca-certificates \
  -a openssh-client && \
  echo '    StrictHostKeyChecking no' >> /etc/ssh/ssh_config && \
  addgroup -g 2000 errbot && \
  adduser -D -u 2000 -G errbot errbot && \
  echo

COPY scripts/runas.sh /usr/local/sbin/runas

COPY scripts/start.sh /bin/start

#VOLUME ["/home/errbot/data/"]

ENTRYPOINT ["/bin/start"]
