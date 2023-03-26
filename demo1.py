import _winreg

def detect_vm():
    try:
        reg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
        key = _winreg.OpenKey(reg, r"HARDWARE\ACPI\DSDT\VBOX__")
        _winreg.CloseKey(key)
        return "VirtualBox"
    except:
        pass

    try:
        reg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
        key = _winreg.OpenKey(reg, r"HARDWARE\ACPI\DSDT\VMWARE")
        _winreg.CloseKey(key)
        return "VMware"
    except:
        pass

    return "Physical machine"
