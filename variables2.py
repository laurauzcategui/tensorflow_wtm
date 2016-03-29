import tensorflow as tf

# Create a Variable, that will be initialized to the scalar value 0.
wtm_16 = tf.Variable(0, name="attendees")

# Create an Op to add one to `state`.
one = tf.constant(1)
new_attendee = tf.add(wtm_16, one)
update = tf.assign(wtm_16, new_attendee)

# Variables must be initialized
init_wtm = tf.initialize_all_variables()

# Launch the graph and run the ops.
with tf.Session() as sess:
    # Run the 'init' op
    sess.run(init_wtm)
    # Print the initial value of 'state'
    print(sess.run(wtm_16))
    # Run the op that updates 'state' and print 'state'.
    for _ in range(160):
        sess.run(update)
        print "Attendee:", sess.run(wtm_16)
