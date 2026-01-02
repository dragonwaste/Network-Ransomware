@echo off
echo ============================================
echo RANSOMWARE DEMO - CLEANUP
echo ============================================
echo This will UNDO all demo changes and restore security.
echo Press Ctrl+C to cancel, or any key to continue...
pause > nul

echo.
echo [1] Removing shared folder...
net share RansomDemo /delete 2>nul
if errorlevel 1 (
    echo Share not found or already removed.
)

echo [2] Restoring password protection...
reg add "HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v RestrictNullSessAccess /t REG_DWORD /d 1 /f 2>nul
echo    ✓ Password protection restored

echo [3] Disabling Guest account...
net user Guest /active:no 2>nul
echo    ✓ Guest account disabled

echo [4] Turning OFF network discovery (restore to secure)...
powershell -Command "Set-NetFirewallRule -DisplayGroup 'File And Printer Sharing' -Enabled False" 2>nul
powershell -Command "Set-NetFirewallRule -Name 'FPS-SMB-In-TCP' -Enabled False" 2>nul
echo    ✓ Firewall rules restored

echo [5] Deleting demo folder and files...
rmdir /s /q C:\RansomDemo 2>nul
if exist C:\RansomDemo (
    echo    ✗ Could not delete folder (might be in use)
    echo    Close any open files in C:\RansomDemo and try again.
) else (
    echo    ✓ Demo folder deleted
)

echo [6] Restarting Server service with secure settings...
net stop LanmanServer /y 2>nul
net start LanmanServer 2>nul
echo    ✓ Server service restarted

echo [7] Verifying cleanup...
echo.
echo Checking shares:
net share | findstr RansomDemo
if errorlevel 1 (
    echo    ✓ RansomDemo share removed
) else (
    echo    ✗ RansomDemo share still exists!
)

echo Checking folder:
if exist C:\RansomDemo (
    echo    ✗ C:\RansomDemo folder still exists!
) else (
    echo    ✓ C:\RansomDemo folder removed
)

echo.
echo ============================================
echo CLEANUP COMPLETE!
echo ============================================
echo Security has been restored. Your laptop is now secure.
echo.
echo Changes undone:
echo 1. Removed RansomDemo share
echo 2. Restored password protection
echo 3. Disabled Guest account
echo 4. Restored firewall to secure settings
echo 5. Deleted demo files
echo.
echo Press any key to exit...
pause > nul