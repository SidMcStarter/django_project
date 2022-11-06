

Basic Idea: Extracing text from images and converting it to speech for the visually impaired.
Tools Used: OpenCV, pytesseract, gtts, django, bootstrap

Project Inspiration: One of our firends at the university is isually impaired and hence has accessibility issues with some of the online quizzes. Like the ones containing screenshots of python code and questions based on it. The screen reader software he uses cannot read text from the image. 

How it works: We came up with this website where one can upload code screenshots from an ide and extract the text from it. The text is extracted through python libraries like OpenCV and pytesseract. We pass this text through Google's text-to-speech api using python and a library called gtts and generate an audio file. The audio file is then uploaded onto the website using the django framework where one can play it. 

