#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -t <text>"
   echo -e "\t-t The text that will be predicted"
   exit 1 # Exit script after printing help
}

while getopts "t:" opt
do
   case "$opt" in
      t ) text="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$text" ]
then
   echo "The text parameter is missing! Add it as shown below";
   echo "Texts that contain spaces must be written within quotes"
   helpFunction
fi

# Begin script in case all parameters are correct
echo "$text"

cluster_ip=$(kubectl get svc tweet-classifier-service -ojsonpath='{.spec.clusterIP}')

echo "$cluster_ip"