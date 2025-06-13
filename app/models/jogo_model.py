import numpy as np

def generate_numbers(model, results):
    onehots = []
    for e in results:
        oh = np.zeros(25); [oh.__setitem__(d-1,1) for d in e["dezenas"]]
        onehots.append(oh)
    k = 5
    seq = np.concatenate(onehots[-k:]).reshape(1,-1)
    probs = model.predict(seq)[0]
    escolha = np.argsort(probs)[-15:] + 1
    return sorted(int(x) for x in escolha)
