while read -r line 
do 
  urlstatus=$(curl -s -I -L https://$line | grep Alt-Svc)
  echo "$line,$urlstatus" >> AltSvc_support_quic_https.txt
done< "$1"
