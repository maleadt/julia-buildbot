#!/bin/sh

# upgrade database
until buildbot upgrade-master .
do
    echo "Can't upgrade master yet. Waiting for database to be ready..."
    sleep 1
done

# use exec so that twistd will use pid 1 of the container,
# and signals are properly forwarded
exec twistd -ny buildbot.tac
