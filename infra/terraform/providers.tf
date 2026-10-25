provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Project     = "netflix-clone"
      ManagedBy   = "Terraform"
      Environment = var.environment
    }
  }
}
