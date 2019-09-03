#definicion de variables
Value PORT_NAME ([a-zA-Z]+\S+)

#inicio fichero FSM
Start
  ^${PORT_NAME}\s+ -> Record

EOF
