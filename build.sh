#!/bin/bash

echo " -----> WORKSHOP DOCKER <----- "
echo
echo " ---> Building Flask Container"
echo

docker build api/ -t price_prediction_api

echo
echo " ---> Building Jupyter Notebook Container"
echo

docker build jupyter_notebook/ -t jupyter_notebook

echo
echo " -----> Done! <-----"
echo

