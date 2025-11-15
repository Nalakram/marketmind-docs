import tensorflow as tf
from _typeshed import Incomplete

class ProbSparseAttention(tf.keras.layers.Layer):
    d_model: Incomplete
    n_heads: Incomplete
    d_k: Incomplete
    q_dense: Incomplete
    k_dense: Incomplete
    v_dense: Incomplete
    out_dense: Incomplete
    def __init__(self, d_model, n_heads) -> None: ...
    def call(self, inputs): ...

class InformerModel(tf.keras.Model):
    encoder: Incomplete
    dense: Incomplete
    input_embedding: Incomplete
    pos_encoding: Incomplete
    def __init__(self, input_dim, output_dim, seq_len, pred_len, d_model: int = 512, n_heads: int = 8, e_layers: int = 3) -> None: ...
    def call(self, inputs): ...

def build_informer(input_dim, output_dim, seq_len, pred_len): ...
