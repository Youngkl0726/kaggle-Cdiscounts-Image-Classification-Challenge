# kaggle-Cdiscounts-Image-Classification-Challenge

I trained the model in inception_resnet_v2 from scratch for about 55 epochs. The best single model get the LB 0.68.  
  
### model1  
In inception_resnet_v2_1_test.prototxt, it don't use the final BN and the output of fc7 is 256. 
It is the best single model that I submitted to test.  
### model2  
In inception_resnet_v2.prototxt, it uses the final BN and the output of fc7 is 256.  
### model3  
In inception_resnet_v2_1_512.prototxt, it don't use the final BN and the output of fc7 is 512. 
It is used for finetune the model1. 
Before the game was over, this model had been trained for 60000 iteraters, so I had to use this to test the data. 
After the game, the trained is going on and the loss has decreased. I think it should be the best single model.  
### model4  
In inception_resnet_v2_512.prototxt, it uses the final BN and the output of fc7 is 512. 
It is used for finetune the model2. 
Before the game was over, the training of this model was just done, so I didn't use this model to test.  
I ensemble four models from model1 for 400000 iteraters, model 2 for 400000 iteraters and finetuned for 80000 iteraters, 
and model3 for 60000 iterators. I chose the max prob from these 4 models' output as the answer for each picture.
  
I also tried to finetune the resnet50 and resnet101 using the pretrained imagenet model. 
However, the result is bad. I think the param I used to finetune the model was too bad.  

Of course, my training of inception_resnet_v2 had problems too. I didn't seperate the data for training and validation.
I used all the data to train the model. No data augmentation. 
The data is so big that I had use a lot of time to train the model from scratch.  
The big model may be suitable for this game.
