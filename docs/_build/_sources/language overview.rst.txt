Language Overview
=================

Variables
---------

Variables have the syntax ``$variable_name``

.. code-block:: spitfire

	My name is $name

This ``name`` variable must be passed with ``render_template`` function like ``env.render_template('tmpl_name', {"name": "Chicky"})``

You can also set variables.

.. code-block:: spitfire

	#set $number = 21*2

Now you can access ``$number`` just like other variables passed from ``render_template``.



Conditionals
------------

.. code-block:: spitfire

	#if condition1
		true value
	#elif condition2
		elseif value
	#else
		else value
	#end


Loops
-----

.. code-block:: spitfire

	#for $item_name in $list_name
		$item_name
	#end for


Nested ``for``:


.. code-block:: spitfire

	#for $outer_item_name in $outer_list_name
		#for $inner_item_name in $inner_list_name
			\... something
		#end for
	#end for


Macros
------

Macros are just like functions in Python.

.. code-block:: spitfire

	#def macro_name($arg1, $arg2, $keyword_arg='default value')
		Hey, you had $arg1, $arg2, $keyword_arg
	#end def

Calling the above macros should be done like this:

.. code-block:: spitfire

	macro_name(1,2)

Which would result in...

.. code-block:: spitfire

	Hey, you had 1, 2, default value



Comments
--------

.. code-block:: spitfire

	## this is a comment
	## this too!


Condensation
------------

You can strip the newlines and useless spaces using 'condensation'.
This is useful in webservers as your pages will be smaller and faster.

.. code-block:: spitfire

	#strip_lines
		Your content here
	#end strip_lines

Filters
-------

Sometimes, your input text needs to be sanitized or filetered to prevent XSS Attacks or for some other purposes.

.. code-block:: spitfire

	#from spitfire.runtime.filters import escape_html
	#filter escape_html
		
	Bad input values such as <script>alert("this is unsafe!!");</script>



