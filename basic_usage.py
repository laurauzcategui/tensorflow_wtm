import tensorflow as tf

# Create a Constant op that produces a 1x2 matrix.  The op is
# added as a node to the default graph.

matrix1 = tf.constant([[3., 3.]])
# Create another Constant that produces a 2x1 matrix.

matrix2 = tf.constant([[2.],[2.]])


# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
product = tf.matmul(matrix1, matrix2)

# Let's run the product of matrix 1 and matrix 2 and store the result
with tf.Session() as sess:
    result = sess.run([product])
    print(result)
