import torch
from torch import nn

class RefineryLSTM(nn.Module):
    """Baseline sequence model for multivariate refinery time series."""
    def __init__(self, input_size: int, hidden_size: int = 64, layers: int = 2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, layers, batch_first=True)
        self.head = nn.Linear(hidden_size, 1)

    def forward(self, x):
        output, _ = self.lstm(x)
        return self.head(output[:, -1, :])

# Training data should be split chronologically.
# Scale using the training partition only.
# Never use future refinery measurements to construct historical features.
