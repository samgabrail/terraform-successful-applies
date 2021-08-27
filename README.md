# Overview
This is a python script to give the successful applies for all workspaces within a certain time period

## Run it
Please note that the `MONTHS` env variable will give you the lookback. Example: `-e MONTHS=12` will provide the successful applies for the past 12 months starting from now.

```sh
export TOKEN=your_TFC_or_TFE_token
docker run --rm -e URL=https://app.terraform.io -e TOKEN=$TOKEN -e ORGANIZATION=HashiCorp-Sam -e MONTHS=12 -it samgabrail/terraform-successful-applies:latest
```

## Output

Output will look like this:
```sh
################
[INFO] Program started running at 2021-08-27 13:17:12.004982
[INFO] 0 successful applies for workspace hashicat-azure for the last 3 month(s) | 1 out of 25 workspaces completed
[INFO] 0 successful applies for workspace terraform-google-nomad for the last 3 month(s) | 2 out of 25 workspaces completed
[INFO] 0 successful applies for workspace infrastructure-gcp-tf-vault-deployment for the last 3 month(s) | 3 out of 25 workspaces completed
[INFO] 0 successful applies for workspace infrastructure-gcp-tf-vault-configuration for the last 3 month(s) | 4 out of 25 workspaces completed
[INFO] 4 successful applies for workspace vault-enterprise-deploy for the last 3 month(s) | 5 out of 25 workspaces completed
[INFO] 2 successful applies for workspace hashicat-azure-workshop for the last 3 month(s) | 6 out of 25 workspaces completed
[INFO] 6 successful applies for workspace azure-backend-test-sbx for the last 3 month(s) | 7 out of 25 workspaces completed
[INFO] 4 successful applies for workspace azure-backend-test-dev for the last 3 month(s) | 8 out of 25 workspaces completed
...truncated
[INFO] SUMMARY:
[{'successfulAppliesCount': 4,
  'workspaceID': 'ws-RBPYi1Cnipqonh9s',
  'workspaceName': 'hashicat-azure'},
 {'successfulAppliesCount': 0,
  'workspaceID': 'ws-AQGi8wi53hV2TLdA',
  'workspaceName': 'terraform-google-nomad'},
 {'successfulAppliesCount': 0,
  'workspaceID': 'ws-hGFEg4NNhz5GMVwd',
  'workspaceName': 'infrastructure-gcp-tf-vault-deployment'},
 {'successfulAppliesCount': 28,
  'workspaceID': 'ws-HcTfUywFMZz85uTy',
  'workspaceName': 'infrastructure-gcp-tf-vault-configuration'},
...truncated
 {'successfulAppliesCount': 0,
  'workspaceID': 'ws-PUNVsynoSS9dELRd',
  'workspaceName': 'gitlab_runner'},
 {'successfulAppliesCount': 0,
  'workspaceID': 'ws-ZYHmG5LkdoE2o4aP',
  'workspaceName': 'web-blog-vault'}]
{'Period': 'Last 12 month(s)',
 'Totals': {'Total Workspaces': 25, 'successfulAppliesCountTotal': 141}}
[INFO] Program completed running at 2021-08-27 13:19:16.383164
[INFO] Program took 0:02:04.378182 time to run
 ```