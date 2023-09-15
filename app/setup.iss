[Setup]
AppName=File Name Saver
AppVersion=1.0
DefaultDirName={pf}\File Name Saver
OutputDir=userdocs:Inno Setup\Output
OutputBaseFilename=file_name_saver_setup
Compression=lzma2/ultra
SolidCompression=yes

[Files]
Source: "file_name_saver.exe"; DestDir: "{app}"
Source: "test_folder\*"; DestDir: "{app}\test_folder"

[Icons]
Name: "{group}\File Name Saver"; Filename: "{app}\file_name_saver.exe"
