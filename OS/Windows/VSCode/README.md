# VSCode on windows

Using VSCode with costmized usr/ext folder

## put files at PATH
* launch_vscode.vbs
  * example: 
  * <div class="load_as_code_session" data-url="launch_vscode.vbs">Loading content...</div>
* vscode.bat
  * example: 
  * <div class="load_as_code_session" data-url="vscode.bat">Loading content...</div>


## Regedit
* folder: 電腦\HKEY_CLASSES_ROOT\Directory\shell\VSCode\command
* key:
  * name:
    * (default)
  * data:
    * cmd /c "wscript.exe "C:\<path-to-it>\launch_vscode.vbs" "%V""



<script src="{{ '/assets/js/LoadAsCodeSession.js' | relative_url }}"></script>