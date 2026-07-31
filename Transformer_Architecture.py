import tensorflow as tf
from tensorflow.keras import layers

# -----------------------------
# Transformer Block
# -----------------------------
class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super().__init__()

        self.att = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.ffn = tf.keras.Sequential([
            layers.Dense(ff_dim, activation="relu"),
            layers.Dense(embed_dim),
        ])

        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)

        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs, training=False):
        attention_output = self.att(inputs, inputs)

        attention_output = self.dropout1(
            attention_output,
            training=training
        )

        out1 = self.layernorm1(inputs + attention_output)

        ffn_output = self.ffn(out1)

        ffn_output = self.dropout2(
            ffn_output,
            training=training
        )

        return self.layernorm2(out1 + ffn_output)


# -----------------------------
# Token + Position Embedding
# -----------------------------
class TokenAndPositionEmbedding(layers.Layer):
    def __init__(self, maxlen, vocab_size, embed_dim):
        super().__init__()

        self.token_emb = layers.Embedding(
            input_dim=vocab_size,
            output_dim=embed_dim
        )

        self.pos_emb = layers.Embedding(
            input_dim=maxlen,
            output_dim=embed_dim
        )

    def call(self, x):
        maxlen = tf.shape(x)[-1]

        positions = tf.range(
            start=0,
            limit=maxlen,
            delta=1
        )

        positions = self.pos_emb(positions)

        x = self.token_emb(x)

        return x + positions


# -----------------------------
# Parameters
# -----------------------------
vocab_size = 20000
maxlen = 200

embed_dim = 64
num_heads = 4
ff_dim = 128

# -----------------------------
# Input
# -----------------------------
inputs = layers.Input(shape=(maxlen,))

embedding_layer = TokenAndPositionEmbedding(
    maxlen,
    vocab_size,
    embed_dim
)

x = embedding_layer(inputs)

# Transformer
transformer_block = TransformerBlock(
    embed_dim,
    num_heads,
    ff_dim
)

x = transformer_block(x)

# Classification Head
x = layers.GlobalAveragePooling1D()(x)

x = layers.Dropout(0.2)(x)

x = layers.Dense(
    64,
    activation="relu"
)(x)

x = layers.Dropout(0.2)(x)

outputs = layers.Dense(
    2,
    activation="softmax"
)(x)

# Build Model
model = tf.keras.Model(
    inputs=inputs,
    outputs=outputs
)

# Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Show Model
model.summary()