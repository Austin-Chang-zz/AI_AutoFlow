@echo off
chcp 65001 >nul
echo ========================================
echo    Augment Code 項目管理系統
echo ========================================
echo.

:menu
echo 請選擇操作:
echo 1. 創建新項目
echo 2. 列出所有項目  
echo 3. 切換項目
echo 4. 保存當前工作
echo 5. 查看項目狀態
echo 6. 查看版本歷史
echo 7. 退出
echo.
set /p choice=請輸入選項 (1-7): 

if "%choice%"=="1" goto create_project
if "%choice%"=="2" goto list_projects
if "%choice%"=="3" goto switch_project
if "%choice%"=="4" goto save_work
if "%choice%"=="5" goto show_status
if "%choice%"=="6" goto show_versions
if "%choice%"=="7" goto exit
goto menu

:create_project
echo.
echo 項目類型:
echo 1. website - 網站開發
echo 2. n8n - n8n工作流程
echo 3. novel - 小說寫作
echo.
set /p project_type_num=請選擇項目類型 (1-3): 

if "%project_type_num%"=="1" set project_type=website
if "%project_type_num%"=="2" set project_type=n8n
if "%project_type_num%"=="3" set project_type=novel

set /p project_name=請輸入項目名稱: 
python project_manager.py init %project_name% %project_type%
echo.
pause
goto menu

:list_projects
echo.
python project_manager.py list
echo.
pause
goto menu

:switch_project
echo.
python project_manager.py list
echo.
set /p project_name=請輸入要切換的項目名稱: 
set /p version=請輸入版本號 (留空使用最新版本): 
if "%version%"=="" (
    python project_manager.py switch %project_name%
) else (
    python project_manager.py switch %project_name% %version%
)
echo.
pause
goto menu

:save_work
echo.
python project_manager.py status
echo.
set /p project_name=請輸入要保存的項目名稱: 
set /p description=請輸入版本描述 (可選): 
python project_manager.py save %project_name% "%description%"
echo.
pause
goto menu

:show_status
echo.
python project_manager.py status
echo.
pause
goto menu

:show_versions
echo.
set /p project_name=請輸入項目名稱: 
python project_manager.py versions %project_name%
echo.
pause
goto menu

:exit
echo 再見！
exit /b 0
