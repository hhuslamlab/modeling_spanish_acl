## for L-shape
library(lme4)
library(emmeans)

mem_df <- read.csv("../../../data/fixed_run/analysis/memorization_generalization/l_shape/dataframes/combine/combine.csv")

gen_df <- read.csv("../../../data/fixed_run/analysis/memorization_generalization/l_shape/unattested_dataframes/combine/combine.csv")

df <- rbind(mem_df, gen_df)

reg_model = glmer(prediction_status ~ memgen * condition + (1|triples) + (1|model), data=df, family="binomial")

summary(reg_model)

emm <- emmeans(reg_model, ~ memgen * condition, type="response")

summary(emm)
pairs(emm, simple="condition")
pairs(emm, simple="memgen")
# df <- data.frame(
#   Condition = factor(rep(c("10%L-90%NL", "50%L-50%NL", "90%L-10%NL"), c(16, 8, 8))),
#   Phenomena = factor(c(rep("Memorization", 8), rep("Generalization", 8), rep("Memorization", 4), rep("Generalization", 4), rep("Memorization", 4), rep("Generalization", 4))),
#   Accuracy = c(61.94, 76.36, 7.4, 10.91, 8.96, 4.85, 83.36, 58.33, 63.08, 2.1, 9.82, 4.76, 11.82, 3.81, 62.54, 3.43,
#                80.59, 66.21, 29.82, 69.85, 31.61, 14.7, 94.44, 55.91,
#                86.9, 54.39, 84.79, 33.64, 91.0, 39.85, 88.44, 43.64)
# )

# str(df)

# model <- lm(Accuracy ~ Condition * Phenomena, data = df)


# emm <- emmeans(model, ~ Condition * Phenomena)

# pairs(emm, simple = "Condition")
# pairs(emm, simple = "Phenomena")
