import tensorflow as tf

#create session with the tensorflow runtime

with tf.Session() as sess:

    # Let's make an inference
    examples = tf.constant([[2.0, 5.0, 1.0], \
                            [3.1, 2.8, 6.5], \
                            [2.5, 4.3, 3.2]])
    weights = tf.constant([[0.3, 0.4], [-0.5, 0.2], [0.3, 0.3]])
    biases = tf.constant([1.0, -0.3])

    # let's multiply the matrix
    output = tf.matmul(examples, weights) + biases

    # Fetch the ouput and execute
    print sess.run(output)
