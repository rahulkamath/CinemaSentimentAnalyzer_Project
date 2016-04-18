install.packages('nnet')
install.packages('e1071')
install.packages('caret')
library(nnet)
library(e1071)
library(caret)

t <- read.csv('C:/Users/dsouz/Documents/trial_OG.csv')

sample_size <- floor(0.6 * nrow(t))

training_index <- sample(seq_len(nrow(t)), size = sample_size)

train <- t[training_index,]
test <- t[-training_index,]


####neural net####

t.nnet <- nnet(formula = Good ~ Released + Rated + Genre1 + Genre2 + Genre3 + Actor1 +
                 Actor2, data = train, size = 4, MaxNWts = 2000)

t.pred <- predict(t.nnet, test, type = 'class')

#breakVector[,1] <- factor(breakVector[,1], levels=levels(FinalTable[,1))#

results <- data.frame(actual = test[,'Good'], predicted = t.pred)

results$correct <- ifelse(results$actual == results$predicted, 1, 0)
results

results.matrix <- confusionMatrix(results$predicted, results$actual)

results.matrix
results.matrix$table



edit(nnet.default)



             