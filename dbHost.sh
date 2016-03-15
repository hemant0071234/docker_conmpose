#!/bin/bash
# My first script

echo "Storing DB host values"
PG_HOST=$(docker inspect testttt_postgresnewtest6_run_1 | grep "\"IPAddress\"" | cut -d ':' -f 2| cut -d '"' -f 2)
