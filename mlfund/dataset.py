import numpy


class GaussianParam(object):
    def __init__(self, mean=[0,0], cov=[[1,0], [0,1]], N=1):
        if mean is not None:
            self.mean = mean
        if cov is not None:
            self.cov = cov
        if N is not None:
            self.N = N


class Gaussian(object):
    @staticmethod
    def generate(params):
        if not isinstance(params, list):
            raise TypeError("'params' must be a list")

        K = len(params)
        if K == 0:
            raise TypeError("The number of categories (i.e., length of 'params') must be greater than 0")

        X = None
        y = None
        m = None
        idxK = int(0)
        for param in params:
            idxK = idxK + 1
            if m == None:
                m = len(param.cov)
            else:
                if m != len(param.cov):
                    raise AttributeError("Dimension of %d-th covariance matrix 'param.cov' is not consistent, expected value: [%d %d]" % (len(param.cov), m, m))

            if len(param.mean) is not m:
                raise AttributeError("Dimension of %d-th mean vector 'gaussianParam.mean' is not consistent, expected value: %d" % (len(param.cov), m))

            if not isinstance(X, numpy.ndarray):
                X = numpy.random.multivariate_normal(param.mean, param.cov, param.N)
                y = numpy.ones(param.N, int) * idxK
            else:
                X2 = numpy.random.multivariate_normal(param.mean, param.cov, param.N)
                X = numpy.append(X, X2, 0)

                y2 = numpy.ones(param.N, int) * idxK
                y = numpy.append(y, y2, 0)

        return (X, y)





