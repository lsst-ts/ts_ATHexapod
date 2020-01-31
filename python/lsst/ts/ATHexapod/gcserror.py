#!/usr/bin python
# -*- coding: utf-8 -*-
"""Provide GCSError definitions and GCSError exception class."""
# Too many lines in module pylint: disable=C0302

import logging
import enum

__signature__ = 0x1d86c75890c9cfded5cd50105c096649


class PIError(enum.Enum):
    """Provide enum for PI Errors."""
    E_1_COM_ERROR = -1
    """Error during com operation (could not be specified)"""
    E_2_SEND_ERROR = -2
    """Error while sending data"""
    E_3_REC_ERROR = -3
    """Error while receiving data"""
    E_4_NOT_CONNECTED_ERROR = -4
    """Not connected (no port with given ID open)"""
    E_5_COM_BUFFER_OVERFLOW = -5
    """Buffer overflow"""
    E_6_CONNECTION_FAILED = -6
    """Error while opening port"""
    E_7_COM_TIMEOUT = -7
    """Timeout error"""
    E_8_COM_MULTILINE_RESPONSE = -8
    """There are more lines waiting in the buffer"""
    E_9_COM_INVALID_ID = -9
    """There is no interface or DLL handle with the given ID"""
    E_10_COM_NOTIFY_EVENT_ERROR = -10
    """Event/message for notification could not be opened"""
    E_11_COM_NOT_IMPLEMENTED = -11
    """Function not supported by this inteface type"""
    E_12_COM_ECHO_ERROR = -12
    """Error while sending "echoed" data"""
    E_13_COM_GPIB_EDVR = -13
    """IEEE488: System error"""
    E_14_COM_GPIB_ECIC = -14
    """IEEE488: Function requires GPIB board to be CIC"""
    E_15_COM_GPIB_ENOL = -15
    """IEEE488: Write function detected no listeners"""
    E_16_COM_GPIB_EADR = -16
    """IEEE488: Interface board not addressed correctly"""
    E_17_COM_GPIB_EARG = -17
    """IEEE488: Invalid argument to function call"""
    E_18_COM_GPIB_ESAC = -18
    """IEEE488: Function requires GPIB board to be SAC"""
    E_19_COM_GPIB_EABO = -19
    """IEEE488: I/O operation aborted"""
    E_20_COM_GPIB_ENEB = -20
    """IEEE488: Interface board not found"""
    E_21_COM_GPIB_EDMA = -21
    """IEEE488: Error performing DMA"""
    E_22_COM_GPIB_EOIP = -22
    """IEEE488: I/O operation started before previous operation was completed"""  # noqa: W505
    E_23_COM_GPIB_ECAP = -23
    """IEEE488: NO capablity for intended operation"""
    E_24_COM_GPIB_EFSO = -24
    """IEEE488: File system operation error"""
    E_25_COM_GPIB_EBUS = -25
    """IEEE488: Command error during device call"""
    E_26_COM_GPIB_ESTB = -26
    """IEEE488: Serial poll-status byte lost"""
    E_27_COM_GPIB_ESRQ = -27
    """IEEE488: SRQ remains asserted"""
    E_28_COM_GPIB_ETAB = -28
    """IEEE488: Return buffer full"""
    E_29_COM_GPIB_ELCK = -29
    """IEEE488: Address or board locked"""
    E_30_COM_RS_INVALID_DATA_BITS = -30
    """RS-232: 5 data bits with 2 stop bits is an invalid combination, as is 6, 7, or 8 data bits with 1.5 stop bits"""  # noqa: E501 W505
    E_31_COM_ERROR_RS_SETTINGS = -31
    """RS-232: Error configuring the COM port"""
    E_32_COM_INTERNAL_RESOURCES_ERROR = -32
    """Error dealing with internal system resources (events, threads, ...)"""
    E_33_COM_DLL_FUNC_ERROR = -33
    """A DLL or one of the required functions could not be loaded"""
    E_34_COM_FTDIUSB_INVALID_HANDLE = -34
    """FTDIUSB: invalid handle"""
    E_35_COM_FTDIUSB_DEVICE_NOT_FOUND = -35
    """FTDIUSB: device not found"""
    E_36_COM_FTDIUSB_DEVICE_NOT_OPENED = -36
    """FTDIUSB: device not opened"""
    E_37_COM_FTDIUSB_IO_ERROR = -37
    """FTDIUSB: IO error"""
    E_38_COM_FTDIUSB_INSUFFICIENT_RESOURCES = -38
    """FTDIUSB: insufficient resources"""
    E_39_COM_FTDIUSB_INVALID_PARAMETER = -39
    """FTDIUSB: invalid parameter"""
    E_40_COM_FTDIUSB_INVALID_BAUD_RATE = -40
    """FTDIUSB: invalid baud rate"""
    E_41_COM_FTDIUSB_DEVICE_NOT_OPENED_FOR_ERASE = -41
    """FTDIUSB: device not opened for erase"""
    E_42_COM_FTDIUSB_DEVICE_NOT_OPENED_FOR_WRITE = -42
    """FTDIUSB: device not opened for write"""
    E_43_COM_FTDIUSB_FAILED_TO_WRITE_DEVICE = -43
    """FTDIUSB: failed to write device"""
    E_44_COM_FTDIUSB_EEPROM_READ_FAILED = -44
    """FTDIUSB: EEPROM read failed"""
    E_45_COM_FTDIUSB_EEPROM_WRITE_FAILED = -45
    """FTDIUSB: EEPROM write failed"""
    E_46_COM_FTDIUSB_EEPROM_ERASE_FAILED = -46
    """FTDIUSB: EEPROM erase failed"""
    E_47_COM_FTDIUSB_EEPROM_NOT_PRESENT = -47
    """FTDIUSB: EEPROM not present"""
    E_48_COM_FTDIUSB_EEPROM_NOT_PROGRAMMED = -48
    """FTDIUSB: EEPROM not programmed"""
    E_49_COM_FTDIUSB_INVALID_ARGS = -49
    """FTDIUSB: invalid arguments"""
    E_50_COM_FTDIUSB_NOT_SUPPORTED = -50
    """FTDIUSB: not supported"""
    E_51_COM_FTDIUSB_OTHER_ERROR = -51
    """FTDIUSB: other error"""
    E_52_COM_PORT_ALREADY_OPEN = -52
    """Error while opening the COM port: was already open"""
    E_53_COM_PORT_CHECKSUM_ERROR = -53
    """Checksum error in received data from COM port"""
    E_54_COM_SOCKET_NOT_READY = -54
    """Socket not ready, you should call the function again"""
    E_55_COM_SOCKET_PORT_IN_USE = -55
    """Port is used by another socket"""
    E_56_COM_SOCKET_NOT_CONNECTED = -56
    """Socket not connected (or not valid)"""
    E_57_COM_SOCKET_TERMINATED = -57
    """Connection terminated (by peer)"""
    E_58_COM_SOCKET_NO_RESPONSE = -58
    """Can't connect to peer"""
    E_59_COM_SOCKET_INTERRUPTED = -59
    """Operation was interrupted by nonblocked signal"""
    E_60_COM_PCI_INVALID_ID = -60
    """No device with this ID is present"""
    E_61_COM_PCI_ACCESS_DENIED = -61
    """Driver  could not be opened (on Vista: run as administrator!)"""
    E_62_COM_SOCKET_HOST_NOT_FOUND = -62
    """Host not found"""
    E_63_COM_DEVICE_CONNECTED = -63
    """Device already connected"""
    E_1001_PI_UNKNOWN_AXIS_IDENTIFIER = -1001
    """Unknown axis identifier"""
    E_1002_PI_NR_NAV_OUT_OF_RANGE = -1002
    """Number for NAV out of range--must be in [1,10000]"""
    E_1003_PI_INVALID_SGA = -1003
    """Invalid value for SGA--must be one of 1, 10, 100, 1000"""
    E_1004_PI_UNEXPECTED_RESPONSE = -1004
    """Controller sent unexpected response"""
    E_1005_PI_NO_MANUAL_PAD = -1005
    """No manual control pad installed, calls to SMA and related commands are not allowed"""  # noqa: W505
    E_1006_PI_INVALID_MANUAL_PAD_KNOB = -1006
    """Invalid number for manual control pad knob"""
    E_1007_PI_INVALID_MANUAL_PAD_AXIS = -1007
    """Axis not currently controlled by a manual control pad"""
    E_1008_PI_CONTROLLER_BUSY = -1008
    """Controller is busy with some lengthy operation (e.g., reference move, fast scan algorithm)"""  # noqa: W505, E501
    E_1009_PI_THREAD_ERROR = -1009
    """Internal error--could not start thread"""
    E_1010_PI_IN_MACRO_MODE = -1010
    """Controller is (already) in macro mode--command not valid in macro mode"""  # noqa: W505
    E_1011_PI_NOT_IN_MACRO_MODE = -1011
    """Controller is (already) in macro mode--command not valid in macro mode"""  # noqa: W505
    E_1012_PI_MACRO_FILE_ERROR = -1012
    """Could not open file to write or read macro"""
    E_1013_PI_NO_MACRO_OR_EMPTY = -1013
    """No macro with given name on controller, or macro is empty"""
    E_1014_PI_MACRO_EDITOR_ERROR = -1014
    """Internal error in macro editor"""
    E_1015_PI_INVALID_ARGUMENT = -1015
    """One or more arguments given to function is invalid (empty string, index out of range)"""  # noqa: W505
    E_1016_PI_AXIS_ALREADY_EXISTS = -1016
    """Axis identifier is already in use by a connected stage"""
    E_1017_PI_INVALID_AXIS_IDENTIFIER = -1017
    """Invalid axis identifier"""
    E_1018_PI_COM_ARRAY_ERROR = -1018
    """Could not access array data in COM server"""
    E_1019_PI_COM_ARRAY_RANGE_ERROR = -1019
    """Range of array does not fit the number of parameters"""
    E_1020_PI_INVALID_SPA_CMD_ID = -1020
    """Invalid parameter ID given to SPA or SPA?"""
    E_1021_PI_NR_AVG_OUT_OF_RANGE = -1021
    """Number for AVG out of range--must be>0"""
    E_1022_PI_WAV_SAMPLES_OUT_OF_RANGE = -1022
    """Incorrect number of samples given to WAV"""
    E_1023_PI_WAV_FAILED = -1023
    """Generation of wave failed"""
    E_1024_PI_MOTION_ERROR = -1024
    """Motion error: position error too large, servo is switched off automatically"""  # noqa: W505
    E_1025_PI_RUNNING_MACRO = -1025
    """Controller is (already) running a macro"""
    E_1026_PI_PZT_CONFIG_FAILED = -1026
    """Configuration of PZT stage or amplifier failed"""
    E_1027_PI_PZT_CONFIG_INVALID_PARAMS = -1027
    """Current settings are not valid for desired configuration"""
    E_1028_PI_UNKNOWN_CHANNEL_IDENTIFIER = -1028
    """Unknown channel identifier"""
    E_1029_PI_WAVE_PARAM_FILE_ERROR = -1029
    """Error while reading/writing wave generator parameter file"""
    E_1030_PI_UNKNOWN_WAVE_SET = -1030
    """Could not find description of wave form. Maybe WG.ini is missing?"""
    E_1031_PI_WAVE_EDITOR_FUNC_NOT_LOADED = -1031
    """The WGWaveEditor DLL function was not found at startup"""
    E_1032_PI_USER_CANCELLED = -1032
    """The user cancelled a dialog"""
    E_1033_PI_C844_ERROR = -1033
    """Error from C-844 controller"""
    E_1034_PI_DLL_NOT_LOADED = -1034
    """DLL necessary to call function not loaded, or function not found in DLL"""  # noqa: W505
    E_1035_PI_PARAMETER_FILE_PROTECTED = -1035
    """The open parameter file is protected and cannot be edited"""
    E_1036_PI_NO_PARAMETER_FILE_OPENED = -1036
    """There is no parameter file open"""
    E_1037_PI_STAGE_DOES_NOT_EXIST = -1037
    """Selected stage does not exist"""
    E_1038_PI_PARAMETER_FILE_ALREADY_OPENED = -1038
    """There is already a parameter file open. Close it before opening a new file"""  # noqa: W505
    E_1039_PI_PARAMETER_FILE_OPEN_ERROR = -1039
    """Could not open parameter file"""
    E_1040_PI_INVALID_CONTROLLER_VERSION = -1040
    """The version of the connected controller is invalid"""
    E_1041_PI_PARAM_SET_ERROR = -1041
    """Parameter could not be set with SPA--parameter not defined for this controller!"""  # noqa: W505
    E_1042_PI_NUMBER_OF_POSSIBLE_WAVES_EXCEEDED = -1042
    """The maximum number of wave definitions has been exceeded"""
    E_1043_PI_NUMBER_OF_POSSIBLE_GENERATORS_EXCEEDED = -1043
    """The maximum number of wave generators has been exceeded"""
    E_1044_PI_NO_WAVE_FOR_AXIS_DEFINED = -1044
    """No wave defined for specified axis"""
    E_1045_PI_CANT_STOP_OR_START_WAV = -1045
    """Wave output to axis already stopped/started"""
    E_1046_PI_REFERENCE_ERROR = -1046
    """Not all axes could be referenced"""
    E_1047_PI_REQUIRED_WAVE_NOT_FOUND = -1047
    """Could not find parameter set required by frequency relation"""
    E_1048_PI_INVALID_SPP_CMD_ID = -1048
    """Command ID given to SPP or SPP? is not valid"""
    E_1049_PI_STAGE_NAME_ISNT_UNIQUE = -1049
    """A stage name given to CST is not unique"""
    E_1050_PI_FILE_TRANSFER_BEGIN_MISSING = -1050
    """A uuencoded file transferred did not start with "begin" followed by the proper filename"""  # noqa: W505, E501
    E_1051_PI_FILE_TRANSFER_ERROR_TEMP_FILE = -1051
    """Could not create/read file on host PC"""
    E_1052_PI_FILE_TRANSFER_CRC_ERROR = -1052
    """Checksum error when transferring a file to/from the controller"""
    E_1053_PI_COULDNT_FIND_PISTAGES_DAT = -1053
    """The PiStages.dat database could not be found. This file is required to connect a stage with the CST command"""  # noqa: E501
    E_1054_PI_NO_WAVE_RUNNING = -1054
    """No wave being output to specified axis"""
    E_1055_PI_INVALID_PASSWORD = -1055
    """Invalid password"""
    E_1056_PI_OPM_COM_ERROR = -1056
    """Error during communication with OPM(Optical Power Meter), maybe no OPM connected"""  # noqa: W505
    E_1057_PI_WAVE_EDITOR_WRONG_PARAMNUM = -1057
    """WaveEditor: Error during wave creation, incorrect number of parameters"""  # noqa: W505
    E_1058_PI_WAVE_EDITOR_FREQUENCY_OUT_OF_RANGE = -1058
    """WaveEditor: Frequency out of range"""
    E_1059_PI_WAVE_EDITOR_WRONG_IP_VALUE = -1059
    """WaveEditor: Error during wave creation, incorrect index for integer parameter"""  # noqa: W505
    E_1060_PI_WAVE_EDITOR_WRONG_DP_VALUE = -1060
    """WaveEditor: Error during wave creation, incorrect index for floating point parameter"""  # noqa: W505
    E_1061_PI_WAVE_EDITOR_WRONG_ITEM_VALUE = -1061
    """WaveEditor: Error during wave creation, could not calculate value"""
    E_1062_PI_WAVE_EDITOR_MISSING_GRAPH_COMPONENT = -1062
    """WaveEditor: Graph display component not installed"""
    E_1063_PI_EXT_PROFILE_UNALLOWED_CMD = -1063
    """User Profile Mode: Command is not allowed, check for required preparatory commands"""  # noqa: W505
    E_1064_PI_EXT_PROFILE_EXPECTING_MOTION_ERROR = -1064
    """User Profile Mode: First target position in User Profile is too far from current position"""  # noqa: W505, E501
    E_1065_PI_EXT_PROFILE_ACTIVE = -1065
    """Controller is (already) in User Profile Mode"""
    E_1066_PI_EXT_PROFILE_INDEX_OUT_OF_RANGE = -1066
    """User Profile Mode: Block or Data Set Index out of allowed range"""
    E_1067_PI_PROFILE_GENERATOR_NO_PROFILE = -1067
    """ProfileGenerator: No profile has been created yet"""
    E_1068_PI_PROFILE_GENERATOR_OUT_OF_LIMITS = -1068
    """ProfileGenerator: Generated profile exceeds limits of one or both axes"""  # noqa: W505
    E_1069_PI_PROFILE_GENERATOR_UNKNOWN_PARAMETER = -1069
    """ProfileGenerator: Unknown parameter ID in Set/Get Parameter command"""
    E_1070_PI_PROFILE_GENERATOR_PAR_OUT_OF_RANGE = -1070
    """ProfileGenerator: Parameter out of allowed range"""
    E_1071_PI_EXT_PROFILE_OUT_OF_MEMORY = -1071
    """User Profile Mode: Out of memory"""
    E_1072_PI_EXT_PROFILE_WRONG_CLUSTER = -1072
    """User Profile Mode: Cluster is not assigned to this axis"""
    E_1073_PI_EXT_PROFILE_UNKNOWN_CLUSTER_IDENTIFIER = -1073
    """Unknown cluster identifier"""
    E_1074_PI_INVALID_DEVICE_DRIVER_VERSION = -1074
    """The installed device driver doesn't match the required version. Please see the documentation to determine the required device driver version."""  # noqa: E501
    E_1075_PI_INVALID_LIBRARY_VERSION = -1075
    """The library used doesn't match the required version. Please see the documentation to determine the required library version."""  # noqa: E501
    E_1076_PI_INTERFACE_LOCKED = -1076
    """The interface is currently not locked by another function. Please try again later."""  # noqa: W505
    E_1077_PI_PARAM_DAT_FILE_INVALID_VERSION = -1077
    """Version of parameter DAT file does not match the required version. Current files are available at www.pi.ws."""  # noqa: E501
    E_1078_PI_CANNOT_WRITE_TO_PARAM_DAT_FILE = -1078
    """Cannot write to parameter DAT file to store user defined stage type"""
    E_1079_PI_CANNOT_CREATE_PARAM_DAT_FILE = -1079
    """Cannot create parameter DAT file to store user defined stage type"""
    E_1080_PI_PARAM_DAT_FILE_INVALID_REVISION = -1080
    """Parameter DAT file does not have correct revision"""
    E_1081_PI_USERSTAGES_DAT_FILE_INVALID_REVISION = -1081
    """User stages DAT file does not have correct revision"""
    E_1082_PI_SOFTWARE_TIMEOUT = -1082
    """Timeout Error. Some lengthy operation did not finish within expected time."""  # noqa: W505
    E_1083_PI_WRONG_DATA_TYPE = -1083
    """A function argument has an expected data type."""
    E_1084_PI_DIFFERENT_ARRAY_SIZES = -1084
    """Length of data arrays is different."""
    E_1085_PI_PARAM_NOT_FOUND_IN_PARAM_DAT_FILE = -1085
    """Parameter value not found in parameter DAT file"""
    E_1086_PI_MACRO_RECORDING_NOT_ALLOWED_IN_THIS_MODE = -1086
    """Macro recording is not allowed in this mode of operation"""
    E_1087_PI_USER_CANCELLED_COMMAND = -1087
    """Command cancelled by user input"""
    E_1088_PI_TOO_FEW_GCS_DATA = -1088
    """Controller sent too few GCS data sets"""
    E_1089_PI_TOO_MANY_GCS_DATA = -1089
    """Controller sent too many GCS data sets"""
    E_1090_PI_GCS_DATA_READ_ERROR = -1090
    """Communication error while reading GCS data"""
    E_1091_PI_WRONG_NUMBER_OF_INPUT_ARGUMENTS = -1091
    """Wrong number of input arguments"""
    E_1092_PI_FAILED_TO_CHANGE_CCL_LEVEL = -1092
    """Change of command level has failed"""
    E_1093_PI_FAILED_TO_SWITCH_OFF_SERVO = -1093
    """Switching off the servo mode has failed"""
    E_1094_PI_FAILED_TO_SET_SINGLE_PARAMETER_WHILE_PERFORMING_CST = -1094
    """A parameter could not be set while performing CST: CST was not performed (parameters remain unchanged)"""  # noqa: E501
    E_1095_PI_ERROR_CONTROLLER_REBOOT = -1095
    """Connection could not be reestablished after reboot"""
    E_1096_PI_ERROR_AT_QHPA = -1096
    """Sending HPA? or receiving the response has failed."""
    E_1097_PI_QHPA_NONCOMPLIANT_WITH_GCS = -1097
    """HPA? response does not comply with GCS2 syntax."""
    E_1098_PI_FAILED_TO_READ_QSPA = -1098
    """Response to SPA? could not be received."""
    E_1099_PI_PAM_FILE_WRONG_VERSION = -1099
    """Version of PAM file cannot be handled (too old or too new)"""
    E_1100_PI_PAM_FILE_INVALID_FORMAT = -1100
    """PAM file does not contain required data in PAM file format"""
    E_1101_PI_INCOMPLETE_INFORMATION = -1101
    """Information does not contain all required data"""
    E_1102_PI_NO_VALUE_AVAILABLE = -1102
    """No value for parameter available"""
    E_1103_PI_NO_PAM_FILE_OPEN = -1103
    """No PAM file is open"""
    E_1104_PI_INVALID_VALUE = -1104
    """Invalid value"""
    E_1105_PI_UNKNOWN_PARAMETER = -1105
    """Unknown parameter"""
    E_1106_PI_RESPONSE_TO_QSEP_FAILED = -1106
    """Response to SEP? could not be received."""
    E_1107_PI_RESPONSE_TO_QSPA_FAILED = -1107
    """Response to SPA? could not be received."""
    E_1108_PI_ERROR_IN_CST_VALIDATION = -1108
    """Error while performing CST: One or more parameters were not set correctly."""  # noqa: W505
    E_1109_PI_ERROR_PAM_FILE_HAS_DUPLICATE_ENTRY_WITH_DIFFERENT_VALUES = -1109
    """PAM file has duplicate entry with different values."""
    E_1110_PI_ERROR_FILE_NO_SIGNATURE = -1110
    """File has not signature"""
    E_1111_PI_ERROR_FILE_INVALID_SIGNATURE = -1111
    """File has invalid signature"""
    E_10000_PI_PARAMETER_DB_INVALID_STAGE_TYPE_FORMAT = -10000
    """PI stage database: String containing stage type and description has invalid format."""  # noqa: W505
    E_10001_PI_PARAMETER_DB_SYSTEM_NOT_AVAILABLE = -10001
    """PI stage database: Database does not contain the selected stage type for the connected controller."""  # noqa: W505, E501
    E_10002_PI_PARAMETER_DB_FAILED_TO_ESTABLISH_CONNECTION = -10002
    """PI stage database: Establishing the connection has failed."""
    E_10003_PI_PARAMETER_DB_COMMUNICATION_ERROR = -10003
    """PI stage database: Communication was interrupted (e.g. because database was deleted)."""  # noqa: W505
    E_10004_PI_PARAMETER_DB_ERROR_WHILE_QUERYING_PARAMETERS = -10004
    """PI stage database: Querying data failed."""
    E_10005_PI_PARAMETER_DB_SYSTEM_ALREADY_EXISTS = -10005
    """PI stage database: System already exists. Rename stage and try again."""
    E_10006_PI_PARAMETER_DB_QHPA_CONTANS_UNKNOWN_PAM_IDS = -10006
    """PI stage database: Response to HPA? contains unknown parameter IDs."""
    E_10007_PI_PARAMETER_DB_AND_QHPA_ARE_INCONSISTENT = -10007
    """PI stage database: Inconsistency between database and response to HPA?"""  # noqa: W505
    E_10008_PI_PARAMETER_DB_SYSTEM_COULD_NOT_BE_ADDED = -10008
    """PI stage database: Stage has not been added."""
    E_10009_PI_PARAMETER_DB_SYSTEM_COULD_NOT_BE_REMOVED = -10009
    """PI stage database: Stage has not been removed."""
    E_10010_PI_PARAMETER_DB_CONTROLLER_DB_PARAMETERS_MISMATCH = -10010
    """Controller does not support all stage parameters stored in PI stage database. NO parameters were set."""  # noqa: E501
    E_10011_PI_PARAMETER_DB_DATABASE_IS_OUTDATED = -10011
    """The version of PISTAGEs3.DB stage database is out of date. Please update via PIUpdateFinder. No parameters were set."""  # noqa: E501
    E_10012_PI_PARAMETER_DB_AND_HPA_MISMATCH_STRICT = -10012
    """Mismatch between number of parameters present in stage database and available in controller interface. NO parameters were set."""  # noqa: E501
    E_10013_PI_PARAMETER_DB_AND_HPA_MISMATCH_LOOSE = -10013
    """Mismatch between number of parameters present in stage database and available in controller interface. Some parameters were ignored."""  # noqa: E501
    E_10014_PI_PARAMETER_DB_FAILED_TO_SET_PARAMETERS_CORRECTLY = -10014
    """One or more parameters could not be set correctly on the controller."""
    E_10015_PI_PARAMETER_DB_MISSING_PARAMETER_DEFINITIONS_IN_DATABASE = -10015
    """One or more parameter definitions are not present in stage database. Please update PISTAGES3.DB via PIUpdateFinder. Missing parameters were ignored."""  # noqa: E501
    E0_PI_CNTR_NO_ERROR = 0
    """No error"""
    E1_PI_CNTR_PARAM_SYNTAX = 1
    """Parameter syntax error"""
    E2_PI_CNTR_UNKNOWN_COMMAND = 2
    """Unknown command"""
    E3_PI_CNTR_COMMAND_TOO_LONG = 3
    """Command length out of limits or command buffer overrun"""
    E4_PI_CNTR_SCAN_ERROR = 4
    """Error while scanning"""
    E5_PI_CNTR_MOVE_WITHOUT_REF_OR_NO_SERVO = 5
    """Unallowable move attempted on unreferenced axis, or move attempted with servo off"""  # noqa: W505
    E6_PI_CNTR_INVALID_SGA_PARAM = 6
    """Parameter for SGA not valid"""
    E7_PI_CNTR_POS_OUT_OF_LIMITS = 7
    """Position out of limits"""
    E8_PI_CNTR_VEL_OUT_OF_LIMITS = 8
    """Velocity out of limits"""
    E9_PI_CNTR_SET_PIVOT_NOT_POSSIBLE = 9
    """Attempt to set pivot point while U,V and W not all 0"""
    E10_PI_CNTR_STOP = 10
    """Controller was stopped by command"""
    E11_PI_CNTR_SST_OR_SCAN_RANGE = 11
    """Parameter for SST or for one of the embedded scan algorithms out of range"""  # noqa: W505
    E12_PI_CNTR_INVALID_SCAN_AXES = 12
    """Invalid axis combination for fast scan"""
    E13_PI_CNTR_INVALID_NAV_PARAM = 13
    """Parameter for NAV out of range"""
    E14_PI_CNTR_INVALID_ANALOG_INPUT = 14
    """Invalid analog channel"""
    E15_PI_CNTR_INVALID_AXIS_IDENTIFIER = 15
    """Invalid axis identifier"""
    E16_PI_CNTR_INVALID_STAGE_NAME = 16
    """Unknown stage name"""
    E17_PI_CNTR_PARAM_OUT_OF_RANGE = 17
    """Parameter out of range"""
    E18_PI_CNTR_INVALID_MACRO_NAME = 18
    """Invalid macro name"""
    E19_PI_CNTR_MACRO_RECORD = 19
    """Error while recording macro"""
    E20_PI_CNTR_MACRO_NOT_FOUND = 20
    """Macro not found"""
    E21_PI_CNTR_AXIS_HAS_NO_BRAKE = 21
    """Axis has no brake"""
    E22_PI_CNTR_DOUBLE_AXIS = 22
    """Axis identifier specified more than once"""
    E23_PI_CNTR_ILLEGAL_AXIS = 23
    """Illegal axis"""
    E24_PI_CNTR_PARAM_NR = 24
    """Incorrect number of parameters"""
    E25_PI_CNTR_INVALID_REAL_NR = 25
    """Invalid floating point number"""
    E26_PI_CNTR_MISSING_PARAM = 26
    """Parameter missing"""
    E27_PI_CNTR_SOFT_LIMIT_OUT_OF_RANGE = 27
    """Soft limit out of range"""
    E28_PI_CNTR_NO_MANUAL_PAD = 28
    """No manual pad found"""
    E29_PI_CNTR_NO_JUMP = 29
    """No more step-response values"""
    E30_PI_CNTR_INVALID_JUMP = 30
    """No step-response values recorded"""
    E31_PI_CNTR_AXIS_HAS_NO_REFERENCE = 31
    """Axis has no reference sensor"""
    E32_PI_CNTR_STAGE_HAS_NO_LIM_SWITCH = 32
    """Axis has no limit switch"""
    E33_PI_CNTR_NO_RELAY_CARD = 33
    """No relay card installed"""
    E34_PI_CNTR_CMD_NOT_ALLOWED_FOR_STAGE = 34
    E35_PI_CNTR_NO_DIGITAL_INPUT = 35
    E36_PI_CNTR_NO_DIGITAL_OUTPUT = 36
    E37_PI_CNTR_NO_MCM = 37
    E38_PI_CNTR_INVALID_MCM = 38
    E39_PI_CNTR_INVALID_CNTR_NUMBER = 39
    E40_PI_CNTR_NO_JOYSTICK_CONNECTED = 40
    E41_PI_CNTR_INVALID_EGE_AXIS = 41
    E42_PI_CNTR_SLAVE_POSITION_OUT_OF_RANGE = 42
    E43_PI_CNTR_COMMAND_EGE_SLAVE = 43
    E44_PI_CNTR_JOYSTICK_CALIBRATION_FAILED = 44
    E45_PI_CNTR_REFERENCING_FAILED = 45
    E46_PI_CNTR_OPM_MISSING = 46
    E47_PI_CNTR_OPM_NOT_INITIALIZED = 47
    E48_PI_CNTR_OPM_COM_ERROR = 48
    E49_PI_CNTR_MOVE_TO_LIMIT_SWITCH_FAILED = 49
    E50_PI_CNTR_REF_WITH_REF_DISABLED = 50
    E51_PI_CNTR_AXIS_UNDER_JOYSTICK_CONTROL = 51
    E52_PI_CNTR_COMMUNICATION_ERROR = 52
    E53_PI_CNTR_DYNAMIC_MOVE_IN_PROCESS = 53
    E54_PI_CNTR_UNKNOWN_PARAMETER = 54
    E55_PI_CNTR_NO_REP_RECORDED = 55
    E56_PI_CNTR_INVALID_PASSWORD = 56
    E57_PI_CNTR_INVALID_RECORDER_CHAN = 57
    E58_PI_CNTR_INVALID_RECORDER_SRC_OPT = 58
    E59_PI_CNTR_INVALID_RECORDER_SRC_CHAN = 59
    E60_PI_CNTR_PARAM_PROTECTION = 60
    E61_PI_CNTR_AUTOZERO_RUNNING = 61
    E62_PI_CNTR_NO_LINEAR_AXIS = 62
    E63_PI_CNTR_INIT_RUNNING = 63
    E64_PI_CNTR_READ_ONLY_PARAMETER = 64
    E65_PI_CNTR_PAM_NOT_FOUND = 65
    E66_PI_CNTR_VOL_OUT_OF_LIMITS = 66
    E67_PI_CNTR_WAVE_TOO_LARGE = 67
    E68_PI_CNTR_NOT_ENOUGH_DDL_MEMORY = 68
    E69_PI_CNTR_DDL_TIME_DELAY_TOO_LARGE = 69
    E70_PI_CNTR_DIFFERENT_ARRAY_LENGTH = 70
    E71_PI_CNTR_GEN_SINGLE_MODE_RESTART = 71
    E72_PI_CNTR_ANALOG_TARGET_ACTIVE = 72
    E73_PI_CNTR_WAVE_GENERATOR_ACTIVE = 73
    E74_PI_CNTR_AUTOZERO_DISABLED = 74
    E75_PI_CNTR_NO_WAVE_SELECTED = 75
    E76_PI_CNTR_IF_BUFFER_OVERRUN = 76
    E77_PI_CNTR_NOT_ENOUGH_RECORDED_DATA = 77
    E78_PI_CNTR_TABLE_DEACTIVATED = 78
    E79_PI_CNTR_OPENLOOP_VALUE_SET_WHEN_SERVO_ON = 79
    E80_PI_CNTR_RAM_ERROR = 80
    E81_PI_CNTR_MACRO_UNKNOWN_COMMAND = 81
    E82_PI_CNTR_MACRO_PC_ERROR = 82
    E83_PI_CNTR_JOYSTICK_ACTIVE = 83
    E84_PI_CNTR_MOTOR_IS_OFF = 84
    E85_PI_CNTR_ONLY_IN_MACRO = 85
    E86_PI_CNTR_JOYSTICK_UNKNOWN_AXIS = 86
    E87_PI_CNTR_JOYSTICK_UNKNOWN_ID = 87
    E88_PI_CNTR_REF_MODE_IS_ON = 88
    E89_PI_CNTR_NOT_ALLOWED_IN_CURRENT_MOTION_MODE = 89
    E90_PI_CNTR_DIO_AND_TRACING_NOT_POSSIBLE = 90
    E91_PI_CNTR_COLLISION = 91
    E92_PI_CNTR_SLAVE_NOT_FAST_ENOUGH = 92
    E93_PI_CNTR_CMD_NOT_ALLOWED_WHILE_AXIS_IN_MOTION = 93
    E94_PI_CNTR_OPEN_LOOP_JOYSTICK_ENABLED = 94
    E95_PI_CNTR_INVALID_SERVO_STATE_FOR_PARAMETER = 95
    E96_PI_CNTR_UNKNOWN_STAGE_NAME = 96
    E97_PI_CNTR_INVALID_VALUE_LENGTH = 97
    E98_PI_CNTR_AUTOZERO_FAILED = 98
    E99_PI_CNTR_SENSOR_VOLTAGE_OFF = 99
    E100_PI_LABVIEW_ERROR = 100
    E200_PI_CNTR_NO_AXIS = 200
    E201_PI_CNTR_NO_AXIS_PARAM_FILE = 201
    E202_PI_CNTR_INVALID_AXIS_PARAM_FILE = 202
    E203_PI_CNTR_NO_AXIS_PARAM_BACKUP = 203
    E204_PI_CNTR_RESERVED_204 = 204
    E205_PI_CNTR_SMO_WITH_SERVO_ON = 205
    E206_PI_CNTR_UUDECODE_INCOMPLETE_HEADER = 206
    E207_PI_CNTR_UUDECODE_NOTHING_TO_DECODE = 207
    E208_PI_CNTR_UUDECODE_ILLEGAL_FORMAT = 208
    E209_PI_CNTR_CRC32_ERROR = 209
    E210_PI_CNTR_ILLEGAL_FILENAME = 210
    E211_PI_CNTR_FILE_NOT_FOUND = 211
    E212_PI_CNTR_FILE_WRITE_ERROR = 212
    E213_PI_CNTR_DTR_HINDERS_VELOCITY_CHANGE = 213
    E214_PI_CNTR_POSITION_UNKNOWN = 214
    E215_PI_CNTR_CONN_POSSIBLY_BROKEN = 215
    E216_PI_CNTR_ON_LIMIT_SWITCH = 216
    E217_PI_CNTR_UNEXPECTED_STRUT_STOP = 217
    E218_PI_CNTR_POSITION_BASED_ON_ESTIMATION = 218
    E219_PI_CNTR_POSITION_BASED_ON_INTERPOLATION = 219
    E220_PI_CNTR_INTERPOLATION_FIFO_UNDERRUN = 220
    E221_PI_CNTR_INTERPOLATION_FIFO_OVERFLOW = 221
    E230_PI_CNTR_INVALID_HANDLE = 230
    E231_PI_CNTR_NO_BIOS_FOUND = 231
    E232_PI_CNTR_SAVE_SYS_CFG_FAILED = 232
    E233_PI_CNTR_LOAD_SYS_CFG_FAILED = 233
    E301_PI_CNTR_SEND_BUFFER_OVERFLOW = 301
    E302_PI_CNTR_VOLTAGE_OUT_OF_LIMITS = 302
    E303_PI_CNTR_OPEN_LOOP_MOTION_SET_WHEN_SERVO_ON = 303
    E304_PI_CNTR_RECEIVING_BUFFER_OVERFLOW = 304
    E305_PI_CNTR_EEPROM_ERROR = 305
    E306_PI_CNTR_I2C_ERROR = 306
    E307_PI_CNTR_RECEIVING_TIMEOUT = 307
    E308_PI_CNTR_TIMEOUT = 308
    E309_PI_CNTR_MACRO_OUT_OF_SPACE = 309
    E310_PI_CNTR_EUI_OLDVERSION_CFGDATA = 310
    E311_PI_CNTR_EUI_INVALID_CFGDATA = 311
    E333_PI_CNTR_HARDWARE_ERROR = 333
    E400_PI_CNTR_WAV_INDEX_ERROR = 400
    E401_PI_CNTR_WAV_NOT_DEFINED = 401
    E402_PI_CNTR_WAV_TYPE_NOT_SUPPORTED = 402
    E403_PI_CNTR_WAV_LENGTH_EXCEEDS_LIMIT = 403
    E404_PI_CNTR_WAV_PARAMETER_NR = 404
    E405_PI_CNTR_WAV_PARAMETER_OUT_OF_LIMIT = 405
    E406_PI_CNTR_WGO_BIT_NOT_SUPPORTED = 406
    E500_PI_CNTR_EMERGENCY_STOP_BUTTON_ACTIVATED = 500
    E501_PI_CNTR_EMERGENCY_STOP_BUTTON_WAS_ACTIVATED = 501
    E502_PI_CNTR_REDUNDANCY_LIMIT_EXCEEDED = 502
    E503_PI_CNTR_COLLISION_SWITCH_ACTIVATED = 503
    E504_PI_CNTR_FOLLOWING_ERROR = 504
    E505_PI_CNTR_SENSOR_SIGNAL_INVALID = 505
    E506_PI_CNTR_SERVO_LOOP_UNSTABLE = 506
    E507_PI_CNTR_LOST_SPI_SLAVE_CONNECTION = 507
    E530_PI_CNTR_CS_DOES_NOT_EXIST = 530
    E531_PI_CNTR_PARENT_CS_DOES_NOT_EXIST = 531
    E532_PI_CNTR_CS_IN_USE = 532
    E533_PI_CNTR_CS_DEFINITION_IS_CYCLIC = 533
    E536_PI_CNTR_HEXAPOD_IN_MOTION = 536
    E537_PI_CNTR_CS_TYPE_CANNOT_BE_ENABLED = 537
    E539_PI_CNTR_CS_PARENT_IDENTICAL_TO_CHILD = 539
    E540_PI_CNTR_CS_DEFINITION_INCONSISTENT = 540
    E542_PI_CNTR_CS_NOT_IN_SAME_CHAIN = 542
    E543_PI_CNTR_CS_MEMORY_FULL = 543
    E544_PI_CNTR_SPI_COMMAND_NOT_SUPPORTED = 544
    E545_PI_CNTR_SOFTLIMITS_INVALID = 545
    E546_PI_CNTR_CS_WRITE_PROTECTED = 546
    E547_PI_CNTR_CS_CONTENT_FROM_CONFIG_FILE = 547
    E548_PI_CNTR_CS_CANNOT_BE_LINKED = 548
    E549_PI_CNTR_KSB_CS_ROTATION_ONLY = 549
    E551_PI_CNTR_CS_DATA_CANNOT_BE_QUERIED = 551
    E552_PI_CNTR_CS_COMBINATION_DOES_NOT_EXIST = 552
    E553_PI_CNTR_CS_COMBINATION_INVALID = 553
    E554_PI_CNTR_CS_TYPE_DOES_NOT_EXIST = 554
    E555_PI_CNTR_UNKNOWN_ERROR = 555
    E556_PI_CNTR_CS_TYPE_NOT_ENABLED = 556
    E557_PI_CNTR_CS_NAME_INVALID = 557
    E558_PI_CNTR_CS_GENERAL_FILE_MISSING = 558
    E559_PI_CNTR_CS_LEVELING_FILE_MISSING = 559
    E601_PI_CNTR_NOT_ENOUGH_MEMORY = 601
    E602_PI_CNTR_HW_VOLTAGE_ERROR = 602
    E603_PI_CNTR_HW_TEMPERATURE_ERROR = 603
    E604_PI_CNTR_POSITION_ERROR_TOO_HIGH = 604
    E606_PI_CNTR_INPUT_OUT_OF_RANGE = 606
    E607_PI_CNTR_NO_INTEGER = 607
    E608_PI_CNTR_FAST_ALIGNMENT_PROCESS_IS_NOT_RUNNING = 608
    E609_PI_CNTR_FAST_ALIGNMENT_PROCESS_IS_NOT_PAUSED = 609
    E650_PI_CNTR_UNABLE_TO_SET_PARAM_WITH_SPA = 650
    E651_PI_CNTR_PHASE_FINDING_ERROR = 651
    E652_PI_CNTR_SENSOR_SETUP_ERROR = 652
    E653_PI_CNTR_SENSOR_COMM_ERROR = 653
    E654_PI_CNTR_MOTOR_AMPLIFIER_ERROR = 654
    E655_PI_CNTR_OVER_CURR_PROTEC_TRIGGERED_BY_I2T = 655
    E656_PI_CNTR_OVER_CURR_PROTEC_TRIGGERED_BY_AMP_MODULE = 656
    E657_PI_CNTR_SAFETY_STOP_TRIGGERED = 657
    E658_PI_SENSOR_OFF = 658
    E700_PI_CNTR_COMMAND_NOT_ALLOWED_IN_EXTERNAL_MODE = 700
    E710_PI_CNTR_EXTERNAL_MODE_ERROR = 710
    E715_PI_CNTR_INVALID_MODE_OF_OPERATION = 715
    E716_PI_CNTR_FIRMWARE_STOPPED_BY_CMD = 716
    E717_PI_CNTR_EXTERNAL_MODE_DRIVER_MISSING = 717
    E718_PI_CNTR_CONFIGURATION_FAILURE_EXTERNAL_MODE = 718
    E719_PI_CNTR_EXTERNAL_MODE_CYCLETIME_INVALID = 719
    E720_PI_CNTR_BRAKE_ACTIVATED = 720
    E731_PI_CNTR_SURFACEDETECTION_RUNNING = 731
    E732_PI_CNTR_SURFACEDETECTION_FAILED = 732
    E733_PI_CNTR_FIELDBUS_IS_ACTIVE = 733
    E1000_PI_CNTR_TOO_MANY_NESTED_MACROS = 1000
    E1001_PI_CNTR_MACRO_ALREADY_DEFINED = 1001
    E1002_PI_CNTR_NO_MACRO_RECORDING = 1002
    E1003_PI_CNTR_INVALID_MAC_PARAM = 1003
    E1004_PI_CNTR_MACRO_DELETE_ERROR = 1004
    E1005_PI_CNTR_CONTROLLER_BUSY = 1005
    E1006_PI_CNTR_INVALID_IDENTIFIER = 1006
    E1007_PI_CNTR_UNKNOWN_VARIABLE_OR_ARGUMENT = 1007
    E1008_PI_CNTR_RUNNING_MACRO = 1008
    E1009_PI_CNTR_MACRO_INVALID_OPERATOR = 1009
    E1010_PI_CNTR_MACRO_NO_ANSWER = 1010
    E1011_PI_CMD_NOT_VALID_IN_MACRO_MODE = 1011
    E1024_PI_CNTR_MOTION_ERROR = 1024
    E1025_PI_CNTR_MAX_MOTOR_OUTPUT_REACHED = 1025
    E1063_PI_CNTR_EXT_PROFILE_UNALLOWED_CMD = 1063
    E1064_PI_CNTR_EXT_PROFILE_EXPECTING_MOTION_ERROR = 1064
    E1065_PI_CNTR_PROFILE_ACTIVE = 1065
    E1066_PI_CNTR_PROFILE_INDEX_OUT_OF_RANGE = 1066
    E1071_PI_CNTR_PROFILE_OUT_OF_MEMORY = 1071
    E1072_PI_CNTR_PROFILE_WRONG_CLUSTER = 1072
    E1073_PI_CNTR_PROFILE_UNKNOWN_CLUSTER_IDENTIFIER = 1073
    E1090_PI_CNTR_TOO_MANY_TCP_CONNECTIONS_OPEN = 1090
    E2000_PI_CNTR_ALREADY_HAS_SERIAL_NUMBER = 2000
    E4000_PI_CNTR_SECTOR_ERASE_FAILED = 4000
    E4001_PI_CNTR_FLASH_PROGRAM_FAILED = 4001
    E4002_PI_CNTR_FLASH_READ_FAILED = 4002
    E4003_PI_CNTR_HW_MATCHCODE_ERROR = 4003
    E4004_PI_CNTR_FW_MATCHCODE_ERROR = 4004
    E4005_PI_CNTR_HW_VERSION_ERROR = 4005
    E4006_PI_CNTR_FW_VERSION_ERROR = 4006
    E4007_PI_CNTR_FW_UPDATE_ERROR = 4007
    E4008_PI_CNTR_FW_CRC_PAR_ERROR = 4008
    E4009_PI_CNTR_FW_CRC_FW_ERROR = 4009
    E5000_PI_CNTR_INVALID_PCC_SCAN_DATA = 5000
    E5001_PI_CNTR_PCC_SCAN_RUNNING = 5001
    E5002_PI_CNTR_INVALID_PCC_AXIS = 5002
    E5003_PI_CNTR_PCC_SCAN_OUT_OF_RANGE = 5003
    E5004_PI_CNTR_PCC_TYPE_NOT_EXISTING = 5004
    E5005_PI_CNTR_PCC_PAM_ERROR = 5005
    E5006_PI_CNTR_PCC_TABLE_ARRAY_TOO_LARGE = 5006
    E5100_PI_CNTR_NEXLINE_ERROR = 5100
    E5101_PI_CNTR_CHANNEL_ALREADY_USED = 5101
    E5102_PI_CNTR_NEXLINE_TABLE_TOO_SMALL = 5102
    E5103_PI_CNTR_RNP_WITH_SERVO_ON = 5103
    E5104_PI_CNTR_RNP_NEEDED = 5104
    E5200_PI_CNTR_AXIS_NOT_CONFIGURED = 5200
    E5300_PI_CNTR_FREQU_ANALYSIS_FAILED = 5300
    E5301_PI_CNTR_FREQU_ANALYSIS_RUNNING = 5301
    E6000_PI_CNTR_SENSOR_ABS_INVALID_VALUE = 6000
    E6001_PI_CNTR_SENSOR_ABS_WRITE_ERROR = 6001
    E6002_PI_CNTR_SENSOR_ABS_READ_ERROR = 6002
    E6003_PI_CNTR_SENSOR_ABS_CRC_ERROR = 6003
    E6004_PI_CNTR_SENSOR_ABS_ERROR = 6004
    E6005_PI_CNTR_SENSOR_ABS_OVERFLOW = 6005

    COM_ERROR__1 = -1
    SEND_ERROR__2 = -2
    REC_ERROR__3 = -3
    NOT_CONNECTED_ERROR__4 = -4
    COM_BUFFER_OVERFLOW__5 = -5
    CONNECTION_FAILED__6 = -6
    COM_TIMEOUT__7 = -7
    COM_MULTILINE_RESPONSE__8 = -8
    COM_INVALID_ID__9 = -9
    COM_NOTIFY_EVENT_ERROR__10 = -10
    COM_NOT_IMPLEMENTED__11 = -11
    COM_ECHO_ERROR__12 = -12
    COM_GPIB_EDVR__13 = -13
    COM_GPIB_ECIC__14 = -14
    COM_GPIB_ENOL__15 = -15
    COM_GPIB_EADR__16 = -16
    COM_GPIB_EARG__17 = -17
    COM_GPIB_ESAC__18 = -18
    COM_GPIB_EABO__19 = -19
    COM_GPIB_ENEB__20 = -20
    COM_GPIB_EDMA__21 = -21
    COM_GPIB_EOIP__22 = -22
    COM_GPIB_ECAP__23 = -23
    COM_GPIB_EFSO__24 = -24
    COM_GPIB_EBUS__25 = -25
    COM_GPIB_ESTB__26 = -26
    COM_GPIB_ESRQ__27 = -27
    COM_GPIB_ETAB__28 = -28
    COM_GPIB_ELCK__29 = -29
    COM_RS_INVALID_DATA_BITS__30 = -30
    COM_ERROR_RS_SETTINGS__31 = -31
    COM_INTERNAL_RESOURCES_ERROR__32 = -32
    COM_DLL_FUNC_ERROR__33 = -33
    COM_FTDIUSB_INVALID_HANDLE__34 = -34
    COM_FTDIUSB_DEVICE_NOT_FOUND__35 = -35
    COM_FTDIUSB_DEVICE_NOT_OPENED__36 = -36
    COM_FTDIUSB_IO_ERROR__37 = -37
    COM_FTDIUSB_INSUFFICIENT_RESOURCES__38 = -38
    COM_FTDIUSB_INVALID_PARAMETER__39 = -39
    COM_FTDIUSB_INVALID_BAUD_RATE__40 = -40
    COM_FTDIUSB_DEVICE_NOT_OPENED_FOR_ERASE__41 = -41
    COM_FTDIUSB_DEVICE_NOT_OPENED_FOR_WRITE__42 = -42
    COM_FTDIUSB_FAILED_TO_WRITE_DEVICE__43 = -43
    COM_FTDIUSB_EEPROM_READ_FAILED__44 = -44
    COM_FTDIUSB_EEPROM_WRITE_FAILED__45 = -45
    COM_FTDIUSB_EEPROM_ERASE_FAILED__46 = -46
    COM_FTDIUSB_EEPROM_NOT_PRESENT__47 = -47
    COM_FTDIUSB_EEPROM_NOT_PROGRAMMED__48 = -48
    COM_FTDIUSB_INVALID_ARGS__49 = -49
    COM_FTDIUSB_NOT_SUPPORTED__50 = -50
    COM_FTDIUSB_OTHER_ERROR__51 = -51
    COM_PORT_ALREADY_OPEN__52 = -52
    COM_PORT_CHECKSUM_ERROR__53 = -53
    COM_SOCKET_NOT_READY__54 = -54
    COM_SOCKET_PORT_IN_USE__55 = -55
    COM_SOCKET_NOT_CONNECTED__56 = -56
    COM_SOCKET_TERMINATED__57 = -57
    COM_SOCKET_NO_RESPONSE__58 = -58
    COM_SOCKET_INTERRUPTED__59 = -59
    COM_PCI_INVALID_ID__60 = -60
    COM_PCI_ACCESS_DENIED__61 = -61
    COM_SOCKET_HOST_NOT_FOUND__62 = -62
    COM_DEVICE_CONNECTED__63 = -63
    PI_UNKNOWN_AXIS_IDENTIFIER__1001 = -1001
    PI_NR_NAV_OUT_OF_RANGE__1002 = -1002
    PI_INVALID_SGA__1003 = -1003
    PI_UNEXPECTED_RESPONSE__1004 = -1004
    PI_NO_MANUAL_PAD__1005 = -1005
    PI_INVALID_MANUAL_PAD_KNOB__1006 = -1006
    PI_INVALID_MANUAL_PAD_AXIS__1007 = -1007
    PI_CONTROLLER_BUSY__1008 = -1008
    PI_THREAD_ERROR__1009 = -1009
    PI_IN_MACRO_MODE__1010 = -1010
    PI_NOT_IN_MACRO_MODE__1011 = -1011
    PI_MACRO_FILE_ERROR__1012 = -1012
    PI_NO_MACRO_OR_EMPTY__1013 = -1013
    PI_MACRO_EDITOR_ERROR__1014 = -1014
    PI_INVALID_ARGUMENT__1015 = -1015
    PI_AXIS_ALREADY_EXISTS__1016 = -1016
    PI_INVALID_AXIS_IDENTIFIER__1017 = -1017
    PI_COM_ARRAY_ERROR__1018 = -1018
    PI_COM_ARRAY_RANGE_ERROR__1019 = -1019
    PI_INVALID_SPA_CMD_ID__1020 = -1020
    PI_NR_AVG_OUT_OF_RANGE__1021 = -1021
    PI_WAV_SAMPLES_OUT_OF_RANGE__1022 = -1022
    PI_WAV_FAILED__1023 = -1023
    PI_MOTION_ERROR__1024 = -1024
    PI_RUNNING_MACRO__1025 = -1025
    PI_PZT_CONFIG_FAILED__1026 = -1026
    PI_PZT_CONFIG_INVALID_PARAMS__1027 = -1027
    PI_UNKNOWN_CHANNEL_IDENTIFIER__1028 = -1028
    PI_WAVE_PARAM_FILE_ERROR__1029 = -1029
    PI_UNKNOWN_WAVE_SET__1030 = -1030
    PI_WAVE_EDITOR_FUNC_NOT_LOADED__1031 = -1031
    PI_USER_CANCELLED__1032 = -1032
    PI_C844_ERROR__1033 = -1033
    PI_DLL_NOT_LOADED__1034 = -1034
    PI_PARAMETER_FILE_PROTECTED__1035 = -1035
    PI_NO_PARAMETER_FILE_OPENED__1036 = -1036
    PI_STAGE_DOES_NOT_EXIST__1037 = -1037
    PI_PARAMETER_FILE_ALREADY_OPENED__1038 = -1038
    PI_PARAMETER_FILE_OPEN_ERROR__1039 = -1039
    PI_INVALID_CONTROLLER_VERSION__1040 = -1040
    PI_PARAM_SET_ERROR__1041 = -1041
    PI_NUMBER_OF_POSSIBLE_WAVES_EXCEEDED__1042 = -1042
    PI_NUMBER_OF_POSSIBLE_GENERATORS_EXCEEDED__1043 = -1043
    PI_NO_WAVE_FOR_AXIS_DEFINED__1044 = -1044
    PI_CANT_STOP_OR_START_WAV__1045 = -1045
    PI_REFERENCE_ERROR__1046 = -1046
    PI_REQUIRED_WAVE_NOT_FOUND__1047 = -1047
    PI_INVALID_SPP_CMD_ID__1048 = -1048
    PI_STAGE_NAME_ISNT_UNIQUE__1049 = -1049
    PI_FILE_TRANSFER_BEGIN_MISSING__1050 = -1050
    PI_FILE_TRANSFER_ERROR_TEMP_FILE__1051 = -1051
    PI_FILE_TRANSFER_CRC_ERROR__1052 = -1052
    PI_COULDNT_FIND_PISTAGES_DAT__1053 = -1053
    PI_NO_WAVE_RUNNING__1054 = -1054
    PI_INVALID_PASSWORD__1055 = -1055
    PI_OPM_COM_ERROR__1056 = -1056
    PI_WAVE_EDITOR_WRONG_PARAMNUM__1057 = -1057
    PI_WAVE_EDITOR_FREQUENCY_OUT_OF_RANGE__1058 = -1058
    PI_WAVE_EDITOR_WRONG_IP_VALUE__1059 = -1059
    PI_WAVE_EDITOR_WRONG_DP_VALUE__1060 = -1060
    PI_WAVE_EDITOR_WRONG_ITEM_VALUE__1061 = -1061
    PI_WAVE_EDITOR_MISSING_GRAPH_COMPONENT__1062 = -1062
    PI_EXT_PROFILE_UNALLOWED_CMD__1063 = -1063
    PI_EXT_PROFILE_EXPECTING_MOTION_ERROR__1064 = -1064
    PI_EXT_PROFILE_ACTIVE__1065 = -1065
    PI_EXT_PROFILE_INDEX_OUT_OF_RANGE__1066 = -1066
    PI_PROFILE_GENERATOR_NO_PROFILE__1067 = -1067
    PI_PROFILE_GENERATOR_OUT_OF_LIMITS__1068 = -1068
    PI_PROFILE_GENERATOR_UNKNOWN_PARAMETER__1069 = -1069
    PI_PROFILE_GENERATOR_PAR_OUT_OF_RANGE__1070 = -1070
    PI_EXT_PROFILE_OUT_OF_MEMORY__1071 = -1071
    PI_EXT_PROFILE_WRONG_CLUSTER__1072 = -1072
    PI_EXT_PROFILE_UNKNOWN_CLUSTER_IDENTIFIER__1073 = -1073
    PI_INVALID_DEVICE_DRIVER_VERSION__1074 = -1074
    PI_INVALID_LIBRARY_VERSION__1075 = -1075
    PI_INTERFACE_LOCKED__1076 = -1076
    PI_PARAM_DAT_FILE_INVALID_VERSION__1077 = -1077
    PI_CANNOT_WRITE_TO_PARAM_DAT_FILE__1078 = -1078
    PI_CANNOT_CREATE_PARAM_DAT_FILE__1079 = -1079
    PI_PARAM_DAT_FILE_INVALID_REVISION__1080 = -1080
    PI_USERSTAGES_DAT_FILE_INVALID_REVISION__1081 = -1081
    PI_SOFTWARE_TIMEOUT__1082 = -1082
    PI_WRONG_DATA_TYPE__1083 = -1083
    PI_DIFFERENT_ARRAY_SIZES__1084 = -1084
    PI_PARAM_NOT_FOUND_IN_PARAM_DAT_FILE__1085 = -1085
    PI_MACRO_RECORDING_NOT_ALLOWED_IN_THIS_MODE__1086 = -1086
    PI_USER_CANCELLED_COMMAND__1087 = -1087
    PI_TOO_FEW_GCS_DATA__1088 = -1088
    PI_TOO_MANY_GCS_DATA__1089 = -1089
    PI_GCS_DATA_READ_ERROR__1090 = -1090
    PI_WRONG_NUMBER_OF_INPUT_ARGUMENTS__1091 = -1091
    PI_FAILED_TO_CHANGE_CCL_LEVEL__1092 = -1092
    PI_FAILED_TO_SWITCH_OFF_SERVO__1093 = -1093
    PI_FAILED_TO_SET_SINGLE_PARAMETER_WHILE_PERFORMING_CST__1094 = -1094
    PI_ERROR_CONTROLLER_REBOOT__1095 = -1095
    PI_ERROR_AT_QHPA__1096 = -1096
    PI_QHPA_NONCOMPLIANT_WITH_GCS__1097 = -1097
    PI_FAILED_TO_READ_QSPA__1098 = -1098
    PI_PAM_FILE_WRONG_VERSION__1099 = -1099
    PI_PAM_FILE_INVALID_FORMAT__1100 = -1100
    PI_INCOMPLETE_INFORMATION__1101 = -1101
    PI_NO_VALUE_AVAILABLE__1102 = -1102
    PI_NO_PAM_FILE_OPEN__1103 = -1103
    PI_INVALID_VALUE__1104 = -1104
    PI_UNKNOWN_PARAMETER__1105 = -1105
    PI_RESPONSE_TO_QSEP_FAILED__1106 = -1106
    PI_RESPONSE_TO_QSPA_FAILED__1107 = -1107
    PI_ERROR_IN_CST_VALIDATION__1108 = -1108
    PI_ERROR_PAM_FILE_HAS_DUPLICATE_ENTRY_WITH_DIFFERENT_VALUES__1109 = -1109
    PI_ERROR_FILE_NO_SIGNATURE__1110 = -1110
    PI_ERROR_FILE_INVALID_SIGNATURE__1111 = -1111
    PI_PARAMETER_DB_INVALID_STAGE_TYPE_FORMAT__10000 = -10000
    PI_PARAMETER_DB_SYSTEM_NOT_AVAILABLE__10001 = -10001
    PI_PARAMETER_DB_FAILED_TO_ESTABLISH_CONNECTION__10002 = -10002
    PI_PARAMETER_DB_COMMUNICATION_ERROR__10003 = -10003
    PI_PARAMETER_DB_ERROR_WHILE_QUERYING_PARAMETERS__10004 = -10004
    PI_PARAMETER_DB_SYSTEM_ALREADY_EXISTS__10005 = -10005
    PI_PARAMETER_DB_QHPA_CONTANS_UNKNOWN_PAM_IDS__10006 = -10006
    PI_PARAMETER_DB_AND_QHPA_ARE_INCONSISTENT__10007 = -10007
    PI_PARAMETER_DB_SYSTEM_COULD_NOT_BE_ADDED__10008 = -10008
    PI_PARAMETER_DB_SYSTEM_COULD_NOT_BE_REMOVED__10009 = -10009
    PI_PARAMETER_DB_CONTROLLER_DB_PARAMETERS_MISMATCH__10010 = -10010
    PI_PARAMETER_DB_DATABASE_IS_OUTDATED__10011 = -10011
    PI_PARAMETER_DB_AND_HPA_MISMATCH_STRICT__10012 = -10012
    PI_PARAMETER_DB_AND_HPA_MISMATCH_LOOSE__10013 = -10013
    PI_PARAMETER_DB_FAILED_TO_SET_PARAMETERS_CORRECTLY__10014 = -10014
    PI_PARAMETER_DB_MISSING_PARAMETER_DEFINITIONS_IN_DATABASE__10015 = -10015
    PI_CNTR_NO_ERROR_0 = 0
    PI_CNTR_PARAM_SYNTAX_1 = 1
    PI_CNTR_UNKNOWN_COMMAND_2 = 2
    PI_CNTR_COMMAND_TOO_LONG_3 = 3
    PI_CNTR_SCAN_ERROR_4 = 4
    PI_CNTR_MOVE_WITHOUT_REF_OR_NO_SERVO_5 = 5
    PI_CNTR_INVALID_SGA_PARAM_6 = 6
    PI_CNTR_POS_OUT_OF_LIMITS_7 = 7
    PI_CNTR_VEL_OUT_OF_LIMITS_8 = 8
    PI_CNTR_SET_PIVOT_NOT_POSSIBLE_9 = 9
    PI_CNTR_STOP_10 = 10
    PI_CNTR_SST_OR_SCAN_RANGE_11 = 11
    PI_CNTR_INVALID_SCAN_AXES_12 = 12
    PI_CNTR_INVALID_NAV_PARAM_13 = 13
    PI_CNTR_INVALID_ANALOG_INPUT_14 = 14
    PI_CNTR_INVALID_AXIS_IDENTIFIER_15 = 15
    PI_CNTR_INVALID_STAGE_NAME_16 = 16
    PI_CNTR_PARAM_OUT_OF_RANGE_17 = 17
    PI_CNTR_INVALID_MACRO_NAME_18 = 18
    PI_CNTR_MACRO_RECORD_19 = 19
    PI_CNTR_MACRO_NOT_FOUND_20 = 20
    PI_CNTR_AXIS_HAS_NO_BRAKE_21 = 21
    PI_CNTR_DOUBLE_AXIS_22 = 22
    PI_CNTR_ILLEGAL_AXIS_23 = 23
    PI_CNTR_PARAM_NR_24 = 24
    PI_CNTR_INVALID_REAL_NR_25 = 25
    PI_CNTR_MISSING_PARAM_26 = 26
    PI_CNTR_SOFT_LIMIT_OUT_OF_RANGE_27 = 27
    PI_CNTR_NO_MANUAL_PAD_28 = 28
    PI_CNTR_NO_JUMP_29 = 29
    PI_CNTR_INVALID_JUMP_30 = 30
    PI_CNTR_AXIS_HAS_NO_REFERENCE_31 = 31
    PI_CNTR_STAGE_HAS_NO_LIM_SWITCH_32 = 32
    PI_CNTR_NO_RELAY_CARD_33 = 33
    PI_CNTR_CMD_NOT_ALLOWED_FOR_STAGE_34 = 34
    PI_CNTR_NO_DIGITAL_INPUT_35 = 35
    PI_CNTR_NO_DIGITAL_OUTPUT_36 = 36
    PI_CNTR_NO_MCM_37 = 37
    PI_CNTR_INVALID_MCM_38 = 38
    PI_CNTR_INVALID_CNTR_NUMBER_39 = 39
    PI_CNTR_NO_JOYSTICK_CONNECTED_40 = 40
    PI_CNTR_INVALID_EGE_AXIS_41 = 41
    PI_CNTR_SLAVE_POSITION_OUT_OF_RANGE_42 = 42
    PI_CNTR_COMMAND_EGE_SLAVE_43 = 43
    PI_CNTR_JOYSTICK_CALIBRATION_FAILED_44 = 44
    PI_CNTR_REFERENCING_FAILED_45 = 45
    PI_CNTR_OPM_MISSING_46 = 46
    PI_CNTR_OPM_NOT_INITIALIZED_47 = 47
    PI_CNTR_OPM_COM_ERROR_48 = 48
    PI_CNTR_MOVE_TO_LIMIT_SWITCH_FAILED_49 = 49
    PI_CNTR_REF_WITH_REF_DISABLED_50 = 50
    PI_CNTR_AXIS_UNDER_JOYSTICK_CONTROL_51 = 51
    PI_CNTR_COMMUNICATION_ERROR_52 = 52
    PI_CNTR_DYNAMIC_MOVE_IN_PROCESS_53 = 53
    PI_CNTR_UNKNOWN_PARAMETER_54 = 54
    PI_CNTR_NO_REP_RECORDED_55 = 55
    PI_CNTR_INVALID_PASSWORD_56 = 56
    PI_CNTR_INVALID_RECORDER_CHAN_57 = 57
    PI_CNTR_INVALID_RECORDER_SRC_OPT_58 = 58
    PI_CNTR_INVALID_RECORDER_SRC_CHAN_59 = 59
    PI_CNTR_PARAM_PROTECTION_60 = 60
    PI_CNTR_AUTOZERO_RUNNING_61 = 61
    PI_CNTR_NO_LINEAR_AXIS_62 = 62
    PI_CNTR_INIT_RUNNING_63 = 63
    PI_CNTR_READ_ONLY_PARAMETER_64 = 64
    PI_CNTR_PAM_NOT_FOUND_65 = 65
    PI_CNTR_VOL_OUT_OF_LIMITS_66 = 66
    PI_CNTR_WAVE_TOO_LARGE_67 = 67
    PI_CNTR_NOT_ENOUGH_DDL_MEMORY_68 = 68
    PI_CNTR_DDL_TIME_DELAY_TOO_LARGE_69 = 69
    PI_CNTR_DIFFERENT_ARRAY_LENGTH_70 = 70
    PI_CNTR_GEN_SINGLE_MODE_RESTART_71 = 71
    PI_CNTR_ANALOG_TARGET_ACTIVE_72 = 72
    PI_CNTR_WAVE_GENERATOR_ACTIVE_73 = 73
    PI_CNTR_AUTOZERO_DISABLED_74 = 74
    PI_CNTR_NO_WAVE_SELECTED_75 = 75
    PI_CNTR_IF_BUFFER_OVERRUN_76 = 76
    PI_CNTR_NOT_ENOUGH_RECORDED_DATA_77 = 77
    PI_CNTR_TABLE_DEACTIVATED_78 = 78
    PI_CNTR_OPENLOOP_VALUE_SET_WHEN_SERVO_ON_79 = 79
    PI_CNTR_RAM_ERROR_80 = 80
    PI_CNTR_MACRO_UNKNOWN_COMMAND_81 = 81
    PI_CNTR_MACRO_PC_ERROR_82 = 82
    PI_CNTR_JOYSTICK_ACTIVE_83 = 83
    PI_CNTR_MOTOR_IS_OFF_84 = 84
    PI_CNTR_ONLY_IN_MACRO_85 = 85
    PI_CNTR_JOYSTICK_UNKNOWN_AXIS_86 = 86
    PI_CNTR_JOYSTICK_UNKNOWN_ID_87 = 87
    PI_CNTR_REF_MODE_IS_ON_88 = 88
    PI_CNTR_NOT_ALLOWED_IN_CURRENT_MOTION_MODE_89 = 89
    PI_CNTR_DIO_AND_TRACING_NOT_POSSIBLE_90 = 90
    PI_CNTR_COLLISION_91 = 91
    PI_CNTR_SLAVE_NOT_FAST_ENOUGH_92 = 92
    PI_CNTR_CMD_NOT_ALLOWED_WHILE_AXIS_IN_MOTION_93 = 93
    PI_CNTR_OPEN_LOOP_JOYSTICK_ENABLED_94 = 94
    PI_CNTR_INVALID_SERVO_STATE_FOR_PARAMETER_95 = 95
    PI_CNTR_UNKNOWN_STAGE_NAME_96 = 96
    PI_CNTR_INVALID_VALUE_LENGTH_97 = 97
    PI_CNTR_AUTOZERO_FAILED_98 = 98
    PI_CNTR_SENSOR_VOLTAGE_OFF_99 = 99
    PI_LABVIEW_ERROR_100 = 100
    PI_CNTR_NO_AXIS_200 = 200
    PI_CNTR_NO_AXIS_PARAM_FILE_201 = 201
    PI_CNTR_INVALID_AXIS_PARAM_FILE_202 = 202
    PI_CNTR_NO_AXIS_PARAM_BACKUP_203 = 203
    PI_CNTR_RESERVED_204_204 = 204
    PI_CNTR_SMO_WITH_SERVO_ON_205 = 205
    PI_CNTR_UUDECODE_INCOMPLETE_HEADER_206 = 206
    PI_CNTR_UUDECODE_NOTHING_TO_DECODE_207 = 207
    PI_CNTR_UUDECODE_ILLEGAL_FORMAT_208 = 208
    PI_CNTR_CRC32_ERROR_209 = 209
    PI_CNTR_ILLEGAL_FILENAME_210 = 210
    PI_CNTR_FILE_NOT_FOUND_211 = 211
    PI_CNTR_FILE_WRITE_ERROR_212 = 212
    PI_CNTR_DTR_HINDERS_VELOCITY_CHANGE_213 = 213
    PI_CNTR_POSITION_UNKNOWN_214 = 214
    PI_CNTR_CONN_POSSIBLY_BROKEN_215 = 215
    PI_CNTR_ON_LIMIT_SWITCH_216 = 216
    PI_CNTR_UNEXPECTED_STRUT_STOP_217 = 217
    PI_CNTR_POSITION_BASED_ON_ESTIMATION_218 = 218
    PI_CNTR_POSITION_BASED_ON_INTERPOLATION_219 = 219
    PI_CNTR_INTERPOLATION_FIFO_UNDERRUN_220 = 220
    PI_CNTR_INTERPOLATION_FIFO_OVERFLOW_221 = 221
    PI_CNTR_INVALID_HANDLE_230 = 230
    PI_CNTR_NO_BIOS_FOUND_231 = 231
    PI_CNTR_SAVE_SYS_CFG_FAILED_232 = 232
    PI_CNTR_LOAD_SYS_CFG_FAILED_233 = 233
    PI_CNTR_SEND_BUFFER_OVERFLOW_301 = 301
    PI_CNTR_VOLTAGE_OUT_OF_LIMITS_302 = 302
    PI_CNTR_OPEN_LOOP_MOTION_SET_WHEN_SERVO_ON_303 = 303
    PI_CNTR_RECEIVING_BUFFER_OVERFLOW_304 = 304
    PI_CNTR_EEPROM_ERROR_305 = 305
    PI_CNTR_I2C_ERROR_306 = 306
    PI_CNTR_RECEIVING_TIMEOUT_307 = 307
    PI_CNTR_TIMEOUT_308 = 308
    PI_CNTR_MACRO_OUT_OF_SPACE_309 = 309
    PI_CNTR_EUI_OLDVERSION_CFGDATA_310 = 310
    PI_CNTR_EUI_INVALID_CFGDATA_311 = 311
    PI_CNTR_HARDWARE_ERROR_333 = 333
    PI_CNTR_WAV_INDEX_ERROR_400 = 400
    PI_CNTR_WAV_NOT_DEFINED_401 = 401
    PI_CNTR_WAV_TYPE_NOT_SUPPORTED_402 = 402
    PI_CNTR_WAV_LENGTH_EXCEEDS_LIMIT_403 = 403
    PI_CNTR_WAV_PARAMETER_NR_404 = 404
    PI_CNTR_WAV_PARAMETER_OUT_OF_LIMIT_405 = 405
    PI_CNTR_WGO_BIT_NOT_SUPPORTED_406 = 406
    PI_CNTR_EMERGENCY_STOP_BUTTON_ACTIVATED_500 = 500
    PI_CNTR_EMERGENCY_STOP_BUTTON_WAS_ACTIVATED_501 = 501
    PI_CNTR_REDUNDANCY_LIMIT_EXCEEDED_502 = 502
    PI_CNTR_COLLISION_SWITCH_ACTIVATED_503 = 503
    PI_CNTR_FOLLOWING_ERROR_504 = 504
    PI_CNTR_SENSOR_SIGNAL_INVALID_505 = 505
    PI_CNTR_SERVO_LOOP_UNSTABLE_506 = 506
    PI_CNTR_LOST_SPI_SLAVE_CONNECTION_507 = 507
    PI_CNTR_CS_DOES_NOT_EXIST_530 = 530
    PI_CNTR_PARENT_CS_DOES_NOT_EXIST_531 = 531
    PI_CNTR_CS_IN_USE_532 = 532
    PI_CNTR_CS_DEFINITION_IS_CYCLIC_533 = 533
    PI_CNTR_HEXAPOD_IN_MOTION_536 = 536
    PI_CNTR_CS_TYPE_CANNOT_BE_ENABLED_537 = 537
    PI_CNTR_CS_PARENT_IDENTICAL_TO_CHILD_539 = 539
    PI_CNTR_CS_DEFINITION_INCONSISTENT_540 = 540
    PI_CNTR_CS_NOT_IN_SAME_CHAIN_542 = 542
    PI_CNTR_CS_MEMORY_FULL_543 = 543
    PI_CNTR_SPI_COMMAND_NOT_SUPPORTED_544 = 544
    PI_CNTR_SOFTLIMITS_INVALID_545 = 545
    PI_CNTR_CS_WRITE_PROTECTED_546 = 546
    PI_CNTR_CS_CONTENT_FROM_CONFIG_FILE_547 = 547
    PI_CNTR_CS_CANNOT_BE_LINKED_548 = 548
    PI_CNTR_KSB_CS_ROTATION_ONLY_549 = 549
    PI_CNTR_CS_DATA_CANNOT_BE_QUERIED_551 = 551
    PI_CNTR_CS_COMBINATION_DOES_NOT_EXIST_552 = 552
    PI_CNTR_CS_COMBINATION_INVALID_553 = 553
    PI_CNTR_CS_TYPE_DOES_NOT_EXIST_554 = 554
    PI_CNTR_UNKNOWN_ERROR_555 = 555
    PI_CNTR_CS_TYPE_NOT_ENABLED_556 = 556
    PI_CNTR_CS_NAME_INVALID_557 = 557
    PI_CNTR_CS_GENERAL_FILE_MISSING_558 = 558
    PI_CNTR_CS_LEVELING_FILE_MISSING_559 = 559
    PI_CNTR_NOT_ENOUGH_MEMORY_601 = 601
    PI_CNTR_HW_VOLTAGE_ERROR_602 = 602
    PI_CNTR_HW_TEMPERATURE_ERROR_603 = 603
    PI_CNTR_POSITION_ERROR_TOO_HIGH_604 = 604
    PI_CNTR_INPUT_OUT_OF_RANGE_606 = 606
    PI_CNTR_NO_INTEGER_607 = 607
    PI_CNTR_FAST_ALIGNMENT_PROCESS_IS_NOT_RUNNING_608 = 608
    PI_CNTR_FAST_ALIGNMENT_PROCESS_IS_NOT_PAUSED_609 = 609
    PI_CNTR_UNABLE_TO_SET_PARAM_WITH_SPA_650 = 650
    PI_CNTR_PHASE_FINDING_ERROR_651 = 651
    PI_CNTR_SENSOR_SETUP_ERROR_652 = 652
    PI_CNTR_SENSOR_COMM_ERROR_653 = 653
    PI_CNTR_MOTOR_AMPLIFIER_ERROR_654 = 654
    PI_CNTR_OVER_CURR_PROTEC_TRIGGERED_BY_I2T_655 = 655
    PI_CNTR_OVER_CURR_PROTEC_TRIGGERED_BY_AMP_MODULE_656 = 656
    PI_CNTR_SAFETY_STOP_TRIGGERED_657 = 657
    PI_SENSOR_OFF_658 = 658
    PI_CNTR_COMMAND_NOT_ALLOWED_IN_EXTERNAL_MODE_700 = 700
    PI_CNTR_EXTERNAL_MODE_ERROR_710 = 710
    PI_CNTR_INVALID_MODE_OF_OPERATION_715 = 715
    PI_CNTR_FIRMWARE_STOPPED_BY_CMD_716 = 716
    PI_CNTR_EXTERNAL_MODE_DRIVER_MISSING_717 = 717
    PI_CNTR_CONFIGURATION_FAILURE_EXTERNAL_MODE_718 = 718
    PI_CNTR_EXTERNAL_MODE_CYCLETIME_INVALID_719 = 719
    PI_CNTR_BRAKE_ACTIVATED_720 = 720
    PI_CNTR_SURFACEDETECTION_RUNNING_731 = 731
    PI_CNTR_SURFACEDETECTION_FAILED_732 = 732
    PI_CNTR_FIELDBUS_IS_ACTIVE_733 = 733
    PI_CNTR_TOO_MANY_NESTED_MACROS_1000 = 1000
    PI_CNTR_MACRO_ALREADY_DEFINED_1001 = 1001
    PI_CNTR_NO_MACRO_RECORDING_1002 = 1002
    PI_CNTR_INVALID_MAC_PARAM_1003 = 1003
    PI_CNTR_MACRO_DELETE_ERROR_1004 = 1004
    PI_CNTR_CONTROLLER_BUSY_1005 = 1005
    PI_CNTR_INVALID_IDENTIFIER_1006 = 1006
    PI_CNTR_UNKNOWN_VARIABLE_OR_ARGUMENT_1007 = 1007
    PI_CNTR_RUNNING_MACRO_1008 = 1008
    PI_CNTR_MACRO_INVALID_OPERATOR_1009 = 1009
    PI_CNTR_MACRO_NO_ANSWER_1010 = 1010
    PI_CMD_NOT_VALID_IN_MACRO_MODE_1011 = 1011
    PI_CNTR_MOTION_ERROR_1024 = 1024
    PI_CNTR_MAX_MOTOR_OUTPUT_REACHED_1025 = 1025
    PI_CNTR_EXT_PROFILE_UNALLOWED_CMD_1063 = 1063
    PI_CNTR_EXT_PROFILE_EXPECTING_MOTION_ERROR_1064 = 1064
    PI_CNTR_PROFILE_ACTIVE_1065 = 1065
    PI_CNTR_PROFILE_INDEX_OUT_OF_RANGE_1066 = 1066
    PI_CNTR_PROFILE_OUT_OF_MEMORY_1071 = 1071
    PI_CNTR_PROFILE_WRONG_CLUSTER_1072 = 1072
    PI_CNTR_PROFILE_UNKNOWN_CLUSTER_IDENTIFIER_1073 = 1073
    PI_CNTR_TOO_MANY_TCP_CONNECTIONS_OPEN_1090 = 1090
    PI_CNTR_ALREADY_HAS_SERIAL_NUMBER_2000 = 2000
    PI_CNTR_SECTOR_ERASE_FAILED_4000 = 4000
    PI_CNTR_FLASH_PROGRAM_FAILED_4001 = 4001
    PI_CNTR_FLASH_READ_FAILED_4002 = 4002
    PI_CNTR_HW_MATCHCODE_ERROR_4003 = 4003
    PI_CNTR_FW_MATCHCODE_ERROR_4004 = 4004
    PI_CNTR_HW_VERSION_ERROR_4005 = 4005
    PI_CNTR_FW_VERSION_ERROR_4006 = 4006
    PI_CNTR_FW_UPDATE_ERROR_4007 = 4007
    PI_CNTR_FW_CRC_PAR_ERROR_4008 = 4008
    PI_CNTR_FW_CRC_FW_ERROR_4009 = 4009
    PI_CNTR_INVALID_PCC_SCAN_DATA_5000 = 5000
    PI_CNTR_PCC_SCAN_RUNNING_5001 = 5001
    PI_CNTR_INVALID_PCC_AXIS_5002 = 5002
    PI_CNTR_PCC_SCAN_OUT_OF_RANGE_5003 = 5003
    PI_CNTR_PCC_TYPE_NOT_EXISTING_5004 = 5004
    PI_CNTR_PCC_PAM_ERROR_5005 = 5005
    PI_CNTR_PCC_TABLE_ARRAY_TOO_LARGE_5006 = 5006
    PI_CNTR_NEXLINE_ERROR_5100 = 5100
    PI_CNTR_CHANNEL_ALREADY_USED_5101 = 5101
    PI_CNTR_NEXLINE_TABLE_TOO_SMALL_5102 = 5102
    PI_CNTR_RNP_WITH_SERVO_ON_5103 = 5103
    PI_CNTR_RNP_NEEDED_5104 = 5104
    PI_CNTR_AXIS_NOT_CONFIGURED_5200 = 5200
    PI_CNTR_FREQU_ANALYSIS_FAILED_5300 = 5300
    PI_CNTR_FREQU_ANALYSIS_RUNNING_5301 = 5301
    PI_CNTR_SENSOR_ABS_INVALID_VALUE_6000 = 6000
    PI_CNTR_SENSOR_ABS_WRITE_ERROR_6001 = 6001
    PI_CNTR_SENSOR_ABS_READ_ERROR_6002 = 6002
    PI_CNTR_SENSOR_ABS_CRC_ERROR_6003 = 6003
    PI_CNTR_SENSOR_ABS_ERROR_6004 = 6004
    PI_CNTR_SENSOR_ABS_OVERFLOW_6005 = 6005


# line too long pylint: disable=C0301
__ERRMSG = {
    -1: "Error during com operation (could not be specified)",
    -2: "Error while sending data",
    -3: "Error while receiving data",
    -4: "Not connected (no port with given ID open)",
    -5: "Buffer overflow",
    -6: "Error while opening port",
    -7: "Timeout error",
    -8: "There are more lines waiting in buffer",
    -9: "There is no interface or DLL handle with the given ID",
    -10: "Event/message for notification could not be opened",
    -11: "Function not supported by this interface type",
    -12: "Error while sending 'echoed' data",
    -13: "IEEE488: System error",
    -14: "IEEE488: Function requires GPIB board to be CIC",
    -15: "IEEE488: Write function detected no listeners",
    -16: "IEEE488: Interface board not addressed correctly",
    -17: "IEEE488: Invalid argument to function call",
    -18: "IEEE488: Function requires GPIB board to be SAC",
    -19: "IEEE488: I/O operation aborted",
    -20: "IEEE488: Interface board not found",
    -21: "IEEE488: Error performing DMA",
    -22: "IEEE488: I/O operation started before previous operation completed",
    -23: "IEEE488: No capability for intended operation",
    -24: "IEEE488: File system operation error",
    -25: "IEEE488: Command error during device call",
    -26: "IEEE488: Serial poll-status byte lost",
    -27: "IEEE488: SRQ remains asserted",
    -28: "IEEE488: Return buffer full",
    -29: "IEEE488: Address or board locked",
    -30: "RS-232: 5 data bits with 2 stop bits is an invalid combination, as is 6, 7, or 8 data bits with \
    1.5 stop bits",
    -31: "RS-232: Error configuring the COM port",
    -32: "Error dealing with internal system resources (events, threads, ...)",
    -33: "A DLL or one of the required functions could not be loaded",
    -34: "FTDIUSB: invalid handle",
    -35: "FTDIUSB: device not found",
    -36: "FTDIUSB: device not opened",
    -37: "FTDIUSB: IO error",
    -38: "FTDIUSB: insufficient resources",
    -39: "FTDIUSB: invalid parameter",
    -40: "FTDIUSB: invalid baud rate",
    -41: "FTDIUSB: device not opened for erase",
    -42: "FTDIUSB: device not opened for write",
    -43: "FTDIUSB: failed to write device",
    -44: "FTDIUSB: EEPROM read failed",
    -45: "FTDIUSB: EEPROM write failed",
    -46: "FTDIUSB: EEPROM erase failed",
    -47: "FTDIUSB: EEPROM not present",
    -48: "FTDIUSB: EEPROM not programmed",
    -49: "FTDIUSB: invalid arguments",
    -50: "FTDIUSB: not supported",
    -51: "FTDIUSB: other error",
    -52: "Error while opening the COM port: was already open",
    -53: "Checksum error in received data from COM port",
    -54: "Socket not ready, you should call the function again",
    -55: "Port is used by another socket",
    -56: "Socket not connected (or not valid)",
    -57: "Connection terminated (by peer)",
    -58: "Can't connect to peer",
    -59: "Operation was interrupted by a nonblocked signal",
    -60: "No Device with this ID is present",
    -61: "Driver could not be opened (on Vista: run as administrator!)",
    -62: "Host not found",
    -63: "Device already connected",
    -1001: "Unknown axis identifier",
    -1002: "Number for NAV out of range--must be in [1,10000]",
    -1003: "Invalid value for SGA--must be one of {1, 10, 100, 1000}",
    -1004: "Controller sent unexpected response",
    -1005: "No manual control pad installed, calls to SMA and related commands are not allowed",
    -1006: "Invalid number for manual control pad knob",
    -1007: "Axis not currently controlled by a manual control pad",
    -1008: "Controller is busy with some lengthy operation (e.g. reference move, fast scan algorithm)",
    -1009: "Internal error--could not start thread",
    -1010: "Controller is (already) in macro mode--command not valid in macro mode",
    -1011: "Controller not in macro mode--command not valid unless macro mode active",
    -1012: "Could not open file to write or read macro",
    -1013: "No macro with given name on controller, or macro is empty",
    -1014: "Internal error in macro editor",
    -1015: "One or more arguments given to function is invalid (empty string, index out of range, ...)",
    -1016: "Axis identifier is already in use by a connected stage",
    -1017: "Invalid axis identifier",
    -1018: "Could not access array data in COM server",
    -1019: "Range of array does not fit the number of parameters",
    -1020: "Invalid parameter ID given to SPA or SPA?",
    -1021: "Number for AVG out of range--must be >0",
    -1022: "Incorrect number of samples given to WAV",
    -1023: "Generation of wave failed",
    -1024: "Motion error: position error too large, servo is switched off automatically",
    -1025: "Controller is (already) running a macro",
    -1026: "Configuration of PZT stage or amplifier failed",
    -1027: "Current settings are not valid for desired configuration",
    -1028: "Unknown channel identifier",
    -1029: "Error while reading/writing wave generator parameter file",
    -1030: "Could not find description of wave form. Maybe WG.INI is missing?",
    -1031: "The WGWaveEditor DLL function was not found at startup",
    -1032: "The user cancelled a dialog",
    -1033: "Error from C-844 Controller",
    -1034: "DLL necessary to call function not loaded, or function not found in DLL",
    -1035: "The open parameter file is protected and cannot be edited",
    -1036: "There is no parameter file open",
    -1037: "Selected stage does not exist",
    -1038: "There is already a parameter file open. Close it before opening a new file",
    -1039: "Could not open parameter file",
    -1040: "The version of the connected controller is invalid",
    -1041: "Parameter could not be set with SPA--parameter not defined for this controller!",
    -1042: "The maximum number of wave definitions has been exceeded",
    -1043: "The maximum number of wave generators has been exceeded",
    -1044: "No wave defined for specified axis",
    -1045: "Wave output to axis already stopped/started",
    -1046: "Not all axes could be referenced",
    -1047: "Could not find parameter set required by frequency relation",
    -1048: "Command ID given to SPP or SPP? is not valid",
    -1049: "A stage name given to CST is not unique",
    -1050: "A uuencoded file transfered did not start with 'begin' followed by the proper filename",
    -1051: "Could not create/read file on host PC",
    -1052: "Checksum error when transfering a file to/from the controller",
    -1053: "The PiStages.dat database could not be found. This file is required to connect \
    a stage with the CST command",
    -1054: "No wave being output to specified axis",
    -1055: "Invalid password",
    -1056: "Error during communication with OPM (Optical Power Meter), maybe no OPM connected",
    -1057: "WaveEditor: Error during wave creation, incorrect number of parameters",
    -1058: "WaveEditor: Frequency out of range",
    -1059: "WaveEditor: Error during wave creation, incorrect index for integer parameter",
    -1060: "WaveEditor: Error during wave creation, incorrect index for floating point parameter",
    -1061: "WaveEditor: Error during wave creation, could not calculate value",
    -1062: "WaveEditor: Graph display component not installed",
    -1063: "User Profile Mode: Command is not allowed, check for required preparatory commands",
    -1064: "User Profile Mode: First target position in User Profile is too far from current position",
    -1065: "Controller is (already) in User Profile Mode",
    -1066: "User Profile Mode: Block or Data Set index out of allowed range",
    -1067: "ProfileGenerator: No profile has been created yet",
    -1068: "ProfileGenerator: Generated profile exceeds limits of one or both axes",
    -1069: "ProfileGenerator: Unknown parameter ID in Set/Get Parameter command",
    -1070: "ProfileGenerator: Parameter out of allowed range",
    -1071: "User Profile Mode: Out of memory",
    -1072: "User Profile Mode: Cluster is not assigned to this axis",
    -1073: "Unknown cluster identifier",
    -1074: "The installed device driver doesn't match the required version. Please see the documentation to \
    determine the required device driver version.",
    -1075: "The library used doesn't match the required version. Please see the documentation to determine \
    the required library version.",
    -1076: "The interface is currently locked by another function. Please try again later.",
    -1077: "Version of parameter DAT file does not match the required version. Current files are available \
     at www.pi.ws.",
    -1078: "Cannot write to parameter DAT file to store user defined stage type.",
    -1079: "Cannot create parameter DAT file to store user defined stage type.",
    -1080: "Parameter DAT file does not have correct revision.",
    -1081: "User stages DAT file does not have correct revision.",
    -1082: "Timeout Error. Some lengthy operation did not finish within expected time.",
    -1083: "A function argument has an unexpected datatype.",
    -1084: "Length of data arrays is different.",
    -1085: "Parameter value not found in parameter DAT file.",
    -1086: "Macro recording is not allowed in this mode of operation.",
    -1087: "command cancelled by user input.",
    -1088: "Controller sent too few GCS data sets",
    -1089: "Controller sent too many GCS data sets",
    -1090: "Communication error while reading GCS data",
    -1091: "Wrong number of input arguments.",
    -1092: "Change of command level has failed.",
    -1093: "Switching off the servo mode has failed.",
    -1094: "A parameter could not be set while performing CST: CST was not performed \
    (parameters remain unchanged).",
    -1095: "Connection could not be reestablished after reboot.",
    -1096: "Sending HPA? or receiving the response has failed.",
    -1097: "HPA? response does not comply with GCS2 syntax.",
    -1098: "Response to SPA? could not be received.",
    -1099: "Version of PAM file cannot be handled (too old or too new)",
    -1100: "PAM file does not contain required data in PAM-file format",
    -1101: "Information does not contain all required data",
    -1102: "No value for parameter available",
    -1103: "No PAM file is open",
    -1104: "Invalid value",
    -1105: "Unknown parameter",
    -1106: "Response to SEP? could not be received.",
    -1107: "Response to SPA? could not be received.",
    -1108: "Error while performing CST: One or more parameters were not set correctly.",
    -1109: "PAM file has duplicate entry with different values.",
    -1110: "File has no signature",
    -1111: "File has invalid signature",
    -10000: "PI stage database: String containing stage type and description has invalid format.",
    -10001: "PI stage database: Database does not contain the selected stage type for the connected \
    controller.",
    -10002: "PI stage database: Establishing the connection has failed.",
    -10003: "PI stage database: Communication was interrupted (e.g. because database was deleted).",
    -10004: "PI stage database: Querying data failed.",
    -10005: "PI stage database: System already exists. Rename stage and try again.",
    -10006: "PI stage database: Response to HPA? contains unknown parameter IDs.",
    -10007: "PI stage database: Inconsistency between database and response to HPA?.",
    -10008: "PI stage database: Stage has not been added.",
    -10009: "PI stage database: Stage has not been removed.",
    -10010: "Controller does not support all stage parameters stored in PI stage database. No parameters \
    were set.",
    -10011: "The version of PISTAGES3.DB stage database is out of date. Please update via PIUpdateFinder. \
    No parameters were set.",
    -10012: "Mismatch between number of parameters present in stage database and available in controller \
    interface. No parameters were set.",
    -10013: "Mismatch between number of parameters present in stage database and available in controller \
    interface. Some parameters were ignored.",
    -10014: "One or more parameters could not be set correctly on the controller.",
    -10015: "One or more parameter definitions are not present in stage database. Please update PISTAGES3.DB \
    via PIUpdateFinder. Missing parameters were ignored.",
    0: "No error",
    1: "Parameter syntax error",
    2: "Unknown command",
    3: "Command length out of limits or command buffer overrun",
    4: "Error while scanning",
    5: "Unallowable move attempted on unreferenced axis, or move attempted with servo off",
    6: "Parameter for SGA not valid",
    7: "Position out of limits",
    8: "Velocity out of limits",
    9: "Attempt to set pivot point while U,V and W not all 0",
    10: "Controller was stopped by command",
    11: "Parameter for SST or for one of the embedded scan algorithms out of range",
    12: "Invalid axis combination for fast scan",
    13: "Parameter for NAV out of range",
    14: "Invalid analog channel",
    15: "Invalid axis identifier",
    16: "Invalid stage name",
    17: "Parameter out of range",
    18: "Invalid macro name",
    19: "Error while recording macro",
    20: "Macro not found",
    21: "Axis has no brake",
    22: "Axis identifier specified more than once",
    23: "Illegal axis or channel",
    24: "Incorrect number of parameters",
    25: "Invalid floating point number",
    26: "Parameter missing",
    27: "Soft limit out of range",
    28: "No manual pad found",
    29: "No more step-response values",
    30: "No step-response values recorded",
    31: "Axis has no reference sensor",
    32: "Axis has no limit switch",
    33: "No relay card installed",
    34: "Command not allowed for selected stage(s)",
    35: "No digital input installed",
    36: "No digital output configured",
    37: "No more MCM responses",
    38: "No MCM values recorded",
    39: "Controller number invalid",
    40: "No joystick configured",
    41: "Invalid axis for electronic gearing, axis can not be slave",
    42: "Position of slave axis is out of range",
    43: "Slave axis cannot be commanded directly when electronic gearing is enabled",
    44: "Calibration of joystick failed",
    45: "Referencing failed",
    46: "OPM (Optical Power Meter) missing",
    47: "OPM (Optical Power Meter) not initialized or cannot be initialized",
    48: "OPM (Optical Power Meter) Communication Error",
    49: "Move to limit switch failed",
    50: "Attempt to reference axis with referencing disabled",
    51: "Selected axis is controlled by joystick",
    52: "Controller detected communication error",
    53: "Command is not allowed while the affected axis is in motion.",
    54: "Unknown parameter",
    55: "No commands were recorded with REP",
    56: "Password invalid",
    57: "Data Record Table does not exist",
    58: "Source does not exist; number too low or too high",
    59: "Source Record Table number too low or too high",
    60: "Protected Param: current Command Level (CCL) too low",
    61: "Command execution not possible while Autozero is running",
    62: "Autozero requires at least one linear axis",
    63: "Initialization still in progress",
    64: "Parameter is read-only",
    65: "Parameter not found in non-volatile memory",
    66: "Voltage out of limits",
    67: "Not enough memory available for requested wave curve",
    68: "Not enough memory available for DDL table; DDL can not be started",
    69: "Time delay larger than DDL table; DDL can not be started",
    70: "The requested arrays have different lengths; query them separately",
    71: "Attempt to restart the generator while it is running in single step mode",
    72: "Motion commands and wave generator activation are not allowed when analog target is active",
    73: "Motion commands are not allowed when wave generator output is active; use WGO to \
    disable generator output",
    74: "No sensor channel or no piezo channel connected to selected axis (sensor and piezo matrix)",
    75: "Generator started (WGO) without having selected a wave table (WSL).",
    76: "Interface buffer did overrun and command couldn't be received correctly",
    77: "Data Record Table does not hold enough recorded data",
    78: "Data Record Table is not configured for recording",
    79: "Open-loop commands (SVA, SVR) are not allowed when servo is on",
    80: "Hardware error affecting RAM",
    81: "Not macro command",
    82: "Macro counter out of range",
    83: "Joystick is active",
    84: "Motor is off",
    85: "Macro-only command",
    86: "Invalid joystick axis",
    87: "Joystick unknown",
    88: "Move without referenced stage",
    89: "Command not allowed in current motion mode",
    90: "No tracing possible while digital IOs are used on this HW revision. Reconnect to \
    switch operation mode.",
    91: "Move not possible, would cause collision",
    92: "Stage is not capable of following the master. Check the gear ratio(SRA).",
    93: "This command is not allowed while the affected axis or its master is in motion.",
    94: "Servo cannot be switched on when open-loop joystick control is enabled.",
    95: "This parameter cannot be changed in current servo mode.",
    96: "Unknown stage name",
    97: "Invalid length of value (too much characters)",
    98: "AutoZero procedure was not successful",
    99: "Sensor voltage is off",
    100: "PI LabVIEW driver reports error. See source control for details.",
    200: "No stage connected to axis",
    201: "File with axis parameters not found",
    202: "Invalid axis parameter file",
    203: "Backup file with axis parameters not found",
    204: "PI internal error code 204",
    205: "SMO with servo on",
    206: "uudecode: incomplete header",
    207: "uudecode: nothing to decode",
    208: "uudecode: illegal UUE format",
    209: "CRC32 error",
    210: "Illegal file name (must be 8-0 format)",
    211: "File not found on controller",
    212: "Error writing file on controller",
    213: "VEL command not allowed in DTR Command Mode",
    214: "Position calculations failed",
    215: "The connection between controller and stage may be broken",
    216: "The connected stage has driven into a limit switch, some controllers need CLR to resume operation",
    217: "Strut test command failed because of an unexpected strut stop",
    218: "While MOV! is running position can only be estimated!",
    219: "Position was calculated during MOV motion",
    220: "FIFO buffer underrun during interpolation",
    221: "FIFO buffer overflow during interpolation",
    230: "Invalid handle",
    231: "No bios found",
    232: "Save system configuration failed",
    233: "Load system configuration failed",
    301: "Send buffer overflow",
    302: "Voltage out of limits",
    303: "Open-loop motion attempted when servo ON",
    304: "Received command is too long",
    305: "Error while reading/writing EEPROM",
    306: "Error on I2C bus",
    307: "Timeout while receiving command",
    308: "A lengthy operation has not finished in the expected time",
    309: "Insufficient space to store macro",
    310: "Configuration data has old version number",
    311: "Invalid configuration data",
    333: "Internal hardware error",
    400: "Wave generator index error",
    401: "Wave table not defined",
    402: "Wave type not supported",
    403: "Wave length exceeds limit",
    404: "Wave parameter number error",
    405: "Wave parameter out of range",
    406: "WGO command bit not supported",
    500: "The 'red knob' is still set and disables system",
    501: "The 'red knob' was activated and still disables system - reanimation required",
    502: "Position consistency check failed",
    503: "Hardware collision sensor(s) are activated",
    504: "Strut following error occurred, e.g. caused by overload or encoder failure",
    505: "One sensor signal is not valid",
    506: "Servo loop was unstable due to wrong parameter setting and switched off to avoid damage.",
    507: "digital connection to external spi slave device is lost",
    530: "A command refers to a coordinate system that does not exist",
    531: "A command refers to a coordinate system that has no parent node",
    532: "Attempt to delete or change a coordinate system that is in use",
    533: "Definition of a coordinate system is cyclic",
    536: "Coordinate system cannot be defined as long as Hexapod is in motion",
    537: "Coordinate system type is not intended for manual enabling",
    539: "A coordinate system cannot be linked to itself",
    540: "Coordinate system definition is erroneous or not complete (replace or delete it)",
    542: "The coordinate systems are not part of the same chain",
    543: "Unused coordinate system must be deleted before new coordinate system can be stored",
    544: "With this coordinate system type SPI usage is not supported",
    545: "Soft limits invalid due to changes in coordinate system",
    546: "Coordinate system is write protected",
    547: "Coordinate system cannot be changed because its content is loaded from a configuration file",
    548: "Coordinate system may not be linked",
    549: "A KSB-type coordinate system can only be rotated by multiples of 90 degrees",
    551: "This query is not supported for this coordinate system type",
    552: "This combination of work and tool coordinate systems does not exist",
    553: "The combination must consist of one work and one tool coordinate system",
    554: "This coordinate system type does not exist",
    555: "BasMac: unknown controller error",
    556: "No coordinate system of this type is enabled",
    557: "Name of coordinate system is invalid",
    558: "File with stored CS systems is missing or erroneous",
    559: "File with leveling CS is missing or erroneous",
    601: "Not enough memory",
    602: "Hardware voltage error",
    603: "Hardware temperature out of range",
    604: "Position error of any axis in the system is too high",
    606: "Maximum value of input signal has been exceeded",
    607: "Value is not integer",
    608: "Fast alignment process cannot be paused because it is not running",
    609: "Fast alignment process cannot be restarted/resumed because it is not paused",
    650: "Parameter could not be set with SPA - SEP needed?",
    651: "Phase finding error",
    652: "Sensor setup error",
    653: "Sensor communication error",
    654: "Motor amplifier error",
    655: "Overcurrent protection triggered by I2T-module",
    656: "Overcurrent protection triggered by amplifier module",
    657: "Safety stop triggered",
    658: "Sensor off?",
    700: "Command not allowed in external mode",
    710: "External mode communication error",
    715: "Invalid mode of operation",
    716: "Firmware stopped by command (#27)",
    717: "External mode driver missing",
    718: "Missing or incorrect configuration of external mode",
    719: "External mode cycletime invalid",
    720: "Brake is activated",
    731: "Command not allowed while surface detection is running",
    732: "Last surface detection failed",
    733: "Fieldbus is active and is blocking GCS control commands",
    1000: "Too many nested macros",
    1001: "Macro already defined",
    1002: "Macro recording not activated",
    1003: "Invalid parameter for MAC",
    1004: "Deleting macro failed",
    1005: "Controller is busy with some lengthy operation (e.g. reference move, fast scan algorithm)",
    1006: "Invalid identifier (invalid special characters, ...)",
    1007: "Variable or argument not defined",
    1008: "Controller is (already) running a macro",
    1009: "Invalid or missing operator for condition. Check necessary spaces around operator.",
    1010: "No answer was received while executing WAC/MEX/JRC/...",
    1011: "Command not valid during macro execution",
    1024: "Motion error: position error too large, servo is switched off automatically",
    1025: "Maximum motor output reached",
    1063: "User Profile Mode: Command is not allowed, check for required preparatory commands",
    1064: "User Profile Mode: First target position in User Profile is too far from current position",
    1065: "Controller is (already) in User Profile Mode",
    1066: "User Profile Mode: Block or Data Set index out of allowed range",
    1071: "User Profile Mode: Out of memory",
    1072: "User Profile Mode: Cluster is not assigned to this axis",
    1073: "Unknown cluster identifier",
    1090: "There are too many open tcpip connections",
    2000: "Controller already has a serial number",
    4000: "Sector erase failed",
    4001: "Flash program failed",
    4002: "Flash read failed",
    4003: "HW match code missing/invalid",
    4004: "FW match code missing/invalid",
    4005: "HW version missing/invalid",
    4006: "FW version missing/invalid",
    4007: "FW update failed",
    4008: "FW Parameter CRC wrong",
    4009: "FW CRC wrong",
    5000: "PicoCompensation scan data is not valid",
    5001: "PicoCompensation is running, some actions can not be executed during scanning/recording",
    5002: "Given axis can not be defined as PPC axis",
    5003: "Defined scan area is larger than the travel range",
    5004: "Given PicoCompensation type is not defined",
    5005: "PicoCompensation parameter error",
    5006: "PicoCompensation table is larger than maximum table length",
    5100: "Common error in Nexline firmware module",
    5101: "Output channel for Nexline can not be redefined for other usage",
    5102: "Memory for Nexline signals is too small",
    5103: "RNP can not be executed if axis is in closed loop",
    5104: "relax procedure (RNP) needed",
    5200: "Axis must be configured for this action",
    5300: "Frequency analysis failed",
    5301: "Another frequency analysis is running",
    6000: "Invalid preset value of absolute sensor",
    6001: "Error while writing to sensor",
    6002: "Error while reading from sensor",
    6003: "Checksum error of absolute sensor",
    6004: "General error of absolute sensor",
    6005: "Overflow of absolute sensor position",
}


def translate_error(value):
    """Return a readable error message of `value`.

    @param value : Error value as integer.
    @return Error message as string.
    """
    try:
        msg = '%s (%d)' % (__ERRMSG[value], value)
    except KeyError:
        msg = str(value)
    return msg


class GCSError(Exception):
    """GCSError exception."""

    def __init__(self, value, message=''):
        Exception.__init__(self)
        self.val = value
        self.msg = translate_error(value)
        if message:
            self.msg += ': %r' % message
        logging.debug('GCSError: %s', self.msg)

    def __str__(self):
        """Handle string representation."""
        return self.msg

    def __repr__(self):
        """Intrepeter representation."""
        return self.msg

    def __eq__(self, other):
        """Equality operator handler."""
        return self.val == other

    def __ne__(self, other):
        """Inequality operator handler."""
        return self.val != other
