import asyncio
from desktop_notifier import DesktopNotifier


notifier = DesktopNotifier()

async def main():
    bildirim_basligi= input("bildirim basligi giriniz: ")
    bildirim_mesaji= input("bildirim mesaji giriniz: ")

    await notifier.send(title=bildirim_basligi, message=bildirim_mesaji)

asyncio.run(main())
