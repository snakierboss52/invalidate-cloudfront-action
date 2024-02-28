import boto3
import time, os, sys
 
# Create CloudFront client
cf = boto3.client('cloudfront')

distribution_id = os.getenv('cloudfront-distribution-id')
invalidation_path = os.getenv('cloudfront-invalidation-path')
  
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
print("Invalidation created successfully with Id: " + id)