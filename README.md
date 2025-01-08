# DataDive

DataDive is a Python-based utility designed to perform deep scans of Windows systems to retrieve lost or inaccessible data. It systematically scans all drives connected to the system, identifying files that are either accessible or potentially lost.

## Features

- Scans all logical drives on a Windows system.
- Identifies and lists accessible and inaccessible files.
- Easy-to-use command-line interface.

## Requirements

- Python 3.x
- PyWin32 library

## Installation

1. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required PyWin32 library:
   ```bash
   pip install pywin32
   ```

## Usage

1. Clone the repository or download the `datadive.py` file.
2. Open a command prompt or terminal.
3. Navigate to the directory containing `datadive.py`.
4. Run the script using Python:
   ```bash
   python datadive.py
   ```

Upon execution, the program will initiate a scan of all available drives and list files that are either accessible or potentially lost/inaccessible.

## Disclaimer

DataDive is intended for use on personal systems. Ensure you have the necessary permissions to scan and access the data on the drives. Use at your own risk.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.