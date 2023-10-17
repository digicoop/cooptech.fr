#!/bin/bash
docker run --rm --volume="$PWD:/srv/jekyll" -it --publish 6600:6600 jekyll/jekyll:4.2.0 jekyll "$@"
