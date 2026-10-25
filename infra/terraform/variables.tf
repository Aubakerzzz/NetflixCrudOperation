variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "ap-south-1"
}

variable "environment" {
  type        = string
  description = "Deployment environment"
  default     = "production"
}

variable "app_name" {
  type        = string
  description = "Short name used for AWS resources"
  default     = "netflix-clone"
}

variable "dockerhub_username" {
  type        = string
  description = "Docker Hub account owning the images"
  default     = "Aubakerzzz"
}

variable "frontend_image_tag" {
  type        = string
  description = "Immutable frontend Docker image tag"
  default     = "latest"
}

variable "backend_image_tag" {
  type        = string
  description = "Immutable backend Docker image tag"
  default     = "latest"
}

variable "db_name" {
  type        = string
  description = "PostgreSQL database name"
  default     = "netflix_clone"
}

variable "db_username" {
  type        = string
  description = "PostgreSQL master username"
  default     = "netflixadmin"
}

variable "db_instance_class" {
  type        = string
  description = "RDS instance size; review pricing before apply"
  default     = "db.t3.micro"
}

variable "db_allocated_storage" {
  type        = number
  description = "Initial RDS storage in GiB"
  default     = 20
}

variable "db_backup_retention_days" {
  type        = number
  description = "Automated RDS backup retention days"
  default     = 7
}

variable "frontend_cpu" {
  type    = number
  default = 256
}
variable "frontend_memory" {
  type    = number
  default = 512
}
variable "backend_cpu" {
  type    = number
  default = 256
}
variable "backend_memory" {
  type    = number
  default = 512
}
variable "backend_container_port" {
  type        = number
  description = "Port exposed by Flask/Gunicorn in the back image"
  default     = 5000
}
variable "frontend_container_port" {
  type        = number
  description = "Port exposed by Nginx in the front image"
  default     = 80
}
