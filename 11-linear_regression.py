import tensorflow as tf

# model parameters
W = tf.Variable([0.3],  dtype=tf.float32)
b = tf.Variable([-0.3],  dtype=tf.float32)

x = tf.placeholder(dtype=tf.float32)
linear_model = W * x + b

y = tf.placeholder(dtype=tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)

train = optimizer.minimize(loss)

# training data
X_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(1000):
        sess.run(train, {x: X_train, y: y_train})

        # evaluate training accuracy
        curr_w, curr_b, curr_loss = sess.run([W, b, loss], {x: X_train, y: y_train})

        print('w:{} b:{} loss:{}'.format(curr_w, curr_b, curr_loss))




