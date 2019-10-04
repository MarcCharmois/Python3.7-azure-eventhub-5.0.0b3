import logging
from azure.eventhub import EventHubClient, EventData, EventPosition
import config as cfg


#EVENT_POSITION = EventPosition("12500000")
EVENT_POSITION = EventPosition("-1")
PARTITION = "0"
client = EventHubClient.from_connection_string(cfg.connection_str)
consumer = client.create_consumer(consumer_group="$default", partition_id=PARTITION, event_position=EVENT_POSITION, prefetch=100000)
total=0
last_offset = -1
with consumer:
    batched_events = consumer.receive(max_batch_size=100000)
    for event_data in batched_events:
        last_offset = event_data.offset
        last_sn = event_data.sequence_number
        total += 1
        print("Partition {}, Received {}, sn={} offset={}".format(
            PARTITION,
            total,
            last_sn,
            last_offset))
        print (event_data)

