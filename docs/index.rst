Spitfire
========

Hello people!!
Spitfire is currently the `fastest  <https://github.com/re-masashi/spitfire/#performance>`_  python templating engine. It is used in YouTube's servers to serve about 5 billion pages everyday.

It is just as simple as any other templating engine but faster(a lot).

  "Any sufficiently advanced technology is indistinguishable from magic"
  ~ Arthur C. Clarke

To break it down to you, Spitfire has a compiler that optimizes and reduces the time taken by various operations. This makes Spitfire *magically fast*. No trade-offs, pure performance.

Some `wonderful people <https://github.com/re-masashi/spitfire/blob/master/CONTRIBUTORS>`_ initially created Spitfire for Python2, which wasn't usable with the Python we know today (Python3). Since such a magical work fannot be left behind, this was ported to Python3.

Using it is as simple as:

.. code-block:: python
  :linenos:
  :caption: main.py

  import spitfire 
  env = spitfire.Environment()
  env.load_dir('templates')
  print(env.render('ample', {"name": "John", "age": 10}))

.. code-block:: spitfire
  :linenos:
  :caption: templates/ample.spf

  $name is $age years old
  #set $gap = 18- $age
  #if ($age >= 18)
    $name can drive a car or a bike.
  #else
    $name can only ride a bicycle for now. Please wait for $gap years.
  #end if

Which returns:

  John can only ride a bicycle for now. He needs to wait 8 years.
  
Pretty simple, right? Because it really is simple.

Check out the `quickstart tutorial <quickstart.html>`_.

-----

.. toctree::
   :maxdepth: 1

   quickstart
   language overview