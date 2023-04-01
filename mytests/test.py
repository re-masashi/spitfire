import spitfire


env = spitfire.Environment('templates')

name = input('Enter your name please: ')
age = int(input('Enter your age: '))

print(env.render('ample.spf',[{'name': name, 'age': age}], template_name="ample"))
