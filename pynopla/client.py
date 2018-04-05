import asyncio
import aiohttp
import async_timeout
import json
from collections import namedtuple

loop = asyncio.get_event_loop()


async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


def json_to_object(data, name):
    return namedtuple(f'{name}', data.keys())(*data.values())


class InoplaClient:

    def __init__(self, api_id, api_key, api_format):
        self.api_id = api_id
        self.api_key = api_key
        self.api_format = api_format
        self.api_url = f'https://api.inopla.de/v1000/{self.api_format}/{self.api_id}/{self.api_key}/SIP'
        self.users = {}
        self.groups = {}
        self.devices = {}

    @classmethod
    async def create(cls, api_id, api_key, api_format='json'):
        self = InoplaClient(api_id, api_key, api_format)
        try:
            await self.check_connection()
        except ConnectionError:
            print("Can't connect to Inopla Api")
            loop.stop()
        return self

    async def check_connection(self):
        async with aiohttp.ClientSession() as session:
            if json.loads(await fetch(session, f'{self.api_url}')).get("error", {'code': 0})['code'] == 401:
                raise ConnectionError

    async def get_users(self):
        async with aiohttp.ClientSession() as session:
            users = json.loads(await fetch(session, f'{self.api_url}/Users'))
            for user in users.get("response").get("data"):
                self.users[user.get('name')] = json_to_object(user, "User")

    async def get_groups(self):
        async with aiohttp.ClientSession() as session:
            groups = json.loads(await fetch(session, f'{self.api_url}/Groups'))
            for group in groups.get("response").get("data"):
                self.groups[group.get('name')] = json_to_object(group, "Group")

    async def get_devices(self):
        async with aiohttp.ClientSession() as session:
            devices = json.loads(await fetch(session, f'{self.api_url}/Devices'))
            for device in devices.get("response").get("data"):
                self.devices[device.get('id')] = json_to_object(device, "Device")
