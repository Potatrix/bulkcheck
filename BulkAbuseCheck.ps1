# Check individual IP
# https://www.abuseipdb.com/check/[IP]/json?key=[API_KEY]&days=[DAYS]

# Check CIDR
# https://www.abuseipdb.com/check-block/json?network=[CIDR]&key=[API_KEY]&days=[DAYS]

function getCSVPath {
    $csvPath = Read-Host -Prompt "CSV File Path"
    return $csvPath
}

function grabIPs($csvPath) {
    # Grab IPs
    $IPs = import-csv C:\Users\Karl\Documents\ips.csv -Header "IP"   
    return $IPs 
}

function grabAPIKey {
    $APIKeyPath = ".\APIKey.txt"
    # $APIKeyPath = read-host -prompt "API Key Path"

    $APIKey = Get-Content -Path $APIKeyPath
    return $APIKey
}

$csvPath = getCSVPath

$APIKey = grabAPIKey


ForEach ($IP in $IPs) {
    $json = Invoke-WebRequest -Uri "https://www.abuseipdb.com/check/$IP/json?key=$APIKey&days=30" -ContentType "application/json" -Method Get
}
Write-Host($json)