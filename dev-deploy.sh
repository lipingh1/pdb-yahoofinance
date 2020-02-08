#! /bin/bash

terraform init --backend=true --backend-config=environments/dev/backend.tfvars
terraform plan --var-file=environments/dev/variables.tfvars
terraform apply -auto-approve --var-file=environments/dev/variables.tfvars