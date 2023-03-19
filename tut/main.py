import sys
import time
from PyQt5 import QtCore
from PyQt5 import QtBluetooth as QtBt


class App(QtCore.QCoreApplication):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.scan_for_devices()
        self.exec()

    def finished(self):
        # print(self.agent.isActive(), self.agent.discoveredDevices())
        print("finishing")
        for info in self.agent.discoveredDevices():
            print(f"Name: {info.name()}")
            print(f"Address: {info.address().toString()}")
        print("Finished")

    # def finish(self, *args, **kwargs):
    #     print("finished", args, kwargs)

    def blt_error(self):
        print("Error occurs")

    def discoverer(self, info):
        print(f"Name: {info.name()}")
        print(f"Uuid: {info.address().toString()}")

    def scan_for_devices(self):
        self.address = QtBt.QBluetoothAddress()
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent(self.address)
        # self.agent.deviceDiscovered.connect(self.discoverer)
        self.agent.finished.connect(self.finished)
        self.agent.error.connect(self.blt_error)

        self.agent.start()


if __name__ == "__main__":
    app = App(sys.argv)
