"""Page router — maps navigation keys to render functions."""

from ui.pages import (
    about,
    benchmark,
    cnn_page,
    gru_page,
    home,
    lstm_page,
    mlp_page,
    rnn_page,
    seq2seq_page,
)

PAGE_RENDERERS = {
    "home": home.render,
    "mlp": mlp_page.render,
    "cnn": cnn_page.render,
    "rnn": rnn_page.render,
    "lstm": lstm_page.render,
    "gru": gru_page.render,
    "seq2seq": seq2seq_page.render,
    "benchmark": benchmark.render,
    "about": about.render,
}
