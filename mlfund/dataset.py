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
    def generate(params, label_type='numeric'):
        assert isinstance(params, list), '`params` must be a %s' % list.__name__

        K = len(params)
        assert K > 0, 'Length of `params` must be greater than 0'
        assert label_type == 'numeric' or label_type == 'positive_negative', '`label_type` must be \'numeric\' or \'positive_negative\''

        if label_type == 'positive_negative':
            assert K == 2, 'Length of `params` must be 2 if `label_type` == \'positive_negative\''

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

                if label_type == 'positive_negative':
                    y = numpy.ones(param.N, int) * -1
                else:
                    y = numpy.ones(param.N, int) * idxK
            else:
                X2 = numpy.random.multivariate_normal(param.mean, param.cov, param.N)
                X = numpy.append(X, X2, 0)

                if label_type == 'positive_negative':
                    y2 = numpy.ones(param.N, int) * 1
                else:
                    y2 = numpy.ones(param.N, int) * idxK
                y = numpy.append(y, y2, 0)

        return (X, y)





