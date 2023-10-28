docker build -t ultralytics-ubuntu .
docker run -it -v "C:\Users\user\Desktop\NNforAnd\5bath\dataset":./dataset" -v "C:/Users/user/Desktop/NNforAnd/5bath/results":"/results" ultralytics-ubuntu