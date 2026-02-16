#!/bin/bash

LANGUAGE=$1
DATABIN=data-bin

CKPTS=checkpoints


fairseq-generate \
      "${DATABIN}/${LANGUAGE}" \
      --gen-subset "test" \
      --source-lang "${LANGUAGE}.src" \
      --target-lang "${LANGUAGE}.tgt" \
      --path "${CKPTS}/${LANGUAGE}-models/checkpoint_best.pt" \
      --beam 5 \
      > "predictions/${LANGUAGE}.pred"
