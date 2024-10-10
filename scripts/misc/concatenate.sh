awk 'FNR==1 && NR!=1{next;}{print}' /home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/suffix_accuracies/10L_90NL/nlshaped/overall_accuracies/*.csv > /home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/suffix_accuracies/10L_90NL/nlshaped/overall_accuracies/combine.csv

awk 'FNR==1 && NR!=1{next;}{print}' /home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/suffix_accuracies/50L_50NL/nlshaped/overall_accuracies/*.csv > /home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/suffix_accuracies/50L_50NL/nlshaped/overall_accuracies/combine.csv

awk 'FNR==1 && NR!=1{next;}{print}' /home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/suffix_accuracies/90L_10NL/nlshaped/overall_accuracies/*.csv > /home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/suffix_accuracies/90L_10NL/nlshaped/overall_accuracies/combine.csv
