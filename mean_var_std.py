import numpy as np

def calculate(list): 
        if len(list) == 9:
            l = np.array(list).reshape(3,3)
            
            mean_values = [np.mean(l,axis = 0).tolist(), np.mean(l,axis = 1).tolist(), np.mean(l).tolist()]
            variance_values = [np.var(l,axis = 0).tolist(), np.var(l,axis = 1).tolist(), np.var(l).tolist()]
            std_values = [np.std(l,axis = 0).tolist(), np.std(l,axis = 1).tolist(), np.std(l).tolist()]
            max_values = [np.max(l,axis = 0).tolist(), np.max(l,axis = 1).tolist(), np.max(l).tolist()]
            min_values = [np.min(l,axis = 0).tolist(), np.min(l,axis = 1).tolist(), np.min(l).tolist()]
            sum_values = [np.sum(l,axis = 0).tolist(), np.sum(l,axis = 1).tolist(), np.sum(l).tolist()]

            calculations = {
                'mean': mean_values,
                'variance': variance_values,
                'standard deviation': std_values,
                'max': max_values,
                'min': min_values,
                'sum': sum_values,
            }
        else:
            raise ValueError('List must contain nine numbers.')
            
        return calculations