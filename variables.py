import tensorflow as tf

#create session with the tensorflow runtime

with tf.Session() as sess:

    # Let's define some variables
    var_wtm = tf.Variable([[0.,0.]])
    tf.initialize_all_variables().run()

    #print the value
    print var_wtm.eval()

    #assign values to the variables
    assign_wtm = var_wtm.assign(tf.constant([[1.5, 2.5]]))

    assign_wtm.eval()
    print var_wtm.eval()
