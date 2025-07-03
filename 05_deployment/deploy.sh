#!/bin/bash

# Configuration
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
FUNCTION_NAME="strands_agents_lambda"
ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/strands-agents-lambda-bedrock-role"  # Replace with your role ARN
REGION="us-east-1"

# Create the Lambda function
aws lambda create-function \
    --function-name $FUNCTION_NAME \
    --runtime python3.12 \
    --handler lambda_function.lambda_handler \
    --timeout 30 \
    --memory-size 512 \
    --role $ROLE_ARN \
    --zip-file fileb://deployment.zip \
    --region $REGION
