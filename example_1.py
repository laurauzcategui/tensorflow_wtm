import tensorflow as tf

#create session with the tensorflow runtime

with tf.Session() as sess:
    #define some ops
    c = tf.constant("Welcome to Women Techmakers")
    # run a step
    print sess.run(c)
