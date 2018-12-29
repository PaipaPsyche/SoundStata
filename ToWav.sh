#!/bin/bash

STR="$1"
#STR=$(echo "${STR}" | cut -f 1 -d '.')
STR="${STR%.*}"
newname="${STR}.wav"
`ffmpeg -i $1 $newname`
`python3 soundstata.py $newname`
