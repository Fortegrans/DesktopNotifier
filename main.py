import asyncio
from email import message

from desktop_notifier import DesktopNotifier


notifier = DesktopNotifier()

async def main():
    await notifier.send(title="Merhaba Hüseyin", message="Ben Jarvis")

asyncio.run(main())
