# For iPython Interactive sessions can be use too.
# Enter an interactive TensorFlow Session.
import tensorflow as tf

sess = tf.InteractiveSession()

x = tf.Variable([5.0, 2.5])
a = tf.constant([3.1, 3.3])

# Initialize 'x' using the run() method of its initializer op.
x.initializer.run()

# Add an op to subtract 'a' from 'x'.  Run it and print the result
sub = tf.sub(x, a)
print(sub.eval())

# ToDo Try it out with add
# more operations here:
add  = tf.add(x, a)
print(add.eval())

# Close the Session when we're done.
sess.close()
