#definicion de variables
Value INT_NAME (\S+)
Value LINE_STATUS (up|down)
Value ADMIN_STATUS (up|down)
Value MAC_ADDRESS (\S+)
Value MTU (\d+)
Value DUPLEX (\S+duplex)
Value SPEED (\d+)

Start
  ^${INT_NAME}\s+is\s+${LINE_STATUS}\s*$$
  ^admin state is\s+${ADMIN_STATUS}.*$$
  ^\s+.*address:\s+${MAC_ADDRESS}.*$$
  ^\s+MTU\s+${MTU}\s+.*$$
  ^\s+${DUPLEX},\s+${SPEED}.*$$ -> Record

EOF
