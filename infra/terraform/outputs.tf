output "application_url" {
  description = "Public application URL (HTTP; add HTTPS/ACM before production)"
  value       = "http://${aws_lb.main.dns_name}"
}
output "ecs_cluster_name" { value = aws_ecs_cluster.main.name }
output "frontend_service_name" { value = aws_ecs_service.frontend.name }
output "backend_service_name" { value = aws_ecs_service.backend.name }
output "rds_endpoint" { value = aws_db_instance.main.address }
output "database_secret_arn" { value = aws_secretsmanager_secret.db_credentials.arn }

output "migration_task_definition_arn" { value = aws_ecs_task_definition.migration.arn }
output "public_subnet_ids" { value = aws_subnet.public[*].id }
output "backend_security_group_id" { value = aws_security_group.backend.id }
