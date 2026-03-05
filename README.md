# Instructions
- Clone the repository
- Create a branch called `devops-challenge` for your work
- Update readme with an Instructions section explaining how to build the container and run the pipeline locally.

# Challenge
Implement a cloud based Doubly Linked List from scratch in the language of your choice (Python or Go recommended for DevOps).

The application needs to support standard DDL operations:
- Insert head
- Insert tail
- Remove all duplicate nodes
- Search for an element (return index)
- Size of the list

**Note:** Focus on the infrastructure, not the code. Don't overthink the implementation; use AI to generate an efficient DDL implementation so you can stay focused on the high-level setup.

## Cloud Infrastructure (IaC)
Your goal is to provide the code necessary to deploy this Linked List utility as a containerized service. To ensure the reviewer can replicate your setup, please follow these requirements:

- Create a `.tf` file (or set of files) that defines the infrastructure needed to run your Docker container in AWS.
- Do not hard-code account IDs, region names, or VPC IDs. Use a variables file so the reviewer can inject their own AWS environment details.
- You must define at least three resources (e.g., ECR repository, ECS Cluster/Service, and the necessary IAM roles)
- Include a standard `provider.tf` block that allows the reviewer to use their local AWS credentials/profile.
- Implement JSON logging for every operation (e.g., `{"event": "node_added", "value": 10, "timestamp": "..."}`) to demonstrate SRE/Monitoring proficiency.
- Provide a `Dockerfile` and a GitHub Actions YAML file that automates linting and testing.
- In your README, include a section called **Deployment Guide** with the exact commands needed to run your Terraform and deploy the container image to the created ECR.
- Include a test suite that covers also edge cases (empty list, removing from a single-node list).

## Architecture Diagram
Add a quick sketch (hand-drawn photo, Mermaid.js, or simple shapes) to your README. It doesn't need to be pretty; it needs to show how you handled networking, security, and multi-tenancy for this SaaS platform.

# Additional details
- 1.5 hours to complete the challange
- This is design work, not coding - focus on architecture and docs
- Architecture diagram can be text if you don't have a drawing tool
- Show that you understand what the DDL app needs to do
- Document your thinking process
- After finishing, upload the changes in a Pull Request, assign it to yourself and ensure you request review from any of the invited collaborators to your repository.

Good luck!
