#!/bin/bash
IFS=$(echo -en "\n\b")
for file in $( ls ); do
  convert "$file" -transparent-color '#ffffff' "${file}.png"
done
