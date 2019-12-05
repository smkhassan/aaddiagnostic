
az login --use-device-code
az account set --subscription "SET YOUR SUBSCRIPTION HERE"

token=$(az account get-access-token --query accessToken)

python3 ./api.py -n "*NAME OF YOUR DIAGNOSTIC SETTING*" \
-s "/subscriptions/*SUBSCRIPTION ID HERE */resourceGroups/*NAME OF YOUR RESOURCE GROUP*/providers/Microsoft.Storage/storageAccounts/*NAME OF YOUR STORAGE ACCOUNT HERE*"  \
-k "$token"
