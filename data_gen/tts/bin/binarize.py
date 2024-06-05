import os
import sys
os.environ["OMP_NUM_THREADS"] = "1"

os.chdir('/content/DiffSinger')
sys.path.append('/content/DiffSinger')

import importlib
from utils.hparams import set_hparams, hparams


def binarize():
    binarizer_cls = hparams.get("binarizer_cls", 'data_gen.tts.base_binarizer.BaseBinarizer')
    pkg = ".".join(binarizer_cls.split(".")[:-1])
    cls_name = binarizer_cls.split(".")[-1]
    binarizer_cls = getattr(importlib.import_module(pkg), cls_name)
    print("| Binarizer: ", binarizer_cls)
    binarizer_cls().process()


if __name__ == '__main__':
    set_hparams()
    binarize()
