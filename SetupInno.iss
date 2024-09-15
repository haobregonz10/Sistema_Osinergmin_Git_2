[Setup]
AppName=Sistema de Registro de Centrales de Energía Eléctrica
AppVersion=1.0
DefaultDirName={pf}\Registros OSINERGMIN
DefaultGroupName=Registros OSINERGMIN
OutputBaseFilename=Instalador_Registros_OSINERGMIN
Compression=lzma
SolidCompression=yes

[Files]
Source: "build\exe.win-amd64-3.10\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Registros OSINERGMIN"; Filename: "{app}\Registros OSINERGMIN.exe"

[Run]
Filename: "{app}\Registros OSINERGMIN.exe"; Description: "{cm:LaunchProgram,Registros OSINERGMIN}"; Flags: nowait postinstall skipifsilent
