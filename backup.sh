IMAGENAME="marufeuille/backup"
VOLUMES=$(docker volume ls -q | grep -e "^jupyterhub-")
for v in ${VOLUMES} ; do
    echo "backup ${v}"
    user=$(echo ${v} | sed -e "s/jupyterhub-user-//")
    docker run --env-file envfile.txt -e OSS_FILEPREFIX=${user} -v ${v}:/data ${IMAGENAME}
done
