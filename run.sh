#!/bin/bash
# Original author of the script : powen
# Edited some bits : maxasix

# Check source and permission
cd "$(dirname "$0")" || exit
echo "Checking source"
if [[ ! -e "AltStore.ipa" ]]; then
    curl -L https://cdn.altstore.io/file/altstore/apps/altstore/1_5.ipa > AltStore.ipa
fi
if [[ ! -e "main" ]]; then
    wget https://github.com/powenn/AltServer-Linux-ShellScript/raw/main/main
fi
if [[ ! -e "ipa" ]]; then
    mkdir ipa
fi
if [[ ! -e "saved.txt" ]]; then
    touch saved.txt
fi
if [[ "stat main | grep -- '-rw-r--r--'" != "" ]] ; then
    chmod +x main
fi
if [[ "stat AltServer | grep -- '-rw-r--r--'" != "" ]] ; then
    chmod +x AltServer
fi

# Version
LocalVersion=$(sed -n 1p version)
LatestVersion=$(curl -Lsk 'https://github.com/maxasix/AltShell/raw/main/version')


# Help message
HELP() {
cat << EOF
    
#####################################
#     Welcome to the AltShell       #
#####################################

ScriptUsage: [OPTION]

OPTIONS

  i, --Install AltStore or ipa files
    Install AltStore or ipa files to your device
  d, --Restart Daemon mode
    Restart Daemon mode to refresh apps or AltStore
  e, --Exit
    Exit script
  h, --Help
    Show this message
  p, --Pair
    Pair device
  u, --Update
    Update this script or AltServer

For more information: https://github.com/maxasix/AltShell

EOF
}

# Print AltServer icon
AltServerIcon() {
    printf "\e[49m       \e[38;5;73;49m▄▄\e[38;5;66;49m▄\e[38;5;66;48;5;73m▄▄▄▄▄▄▄▄\e[38;5;66;49m▄\e[38;5;73;49m▄▄\e[49m       \e[m
\e[49m     \e[38;5;73;49m▄\e[38;5;66;48;5;73m▄\e[38;5;66;48;5;66m▄▄▄▄▄▄\e[38;5;67;48;5;66m▄▄\e[38;5;66;48;5;66m▄▄▄▄▄▄\e[38;5;66;48;5;73m▄\e[38;5;73;49m▄\e[49m     \e[m
\e[49m   \e[38;5;73;49m▄\e[38;5;30;48;5;73m▄\e[38;5;30;48;5;30m▄▄▄▄▄▄\e[38;5;109;48;5;73m▄\e[38;5;109;48;5;109m▄▄▄▄\e[38;5;109;48;5;73m▄\e[38;5;30;48;5;30m▄▄▄▄▄▄\e[38;5;30;48;5;73m▄\e[38;5;73;49m▄\e[49m   \e[m
\e[49m \e[38;5;73;49m▄\e[38;5;30;48;5;73m▄\e[38;5;30;48;5;30m▄▄▄▄▄▄\e[38;5;73;48;5;30m▄\e[38;5;73;48;5;73m▄▄▄▄▄▄▄▄\e[38;5;73;48;5;30m▄\e[38;5;30;48;5;30m▄▄▄▄▄▄\e[38;5;30;48;5;73m▄\e[38;5;73;49m▄\e[49m \e[m
\e[49m \e[38;5;30;48;5;73m▄\e[38;5;30;48;5;30m▄▄▄▄▄\e[38;5;73;48;5;30m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;15;48;5;73m▄\e[38;5;15;48;5;15m▄▄\e[38;5;15;48;5;73m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;73;48;5;30m▄\e[38;5;30;48;5;30m▄▄▄▄▄\e[38;5;30;48;5;73m▄\e[49m \e[m
\e[38;5;73;48;5;73m▄\e[38;5;30;48;5;30m▄▄▄\e[38;5;73;48;5;30m▄▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;15;48;5;73m▄\e[38;5;15;48;5;15m▄\e[48;5;15m    \e[38;5;15;48;5;15m▄\e[38;5;15;48;5;73m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;73;48;5;30m▄▄\e[38;5;30;48;5;30m▄▄▄\e[38;5;73;48;5;73m▄\e[m
\e[38;5;73;48;5;73m▄\e[38;5;30;48;5;30m▄▄\e[38;5;66;48;5;30m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;15;48;5;73m▄\e[48;5;15m          \e[38;5;15;48;5;73m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;66;48;5;30m▄\e[38;5;30;48;5;30m▄▄\e[38;5;73;48;5;73m▄\e[m
\e[38;5;73;48;5;73m▄\e[38;5;30;48;5;30m▄▄\e[38;5;30;48;5;66m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;73;48;5;15m▄\e[48;5;15m          \e[38;5;73;48;5;15m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;30;48;5;66m▄\e[38;5;30;48;5;30m▄▄\e[38;5;73;48;5;73m▄\e[m
\e[38;5;73;48;5;73m▄\e[38;5;6;48;5;6m▄▄▄\e[38;5;6;48;5;66m▄\e[38;5;6;48;5;73m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;73;48;5;15m▄\e[38;5;15;48;5;15m▄\e[48;5;15m    \e[38;5;15;48;5;15m▄\e[38;5;73;48;5;15m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;6;48;5;73m▄\e[38;5;6;48;5;72m▄\e[38;5;6;48;5;6m▄▄▄\e[38;5;73;48;5;73m▄\e[m
\e[49m \e[38;5;73;48;5;6m▄\e[38;5;6;48;5;6m▄▄▄▄▄\e[38;5;6;48;5;73m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;73;48;5;15m▄\e[38;5;15;48;5;15m▄▄\e[38;5;73;48;5;15m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;6;48;5;73m▄\e[38;5;6;48;5;6m▄▄▄▄▄\e[38;5;73;48;5;6m▄\e[49m \e[m
\e[49m \e[49;38;5;66m▀\e[38;5;67;48;5;6m▄\e[38;5;6;48;5;6m▄▄▄▄▄▄\e[38;5;6;48;5;73m▄\e[38;5;73;48;5;73m▄▄▄▄▄▄▄▄\e[38;5;6;48;5;73m▄\e[38;5;6;48;5;6m▄▄▄▄▄▄\e[38;5;67;48;5;6m▄\e[49;38;5;66m▀\e[49m \e[m
\e[49m   \e[49;38;5;67m▀\e[38;5;66;48;5;6m▄\e[38;5;6;48;5;6m▄▄▄▄▄▄\e[38;5;66;48;5;73m▄\e[38;5;73;48;5;73m▄▄▄▄\e[38;5;66;48;5;73m▄\e[38;5;6;48;5;6m▄▄▄▄▄▄\e[38;5;66;48;5;6m▄\e[49;38;5;67m▀\e[49m   \e[m
\e[49m     \e[49;38;5;66m▀\e[38;5;66;48;5;6m▄\e[38;5;6;48;5;6m▄▄▄▄▄▄\e[38;5;6;48;5;30m▄▄\e[38;5;6;48;5;6m▄▄▄▄▄▄\e[38;5;66;48;5;6m▄\e[49;38;5;66m▀\e[49m     \e[m
\e[49m       \e[49;38;5;66m▀▀\e[49;38;5;6m▀\e[38;5;66;48;5;6m▄▄▄▄▄▄▄▄\e[49;38;5;6m▀\e[49;38;5;66m▀▀\e[49m       \e[m
";
}

# Show update avaliable message
UpdateNotification() {
if [[ $LatestVersion > $LocalVersion ]] ; then
cat << EOF

-------<< UPDATE AVALIABLE >>-------

EOF
fi
}

# Start script
AltServerIcon
HELP
UpdateNotification

./AltServer &> /dev/null &

RunScript=0
while [ $RunScript = 0 ] ; do
    echo "Enter an option to continue. For a list of options, type h or --Help"
    read option
    case "$option" in
    
  i|--Install-AltStore-or-ipa-files )
    ./main
    ;;
  d|--Restart-Daemon-mode )
    killall AltServer
    for job in `jobs -p`
    do
    wait $job
    done

    ./AltServer &> /dev/null &
    ;;
  e|--Exit )
    killall AltServer
    exit
    ;;
  h|--Help )
    AltServerIcon
    HELP
    UpdateNotification
    ;;
  p|--Pair )
    idevicepair pair
    ;;
  u|--Update )
    curl -Lsk 'https://github.com/maxasix/AltShell/raw/main/update.sh' | bash
    ;;
    esac

done

