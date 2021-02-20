# BokiLib
Some scripts to help archive some of my doujin.

# Usage
1. mkdir data tmp
2. Build docker image with `docker build -t jwy/bokilib:0.01 .`
3. Edit `app/gunicorn.conf` as you like.
4. Run `docker run --rm -p 5000:5000 -v $PWD/app:/app -v $PWD/data:/data jwy/bokilib:0.01`
5. Run `source client/set_alias.sh` for shell integration of `bokinfo`, `bokiupl` and `bokidl`.


# Testing

```shell

[tpe@manjaro-home BokiLib]$ git pull && source client/set_alias.sh


[tpe@manjaro-home BokiLib]$ bokiupl README.md
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1541  100    43  100  1498   4300   146k --:--:-- --:--:-- --:--:--  150k
-bash: [: "71d5b00006f7fd965d00824146057a02373d77b4": integer expression expected
71d5b00006f7fd965d00824146057a02373d77b4|README.md|1297


[tpe@manjaro-home BokiLib]$ bokinfo READ
{"hash": "READ", "size": "Invalid hash.", "date": "Invalid hash."}
71d5b00006f7fd965d00824146057a02373d77b4|README.md|1297


[tpe@manjaro-home BokiLib]$ bokinfo README
{"hash": "README", "size": "Invalid hash.", "date": "Invalid hash."}
71d5b00006f7fd965d00824146057a02373d77b4|README.md|1297


[tpe@manjaro-home BokiLib]$ bokinfo 71d5b00006f7fd965d00824146057a02373d77b4
{"hash": "71d5b00006f7fd965d00824146057a02373d77b4", "size": 1297, "date": 1613303797}
71d5b00006f7fd965d00824146057a02373d77b4|README.md|1297


[tpe@manjaro-home BokiLib]$ bokidl 71d5b00006f7fd965d00824146057a02373d77b4 README.b
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1297    0  1297    0     0   316k      0 --:--:-- --:--:-- --:--:--  316k
71d5b00006f7fd965d00824146057a02373d77b4|README.b|1297
71d5b00006f7fd965d00824146057a02373d77b4|README.md|1297


[tpe@manjaro-home BokiLib]$ diff README.*
[tpe@manjaro-home BokiLib]$




```

```shell

jwyjohn@JwyJohndeAir ~ % curl -X POST -H "Content-Type: multipart/form-data" -F "file=@"/Users/jwyjohn/Downloads/3-参数点估计（2）.pdf ""  http://192.168.1.43:5000/u
curl: (3) URL using bad/illegal format or missing URL
"f49dd60922a52f0136f60c21a38ff43fbb08dd87"


jwyjohn@JwyJohndeAir ~ % curl http://192.168.1.43:5000/i/f49dd60922a52f0136f60c21a38ff43fbb08dd87
{"hash": "f49dd60922a52f0136f60c21a38ff43fbb08dd87", "size": 428182, "date": 1613285477}


jwyjohn@JwyJohndeAir ~ % wc -c /Users/jwyjohn/Downloads/3-参数点估计（2）.pdf
  428182 /Users/jwyjohn/Downloads/3-参数点估计（2）.pdf


jwyjohn@JwyJohndeAir ~ % curl http://192.168.1.43:5000/f49dd60922a52f0136f60c21a38ff43fbb08dd87 > Desktop/Test.pdf
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  418k    0  418k    0     0  3167k      0 --:--:-- --:--:-- --:--:-- 3167k

jwyjohn@JwyJohndeAir ~ %

```

testing git conf on apple m1
