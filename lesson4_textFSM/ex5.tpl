Value DEVICE_ID (\S+)
Value LOCAL_INT (\S+)
Value CAPABILITY (\S+)
Value PORT_ID (\S+)

Start
  ^${DEVICE_ID}\s+${LOCAL_INT}\s+\d+\s+${CAPABILITY}\s+${PORT_ID}\s*$$ -> Record

EOF
