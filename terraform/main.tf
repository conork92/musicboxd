terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_budgets_budget" "musicboxd_budget" {
  name              = "monthly-budget"
  budget_type       = "COST"
  limit_amount      = "15.0"
  limit_unit        = "USD"
  time_unit         = "MONTHLY"
  time_period_start = "2022-01-01_00:01"
} 

resource "aws_instance" "linux_server" {
  ami           = "ami-096f43ef67d75e998"
  instance_type = "t2.micro"

  tags = {
    Name = "Musicboxd Server"
  }
}