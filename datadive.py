import os
import ctypes
from ctypes import wintypes
import win32file
import win32con

class DataDive:
    def __init__(self):
        print("Initializing DataDive...")

    def scan_drives(self):
        print("Scanning drives for lost or inaccessible data...")
        drives = self.get_drives()
        for drive in drives:
            print(f"Scanning {drive}...")
            self.scan_drive(drive)

    def get_drives(self):
        drives = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in range(26):
            if bitmask & 1:
                drives.append(chr(65 + letter) + ":\\")
            bitmask >>= 1
        return drives

    def scan_drive(self, drive):
        try:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    file_path = os.path.join(root, file)
                    if self.is_file_accessible(file_path):
                        print(f"Accessible file: {file_path}")
                    else:
                        print(f"Lost/Inaccessible file detected: {file_path}")
        except Exception as e:
            print(f"Error scanning drive {drive}: {e}")

    def is_file_accessible(self, filepath):
        try:
            hfile = win32file.CreateFile(
                filepath,
                win32con.GENERIC_READ,
                0,
                None,
                win32con.OPEN_EXISTING,
                win32con.FILE_ATTRIBUTE_NORMAL,
                None
            )
            win32file.CloseHandle(hfile)
            return True
        except Exception as e:
            return False

if __name__ == "__main__":
    data_dive = DataDive()
    data_dive.scan_drives()