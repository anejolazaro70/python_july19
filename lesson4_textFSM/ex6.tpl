Value Filldown ROUTER_ID (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value Filldown LOCAL_AS (\d+)
Value NEIGHBOR (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value REMOTE_AS (\d+)
Value UP_DOWN (\S+)
Value STATE_PREF_RECVD (\S+)

Start
  ^BGP router identifier ${ROUTER_ID}, local AS number ${LOCAL_AS}\s*$$
  ^${NEIGHBOR}\s+\d+\s+${REMOTE_AS}\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+${UP_DOWN}\s+${STATE_PREF_RECVD}.*$$ -> Record

EOF
