@echo off
REM AI Medical Voicebot - Startup Script
color 0A
cls
echo.
echo ============================================================
echo   🏥 AI Medical Voicebot
echo ============================================================
echo.
echo   Starting the application...
echo.

cd /d "C:\Pradeep Kumar\Deploy Projects\Deploy AI Agent Medical"
pipenv run python Gradio_App.py

echo.
echo   Application stopped.
pause
