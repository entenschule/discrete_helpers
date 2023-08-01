def apply_on_vector(self, vector):
    arg_type = type(vector)
    inv = self.inverse
    return arg_type([vector[inv[i]] for i in range(len(vector))])
