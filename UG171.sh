#!/bin/bash

# Accept a parameter as the first argument
path=$1

# Output the arguments for debugging
echo "Received arguments: $path"

# Run the klara command with the provided path
klara "$path"