import json
import os
import logging
logger = logging.getLogger()

print('Loading function')


def lambda_handler(event, context):
    
    with open("CounterPartyStatic.txt", "r") as file:
        counter_party_static_content = file.read()
        counter_party_id = event['counter_party_id']
        if counter_party_id in counter_party_static_content:
            logger.info(f"Found counterparty {counter_party_id} static file.")  
        else:
            logger.error(f"Counterparty {counter_party_id} not found in static file.")  
    return 200
    
