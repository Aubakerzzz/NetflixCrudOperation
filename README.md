# Netflix Clone CI/CD + Terraform starter

This starter assumes repository folders `front/`, `back/`, and `db/`, each with a Dockerfile, and a Flask backend listening on 5000 with `/api/health`. The frontend container serves HTTP on port 80. Review and adapt the Docker build contexts, container ports, DB environment variable names, health endpoint and SQL migration process to match your actual code.

## Architecture

- GitHub Actions builds and pushes `aubakerzzz/netflix-clone-frontend`, `aubakerzzz/netflix-clone-backend`, and `aubakerzzz/netflix-clone-db` to Docker Hub on every push to `main`.
- Terraform provisions an ALB, ECS Fargate services, VPC/subnets/security groups, RDS PostgreSQL, Secrets Manager, CloudWatch logs and IAM roles.
- The database image is pushed as a build artifact but is NOT run as the production database. RDS provides persistent managed PostgreSQL storage.
- The ALB routes `/api/*` to Flask and all other paths to the frontend. Frontend code must call relative URLs such as `/api/movies`, not `http://127.0.0.1:5000`.

## Important before deploying

1. Ensure Dockerfiles exist at `front/Dockerfile`, `back/Dockerfile`, and `db/Dockerfile`.
2. Make frontend API base URL relative. In Vite, use `const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "";` so `MOVIES_URL` becomes `/api/movies` in production. Check Nginx/React build behaviour.
3. Confirm the backend accepts `DB_HOST`, `DB_PORT`, `DB_NAME`, and `DB_PASSWORD` (or edit Terraform environment names to match the backend). Do not use localhost for the production database.
4. Make the Docker Hub repositories public for this starter, or configure ECS `repositoryCredentials` backed by Secrets Manager for private repositories.
5. This starter has no HTTPS certificate and serves HTTP. Add Route 53 + ACM before production use.
6. The Terraform bootstrap role below currently uses AdministratorAccess to get the first deployment running. This is powerful; replace it with a reviewed least-privilege policy before production.
7. RDS password is stored in Terraform state and Secrets Manager. Protect state access. RDS deletion protection is enabled; keep backups and don't disable protection casually.
8. Database scripts are NOT run on every push. For a first initialization, use Actions → Run workflow and set `run_db_migrations` to `true` only after reviewing the SQL for compatibility with RDS and duplicate seed inserts. The migration task runs the copied SQL files in order against RDS. Do not rerun seed SQL if it inserts duplicate rows; make seed statements idempotent first.
9. The no-NAT design uses public subnets and assigns public IPs to Fargate tasks for outbound image pulls. Security groups restrict inbound app traffic to the ALB; the database stays in private subnets. For production, consider private ECS subnets plus NAT or VPC endpoints.

## Bootstrap GitHub OIDC role (one time, no AWS console)

You need an AWS account and AWS CLI credentials already configured locally (for example, `aws configure` or `aws configure sso`). From the repo root:

```powershell
cd infra/bootstrap
Copy-Item terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your actual GitHub owner and repository name.
terraform init
terraform plan
terraform apply
terraform output -raw github_actions_role_arn
```

The bootstrap currently attaches AdministratorAccess to the GitHub role for convenience. Treat this as a temporary development setup and scope it down before production.

Add GitHub repository Actions secrets:

- `AWS_ROLE_ARN`: output of `terraform output -raw github_actions_role_arn`
- `DOCKERHUB_USERNAME`: your Docker Hub username (`Aubakerzzz`)
- `DOCKERHUB_TOKEN`: a Docker Hub access token (not your account password)

You can configure GitHub repository secrets in GitHub Settings → Secrets and variables → Actions, or with GitHub CLI `gh secret set`.

## Deploy

Commit these files into the actual repository, verify the repository paths, then push to `main`. The workflow creates an encrypted/versioned S3 state bucket, runs Terraform, optionally runs the database initialization task only when manually requested, and waits for ECS services to stabilize. AWS resources incur charges. The Terraform state bucket is retained after app resources are destroyed.

## Important frontend API change

Your current service fallback was `http://127.0.0.1:5000`. In a user's browser that means the user's own computer, not the ECS backend. Use relative `/api` URLs behind the ALB path routing described above.
