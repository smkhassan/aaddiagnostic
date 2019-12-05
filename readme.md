### AAD Diagnostic Script

AAD Diagnostic Script requires [Python3](https://www.python.org/downloads/) Python 3.7.4

How to use?

- **YOU CAN ONLY USE THIS SCRIPT IF YOU ARE A GLOBAL ADMIN OF THE TENANT**
- **DONT FORGET TO CREATE THE Storage Account you want to dump into**

```sh
$ pip3 install pipenv
$ pipenv shell
$ pip3 install -r requirements.txt
$ ./bash.sh
```
**Free Software, Hell Yeah!**

### Usage
- Please define what Subscription you want to set up Diagnostic Settings for : `az account set --subscription "*****"`
- Please define in bash parameter `-s` in command for what Storage Account to dumps logs : `/subscriptions/*****/resourceGroups/****/providers/Microsoft.Storage/storageAccounts/*****`
- Please define in bash parameter `-n` in command for the name of Diagnostic Settings : `*****`
- Bash parameter `-t` stands for bearer token that we acquire through `token=$(az account get-access-token --query accessToken)`
- Please check by going to portal and checking if values are set up.
