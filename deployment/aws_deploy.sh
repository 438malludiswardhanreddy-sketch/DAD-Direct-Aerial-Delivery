#!/bin/bash
# Solapur University Final Year Project - DAD AWS Deployment Script
# Automatically builds Docker images and pushes to AWS ECR, and deploys to Elastic Beanstalk.

echo "=========================================================="
echo "    DAD AWS Elastic Beanstalk Deployment Pipeline         "
echo "=========================================================="

# 1. AWS Configuration Check
if ! command -v aws &> /dev/null; then
    echo "[AWS] Error: AWS CLI is not installed. Exiting."
    exit 1
fi

# 2. Login to AWS Elastic Container Registry (ECR)
AWS_REGION="ap-south-1"  # Mumbai Region (nearest to Solapur)
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text 2>/dev/null)

if [ -z "$AWS_ACCOUNT_ID" ]; then
    echo "[AWS] Error: Failed to fetch AWS account details. Please run 'aws configure'."
    exit 1
fi

echo "[AWS] Authenticating Docker registry to ECR..."
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# 3. Create ECR repo if it doesn't exist
echo "[AWS] Creating ECR Repository for DAD backend..."
aws ecr create-repository --repository-name dad-backend --region $AWS_REGION &>/dev/null || echo "[AWS] Repository already exists."

# 4. Build and Push Image
echo "[AWS] Building DAD Docker image..."
docker build -t dad-backend -f Dockerfile ../
docker tag dad-backend:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/dad-backend:latest

echo "[AWS] Pushing image to AWS ECR..."
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/dad-backend:latest

# 5. Deploy to AWS Elastic Beanstalk
echo "[AWS] Redeploying Elastic Beanstalk application..."
aws elasticbeanstalk update-environment --environment-name Dad-env --version-label v2.0.0 --region $AWS_REGION

echo "[AWS] Deployment complete."
