library(lme4)
library(ggplot2)
# library(tidyverse)

df <- read.csv("../../../data/fixed_run/analysis/memorization_generalization/nl_shape/dataframes/90L_10NL/combine.csv")

# table(df$prediction_status)
#table(table(df$triples))
# df.correct <- subset(df, df$prediction_status == 1)
# summary(df.correct)

## TODO: nested model comparison. Check AIC and BIC. BIC lower the better. more than 2 is significant. M1 = BIC of (1|run) and 1|model against 1|run, 1|model.

## to avoid overfitting we used BIC and AIC. best model justified by the data.
##
str(df)
table(df$model)
table(df$condition)
table(df$prediction_status)
df$prediction_status_f = as.factor(as.character(df$prediction_status))
contrasts(df$prediction_status_f)
levels(df$prediction_status_f)

# reg_model = glmer(prediction_status_f ~ log10(frequency) + (1|triples)+ (1|run) + (1|model), data=df, family="binomial")

reg_model = glmer(prediction_status_f ~ log10(frequency) + (1|triples) + (1|model), data=df, family="binomial")
# str(model)
summary(reg_model)

# save(reg_model, file="../../../data/fixed_run/analysis/memorization_generalization/l_shape/r_models/10L_90NL/glmer.rda")

# model = glmer(df.correct$prediction_status ~ df.correct$frequency + (1|df.correct$seen), family="logit", control=glmerControl(optimizer="bobyqa",optCtrl=list(maxfun=2e5)))
# summary(model)


# model = lm(df$prediction_status ~ df$frequency.log, family="binomial", control=glmerControl(optimizer="bobyqa",optCtrl=list(maxfun=2e5)))
# summary(model)
