
TUTORS = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
KLASSES = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А' ]

def _return_ ():
    student = (i for i in TUTORS)
    klass = (i for i in KLASSES)
    for list_students in zip (student,klass):
        yield list_students [::-1]
    for list_students2 in student:
        yield list_students2, None

__ret__=_return_()
for x in __ret__:
    print(x)



# long = len(list1) - len(list2)
# if long > 0:
# for i in range (long)
# list2.append(None)
 #   for tutors,klasses in zip (list1,list2):
  #      yield (tutors,klasses)
