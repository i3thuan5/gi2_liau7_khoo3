import Pyro4
from django.core.management.base import BaseCommand
from 校對工具.views import 工具


class Command(BaseCommand):

    def handle(self, *args, **參數):
        daemon = Pyro4.Daemon()                # make a Pyro daemon
        ns = Pyro4.locateNS()                  # find the name server
        # register the greeting maker as a Pyro object
        uri = daemon.register(工具())
        # register the object with a name in the name server
        ns.register("校對工具", uri)
        print('載入好矣')

        # start the event loop of the server to wait for calls
        daemon.requestLoop()
