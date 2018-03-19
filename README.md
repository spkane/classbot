# classbot (errbot)

Docker images for [Err](http://errbot.net), a chat-bot designed to be easily deployable, extensible and maintainable.

* *Inspired by*:
   * https://github.com/zoni/docker-err
   * https://github.com/jfloff/alpine-python

## Usage

This container can be started in three different modes:

* ___shell:___ Start a bash session as the bot account (*err*).
* ___rootshell:___ Start a bash session as the root account.
* ___errbot:___ Start the bot itself. Any additional arguments passed here will be passed on to `errbot`.

For example, try: `docker run --rm -it spkane/classbot:latest errbot --help`
or try: `docker-compose up -d`

To successfully run the bot, you will have to mount a [config.py](http://errbot.net/_downloads/config-template.py) into the `/home/errbot` directory (`--volume` option to docker run).

Examine the `docker-compose.yaml` file to get a feel from how you should run this.

## Installing dependencies

Some plugins require additional dependencies that may not be installed in the virtualenv by default. There are three ways to deal with this, listed from best practice to worst:

1. Build your own image based on this one.
2. Let errbot install dependencies automatically by setting `AUTOINSTALL_DEPS = True` in `setting.py`.
3. Enter a running container manually (`docker exec --interactive --tty <container-name> /bin/sh -c "TERM=$TERM exec /bin/sh --login"` where `<container-name>` is the name listed by `docker ps`) and install with pip.


## Container layout

* `/home/errbot`: Home directory of the user account for errbot. `config.py` is expected to go here.
* `/home/errbot/.ssh/`: The `.ssh` directory of the bot user (you can mount private SSH keys into this directory if you need to install plugins from private repositories).
* `/homr/errbot/data/`: A volume intended to store bot data (`BOT_DATA_DIR` setting of `config.py`).


## Security notes

* The bot is run under its own user account (*errbot*), not as root.
* SSH is set up to automatically add unknown host keys (*StrictHostKeyChecking no*).

## Local Testing

* Interactive shell testing of bot

```
ln -s config.py.local config.py
errbot -T -c config.py
```

* Most plugins can be tested in their directories by running:

```
py.test -sv --pep8
coverage run --source students -m py.test --pep8
```


