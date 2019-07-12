from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)   


    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    num_samples=X.shape[0]
    num_classes=W.shape[1]
    for i in np.arange(num_samples):
        scores  = np.dot(X[i,:],W)
        scores -= np.max(scores)
        num=np.exp(scores[y[i]])
        den=sum(np.exp(scores))
        loss += -np.log(num/den)
        for j in np.arange(num_classes):
            if j==y[i]:
                dW[:,j] += -X[i, ]*(den-num)/den
            else:
                dW[:,j] += X[i, ]*np.exp(scores[j])/den
                
                            
    loss /= num_samples
    loss += 0.5* reg*np.sum(np.square(W))
    dW   /= num_samples
    dW   += reg*W
        
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    num_samples=X.shape[0]
    num_classes=W.shape[1]
    scores =  X.dot(W)
    scores -= np.max(scores, axis=1)[:, np.newaxis]
    num = np.exp(scores[np.arange(num_samples),y])
    den = np.sum(np.exp(scores), axis=1)
    loss = -np.log(num/den)
    dscores=np.zeros_like(scores)
    dscores[np.arange(num_samples),y]=-1
    dscores +=np.exp(scores)/den[:,np.newaxis] 
    dW=X.T.dot(dscores)   
    loss=np.mean(loss)+0.5* reg*np.sum(np.square(W))
    dW /= num_samples
    dW += reg*W   
   

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
