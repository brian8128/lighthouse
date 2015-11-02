import matplotlib.pyplot as plt
import numpy as np

class Bayes(object):
    '''
    INPUT:
        prior (dict): key is the value (e.g. 4-sided die),
                      value is the probability

        likelihood_func (function): takes a new piece of data and the value and
                                    outputs the likelihood of getting that data
    '''
    def __init__(self, prior, likelihood_func):
        self.prior = prior
        self.likelihood_func = likelihood_func


    def normalize(self):
        '''
        INPUT: None
        OUTPUT: None

        Makes the sum of the probabilities equal 1.
        '''
        total = sum([prob for item, prob in self.prior.iteritems()])
        self.prior = {item: (prob/total) for item, prob in self.prior.iteritems()}

    def update(self, data):
        '''
        INPUT:
            data (int or str): A single observation (data point)

        OUTPUT: None
        
        Conduct a bayesian update. Multiply the prior by the likelihood and
        make this the new prior.
        '''
        self.prior = {item: (self.likelihood_func(data, item) * prob) for item, prob in self.prior.iteritems()}
        self.normalize()

    def print_distribution(self):
        '''
        Print the current posterior probability.
        '''
        print sorted(self.prior.iteritems())
    
    def plot(self, color=None, title=None, label=None):
        '''
        Plot the current prior.
        '''
##        x, y = [], []
##        for xi, yi in sorted(self.prior.items()):
##            x.append(xi)
##            y.append(yi)
#setup the 2D grid with Numpy
        x = np.linspace(0, 1, 100)
        y = np.linspace(0, 1, 100)
        x, y = np.meshgrid(x, y)

        pdfmesh = np.zeros((100,100))
        #convert intensity (list of lists) to a numpy array for plotting
        for (a,b),prob in self.prior.iteritems():
             pdfmesh[a*100-1,b*100-1] += prob
        #now just plug the data into pcolormesh, it's that easy!
        print pdfmesh
        plt.pcolormesh(x, y, pdfmesh)
        plt.colorbar() #need a colorbar to show the intensity scale
        plt.show() #boom
        plt.plot(x,y)
        plt.show()