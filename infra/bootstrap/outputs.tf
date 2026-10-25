output "github_actions_role_arn" {
  description = "Set this value as the GitHub Actions repository secret AWS_ROLE_ARN"
  value       = aws_iam_role.github_actions.arn
}
