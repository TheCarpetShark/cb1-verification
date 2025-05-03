# Define the CB1 IP address and login credentials
$cb1_ip = "192.168.1.216"
$username = "root"

# Prompt user to enter password (optional)
$password = Read-Host "Enter CB1 root password (Just press Enter if using SSH keys)"

# Define the command to run after login
$remoteCommand = "uptime; df -h; free -h"

# Use ssh.exe to connect and run the command
$sshCommand = "ssh $username@$cb1_ip '$remoteCommand'"

# Execute the ssh command
Invoke-Expression $sshCommand
