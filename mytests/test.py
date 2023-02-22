
import spitfire


env = spitfire.Environment('templates')
TABLE_DATA = [
    dict(a=1,
         b=2,
         c=3,
         d=4,
         e=5)
]

print(env.render('ample.spf', 
			[{'table': [{"a":1,"b":2} for x in range(4)]}], 
			template_name="ample"
))
