# Srt File Generator

## Introduction

this project has a simple idea , this project helps users to create srt (SubRip File Format) easily

## Project Describtion

this project has been designed by **PyQt5** and **QtDesigner** for Ui (User Interface)


## What Is Srt File Format ?

* definitly you have watched movies that has Subtitle , Subtitles follow srt file structure 
* following text is simple srt file format

``` 
    1
    00:00:10 --> 00:00:20
    Hello World

    2
    00:00:21 --> 00:00:31
    This is Simple Subtitle

```

above text is peace of srt file , if you watch above text you probably undrestand what is happening !

* at the first line of above text we see number that is item number , 
* second line is most important part of srt files , second line has two period of time , left time is start time , and right time is end time , it means how much time should i show third line text 
* this is text will showing between start time and end time at line 2

## How to Run Project ?

running this project is simple , you just need to create virtual environment (env) then install 
requirements.txt packages

1 - ``` python3 -m venv env ``` <br/>
2 - ``` cd env/Scripts/ ``` <br />
3 - ``` source activate or activate.exe ``` <br />
4 - ``` pip3 install -r requirements.txt ``` <br />
5 - ``` python3 main.py ```


## How to Use this Project ?

![Project Ui](src/assets/images/1.png)

above picture is our application main window

for start working with app at the first you should click on ```Select File``` button to create a new (*.srt) file 

for each part of subtitle you should enter you subtitle text in Text box , and enter your start time and end time , after finishing each item you click on add button to add item in srt file , after you adding items finished you should enter on ``` Save ``` button to save entered items in file

you can use of ``` italic ``` , ``` bold ``` and ``` underline ``` check boxes to style your text


## Hope to Enjoy

i hope to enjoy of this app , i will happy if you want to contribute to this project and develope it and add new fun features


