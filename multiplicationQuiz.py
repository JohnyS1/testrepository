import random, time, pyinputplus as pyi

##numberOfQuestions = 11 # wersja w pełni moja
##correctAnswers = 0
##for questionNumber in range(1, numberOfQuestions):
##    num1=random.randint(0,9)
##    num2=random.randint(0,9)
##    answer=pyi.inputNum(prompt='%s: %s*%s= \n'%(questionNumber,num1,num2), default='', timeout=8)
##    if answer==(num1*num2):
##        print('good answer')
##        correctAnswers+=1
##        time.sleep(1)
##    else:
##        print('bad answer')
##        print('Correct answer was:%s' %(str(num1*num2)))
##        time.sleep(1)
##
##
##print(f'you hade {correctAnswers} correct answers')
##    

numberOfQuestions = 11
correctAnswers = 0
for questionNumber in range(1, numberOfQuestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    try:
        answer=pyi.inputNum(prompt='%s: %s*%s= \n'%(questionNumber,num1,num2),
                            allowRegexes=['^%s$' % (num1 * num2)],
                            blockRegexes=[('.*', 'Incorrect!')],#przy block regex mozna fajnie wrzucic co ma sie wyswietlać  przy złej odpowiedzi,
                            timeout=8, limit=3)
    except pyi.TimeoutException:
        print('Out of time!')
    except pyi.RetryLimitException:
        print('Out of tries!')
    else:
        print('good answer')
        correctAnswers+=1
        time.sleep(1)


print(f'you hade {correctAnswers} correct answers')
    
