#!/bin/bash
for s in *.scss; do
	bn=$(basename $s)
	sass --sourcemap=none $s:${bn/.scss}.css
done
