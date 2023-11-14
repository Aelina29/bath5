Windows
docker build -t bath-teach .
docker run -it -v "C:\Users\user\Desktop\NNforAnd\5bath\dataset:/usr/src/app/dataset" -v "C:/Users/user/Desktop/NNforAnd/5bath/results:/usr/src/app/results" bath-teach

LINUX
sudo docker build -t bath-teach .
sudo docker run -it -v $(pwd)/data:/usr/src/app/data -v $(pwd)/results:/usr/src/app/results bath-teach
