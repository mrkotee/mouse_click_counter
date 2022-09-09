import os
import sys

from daemon import Daemon

from counter import ClickCounter


class ClickCounterDaemon(Daemon):
    def __init__(self, pidfile):
        super().__init__(pidfile)
        self.click_counter = ClickCounter()

    def run(self):
        self.click_counter.run()


if __name__ == '__main__':
    click_daemon = ClickCounterDaemon("/tmp/click_daemon.pid")
    # click_daemon.click_counter.run()

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            click_daemon.start()
        elif 'stop' == sys.argv[1]:
            click_daemon.stop()
        elif 'restart' == sys.argv[1]:
            click_daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"usage: {sys.argv[0]} start|stop|restart")
        sys.exit(2)
