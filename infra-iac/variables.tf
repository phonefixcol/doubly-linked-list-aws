variable "aws_region" {
  type        = string
  description = "AWS region to use for resources."
  default     = "us-east-1"
}

variable "vpc_name" {
  type        = string
  description = "Name of the VPC"
  default     = "kommit-eks-cluster"
}

variable "vpc_cidr_block" {
  type        = string
  description = "Base CIDR Block for VPC"
  default     = "10.0.0.0/16"
}

variable "eks_cluster_name" {
  type        = string
  description = "Name of the EKS Cluster"
  default     = "kommit-eks-cluster"
}

variable "environment" {
  type        = string
  description = "Environment for deployment"
  default     = "DEV"
}