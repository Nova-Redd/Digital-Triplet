from opcua import Server, Client, ua, uamethod
from snap7.client import Client as SnapClient
from plc_utils import read_data
import time


server = Server()
url = "opc.tcp://localhost:53530/OPCUA/SimulationServer"
server.set_endpoint(url)


def plc_connect():
    global plc
    plc = SnapClient()
    plc_address = "192.168.0.1"
    plc.connect(plc_address, 0, 1)
    plc.get_connected()
    print('plc connected')

plc_connect()

name = "AI intergration"
add_space = server.register_namespace(name)
object = server.get_objects_node()
plc_type = object.add_object(add_space, "PLC_S71200")



ProcessTemp = plc_type.add_variable(add_space, 'ProcessTemp', 0.0)
ProcessTemp.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("ProcessTemp")))

Setpoint = plc_type.add_variable(add_space, 'SetPoint', 0.0)
Setpoint.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("SetPoint")))

Start = plc_type.add_variable(add_space, 'Start', False, ua.VariantType.Boolean)
Start.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("Start")))

Stop = plc_type.add_variable(add_space, 'Stop', False, ua.VariantType.Boolean)
Stop.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("Stop")))

ChillerON = plc_type.add_variable(add_space, 'ChillerON', False, ua.VariantType.Boolean)
ChillerON.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("ChillerON")))

ChillerOFF = plc_type.add_variable(add_space, 'ChillerOFF', False, ua.VariantType.Boolean)
ChillerOFF.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("ChillerOFF")))

ChillerExchangerON = plc_type.add_variable(add_space, 'ChillerExchangerON', False, ua.VariantType.Boolean)
ChillerExchangerON.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("ChillerExchangerON")))

ChillerExchangerOFF = plc_type.add_variable(add_space, 'ChillerExchangerOFF', False, ua.VariantType.Boolean)
ChillerExchangerOFF.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("ChillerExchangerOFF")))

HeaterON = plc_type.add_variable(add_space, 'HeaterON', False, ua.VariantType.Boolean)
HeaterON.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("HeaterON")))

HeaterOFF = plc_type.add_variable(add_space, 'HeaterOFF', False, ua.VariantType.Boolean)
HeaterOFF.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("HeaterOFF")))

HWExchangerON = plc_type.add_variable(add_space, 'H_exchangerON', False, ua.VariantType.Boolean)
HWExchangerON.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("HWExchangerON")))

HWExchangerOFF = plc_type.add_variable(add_space, 'H_exchangerOFF', False, ua.VariantType.Boolean)
HWExchangerOFF.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("HWExchangerOFF")))

HWPumpON = plc_type.add_variable(add_space, 'HWPumpON', False, ua.VariantType.Boolean)
HWPumpON.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("HWPumpON")))

HWPumpOFF = plc_type.add_variable(add_space, 'HWPumpOFF', False, ua.VariantType.Boolean)
HWPumpOFF.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("HWPumpOFF")))

PPumpON = plc_type.add_variable(add_space, 'PPumpON', False, ua.VariantType.Boolean)
PPumpON.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("PPumpON")))

PPumpOFF = plc_type.add_variable(add_space, 'PPumpOFF', False, ua.VariantType.Boolean)
PPumpOFF.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("PPumpOFF")))

ProcessHeating = plc_type.add_variable(add_space, 'ProcessHeating', False, ua.VariantType.Boolean)
ProcessHeating.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("ProcessHeating")))

ProcessCooling = plc_type.add_variable(add_space, 'ProcessCooling', False, ua.VariantType.Boolean)
ProcessCooling.set_attribute(ua.AttributeIds.Description, ua.DataValue(ua.LocalizedText("ProcessCooling")))

ProcessTemp.set_writable()
Setpoint.set_writable()

# start.set_writable()
Start.set_writable()
Stop.set_writable()

ChillerON.set_writable()
ChillerOFF.set_writable()

ChillerExchangerOFF.set_writable()
ChillerExchangerON.set_writable()

HeaterON.set_writable()
HeaterOFF.set_writable()

HWExchangerON.set_writable()
HWExchangerON.set_writable()

HWPumpON.set_writable()
HWPumpOFF.set_writable()

PPumpON.set_writable()
PPumpOFF.set_writable()

ProcessHeating.set_writable()
ProcessCooling.set_writable()

server.start()
print("Server started at {}".format(url))


while True:
    start = read_data(plc, 'M0.1')
    stop = read_data(plc, 'M0.2')
    setpoint = read_data(plc, 'DB2.DBD0')
    process_temp = read_data(plc, 'DB2.DBD4')
    chiller_on = read_data(plc, 'M3.1')
    chiller_off = read_data(plc, 'M4.0')
    chillerexchanger_on = read_data(plc, 'M3.4')
    chillerexchanger_off = read_data(plc, 'M4.4')
    heater_on = read_data(plc, 'M3.0')
    heater_off = read_data(plc, 'M3.7')
    hwexchanger_on = read_data(plc, 'M3.5')
    hwexchanger_off = read_data(plc, 'M4.3')
    hwpump_on = read_data(plc, 'M3.3')
    hwpump_off = read_data(plc, 'M4.1')
    ppump_on = read_data(plc, 'M3.2')
    ppump_off = read_data(plc, 'M4.2')
    process_heating = read_data(plc, 'M4.5')
    process_cooling = read_data(plc, 'M4.6')

    ProcessTemp = server.get_node('ns=2;i=2')
    ProcessTemp = ProcessTemp.set_value(process_temp)

    print(ProcessTemp)

    SetPoint = server.get_node('ns=2; i=3')
    SetPoint = SetPoint.set_value(setpoint)

    print(SetPoint)

    Start = server.get_node('ns=2; i=4')
    Start = Start.set_value(start)

    print(Start)

    Stop = server.get_node('ns=2; i=5')
    Stop = Stop.set_value(stop)

    print(Stop)

    ChillerON = server.get_node('ns=2; i=6')
    ChillerON = ChillerON.set_value(chiller_on)

    print(ChillerON)

    ChillerOFF = server.get_node('ns=2; i=7')
    ChillerOFF = ChillerOFF.set_value(chiller_off)

    print(ChillerOFF)

    ChillerExchangerON = server.get_node('ns=2; i=8')
    ChillerExchangerON = ChillerExchangerON.set_value(chillerexchanger_on)

    print(ChillerExchangerON)

    ChillerExchangerOFF = server.get_node('ns=2; i=9')
    ChillerExchangerOFF = ChillerExchangerOFF.set_value(chillerexchanger_off)

    print(ChillerExchangerOFF)

    HeaterON = server.get_node('ns=2; i=10')
    HeaterON = HeaterON.set_value(heater_on)

    print(HeaterON)

    HeaterOFF = server.get_node('ns=2; i=11')
    HeaterOFF = HeaterOFF.set_value(heater_off)

    print(HeaterOFF)

    HWExchangerON = server.get_node('ns=2; i=12')
    HWExchangerON = HWExchangerON.set_value(hwexchanger_on)

    print(HWExchangerON)

    HWExchangerOFF = server.get_node('ns=2; i=13')
    HWExchangerOFF = HWExchangerOFF.set_value(hwexchanger_off)

    print(HWExchangerOFF)

    HWPumpON = server.get_node('ns=2; i=14')
    HWPumpON = HWPumpON.set_value(hwpump_on)

    print(HWPumpON)

    HWPumpOFF = server.get_node('ns=2; i=15')
    HWPumpOFF = HWPumpOFF.set_value(hwpump_off)

    print(HWPumpOFF)

    ProcessPumpON = server.get_node('ns=2; i=16')
    ProcessPumpON = ProcessPumpON.set_value(ppump_on)

    print(ProcessPumpON)

    ProcessPumpOFF = server.get_node('ns=2; i=17')
    ProcessPumpOFF = ProcessPumpOFF.set_value(ppump_off)

    print(ProcessPumpOFF)

    ProcessHeating = server.get_node('ns=2; i=18')
    ProcessHeating = ProcessHeating.set_value(process_heating)

    print(ProcessHeating)

    ProcessCooling = server.get_node('ns=2; i=19')
    ProcessCooling = ProcessCooling.set_value(process_cooling)

    print(ProcessCooling)

    time.sleep(2)




