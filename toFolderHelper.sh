#!/bin/bash
echo -e "pass the file extension: "
read extensionPassed

for x in ./*.$extensionPassed; do
  mkdir "${x%.*}" && mv "$x" "${x%.*}"
done
