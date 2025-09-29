from typing import Tuple
import torch
from fairseq.models.transformer import TransformerModel
import matplotlib.pyplot as plt
import seaborn as sns
from fairseq.data import Dictionary

model = TransformerModel.from_pretrained('../data/checkpoints', checkpoint_file='checkpoint_best.pt')
model.eval()

src_dict = Dictionary.load('../data/checkpoints/dict.10L_90NL_1_1.src.txt')
tgt_dict = Dictionary.load('../data/checkpoints/dict.10L_90NL_1_1.tgt.txt')

def get_attention_weights(model: TransformerModel, src_tokens: torch.Tensor, src_lengths: torch.Tensor, tgt_tokens: torch.Tensor) -> torch.Tensor:
    with torch.no_grad():
        transformer_model = model.models[0]
        encoder_out = transformer_model.encoder(src_tokens, src_lengths)
        decoder_out, extra = transformer_model.decoder(tgt_tokens, encoder_out=encoder_out)
        attn_weights = extra['attn'][0]
        return attn_weights.cpu().numpy()

source_sentence = "s u p e ɾ b e n ɡ ˈ a m o s <V;SBJV;PRS;1;PL> # s u p e ɾ b ˈ e n ɡ a n <V;SBJV;PRS;3;PL> # <V;SBJV;PRS;2;PL>"
target_sentence = "s u p e ɾ b e n ɡ ˈ a j s"

# Encode without appending EOS
src_tokens = src_dict.encode_line(source_sentence, append_eos=False).unsqueeze(0)
tgt_tokens = tgt_dict.encode_line(target_sentence, append_eos=False).unsqueeze(0)

src_lengths = torch.LongTensor([src_tokens.size(1)])

attention_weights = get_attention_weights(model, src_tokens, src_lengths, tgt_tokens)

print("Attention weights shape:", attention_weights.shape)
print("Sample attention weights:\n", attention_weights[0, :3, :3])

src_labels = [src_dict[i] for i in src_tokens[0]]
tgt_labels = [tgt_dict[i] for i in tgt_tokens[0]]

num_heads = attention_weights.shape[0]
num_rows = (num_heads + 3) // 4
plt.figure(figsize=(20, 5 * num_rows))

for i in range(num_heads):
    plt.subplot(num_rows, 4, i + 1)
    sns.heatmap(attention_weights[i], cmap='viridis', annot=False,
                xticklabels=src_labels if i >= num_heads - 4 else [],
                yticklabels=tgt_labels if i % 4 == 0 else [])
    plt.title(f'Head {i + 1}')
    if i >= num_heads - 4:
        plt.xlabel('Source')
    if i % 4 == 0:
        plt.ylabel('Target')

plt.tight_layout()
plt.savefig('attention_weights.png', dpi=300, bbox_inches='tight')
print("Attention weights visualization saved as 'attention_weights.png'")
