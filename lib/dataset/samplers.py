import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import torch
from torch.utils.data import Sampler

class PartialSampler(Sampler):
    def __init__(self, ds, epoch_size):
        self.n_items = len(ds)
        if epoch_size is not None:
            self.epoch_size = min(epoch_size, len(ds))
        else:
            self.epoch_size = len(ds)
        super().__init__(None)

    def __len__(self):
        return self.epoch_size

    def __iter__(self):
        return (i.item() for i in torch.randperm(self.n_items)[:len(self)])
    

class ListSampler(Sampler):
    def __init__(self, ids):
        self.ids = ids

    def __len__(self):
        return len(self.ids)

    def __iter__(self):
        return iter(self.ids)
