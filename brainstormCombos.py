import numpy as np

descriptor = ['redundant','solar powered','huge','burning','reductive','radiative','expansive','combinatorial','convergent','edible','solid','freeze dried','genetically engineered','compressed','miniature','woven','psychedelic','empirical','loving','social','kinesthetically powered','reproducing','chewy','autonamous','nuclear','reflective','auto weighted','internet connected','extra-dimensional','dialectical','wooden','soft','explosive','space aged','nanotech','vertically integrated']

thing = ['bookshelf','street','shower','painting','keyboard','tape','globe','syringe','projector','shoes','writing implement','tree','toilet','dice','outlet','plate','bandage','oil','money','book','star','hat','dress','fire','take out','bitcoin','clothes','pillow','candle','bread','monitor','MRI','phone','swing','window','rocket','blood pressure cuff','sculpture','spy','key','door','musical instrument','box','computer','elevator','rock','light','car','mouse','train','telescope','containers','pacemaker']

print('What about a ' + descriptor[np.random.randint(len(descriptor))] + ' ' + thing[np.random.randint(len(thing))]'?')
