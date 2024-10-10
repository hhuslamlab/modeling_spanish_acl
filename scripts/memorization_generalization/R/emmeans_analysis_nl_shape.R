## for NL-shape
library(lme4)
library(emmeans)

mem_df <- read.csv("../../../data/fixed_run/analysis/memorization_generalization/nl_shape/dataframes/combine/combine.csv")

gen_df <- read.csv("../../../data/fixed_run/analysis/memorization_generalization/nl_shape/unattested_dataframes/combine/combine.csv")

df <- rbind(mem_df, gen_df)

reg_model = glmer(prediction_status ~ memgen * condition + (1|triples) + (1|model), data=df, family="binomial")

summary(reg_model)

emm <- emmeans(reg_model, ~ memgen * condition, type="response")

summary(emm)
pairs(emm, simple="condition")
pairs(emm, simple="memgen")
