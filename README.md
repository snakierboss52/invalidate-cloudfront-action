# Create invalidation caches in AWS Cloudfront

Whith this action you can request a invalidation of caches in one of your cloudfront distribution

# Requirements

*Previously you must have configured your action of AWS Credentials using your Access and Secret Key below you have an example of how can you do this*

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
    distribution-id: *DISTRIBUTION_ID*
    paths: '/*'
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

