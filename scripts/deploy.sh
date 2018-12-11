#!/usr/bin/env bash

# deploy this code using rsync to a remove ssh host
# just use
#   ./deploy.sh
# to incrementally deploy
# use
#  ./deploy.sh complete
# to DELETE EVERYTHING first and then redeploy
# and use
#  ./deploy.sh delete
# to DELETE EVERYTHING on the pepper fs
#
#
# WARNING: be sure that you can connect to pepper via your own public/private key


# amber
deploy_user_host="nao@192.168.1.101"
# porter
# deploy_user_host="nao@192.168.1.102"

# relative to home directory unless preceded by a slash,
# WARNING: watch out not to delete the whole thing when using:
#   deploy.sh complete
deployment_folder="FloorGuide/deployment"

rsyncToPepper()
{
    rsync -avz --exclude-from="$d"/.gitignore --exclude .git "$d/" "$deploy_user_host:$deployment_folder/"
}

d="$(cd "$(dirname "${BASH_SOURCE[0]}")"&& cd .. && pwd)"
if [ "x${1:-}" == "xcomplete" ]; then
    echo "Deleting previous deployment:"
    ssh "$deploy_user_host" "test -n "\$HOME" && rm -rv '$deployment_folder'"
    rsyncToPepper
else
    rsyncToPepper
fi

# delete everything...
if [ "x${1:-}" == "xdelete" ]; then
    echo "Deleting deployment directory:"
    ssh "$deploy_user_host" "test -n "\$HOME" && rm -rv '$deployment_folder'"
fi