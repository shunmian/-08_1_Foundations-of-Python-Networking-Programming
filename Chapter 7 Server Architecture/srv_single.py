import zen_utils

if __name__=='__main__':
    address = zen_utils.parse_command_line("single-threaded server")
    listener = zen_utils.create_srv_socket(address)
    zen_utils.accept_connection_forever(listener)
