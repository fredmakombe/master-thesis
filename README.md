# master-thesis

Decision boundaries of Artificial Neural Networks (ANNs) are particularly challenging to
explain due to the intractability of the decision boundaries they converge to.
An optimization objective on f(x,θ) using SGD searches for values of θ , starting from
initial values θ0 which do not take the properties of x into account. Moreover,explanations 
on how high-dimensional samples are correctly or incorrectly misclassified
rely on a posteriori evidence of the classification e.g., a confusion matrix or applying
sensitivity analysis of the input after the model has been trained.

For this thesis, we will study the initial conditions of ANNs (i.e., before training) and
characterize the propensity of decision boundaries to form around a certain region of the
input domain. For complex problems like the classification of objects in natural images,
state of the art ANNs use inputs that range between 3000 and 300000 dimensions while
optimizing architectures that contain 1 to well over 100 million parameters. 


We will leverage the lower dimensionality of the input space (with respect to the parameter space)
and perform a simulated optimization on x instead of θ . In other words, study f by
analyzing the evolution of x when the cost function operates on it i.e., for a cost
function C , optimize based on δC/ δ x instead of the usual δ δC θ using SGD for example.

Due to the end-to-end differentiable nature of these models, properties found on the input
space describe analogous features of the parameter space.
