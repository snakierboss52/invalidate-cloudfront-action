import boto3
import time, os, sys
 
# Create CloudFront client
cf = boto3.client('cloudfront')
  
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
id = create_invalidation_cache(sys.argv[1], sys.argv[2])
print("Invalidation created successfully with Id: " + id)