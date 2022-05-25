# Pydater
EN:

When you make a program associated with Github, you can easily update with this module without the need to write an update system.

Specify the path, write a version and leave the rest to the module

TR:

Github ile ilişikli bir program yaptığınızda güncelleme sistemi yazmanıza gerek kalmadan bu modül ile rahatça güncelleme yapabilirsiniz.

Yol belirtin, bir versiyon yazın sonrasını modüle bırakın

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pydater.

```bash
pip install pydater
```

## Usage
EN:

• First of all, you should save your current version number from github.

• Create a repository for this or use an existing one.

• Create a ".json" file named "version.json" in the repo.

• Its content must be { "version" : "<version_number>"}.

• After doing this and saving, copy the `raw link` of the `version.json` file

• Come back to the relevant repo and import your most up-to-date program/application/software.

• As a last step, copy the `download link` of your program/application/software in the relevant repo.

TR:

• Öncelikle github'dan güncel versiyon numaranızı saklamalısınız.

• Bunun için repository oluşturun veya var olanı kullanın.

• Reponun içerisine `version.json` adında bir `.json` dosyası oluşturun.

• İçeriği `{ "version" : "<versiyon_numarası>"}` olmalı.

• Bu işlemi yapıp kaydettikten sonra `version.json` dosyasına ait `raw linkini` kopyalayın

• Tekrar ilgili repoya gelip en güncel tuttuğunuz programınızı/uygulamanızı/yazılımınızı içeriye aktarın.

• Son işlem olarak ilgili repodaki programınızın/uygulamanızın/yazılımınızın indirme linkini kopyalayın
## Example
```python
from Pydate import pydate

pd = pydate.PyDate("<folder_here>","<raw_link_here>")

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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
