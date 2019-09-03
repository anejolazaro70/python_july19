Value MAC_ADDRESS (\S+)
Value IP_ADDRESS (\S+)
Value NAME (\S+)
Value INTERFACE (\S+)

Start
  ^MAC.*Flags\s*$$ -> ARP_Table

ARP_Table
  ^${MAC_ADDRESS}\s+${IP_ADDRESS}\s+${NAME}\s+${INTERFACE}\s+.*$$ -> Record

EOF
