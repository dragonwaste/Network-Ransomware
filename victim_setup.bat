@echo off
echo ============================================
echo RANSOMWARE DEMO - VICTIM SETUP
echo ============================================
echo This will configure Windows for the demo.
echo Press Ctrl+C to cancel, or any key to continue...
pause > nul

echo.
echo [1] Creating demo folder...
mkdir C:\RansomDemo 2>nul
echo This is a test file for ransomware demo. > C:\RansomDemo\test1.txt
echo Important document content here. > C:\RansomDemo\document.docx
echo Financial data for demo. > C:\RansomDemo\bank.pdf

echo [2] Sharing folder with Everyone...
net share RansomDemo=C:\RansomDemo /GRANT:Everyone,FULL

echo [3] Turning on network discovery...
powershell -Command "Set-NetFirewallRule -DisplayGroup 'File And Printer Sharing' -Enabled True"
powershell -Command "Set-NetFirewallRule -Name 'FPS-SMB-In-TCP' -Enabled True"

echo [4] Disabling password protection (temporarily)...
reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v RestrictNullSessAccess /t REG_DWORD /d 0 /f
net user Guest /active:yes 2>nul

echo [5] Getting network info...
ipconfig | findstr IPv4
echo.
echo Share path: \\%COMPUTERNAME%\RansomDemo
echo.
echo [6] Restarting Server service...
net stop LanmanServer /y
net start LanmanServer

echo ============================================
echo SETUP COMPLETE!
echo ============================================
echo Share this info with attacker:
echo 1. Computer Name: %COMPUTERNAME%
echo 2. IP Address: (see above)
echo 3. Share Name: RansomDemo
echo.
echo Press any key to exit...
pause > nul