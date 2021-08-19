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
 ```