import tensorflow as tf

#define the variables - Model Parameters
W=tf.Variable([.3],tf.float32)
b=tf.Variable([-.3],tf.float32)

#define the placeholder for Input
x=tf.placeholder(tf.float32)

#Placeholder for the desired output
y = tf.placeholder(tf.float32)

#define the model
linear_model = W*x+b

#sqaured difference between the actual output and desired output
sq_delta = tf.square(linear_model-y)

#- Loss Function - Sum up all the squared differences
loss = tf.reduce_sum(sq_delta)

#Optimizer - it checks the change in the loss with respect to the change in the variable
optimizer = tf.train.GradientDescentOptimizer(0.01)#here 0.01 is the learning rate - steps in which you change the variables
train=optimizer.minimize(loss)

#initialize the variables
init = tf.global_variables_initializer()

#Launch the graph
session = tf.Session()
session.run(init)

#run the optimizer on different values of W and b
for i in range (1000):
     session.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

#final value of w and b
print(session.run([W,b]))
