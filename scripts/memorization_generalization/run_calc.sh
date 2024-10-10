#!/bin/bash

echo "calculating NL shape attested...."
python section_6_4_1_calc_attested_nl_shape.py --condition 10L_90NL --train_triples_set all

python section_6_4_1_calc_attested_nl_shape.py --condition 50L_50NL --train_triples_set all

python section_6_4_1_calc_attested_nl_shape.py --condition 90L_10NL --train_triples_set all

python section_6_4_1_calc_attested_nl_shape.py --condition 10L_90NL --train_triples_set nl

python section_6_4_1_calc_attested_nl_shape.py --condition 50L_50NL --train_triples_set nl

python section_6_4_1_calc_attested_nl_shape.py --condition 90L_10NL --train_triples_set nl

echo "calculating NL shape unattested...."
python section_6_4_1_calc_unattested_nl_shape.py --condition 10L_90NL --train_triples_set all

python section_6_4_1_calc_unattested_nl_shape.py --condition 50L_50NL --train_triples_set all

python section_6_4_1_calc_unattested_nl_shape.py --condition 90L_10NL --train_triples_set all

python section_6_4_1_calc_unattested_nl_shape.py --condition 10L_90NL --train_triples_set nl

python section_6_4_1_calc_unattested_nl_shape.py --condition 50L_50NL --train_triples_set nl

python section_6_4_1_calc_unattested_nl_shape.py --condition 90L_10NL --train_triples_set nl

echo "calculating L shape attested...."
python section_6_4_1_calc_attested_l_shape.py --condition 10L_90NL --train_triples_set all

python section_6_4_1_calc_attested_l_shape.py --condition 50L_50NL --train_triples_set all

python section_6_4_1_calc_attested_l_shape.py --condition 90L_10NL --train_triples_set all

python section_6_4_1_calc_attested_l_shape.py --condition 10L_90NL --train_triples_set l

python section_6_4_1_calc_attested_l_shape.py --condition 50L_50NL --train_triples_set l

python section_6_4_1_calc_attested_l_shape.py --condition 90L_10NL --train_triples_set l

echo "calculating L shape unattested...."
python section_6_4_1_calc_unattested_l_shape.py --condition 10L_90NL --train_triples_set all

python section_6_4_1_calc_unattested_l_shape.py --condition 50L_50NL --train_triples_set all

python section_6_4_1_calc_unattested_l_shape.py --condition 90L_10NL --train_triples_set all

python section_6_4_1_calc_unattested_l_shape.py --condition 10L_90NL --train_triples_set l

python section_6_4_1_calc_unattested_l_shape.py --condition 50L_50NL --train_triples_set l

python section_6_4_1_calc_unattested_l_shape.py --condition 90L_10NL --train_triples_set l
