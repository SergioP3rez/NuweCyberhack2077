cd
ls
cd sysadmin
ls
./prepare_ctf.sh 
ls
cd ..
ls
cd sysadmin
ls
cat README.md 
ls
cat /etc/shadow
ls
cd ..
ls
rm -rf sysadmin*
ls
docker ps
ls
ls -la
cat .bash_history 
rm .bash_history 
ls
exit
curl --connect-timeout 2 -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" 2>/dev/null || wget --timeout 2 --tries 1 -q -O - --method PUT "http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 21600" 2>/dev/null
exit
docker ps
systemctl restart initiate-genesis.service 
docker ps
exit
