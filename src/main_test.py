# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import torch
import utility
import data
import model
import loss
from option import args
from trainer_seg_hist_fuse import Trainer

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()

    torch.manual_seed(args.seed)
    checkpoint = utility.checkpoint(args)
    print("-----")
    if checkpoint.ok:
        loader = data.Data(args)
        my_model = model.Model(args, checkpoint)
        # my_model.model.load_state_dict(torch.load('../checkpoints/LOLv2-DRBN-SKF/model_lol_v2.pt'))
        my_model.model.load_state_dict(torch.load('../ckpt/LOLv2-DRBN-SKF/model_lol_v2.pt'))
        print("-------")
        args.n_colors = 3

        loss = loss.Loss(args, checkpoint) if not args.test_only else None
        # print("ares",args)
        t = Trainer(args, loader, my_model, loss, checkpoint, adv=True)
        while not t.terminate():
            t.train()
            t.test()

        checkpoint.done()
