@echo off
setlocal enabledelayedexpansion

echo ================================
echo  🚀 Iniciando la aplicación...
echo ================================

:: Verificar que Docker esté corriendo
docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker no está corriendo. Por favor, abre Docker Desktop y vuelve a intentarlo.
    pause
    exit /b
)

:: Construir y ejecutar el contenedor
docker-compose up --build

echo ================================
echo  ✅ Contenedor ejecutándose correctamente.
echo  Puedes acceder a la aplicación en http://localhost:5000
echo ================================
pause
