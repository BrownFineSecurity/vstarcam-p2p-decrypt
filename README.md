# vstarcam-p2p-decrypt

The VStarcam CB73 security camera P2P protocol using for mobile app communications is vulnerable to the following attacks:
- simple replay attack of captured UDP data
- chosen ciphertext analysis via UART logs
- complete

## generate-byte-seeds.py

Run this script first to generate the byte seed database

## decrypt.py

Takes hexstring of encrypted P2P bytes 

Usage:
```
decrypt.py <hexstring>
```
