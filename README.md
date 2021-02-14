# BokiLib
Some scripts to help archive some of my doujin.

# Usage
1. mkdir data tmp
2. Build docker image with `docker build -t jwy/bokilib:0.01 .`
3. Edit `app/gunicorn.conf` as you like.
4. Run `docker run --rm -p 5000:5000 -v $PWD/app:/app -v $PWD/data:/data jwy/bokilib:0.01`

# Testing

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
