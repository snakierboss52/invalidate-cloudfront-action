import sys
from main import create_invalidation

invalidation_path = []

def load():
    distribution_id = sys.argv[1]
    invalidation_path.extend(sys.argv[2])
    wait_for_service_update = sys.argv[3] if len(sys.argv) > 3 else None

    quantity = invalidation_path.count()

    create_invalidation(distribution_id, quantity ,invalidation_path)