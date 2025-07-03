#!/bin/bash
set -e

echo "Creating Lambda deployment package..."

# Ensure we have a clean workspace
rm -rf package deployment.zip
mkdir -p package

# Copy function code
cp lambda_function.py package/

echo "Installing dependencies..."
# Install Lambda-compatible packages
pip install --platform manylinux2014_x86_64 --implementation cp --python-version 3.9 --only-binary=:all: --target ./package strands-agents
pip install --platform manylinux2014_x86_64 --implementation cp --python-version 3.9 --only-binary=:all: --target ./package pydantic

# Create deployment package
echo "Creating ZIP file..."
cd package
zip -r ../deployment.zip .
cd ..

# Clean up
rm -rf package
echo "✅ Deployment package created successfully: deployment.zip"
echo "You can now upload this to AWS Lambda using:"
echo "aws lambda update-function-code --function-name YOUR_FUNCTION_NAME --zip-file fileb://deployment.zip"
