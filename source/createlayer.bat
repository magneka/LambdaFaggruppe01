cd ./dockerlayer
docker run -v ${pwd}:/var/task "amazon/aws-sam-cli-build-image-python3.8" /bin/sh -c "pip install -r requirements.txt -t layerfiles/python; exit"
cd ./layerfiles
c:\util\GnuWin32\bin\zip.exe -r ../layer.zip .