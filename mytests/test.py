import spitfire


env = spitfire.Environment('templates')

name = input('Enter your name please: ')
age = int(input('Enter your age: '))

print(env.render_template('ample',[{'name': name, 'age': age}]))
