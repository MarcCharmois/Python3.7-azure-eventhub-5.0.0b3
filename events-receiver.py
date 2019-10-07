import logging
from azure.eventhub import EventHubClient, EventData, EventPosition
import config as cfg

# set your event position to have the latest one so as you can see the latest events
EVENT_POSITION = EventPosition("14500000")
#EVENT_POSITION = EventPosition("-1")
PARTITION = "0"
client = EventHubClient.from_connection_string(cfg.connection_str)
#for a vanilla eventhub replace "custom" consumer_group by "$default"
consumer = client.create_consumer(consumer_group="custom", partition_id=PARTITION, event_position=EVENT_POSITION, prefetch=100000)
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

