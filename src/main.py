
from torch import nn, optim, Tensor, utils
import lightning as L
import chess


class LitModel(L.LightningModule):
    def __init__(self):
        super().__init__()
        model = nn.Sequential(
            nn.Linear()
        )

    def training_loop():
        pass