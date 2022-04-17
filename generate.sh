#!/bin/bash

# python3 generate_instances.py ./data/instance01.txt
for i in {1..99}
do
    python3 generate_instances.py ./data/instance${i}.txt
done