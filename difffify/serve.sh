HEAD='GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n'

ncat -l 192.168.1.81 3000 -k -c 'echo ${HEAD} \r\n $(cat getFilenames.json)'
