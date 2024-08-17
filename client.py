import aiohttp
import asyncio

async def main():
    headers = {"User-Agent": "MyApp/1.0"}
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60), headers=headers) as session:
        async with session.get('http://localhost:8080') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.run(main())