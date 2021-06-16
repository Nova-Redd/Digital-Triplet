from plc_utils import write_data,read_data
from opcua import Client
from snap7.client import Client as SnapClient
import speech_recognition as sr
import pyttsx3 as tts
import os
from facerec import face_rec
import regex as re
from AI_chatbot_functions import *
from mask_detector import *


def plc_connect():
    predictor = face_rec()

    if predictor is True:
        global plc
        plc = SnapClient()
        url = "opc.tcp://localhost:53530/OPCUA/SimulationServer"
        opc_client = Client(url)
        opc_client.connect()
        plc_address = "192.168.0.1"
        plc.connect(plc_address, 0, 1)
        plc.get_connected()
        print('plc connected')



        engine = tts.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 180)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def talk(text):
            engine.say(text)
            engine.runAndWait()

        On_command = 'turn the machine on'
        Off_command = 'turn the machine off'
        Chiller_on = 'turn the chiller on'
        Chiller_off = 'turn the chiller off'
        Heater_on = 'turn the heater on'
        Heater_off = 'turn the heater off'
        Ppump_on = 'turn the process pump on'
        Ppump_off = 'turn the process pump on'
        HWpump_on = 'turn the hot water pump on'
        HWpump_off = 'turn the hot water pump off'
        simulation = 'show me the simulation'
        valve = 'open the Valve'
        setpoint = 'change the set point to'
        process = 'show me the process temperature'
        simulation = 'show me the simulation'
        status = 'show me the status of all components'
        pattern = ["hi", "how are you", "is anyone there?", "hello","bye", "see you later", "goodbye","thanks", "thank you", "that's helpful", "what hours are you open?", "what are your hours?", "when are you open?", "what time are you open", "what is the boiling point of water?", "at what temperature does water boil?", "when is the lab open?", "when do you open today?", "what are your hours today?", "What is the temperature range of the machine", "How hot can the water get", "How cold can the water get", "How high can the temperature get?", "how low can the temperature get", "how do you heat the water", "how do you raise the set point", "how do you raise the process temperature", "describe the heating procedure", "how do you cool the water", "how do you lower the set point", "how do you lower the process temperature", "how do you decrease the process temperature", "Describe the cooling procedure", "how does the system work", "how does the machine work", "describe the system to me", "tell me everything about your system", "describe the parts of the system to me", "how many sensors do you have", "how do your sensors operate", "how do your sensors work", "tell me how your sensors work"]

        def get_command():
            Rec = sr.Recognizer()

            with sr.Microphone() as source:
                Rec.energy_threshold = 10000
                Rec.adjust_for_ambient_noise(source, 1.2)
                print("Listening")
                audio = Rec.listen(source)
                command = ""
                try:
                    command = Rec.recognize_google(audio)
                    print(command)
                except sr.UnknownValueError:
                    print('repeat your statement')
                except sr.RequestError:
                    print('The system is down')
            return command

        while True:
            mask = mask_detector()
            if mask is True:
                talk('talk to me')
                command = get_command()

                if On_command in command:
                    talk("Turning the machine on")
                    write_data(plc, "M0.2", False)
                    write_data(plc, "M0.1", True)
                    write_data(plc, "M2.6", True)

                if Off_command in command:
                    talk("Turning the machine off")
                    write_data(plc, "M0.2", True)

                if Chiller_on in command:
                    talk("Turning the chiller on")
                    write_data(plc, "M1.0", True)

                if Chiller_off in command:
                    talk("Switching the chiller off")
                    write_data(plc, "M1.0", False)

                if valve in command:
                    opening = re.findall('\d+', command)
                    percentage = int(opening[0])
                    talk(f"opening the valve at {percentage} percent")
                    write_data(plc, 'QW96', percentage)

                if setpoint and "degrees" in command:
                    set_point = re.findall('\d+', command)
                    temp = int(set_point[0])
                    talk(f"setting a set point of {temp} degrees")
                    write_data(plc, 'DB2.DBD0', temp)
                    temperature = read_data(plc, 'DB2.DBD4')

                    if temp < temperature:
                        talk("Turning the chiller on")
                        write_data(plc, "M1.0", True)

                if process in command:
                    process_temp = read_data(plc, 'DB2.DBD4')
                    talk(f'The process temperature is {process_temp} degrees')

                if simulation in command:
                    filename = r'C:\\Users\\ADMIN\\PycharmProjects\\TPCAIchatbot\\THERMAL_PROCESS_CONTROL\\T.P.C.S_simulation_assembly.prt'
                    FILE = os.system("start " + filename)
                    talk('Opening the CAD model, please follow the instructions below when loading is complete')
                    print("""
                    1. Click the Home tab.In the Automation Group, click Symbol Table then choose Signal Mapping
                    2. Next to OPC UA servers click is a tiny button named Setting, another table named External signal configuration will appear
                    3. Click the top button on the right side named Add New Server
                    4. Enter this url opc.tcp://localhost:53530/OPCUA/SimulationServer and click OK
                    """)

                if status in command:
                    start = read_data(plc, 'M0.1')
                    set_point = read_data(plc, 'DB2.DBD0')
                    process_temp = read_data(plc, 'DB2.DBD4')
                    chhiller_on = read_data(plc, 'M3.1')
                    chiller_exchanger_on = read_data(plc, 'M3.4')
                    hheater_on = read_data(plc, 'M3.0')
                    hw_exchanger_on = read_data(plc, 'M3.5')
                    hw_pump_on = read_data(plc, 'M3.3')
                    p_pump_on = read_data(plc, 'M3.2')
                    process_heating = read_data(plc, 'M4.5')
                    process_cooling = read_data(plc, 'M4.6')

                    print(f'Machine start:{start}')
                    print(f'Setpoint:{set_point}')
                    print(f'Process Temperature:{process_temp}')
                    print(f'Chiller:{chhiller_on}')
                    print(f'Chiller Exchanger: {chiller_exchanger_on}')
                    print(f'Heater:{hheater_on}')
                    print(f'Hot Water Exchanger:{hw_exchanger_on}')
                    print(f'Hot Water Pump:{hw_pump_on}')
                    print(f'Process Pump:{p_pump_on}')
                    print(f'Process Cooling:{process_cooling}')
                    print(f'Process Heating:{process_heating}')

                if command in pattern:
                    talk(chatbot_response(command))
            else:
                talk('Put your mask on')


    else:
        print('Unauthorised user please step away from the machine')


plc_connect()
