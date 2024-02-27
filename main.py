import boto3
import time, os
 
# Create CloudFront client
cf = boto3.client('cloudfront')
 
# Enter Original name
 
#DISTRIBUTION_ID = os.environ.get("DISTRIBUTION_ID")
 
# Create CloudFront invalidation
def create_invalidation(distribution_id, quantity ,invalidation_path, wait_for_service_update):
    res = cf.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': quantity,
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
id = create_invalidation()
print("Invalidation created successfully with Id: " + id)