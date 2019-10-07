# Python3.7 Azure Eventhub 5.0.0b3 - Events Sender Receiver
## Description
several python 3.7 applications to send or receive events to or from an Azure Event Hub based on azure.eventhub 5.0.0b3
## Warnings
 - this python code is based on the **5.0.0b3 preview version of the azure-eventhub module**   
 for a version based on the azure-eventhub module 1.3.2 version see <a href="https://github.com/MarcCharmois/Python3.7-azure-eventhub-1.3.2">Python3.7-azure-eventhub-1.3.2</a>

## Installation
mkvirtualenv    
pip install --pre  azure.eventhub    
Add a config.py file   
In the config.py file, add a variable connection_str
Value of the variable : connection_str = 'Endpoint=sb://<your enventhub namespace name>.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<vaue of your shared ket>;EntityPath=<name of your event hub>     



## Features
 - events-receiver.py    
    to receive events (you will have to set EventPosition to get the latest events)    
  - events-listener.py    
    this application use a recursive method that tracks all the events untill the latest, then listen to the latest event


