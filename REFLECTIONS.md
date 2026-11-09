# Reflections

1. Share one aspect of building this project you found challenging and how you
   overcame it.

One aspect of building this project that I found challenging was figuring out how to sort a list of dictionaries to display my high scores from highest to lowest. At first I was having trouble on how to sort a list by a certain value because so far we've just been taught that `.sort()` and `sorted()` take the argument `reverse=`. After doing research I discovered that both `.sort()` and `sorted()` also can take an argument names `key=` which allows the `.sort()` method to take the argument `key=` to get the "score" value of each dictionary and sort the dictonaries. The argument `key=` however, takes a function that Python calls on each item of the list to produce a key to sort by. I was able to then overcome my challenge and use my findings to sort the dictonaries by the value of the `"score"` key and properly display by high scores.

2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

One technical concept that I gained a deeper understanding of through building my project was 2D Lists. In simple terms, a 2D list is a list containing other lists. When that inner list has values, it is then called a 2-Dimensional list or a "matrix". This concept is used in my project in my `quiz_data.py` file. I created a `questions` list which is the list of each subject and its questions. Each subject is a list inside the outer list `questions` which contains dictionaries with records of each question. This includes the question, the choices, the answer index, and the type of subject the question is from. I was able to research how to access the values on the inner list properly and efficiently, and gain a better understanding of managing the different rows and its keys for that certain row. Going back through the module on lists and how they function definetly helped me to gain a deeper understanding of 2D lists and the problems that may arise when trying to access the values on the innner lists.