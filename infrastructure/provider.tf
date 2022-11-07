provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle de estado do Terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-adriano"
    key    = "state/igti/edc/mod2/terraform.tfstate"
    region = "us-east-2"
  }
}