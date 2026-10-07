$ErrorActionPreference = "SilentlyContinue"
Write-Host "=== Windows System Health ==="
Write-Host "Computer: $env:COMPUTERNAME"
Write-Host "User: $env:USERNAME"
$os = Get-CimInstance Win32_OperatingSystem
Write-Host ("OS: {0} {1}" -f $os.Caption, $os.Version)
Write-Host ("Last boot: {0}" -f $os.LastBootUpTime)
Write-Host "
Disk:"
Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" |
  Select-Object DeviceID,
    @{N="SizeGB";E={[math]::Round($_.Size/1GB,2)}},
    @{N="FreeGB";E={[math]::Round($_.FreeSpace/1GB,2)}}
$total = [math]::Round($os.TotalVisibleMemorySize/1MB,2)
$free = [math]::Round($os.FreePhysicalMemory/1MB,2)
Write-Host "
Memory: $free GB free / $total GB total"
Write-Host "
Key services:"
"Winmgmt","EventLog","Dnscache" | ForEach-Object {
  Get-Service $_ | Select-Object Name, Status, StartType
}
