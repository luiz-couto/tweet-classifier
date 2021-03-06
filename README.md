# tweet-classifier
A simple tweet classifier developed in python using Machine Learning. This project is for the Cloud Computing course at UFMG.


## How the project is structured

The project have the folder tree below:

```
project
│   
│   README.md (this document)
│   argocd.yaml (the yaml file containing the description of the app on ArgoCD)
|   discussion-tp2.pdf (the discussion about the tests performed on the CI/CD structure)
│
└─── api (the REST API implementation)
│   │   .dockerignore
│   │   app.py
│   │   Dockerfile
│   │   requirements.txt
│   
└─── client (the cllient code - a bash script that connects with the kubernetes service tweet-classifier-service)
    │   client.sh
    │   README.md (instructions on how to run the client)
│
└─── kube (folder containing the .yaml files)
    │   deployment.yaml
    │   service.yaml
│
└─── models (contains all the models generated by the python ML classifier - pickle objects)
    │   v0.0.1
    │   v0.0.2
│
└─── src (contains the code of the python classifier)
    │   classifier.py

```