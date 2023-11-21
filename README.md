# Teach

LINUX
sudo docker build -f TrainDockerfile -t bath-teach .
sudo docker run -it -v $(pwd)/data:/usr/src/app/datasets/data -v $(pwd)/results:/usr/src/app/results bath-teach

<!-- WINDOWS
docker build -t bath-teach2 .
docker run -it -v "C:\Users\user\Desktop\NNforAnd\5bath\dataset:/usr/src/app/dataset" -v "C:/Users/user/Desktop/NNforAnd/5bath/results:/usr/src/app/results" bath-teach2 -->

# Validate

LINUX
sudo docker build -f ValDockerfile -t bath-val5 .
sudo docker run -it -v $(pwd)/data:/usr/src/app/datasets/data -v $(pwd)/results:/usr/src/app/results bath-val5


# Delete docker image
sudo docker images