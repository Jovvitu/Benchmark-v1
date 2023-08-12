import tkinter as tk
from tkinter import ttk
import platform
import psutil
import cpuinfo
import multiprocessing
import threading
import wmi
import json
import time

#________________________
#Todas Informaçoes Da CPu

def update_info_label(info_label):
    system_info = get_system_info()
    info_label.config(text=system_info)
    info_label.after(5000, update_info_label, info_label)  # Update every 2 seconds

def get_code_name():
    processor_info = cpuinfo.get_cpu_info()
    code_name = processor_info.get('brand_raw', 'N/A')
    return code_name

def get_core_vid():
    processor_info = cpuinfo.get_cpu_info()
    core_vid = processor_info.get('voltage_id', 'N/A')
    return core_vid

def get_package():
    processor_info = cpuinfo.get_cpu_info()
    package = processor_info.get('package', 'N/A')
    return package

def get_processor_family():
    processor_info = cpuinfo.get_cpu_info()
    family = processor_info.get('family', 'N/A')
    return family

def get_processor_model():
    processor_info = cpuinfo.get_cpu_info()
    model = processor_info.get('model', 'N/A')
    return model

def get_stepping():
    processor_info = cpuinfo.get_cpu_info()
    stepping = processor_info.get('stepping', 'N/A')
    return stepping

def get_extended_family():
    processor_info = cpuinfo.get_cpu_info()
    ext_family = processor_info.get('extfamily', 'N/A')
    return ext_family

def get_extended_model():
    processor_info = cpuinfo.get_cpu_info()
    ext_model = processor_info.get('extmodel', 'N/A')
    return ext_model

def get_processor_revision():
    processor_info = cpuinfo.get_cpu_info()
    revision = processor_info.get('revision', 'N/A')
    return revision

def get_core_speed():
    processor_info = cpuinfo.get_cpu_info()
    core_speed = processor_info.get('hz_actual', 'N/A')
    return core_speed

def get_multiplier():
    processor_info = cpuinfo.get_cpu_info()
    multiplier = processor_info.get('multiplier', 'N/A')
    return multiplier

def get_bus_speed():
    processor_info = cpuinfo.get_cpu_info()
    bus_speed = processor_info.get('external_clock', 'N/A')
    return bus_speed

core_speed = get_core_speed()
multiplier = get_multiplier()
bus_speed = get_bus_speed()

def get_cache_l1_data():
    processor_info = cpuinfo.get_cpu_info()
    cache_l1_data = processor_info.get('l1_data_cache_size', 'N/A')
    return cache_l1_data

def get_cache_l1_inst():
    processor_info = cpuinfo.get_cpu_info()
    cache_l1_inst = processor_info.get('l1_instruction_cache_size', 'N/A')
    return cache_l1_inst

def get_cache_l2():
    processor_info = cpuinfo.get_cpu_info()
    cache_l2 = processor_info.get('l2_cache_size', 'N/A')
    return cache_l2

def get_cache_l3():
    processor_info = cpuinfo.get_cpu_info()
    cache_l3 = processor_info.get('l3_cache_size', 'N/A')
    return cache_l3

def get_num_cores():
    processor_info = cpuinfo.get_cpu_info()
    num_cores = processor_info.get('count', 'N/A')
    return num_cores

num_cores = get_num_cores()

def get_num_threads():
    num_threads = threading.active_count()
    return num_threads

num_threads = get_num_threads()
#________________________

#Pega as informaçoes mainboard
def get_mainboard_info():
    c = wmi.WMI()
    board = c.Win32_BaseBoard()[0]
    manufacturer = board.Manufacturer
    model = board.Product
    version = board.Version
    return manufacturer, model, version

def get_bus_specs():
    c = wmi.WMI()
    bus = c.Win32_Bus()[0]
    bus_specs = bus.Name
    return bus_specs
    
def get_chipset_info():
    c = wmi.WMI()
    board = c.Win32_BaseBoard()[0]
    chipset = board.Description
    return chipset

def get_southbridge_info():
    c = wmi.WMI()
    devices = c.Win32_PnPEntity()
    southbridge = [device.Description for device in devices if device.Description and "southbridge" in device.Description.lower()]
    if southbridge:
        return southbridge[0]
    else:
        return "N/A"

def get_bios_info():
    c = wmi.WMI()
    bios = c.Win32_BIOS()[0]
    brand = bios.Manufacturer
    version = bios.SMBIOSBIOSVersion
    date = bios.ReleaseDate
    return f"Brand: {brand}\nVersion: {version}\nDate: {date}"

def get_graphics_info():
    c = wmi.WMI()
    graphics = c.Win32_VideoController()[0]
    bus = graphics.AdapterCompatibility
    current_link_width = graphics.CurrentBitsPerPixel
    max_supported_link_width = graphics.MaxMemorySupported
    current_link_speed = graphics.CurrentRefreshRate
    max_supported_link_speed = graphics.MaxRefreshRate

    return f"Bus: {bus}\nCurrent Link Width: {current_link_width} bits\nMax Supported Link Width: {max_supported_link_width} bits\nCurrent Link Speed: {current_link_speed} Hz\nMax Supported Link Speed: {max_supported_link_speed} Hz"



#Função Cpu
def get_system_info():
    system_info = f"  Procesor\n" 
    system_info += f"Operating System: {platform.system()} {platform.release()}\n"
    processor_info = cpuinfo.get_cpu_info()
    system_info += f"Code Name: {get_code_name()}\n"
    system_info += f"Package: {get_package()}\n"
    system_info += f"Core VID: {get_core_vid()}\n"
    brand = processor_info['brand_raw']
    system_info += f"Processor: {brand}\n"
    system_info += f"Family of Processor: {get_processor_family()}\n"
    system_info += f"Model of Processor: {get_processor_model()}\n"
    system_info += f"Stepping: {get_stepping()}\n"
    system_info += f"Ext. Family of Processor: {get_extended_family()}\n"
    system_info += f"Ext. Model of Processor: {get_extended_model()}\n"
    system_info += f"Revision of Processor: {get_processor_revision()}\n"
    system_info += f"   Clocks (Core #0)\n" 
    system_info += f"Core Speed: {get_core_speed()}\n"
    system_info += f"Multiplier: {get_multiplier()}\n"
    system_info += f"Bus Speed: {get_bus_speed()}\n"
    system_info += f"  Cache\n" 
    system_info += f"Cache L1 Data: {get_cache_l1_data()}\n"
    system_info += f"Cache L1 Instruction: {get_cache_l1_inst()}\n"
    system_info += f"Cache L2: {get_cache_l2()}\n"
    system_info += f"Cache L3: {get_cache_l3()}\n"

    system_info += f"Número de núcleos da CPU: {num_cores}\n\n"
    num_threads = get_num_threads()
    system_info += f"Número de threads ativas: {num_threads}\n"

    return system_info



#_________________

#Função Aba_Mainboard
def get_mainboard_system_info():
    manufacturer, model, version = get_mainboard_info()
    system_info = f"  Motherboard\n"
    system_info += f"Manufacturer: {manufacturer}\nModel: {model}\nVersion: {version}\n"
    bus_specs = get_bus_specs()
    system_info += f"Bus Specs:{bus_specs}\n"
    chipset = get_chipset_info()
    system_info += f"Chipset: {chipset}\n"
    southbridge = get_southbridge_info()
    system_info += f"Southbridge: {southbridge}\n"
    system_info = f"  Bios\n"
    bios_info = get_bios_info()
    system_info += f"\nBIOS Information:\n{bios_info}"
    graphics_info = get_graphics_info()
    system_info = f"Graphic Interface\n"
    system_info += f"\nGraphics Interface Information:\n{graphics_info}"
    return system_info
#________

#Função Aba_Memory
def get_memory_system_info():
    memory_info = ""
    # Obtenha as informações da memória aqui e adicione ao memory_info
    # Exemplo:
    memory_info +=f"General\n"
    memory_info += "Total Memory: {} GB\n".format(psutil.virtual_memory().total / (1024**3))
    memory_info += "Available Memory: {} GB\n".format(psutil.virtual_memory().available / (1024**3))
    memory_info += "Used Memory: {} GB\n".format(psutil.virtual_memory().used / (1024**3))
    memory_info += "Memory Usage Percentage: {}%\n".format(psutil.virtual_memory().percent)
    
    # Informações sobre os canais de memória
    c = wmi.WMI()
    memory_chips = c.Win32_PhysicalMemory()
    channel_count = len(set(chip.DeviceLocator for chip in memory_chips))
    memory_info += "Memory Channels: {}\n".format(channel_count)
    
    # Informações sobre a frequência e tipo da memória
    memory_modules = c.Win32_PhysicalMemory()
    for module in memory_modules:
        uncore_frequency = module.ConfiguredClockSpeed
        memory_type = module.MemoryType
        memory_info += "Uncore Frequency: {} MHz\n".format(uncore_frequency)
        memory_info += "Memory Type: {}\n".format(memory_type)
        
        # Obtém as informações FSB:DRAM usando a propriedade "PartNumber"
        if "partnumber" in module.Properties_:
            part_number = module.Properties_["PartNumber"].Value
            fsb_dram = extract_fsb_dram_from_part_number(part_number)
            memory_info += "FSB:DRAM: {}\n".format(fsb_dram)
        
        # Obtém os timings da memória
        if "configuredtimings" in module.Properties_:
            memory_info +=f"Timings\n"
            timings = module.Properties_["configuredtimings"].Value
            memory_info += "CAS# LATENCY (CL): {}\n".format(timings[0])
            memory_info += "RAS# PRECHARGE (tRP): {}\n".format(timings[1])
            memory_info += "CYCLE TIME (tRAS): {}\n".format(timings[2])
            memory_info += "BANK CYCLE TIMER (tRC): {}\n".format(timings[3])
            memory_info += "COMMAND RATE (CR): {}\n".format(timings[4])
            memory_info += "DRAM Idle Timer: {}\n".format(timings[5])
            memory_info += "Total CAS# (tRDRAM): {}\n".format(timings[6])
            memory_info += "Row to Column (tRCD): {}\n".format(timings[7])
    
    return memory_info

def extract_fsb_dram_from_part_number(part_number):
    # Implemente a lógica para extrair as informações FSB:DRAM do número da peça
    # Substitua esta implementação pelo seu código real para extrair as informações FSB:DRAM
    fsb_dram = "N/A"
    return fsb_dram


#________

#Função aba SPD
def get_memory_slot_info():
    slot_info = ""
    c = wmi.WMI()
    memory_devices = c.Win32_PhysicalMemory()

    for device in memory_devices:
        slot_info +=f"Memory Slot Selection\n"
        slot_info += "Memory Slot: {}\n".format(device.DeviceLocator)
        slot_info += "Type: {}\n".format(device.MemoryType)

        # Obtendo as informações do SPD (Serial Presence Detect) para o slot de memória
        spd_info = get_spd_info(device.SerialNumber)
        if spd_info is not None:
            slot_info += "Module Manufacturer: {}\n".format(spd_info.get("ModuleManufacturer", "N/A"))
            slot_info += "DRAM Manufacturer Part Number: {}\n".format(spd_info.get("DRAMManufacturerPartNumber", "N/A"))
            slot_info += "Serial Number: {}\n".format(spd_info.get("SerialNumber", "N/A"))
            slot_info += "Module Size: {}\n".format(spd_info.get("ModuleSize", "N/A"))
            slot_info += "Week/Year: {}\n".format(spd_info.get("WeekYear", "N/A"))
            slot_info += "Registered: {}\n".format(spd_info.get("Registered", "N/A"))

        slot_info += "\n"
        timings_table = spd_info.get("TimingsTable")
        if timings_table:
            
            slot_info += "Timings Table:\n"
            for row in timings_table:
                slot_info += "\t".join(row) + "\n"

        slot_info += "\n"
    return slot_info
#___________________________

#

# Função auxiliar para obter as informações do SPD (Serial Presence Detect) para um determinado slot de memória
def get_spd_info(serial_number):
    c = wmi.WMI()
    memory_modules = c.Win32_PhysicalMemory()

    for module in memory_modules:
        if module.SerialNumber == serial_number:
            spd_info = {}
            spd_info["ModuleManufacturer"] = module.Manufacturer
            spd_info["DRAMManufacturerPartNumber"] = module.PartNumber
            spd_info["SerialNumber"] = module.SerialNumber
            spd_info["ModuleSize"] = module.Capacity
            spd_info["WeekYear"] = module.Manufacturer
            return spd_info
        


    return None
#__________

#Função Aba Graphics
def get_graphics_info():
    info = ""

    c = wmi.WMI()
    graphics_devices = c.Win32_VideoController()

    # Display Device Selection
    info += "Display Device Selection:\n"
    # Adicione aqui o código para exibir opções de escolha das placas de vídeo a serem mostradas

    # Loop para obter informações de cada dispositivo de vídeo selecionado
    for device in graphics_devices:
        info += "\n"
        info += "GPU\n"
        info += "Device Name: {}\n".format(device.Name)

        # Informações de Clocks
        info += "Clocks:\n"
        info += "  GFX Core: {}\n".format(device.CurrentRefreshRate)
        info += "  Memory: {}\n".format(device.CurrentHorizontalResolution)

        # Informações de Memória
        info += "Memory:\n"
        info += "  Size: {}\n".format(device.AdapterRAM)
        info += "  Vendor: {}\n".format(device.VideoProcessor)

    return info

#________________

#Função Aba Bench

def get_bench_info():
    # Lógica para obter as informações de benchmark
    # Substitua esta parte pelo seu código real
    bench_info = "In-Work Progression"
    return bench_info
#__________

#Função Aba About
def get_windows_version():
    return platform.platform()

def get_directx_version():
    c = wmi.WMI(namespace="root\CIMv2")
    directx = c.Win32_VideoController()[0].DriverVersion
    return directx

def get_about_info():
    about_info = "About JamesInspectorX\n"
    about_info += "Version 0.0.1 - May 2023\n"
    about_info += "Author: Joao Vitor A. Gasparotto\n\n"
    about_info += "JamesInspectorX is a freeware inspired by CPU-Z.\n\n"
    about_info += "Windows Version: {}\n".format(get_windows_version())
    about_info += "DirectX Version: {}\n".format(get_directx_version())
    return about_info
#________________

#Interface

root = tk.Tk()
root.title("JamesInspectorX")
root.geometry("800x600")  # Defina o tamanho desejado da janela
root.resizable(False, False)  # Impede que a janela seja redimensionada
style = ttk.Style()
style.theme_use("clam")
 
# Criação do widget Notebook
notebook = ttk.Notebook(root, style="Custom.TNotebook")
style.configure("Custom.TNotebook.Tab", font=("Arial", 13, "bold"))

# Criação das abas
style.configure("Custom.TNotebook.Tab", foreground="blue")
tab_names = ["CPU", "Mainboard", "Memory", "SPD", "Graphics", "Bench", "About"]

tabs = []
for name in tab_names:
    tab = ttk.Frame(notebook)
    tabs.append(tab)
    notebook.add(tab, text=name)

notebook.pack(padx=10, pady=10)

# Criação do rótulo em cada aba
info_labels = []
for i, tab in enumerate(tabs):
    info_label = tk.Label(tab, font=("Arial", 12), justify="left")
    info_label.pack(padx=10, pady=10)
    info_labels.append(info_label)

#_____________________________



# Função para atualizar as informações em cada aba

def update_info_labels():
    cpu_system_info = get_system_info()
    info_labels[0].config(text=cpu_system_info)
    mainboard_system_info = get_mainboard_system_info()
    info_labels[1].config(text=mainboard_system_info)
    memory_system_info = get_memory_system_info()
    info_labels[2].config(text=memory_system_info)
    memory_slot_info = get_memory_slot_info()
    info_labels[3].config(text=memory_slot_info)
    graphics_info = get_graphics_info()
    info_labels[4].config(text=graphics_info)
    bench_system_info = get_bench_info()
    info_labels[5].config(text=bench_system_info)
    about_info = get_about_info()
    info_labels[6].config(text=about_info)
  #  root.after(2000, update_info_labels)#atualiza a cada 5 segundos


# Inicia a atualização das informações
update_info_labels()

root.mainloop()
