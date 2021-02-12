#!/bin/bash

echo Enter short git commit message: 
read m1
echo Enter longer git commit description:
read m2
git add .
git commit -m "$m1" -m "$m2"
git push
