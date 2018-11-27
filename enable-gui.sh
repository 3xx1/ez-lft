isQuartzRunning=$(ps -A | grep XQuartz | grep -v grep)
if [ ${#isQuartzRunning} -lt 1 ]
then
  # Export IP
  export IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
  open -a XQuartz
  xhost + $IP
fi
