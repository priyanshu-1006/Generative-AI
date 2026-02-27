# Activate the project's virtual environment and start Jupyter Lab
$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    . $venvActivate
} else {
    Write-Error "Virtual environment not found at $venvActivate. Run: python -m venv .venv"
    exit 1
}
# Start Jupyter Lab (change to `jupyter notebook` if preferred)
jupyter lab