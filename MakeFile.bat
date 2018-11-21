@echo off
:: Make File for Windows User, it copy all config values from the make_env
:: Currently it supports two params: "build" or "dev" i.e. .\MakeFile build
set arg1=%1
for /f "delims=" %%x in (make.env) do (set "%%x")
IF /I "%arg1%" EQU "build" (
  docker build --no-cache=true -t %DOCKER_NAMESPACE%/%DOCKER_REPOSITORY%:%DOCKER_IMAGE_VERSION% .
) ELSE IF /I "%arg1%" EQU "dev" (
  docker run --rm --name ez-lft -i -t -p 80:80 -v "%cd%/:/ez-lft" -e ORIGIN=http://localhost:80 kk/ez-lft:latest /bin/bash -c "python diagnose.py"
) ELSE IF /I "%arg1%" EQU "shell" (
  docker run --rm --name ez-lft -i -t -p 80:80 -v "%cd%/:/ez-lft" -e ORIGIN=http://localhost:80 kk/ez-lft:latest /bin/bash
) ELSE (
  ECHO No command found: build / dev
)
