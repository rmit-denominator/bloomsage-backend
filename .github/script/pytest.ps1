#!/bin/pwsh

if (Get-Command pytest -ErrorAction SilentlyContinue) {
    Write-Host "Running tests..."
    pytest --version
    pytest
}
else {
    Write-Host "pytest is not installed"
    Write-Host "installing pytest"
    pip install pytest
    pytest --version
    pytest
}