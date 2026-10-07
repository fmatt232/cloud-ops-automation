# Project 5 — IT & Cloud Operations Automation Toolkit

A practical Python and PowerShell toolkit for support and cloud-operations work: log analysis and Windows system diagnostics.

## Skills demonstrated
Python • PowerShell • Troubleshooting • Log Analysis • Automation • IT Support • Operations

## Python log analyzer
```bash
python scripts/log_analyzer.py sample.log
```
Summarizes DEBUG, INFO, WARNING, ERROR, and CRITICAL events locally.

## PowerShell health check
```powershell
./scripts/system-health.ps1
```
Reports Windows host, OS, disk, memory, and key service status.

## Safety
Scripts are read-only by default, contain no credentials, and make no administrative configuration changes.
