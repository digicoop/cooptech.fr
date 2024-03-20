#!/bin/bash
docker run --rm --volume="$PWD:/srv/jekyll" -it --publish 4000:4000 jekyll/jekyll:4.2.0 jekyll "$@"
