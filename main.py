import boto3
import time, os, sys
 
# Create CloudFront client
cf = boto3.client('cloudfront')

distribution_id = os.environ('INPUT_CLOUDFRONT-DISTRIBUTION-ID')
invalidation_path = os.environ('INPUT_CLOUDFRONT-INVALIDATION-PATH')
  
def create_invalidation_cache(distribution_id, invalidation_path):
    res = cf.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    invalidation_path
                ]
            },
            'CallerReference': str(time.time()).replace(".", "")
        }
    )
    invalidation_id = res['Invalidation']['Id']
    return invalidation_id
 
# Create CloudFront Invalidation
id = create_invalidation_cache(distribution_id, invalidation_path)

with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
    print(f'invalidation-id={id}', file=gh_output)