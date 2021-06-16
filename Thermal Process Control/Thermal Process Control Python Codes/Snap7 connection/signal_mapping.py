from opcua import Client
import time

url = "opc.tcp://localhost:53530/OPCUA/SimulationServer"
nx_client = Client(url)
nx_client.connect()
print('client connected')

while True:
    ProcessTemp = nx_client.get_node('ns=2;i=2')
    Temperature = ProcessTemp.get_value()
    print(Temperature)

    SetPoint = nx_client.get_node('ns=2; i=3')
    SetPoint = SetPoint.get_value()
    print(SetPoint)

    Start = nx_client.get_node('ns=2; i=4')
    Start = Start.get_value()
    print(Start)

    Stop = nx_client.get_node('ns=2; i=5')
    Stop = Stop.get_value()
    print(Stop)

    ChillerON = nx_client.get_node('ns=2; i=6')
    ChillerON = ChillerON.get_value()
    print(ChillerON)

    ChillerOFF = nx_client.get_node('ns=2; i=7')
    ChillerOFF = ChillerOFF.get_value()
    print(ChillerOFF)

    ChillerExchangerON = nx_client.get_node('ns=2; i=8')
    ChillerExchangerON = ChillerExchangerON.get_value()
    print(ChillerExchangerON)

    ChillerExchangerOFF = nx_client.get_node('ns=2; i=9')
    ChillerExchangerOFF = ChillerExchangerOFF.get_value()
    print(ChillerExchangerOFF)

    HeaterON = nx_client.get_node('ns=2; i=10')
    HeaterON = HeaterON.get_value()
    print(HeaterON)

    HeaterOFF = nx_client.get_node('ns=2; i=11')
    HeaterOFF = HeaterOFF.get_value()
    print(HeaterOFF)

    HWExchangerON = nx_client.get_node('ns=2; i=12')
    HWExchangerON = HWExchangerON.get_value()
    print(HWExchangerON)

    HWExchangerOFF = nx_client.get_node('ns=2; i=13')
    HWExchangerOFF = HWExchangerOFF.get_value()
    print(HWExchangerOFF)

    HWPumpON = nx_client.get_node('ns=2; i=14')
    HWPumpON = HWPumpON.get_value()
    print(HWPumpON)

    HWPumpOFF = nx_client.get_node('ns=2; i=15')
    HWPumpOFF = HWPumpOFF.get_value()
    print(HWPumpOFF)

    ProcessPumpON = nx_client.get_node('ns=2; i=16')
    ProcessPumpON = ProcessPumpON.get_value()
    print(ProcessPumpON)

    ProcessPumpOFF = nx_client.get_node('ns=2; i=17')
    ProcessPumpOFF = ProcessPumpOFF.get_value()
    print(ProcessPumpOFF)

    ProcessHeating = nx_client.get_node('ns=2; i=18')
    ProcessHeating = ProcessHeating.get_value()
    print(ProcessHeating)

    ProcessCooling = nx_client.get_node('ns=2; i=19')
    ProcessCooling = ProcessCooling.get_value()
    print(ProcessCooling)

    time.sleep(2)
