# TreatYoSelf 

This repo conatins python scripts created for automating some of the boring tasks for me.

All scipts are in single folder because this folder has been added to path.

For now it only contains .bat files (i.e. for windows only) . I might add linux shell scripts soon.


## Automation Scripts
 
 - [Movie/TV search](#Movie)

## Installation

### Python Packages 

```
python -m pip install -r requirements.txt
```
### Webdriver

Along with python packages you will require webdrivers.
Here i am using ChromDriver 81.0.4044.138.

You can either the webdriver included in repo or download your own depending on your browser and version.

For Chrome webdrivers different than used here:
<a href = "https://chromedriver.chromium.org/downloads" target="_blank">ChromeDrivers</a>

### Running scripts

 1.  <b>Python</b> You can either run these scripts as 
```
python <scriptname.py> <arguments>
```
 2. <b>On Windows</b> just double click on bat file or just add this folder on your system path and type
 ```
 <batchfilename> <arguments>
 ```
 <b>Important:</b> You need to change absolute address of the scripts in your batch files. e.g.:
```
@python "<Change this address to absolute path for scripts>" %*
@pause
```

## Movie 

This script takes the title of movie or tv series you want to search on all of streaming platforms provided in the script `movie.py` .

I have added Netflix ,Amazon prime and Hotstar but you can add more.

It is pretty simple script, you just need to pass the title as argument.

<b>Important:</b> You must be logged in on these services in your browser for it to work.

#### Usage

```
python Movie.py <optional arguments> <Title of Movie/Tv series> 
```
#### Example
```
python Movie.py Westworld
```