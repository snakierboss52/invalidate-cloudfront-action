# Create invalidation caches in AWS Cloudfront

With this action you can request a invalidation of caches in one of your cloudfront distribution

# Requirements

*Previously you must have configured your action of AWS Credentials using your Access and Secret Key. You have an example of how to do it below*

```
    - name: Setup AWS CLI
      uses: aws-actions/configure-aws-credentials@v4
      with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY }}
          aws-secret-access-key: ${{ secretsAWS_SECRET_KEY }}
          aws-region: us-east-1
```

# Usage

```
    - name: Invalidate Caches from AWS Cloudfront Distribution
      uses: snakierboss/cloudfront-invalidate-caches@v0.1.0
      with:
        cloudfront-distribution-id: *DISTRIBUTION_ID*
        cloudfront-invalidation-path: '/*'
```

# Inputs

```
    inputs:
      cloudfront-distribution-id:
        description: 'The Id of a your AWS Cloudfront distribution'
        required: true
      cloudfront-invalidation-path:
        description: 'Path to invalidate in the cloudfront distribution'
        required: true
        default: '/*'
```

# Outputs

```
  outputs:
    invalidation-id:
      description: 'The ID of invalidation caches created.'
```

