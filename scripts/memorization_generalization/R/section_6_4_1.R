library(lme4)

df <- read.csv("/home/akhilesh/personal/hmall_acl/data/fixed_run/analysis/memorization_generalization/l_shape/section_6_4_1/attested/triples_l/90L_10NL/combine.csv")
str(df)
dim(df)
df = unique(df)
dim(df)
model = lmer(test_frequency ~ training_frequency + (1|run), data=df)

summary(model)
