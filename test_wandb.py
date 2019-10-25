# Inside my model training code
import wandb

wandb.init(project="my-project")
wandb.config.dropout = 0.2
wandb.config.hidden_layer_size = 128
wandb.log()

