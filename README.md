# Challenge
Implement a cloud based Doubly Linked List from scratch in the language of your choice (Python or Go recommended for DevOps).

The application needs to support standard DDL operations:
- Insert head
- Insert tail
- Remove all duplicate nodes
- Search for an element (return index)
- Size of the list

# Building the image
Test in locally

 docker build -t dll-api .
 docker run -p 8080:80 dll-api:latest


## Cloud Infrastructure (IaC)
 The service will be run in a EKS service


# Deployment Guide
terraform init
terraform plan
terrafrom apply

## Architecture Diagram
                        Internet
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Application Load   │
                 │      Balancer       │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Service:
                 | NodePort 8080     │
                 └─────────┬───────────┘
                           │
                           ▼
                ┌───────────────────────┐
                │  Kubernetes Cluster   │
                │  (EKS Control Plane)  │
                └─────────┬─────────────┘
                          │
         ┌────────────────┼────────────────┐
         │                │                │
         ▼                ▼                ▼
 ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
 │   Pod       │  │   Pod       │  │   Pod       │
 │ FastAPI API │  │ FastAPI API │  │ FastAPI API │
 │ DLL Service │  │ DLL Service │  │ DLL Service │
 └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
        │                 │                │
        └───────────Kubernetes Service────┘
                          │
                          ▼
               Docker Container Image
                          │
                          ▼
          Amazon Elastic Container Registry



# Unit testing
- Include a test suite that covers also edge cases (empty list, removing from a single-node list).

# Additional details
- After finishing, upload the changes in a Pull Request, assign it to yourself and ensure you request review from any of the invited collaborators to your repository.

# Future implementations
 Implement JSON logging for every operation (e.g., `{"event": "node_added", "value": 10, "timestamp": "..."}`) to demonstrate SRE/Monitoring proficiency.
