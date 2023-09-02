Quickstart
==========

Installation
------------

.. code-block:: bash

	python -m pip install spitfire3

Creating a Template
-------------------

First, create a templates directory/folder. This folder will store all your templates and will be the "home" of your spitfire environment.

.. code-block:: bash

	mkdir templates

Next, we create the template. We will call it 'fruits'. Any spitfire template must end with .spf so we will save it as 'fruits.spf'.

.. code-block:: spitfire
	:caption: templates/fruits.spf

	<ul>
	#for $fruit in $list
		<li> $fruit.name costs $fruit.price</li>
	#end for
	</ul>


The Python Code
---------------

.. code-block:: python
	:caption: main.py
	
	import spitfire
	env = spitfire.Environment('templates') 
	# 'templates' folder becomes the "home" of this Environment
	env.load_dir() # no parameters on load_dir() loads the "home" directory
	print(env.render_template('fruits', {"list": [
		{"name": "apple", "price": '$0.3'},
		{"name": "kiwi", "price": "$0.7"},
		{"name": "banana", "price": "$0.5"},
	]}))

Run this in your terminal...

.. code-block:: bash

	$ python main.py


\.... and you shall get the following output.

.. code-block::

	<ul>
		<li> apple costs $0.3</li>
		<li> kivi costs $0.7</li>		
		<li> banana costs $0.5</li>
	</ul>





Congratulations!!
-----------------
You succesfully used Spitfire!! Now check out the `language overview </language%20overview.html>`_.