#!/bin/bash
for s in source/*.scss; do
	bn=$(basename $s)
	sass --sourcemap=none $s:${bn/.scss}.css
done
