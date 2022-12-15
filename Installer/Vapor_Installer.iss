; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppId={{B4F07DEF-0806-4124-8FE6-76DCA3FF2C7E}}
AppName=Vapor
AppVersion=1.0.0
AppCopyright=Enten Gang
AppPublisher=Enten Gang
WizardStyle=modern
DefaultDirName={autopf}\Vapor
DefaultGroupName=Vapor
UninstallDisplayIcon={app}\Vapor.exe
Compression=lzma2
SolidCompression=yes
OutputDir= "Installer"

DisableWelcomePage=no
LicenseFile=license.txt
DisableDirPage=no
DisableProgramGroupPage=no

[Files]
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "CookieClicker\*"; DestDir: "{app}\CookieClicker"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "images\*"; DestDir: "{app}\images"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "venv\*"; DestDir: "{app}\venv"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "Font\*"; DestDir: "{app}\Font"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "python3.dll"; DestDir: "{app}"
Source: "python310.dll"; DestDir: "{app}"
Source: "MyProg.exe"; DestDir: "{app}"; DestName: "Vapor.exe"
Source: "Readme.txt"; DestDir: "{app}"; Flags: isreadme
Source: "License.txt"; DestDir: "{app}"

[Icons]
Name: "{group}\Vapor"; Filename: "{app}\Vapor.exe"

[Languages]
Name: de; MessagesFile: "compiler:Languages\German.isl"