import logging
import asyncio
import platform
import ast
import struct
from zlib import Z_DEFAULT_STRATEGY

from bleak import BleakClient, BleakScanner, discover

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import threading

def UUID_vals():
    # UUID values
    return {
        'ppg': 'a7361e96-1414-4926-a415-91e5cabfe126',
        'temp': '13e9f3cc-0caf-472f-963b-5458cca2d734',
        'x': 'fba5da1c-dc0b-4100-abf7-ab2b2b23ba08',
        'y': '80bf7d48-23ce-4f68-93b1-4c34b81d9757',
        'z': '04545938-d3b6-4fb5-8141-fc1f5849ffa5'
    }

def connect():
    global uuids, data
    uuids = UUID_vals()
    data = {
        'ppg': [],
        'temp': [],
        'x': [],
        'y': [],
        'z': [],
    }

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())

async def run():
    sensor_name = 'Your Health Sensor'

    found = False
    devices = await discover()

    for d in devices:       
        if sensor_name in d.name:
            found = True
            async with BleakClient(d.address) as client:
                print(f'Connected to {d.address}')
                while(True):
                    ppg_recent = await client.read_gatt_char(uuids['ppg'])
                    data['ppg'].append(struct.unpack('d', ppg_recent)[0])

                    temp_recent = await client.read_gatt_char(uuids['temp'])
                    data['temp'].append(struct.unpack('d', temp_recent)[0])

                    x_recent = await client.read_gatt_char(uuids['x'])
                    data['x'].append(struct.unpack('d', x_recent)[0])
                    
                    y_recent = await client.read_gatt_char(uuids['y'])
                    data['y'].append(struct.unpack('d', y_recent)[0])

                    z_recent = await client.read_gatt_char(uuids['z'])
                    data['z'].append(struct.unpack('d', z_recent)[0])

    if not found:
        print('Could not connect')

connect()