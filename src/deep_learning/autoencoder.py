import torch
from torch import nn

class RefineryAutoencoder(nn.Module):
    """Unsupervised baseline for multivariate anomaly detection."""
    def __init__(self, n_features: int, latent_dim: int = 16):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(n_features, 64), nn.ReLU(),
            nn.Linear(64, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64), nn.ReLU(),
            nn.Linear(64, n_features)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))
