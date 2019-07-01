"""
This is an example script which demonstrates how to use CRETA.NET's API (AVL List GmbH)
privided by SCHOSTE.COM GmbH (http://www.schoste.com/)

Contact office@schoste.com for all inqueries.

NOTES:
Tested with Python 3.7.3 for Win64 using PythonNET
If you use standard Python make sure to install PythonNET (pip install pythonnet)
"""
import sys
GLOBAL_IRONPython = "Iron" in sys.version

#WARNING if installed using   pip install clr   this will fail
import clr
CRETA_NET_DLL_PATH = r"C:\Program Files\AVL\Creta"

if GLOBAL_IRONPython:
    print ("IRON Python Startup")
    clr.AddReferenceToFileAndPath(CRETA_NET_DLL_PATH)
    import AVL.CRETA.API.NET.ApiFactory as CretaNET
    api = CretaNET.CreateInstance()
else:
    print ("Python .NET Startup")
    from System.Reflection import Assembly
    CretaNET = Assembly.LoadFile(CRETA_NET_DLL_PATH+"\\CretaNET.dll")
    Log4Net = Assembly.LoadFile(CRETA_NET_DLL_PATH+"\\log4net.dll")
    apiFactoryClass = CretaNET.GetType('AVL.CRETA.API.NET.ApiFactory')
    CreateInstanceMethod = apiFactoryClass.GetMethod('CreateInstance')
    api = CreateInstanceMethod.Invoke('AVL.CRETA.API.NET.CretaAPI', [''])

"""
NOTE: On x64 you cannot connect to MS Access databases because the driver is only available for x86!
Invoke the Connect() method using the parameters Connect(CRETA user name, CRETA password, server index)
"""
connected = api.Connect('administrator', '', 1)
if not connected:
    print ("Connection failed: "+api.LastError)
else:
    allProjects = api.GetProjectSUID('')
    print (allProjects)