#!/usr/bin/env bash
#
EXEC_NAME=${0##*/}
EXEC_TITLE="This script is used for work with Pepper."

# -----------------------------------------------------------------------
#  f_usage
# -----------------------------------------------------------------------
f_usage() {
    cat <<-END_OF_INPUT >&2

        Usage: $EXEC_NAME [-H -D] \\
                           -m  <mode> \\
                           -p  <NameFromPepper>

        Desc : $EXEC_TITLE

               Options:
               -H  show this help
               -D  debug (set -x)
               -m  mode
               -p  peppername
END_OF_INPUT
    exit $1
}

# -----------------------------------------------------------------------
#  read input
# -----------------------------------------------------------------------
while getopts m:p:H:D option
do
    case "${option}" in
        m)   _mode="${OPTARG}";;
        p)   pepper="${OPTARG}";;
        H)   f_usage 0;;
        D)   set -x;;
        \?)  echo "Bad option. (-H for usage)"
             f_usage 9;;
    esac
done
shift $(expr $OPTIND - 1)

# -----------------------------------------------------------------------
#  Skript name
# -----------------------------------------------------------------------
_scriptName=${0}

# -----------------------------------------------------------------------
#  print
# -----------------------------------------------------------------------
echo "INFO: Modus = $_mode"

# -----------------------------------------------------------------------
#  disableAutonomousLife
# -----------------------------------------------------------------------
disableAutonomousLife ()
{
    #--------------------------------------------------------------------
    #  Plausis pepper. 
    #--------------------------------------------------------------------
    # Check if empty
    if [ -z "${pepper}" ] 
    then
        echo "ERROR: parameter -p <peppername> is empty. Please give me a peppername."
        exit 2
    fi

    if [ "${pepper}" == "amber" ]
    then
        echo "INFO: work with amber"
        nao_ip="192.168.1.101"
    fi

    if [ "${pepper}" == "porter" ]
    then
        echo "INFO: work with porter"
        nao_ip="192.168.1.102"
    fi




# ssh nao@$NAO_IP, then:

# $ nao stop
# $ naoqi-bin --disable-life

# # different cmdline - wake pepper up
# ssh nao@$NAO_OIP, then:

# $ qicli call ALMotion.wakeUp





# putty verbinden
# 192.168.1.101 Amber
# 192.168.1.102 Porter

# username: nao
# PW: i1-p2e3p (Amber) i2-p2e3p (Porter)

# nao stop
# naoqi-bin --disable-life

# Fenster offen halten
# dann separates Putty ffnen

# qicli call ALMotion.wakeUp



}



# --------------------------------
#  Run Programm in selected Mode
# --------------------------------
case $_mode in
            disableAutonomousLife)
      echo "*********************************************************"
      echo "********  START: disableAutonomousLife"
      echo "*********************************************************"
                      disableAutonomousLife
      echo "*********************************************************"
      echo "********  END: disableAutonomousLife"
      echo "*********************************************************"
      ;;
    *)
      exit 1
    ;;
esac