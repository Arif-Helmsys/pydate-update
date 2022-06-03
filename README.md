# Pydater

When you make a program associated with Github, you can easily update with this module without the need to write an update system.

Specify the path, write a version and leave the rest to the module

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **`pydater`**.

```bash
pip install pydater
```

## Usage

- First of all, you should save your current version number from github.

- Create a repository for this or use an existing one.

- Create a **`.json`** file named **`version.json`** in the repo.

- Its content must be **`{ "version" : "<version_number>"}`**.

- After doing this and saving, copy the **`raw link`** of the **`version.json`** file

- Come back to the relevant repo and import your most up-to-date program/application/software.

- As a last step, copy the **`download link`** of your program/application/software in the relevant repo.

## Example for Update 0.1
```python
from Pydate import pydate

path = r"C:\Users\...\MyFolder"
raw = "https://raw.githubusercontent.com/..."
pd = pydate.PyDate(path= path, raw_link= raw)

if pd.create_version_file(0.1):
    print("Update File Created")
else:
    print("Update File Already Exists")

if pd.isUpdate:
    print("Current")
else:
    print("Not Current")
    pd.downloadLink(url="<download_link_here>",extension="<'.exe' or '.pdf' or '.py' or 'bla_bla'>")
    pd.writeNewVersion()
```
---
## Example for Update 0.2
```python
from Pydate import pydate

path = r"C:\Users\...\MyFolder"
raw = "https://raw.githubusercontent.com/..."

pd = pydate.PyDate(path= path, raw_link= raw)

if pd.create_version_file(0.1):
    print("Update File Created")
else:
    print("Update File Already Exists")

if pd.isUpdate:
    print("Current")
else:
    print("Not Current")
    pd.downloaded_name = "program.exe"
    pd.downloadLink(url="<download_link_here>")
    pd.openNewVersion()
```
- Added
  * **`downloaded_name`** is added ➥ **_property_**
  * **`openNewVersion`**  is added ➥ **_method_**

- Removed
  * **`writeNewVersion`** is removed ➥ **_method_**
## Example For Update 1.0
```python
import os
from Pydate import PyDate

path = r"C:\Users\...\MyFolder"
raw = "https://raw.githubusercontent.com/..."

pd = pydate.PyDate(path= path, raw_link= raw)

if pd.createVersionFile(0.1):
    print("Update File Created")

else:
    print("Update File Already Exists")


if pd.isUpdate:
    print("Current")
else:
    print("Not Current")
    pd.downloaded_name = "program.exe"
    pd.downloadLink(url="<download_link_here>")
    pd.saveNewVersion(open_=False)

print(pd.readNewVersion["version"])
```
- Added
  * **`readNewVersion`** is added ➥ **_property_**
  * **`saveNewVersion`** is added ➥ **_method_**
- Removed
  * **`openNewVersion`** is removed  ➥ **_method_**
---
## About the **Pydate** Class

* **`createVersionFile`** **(_method_)**: If the version file does not exist, it will create it. The resulting file is a **`json`** file. Returns **`False`** if the version file exists. Returns **`True`** if the version file does not exist. Takes **`one float argument`**

* **`get_version`** **(_property_)**: Returns version file written on github

* **`isUpdate`** **(_property_)**: Returns **`True`** if Current, **`False`** if Not Current.

* **`downloaded_name`** **(_property_)**: Value by adding an extension to the end of the name.  **_eg_**: **`pd.downloaded_name = "my_file_name.exe"`** or **_eg_**: **`pd.downloaded_name = "my_file_name.py"`**... Examples can be expanded.

* **`readNewVersion`** **(_property_)**: Returns the version of the locally created version file

* **`downloadLink`** **(_method_)**: The argument given to the PyDate class is used as the path. Creates a folder named **`Installed`**. His argument; Download link of program/file/exe available on Github.

* **`saveNewVersion`** **(_method_)**: Upgrades the version value written in the locally maintained version. json file to the version on github. Takes one parameter. Default `True`. If open_ parameter is `True`: Opens the downloaded file in the `Installed` folder and upgrades the `version.json` version. If open_ parameter is `False`: only upgrades the version of the script at the specified location


## Author
[Helmsys](https://github.com/Arif-Helmsys)

## License
[MIT](https://choosealicense.com/licenses/mit/)
