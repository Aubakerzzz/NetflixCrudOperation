variable "aws_region" {
  description = "AWS region for the GitHub Actions deployment role"
  type        = string
  default     = "ap-south-1"
}

variable "github_owner" {
  description = "GitHub organization or username that owns the repository"
  type        = string
}

variable "github_repo" {
  description = "GitHub repository name, without owner"
  type        = string
}
