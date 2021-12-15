# Segmentation_GUI

### 사용자 중심의 비디오 인터랙션을 위한 시공간 메모리네트워크 기반 비디오 객체 분할 및 불확실성 분석 
 KSC2021 / Minkuk Kim, Yulim Kim, Seong Tae Kim

 
### Capstone_team7

Team Repository for implementing GUI program of video segmentation in Capstone Design class



**This project is..**
------------
<img width="616" alt="a1" src="https://user-images.githubusercontent.com/32739719/146261231-f8c4c96b-45b1-490f-87be-5c86ee5ab373.png">


In this study, based on Video Object Segmentation technology based on Space-Time Memory Networks (STM) model, the purpose of this study is to create a GUI program that allows users to edit video in real time and interact with the computer. On gui program, You can put in your videos and mask the object what you want. Of course you can virtualize the segmentation result and the Uncertainty of segmentation result. The uncertainty provides information to you which frame's segmentation is uncertain.


**Python GUI**
------------
![a2](https://user-images.githubusercontent.com/32739719/146261362-5b33b2d6-5f81-4bfc-a8a8-1d1c2773dde9.png)


GUI was configured using Tkinter, video playback is possible on Python using Opencv, and Python image library (PIL) was used to bring various image file formats from Python.
In addition, Matplot has been implemented to bring up images that do not meet the uncertainty standard in the uncertainty part.

**Model**
------------
This model is based on pretrained Space-time Memory Network. STM is Semi-supervised learning-based video object segmentation model. We implemented additional codes that about Uncertainty on STM. So you can execute this project codes through STM's recommendation setting. You can access STM's setting and pretrained model below. 

https://github.com/seoungwugoh/STM


**Requirement**
------------
*GUI Program*
- Pip install tkinter
- Pip install opencv-python
- Pip install image
- Pip install pillow
- Pip install matplotlib

*Model(STM based)*
- python 3.6
- pytorch 1.0.1.post2
- numpy, opencv, pillow



**Advisor**
------------
**SeongTae Kim**<br/>-Assistant Professor, Department of Computer Science and Engineering & Department of Artificial Intelligence, College of Software, Kyung Hee University<br/>http://ailab.khu.ac.kr/


**Team members** 
------------
**Yulim Kim**<br/>-Department of computer engineering, Undergraduate, Kyung Hee University<br/>https://github.com/yeaygit

**Minkuk Kim**<br/>-Department of computer engineering, Undergraduate, Kyung Hee University<br/>https://github.com/Geppa
