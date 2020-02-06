provider "aws" {
	region = "eu-west-1"
	
}

terraform {
  backend "s3" {
    bucket = "pigly-nonprod-terraform-state"
    key = "service/yahoofinance/dev/datalake/terraform-state.tfstate"
    region = "eu-west-1"
    
  }
}