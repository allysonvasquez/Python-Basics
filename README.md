# Python Basics
The purpose of this repository is to brush up on my Python skills and implement old & new concepts into different types of scripts.
My end goal is to apply what I learn to future AI/ML concepts, algorithms, and models.

Sources Used:
* Al Sweigart's [Automate the Boring Stuff](https://automatetheboringstuff.com/#toc)
* Youtube videos from [Corey Schafer](https://www.youtube.com/user/schafer5)
* Coding exercises from [w3resource](https://www.w3resource.com/python/python-tutorial.php)

## Index
- [Programming Basics](#Programming-Basics)
- [Automating Tasks](#Automating-Tasks)
- [Side Projects/Scripts](#Side-Projects)

# Programming Basics
My goal in this section is to simply refresh my memory on python syntax.

* [Calculator](https://github.com/allysonvasquez/Python-Basics/blob/master/1-Programming%20Basics/Calculator.py)
  - Review over basic syntax, math operators, and data type casting for variables.
* [String Manipulator](https://github.com/allysonvasquez/Python-Basics/blob/master/1-Programming%20Basics/StringManipulation.py)
  - Manipulation of strings; uses concatenation, substrings, slicing, and other string operators.
* [Comparison/Boolean Operators](https://github.com/allysonvasquez/Python-Basics/blob/master/1-Programming%20Basics/Comparison.py)
  - Practice using random operator & boolean/comparison operators with user input
* [Functions](https://github.com/allysonvasquez/Python-Basics/blob/master/1-Programming%20Basics/FunctionPractice.py)
  - Using lists and functions to solve prompts in [Python functions - Exercises, Practice, Solution](https://www.w3resource.com/python-exercises/python-functions-exercises.php)
* [Dictionaries](https://github.com/allysonvasquez/Python-Basics/blob/master/1-Programming%20Basics/Classes.py)
  - Notes on dictionaries that cover its syntax and methods
* [Classes](https://github.com/allysonvasquez/Python-Basics/blob/master/1-Programming%20Basics/Classes.py)
  - Example of class syntax

# Automating Tasks
This section will cover topics that are unfamiliar to me. There will be a mix of in-depth notes and practice projects.
My goal in this section is to fully understand web scraping (just a personal interest that I've been wanting to get into🥺).

* [Pattern Matching](Python-Basics/2-Automating-Tasks/Regexes.py) - Notes on Regular Expressions (Regexes)
  - TODO: Practice project to apply understanding of regexes
* [File I/O](https://github.com/allysonvasquez/Python-Basics/blob/master/2-Automating%20Tasks/FileIO.py) - Notes on File I/O Syntax
  - TODO: Practice project on FileIO & File organization
* [Web scraping](https://github.com/allysonvasquez/Python-Basics/blob/master/2-Automating%20Tasks/WebScraping.py) - Basic web scrape using a simple html [file](https://github.com/allysonvasquez/Python-Basics/blob/master/2-Automating%20Tasks/simple.html) and Corey Shafer's [tutorial](https://youtu.be/ng2o98k983k)
  - [Practice project](https://github.com/allysonvasquez/Python-Basics/blob/master/2-Automating%20Tasks/WebScraping2.py) - web scrape using data from [Corey Schafer's](https://coreyms.com) website
  - [Requests](https://github.com/allysonvasquez/Python-Basics/blob/master/2-Automating%20Tasks/Requests.py) - Notes on requests library for use in web scraping
* [Excel, Word, PDF](https://github.com/allysonvasquez/Python-Portfolio/blob/master/2-Automating%20Tasks/Excel_Word_PDF.py) - Notes on reading, writing, and editing data in these formats
* [Time & Scheduling](https://github.com/allysonvasquez/Python-Portfolio/blob/master/2-Automating%20Tasks/Time.py) - Notes on time modules, automating scripts on a schedule
  - [Stopwatch](https://github.com/allysonvasquez/Python-Portfolio/blob/master/2-Automating%20Tasks/Stopwatch.py) - Simple stopwatch script. Is a follow-along project in Automate the Boring Stuff Ch.15
  - [Multithreading](https://github.com/allysonvasquez/Python-Portfolio/blob/master/2-Automating%20Tasks/threadDemo.py) - Notes on multithreading basics
* [Image Manipulation](https://github.com/allysonvasquez/Python-Portfolio/blob/master/2-Automating%20Tasks/Image%20Manipulation/Image_Manipulation.ipynb) - Notes on basic image manipulation, using cute bears as references.
* [Sending Mail](https://github.com/allysonvasquez/Python-Portfolio/blob/master/2-Automating%20Tasks/Mail_Demo.py) - Notes on sending emails through Python (SMTP Server)

# Side Projects
This section will consist of side projects/scripts I create on my own to apply what I learned! It allows me to practice the basic development steps needed to create larger projects.
## Recipe Scrape
[RecipeScrape](https://github.com/allysonvasquez/Python-Basics/tree/master/3-Side%20Projects/RecipeScraper) scrapes the [Breakfast Eggs Ready](https://www.allrecipes.com/gallery/easy-egg-breakfast/) article from allrecipes.com. 

The current purpose of RecipeScrape is to collect the simplest-to-make egg recipes and format the data into an easy to read table. I will be personally cooking and eating the recipes mentioned... to ensure that they are worhty of being listed.
#### Problems
The biggest issue I had was figuring out the html attributes and tags in order to parse all of the data and links. My knowledge in html is basic, so this was a slight learning curve.
  - Reading through Dataquest's [tutorial](https://www.dataquest.io/blog/web-scraping-tutorial-python/) helped immensely with being able to identify tags.
#### How to Improve This Project
Reformatting the third column of the recipe table to display the actual recipe instead of a link to the recipe online.

## Photo Resizer
[PosterResizer](https://github.com/allysonvasquez/Python-Portfolio/blob/master/3-Side%20Projects/PosterResizer/Resizer.py) is a simple script to resize downloaded images into an 8x10 format for photo printing. I created this script to convert all my pinterest photos into a uniform size to print and create a wall collage in my bedroom!

#### Before -> After
<img src="https://github.com/allysonvasquez/Python-Portfolio/blob/master/3-Side%20Projects/PosterResizer/original_pictures/pic8.jpg" width="200">  <img src="https://github.com/allysonvasquez/Python-Portfolio/blob/master/3-Side%20Projects/PosterResizer/pngs/pic8.png" width="200">

#### Problems
Initial issues with resizing the images while maintaining aspect ratio.
#### How to Improve This Project
Optimizing the for loop for faster reformatting.


## Other/Future Goals
More of a 'TODO' section:
- Get comfortable using Git and Jupyter Notebook
- Refresh on Calculus, Linear Algebra, Statistics
- Create AI/ML Repository
