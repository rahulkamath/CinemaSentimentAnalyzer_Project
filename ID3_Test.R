library(forecast)
library(tseries)
library(sqldf)
library(ggplot2)
library(C50)
getwd()

install.packages('C50')
install.packages('ggplot2')
movies <- read.csv('C:/Users/dsouz/Documents/trial1_bkup.csv')
str(movies)

sample_size <- floor(0.8 * nrow(movies))
seq_len(5)
training_index <- sample(seq_len(nrow(movies)), size = sample_size)
# get the rows by the index from our sample
train <- movies[training_index,]
# get the rows not in the index
test <- movies[-training_index,]

predictors <- c('Actor1', 'Genre1', 'Director')

model <- C5.0.default(x = train[,predictors], y = train$Average)

#str(model)#

summary(model)

plot(model)

pred <- predict(model, newdata = test)
evaluation <- cbind(test, pred)
ncol(evaluation)
evaluation$correct <- ifelse(evaluation$Average == evaluation$pred,1,0)
sum(evaluation$correct)/nrow(evaluation)

TPR <- sum(evaluation$pred == 'Yes' & evaluation$Average == 'Yes')/
  sum(evaluation$Average == 'Yes')
TNR <- sum(evaluation$pred == 'No' & evaluation$Average == 'No')/
  sum(evaluation$Average == 'No')
FPR <- sum(evaluation$pred == 'Yes' & evaluation$Average == 'No')/
  sum(evaluation$Average == 'No')
FNR <- sum(evaluation$pred == 'No' & evaluation$Average == 'Yes')/
  sum(evaluation$Average == 'Yes')
TPR
TNR
FPR
FNR
TPR <- count(evaluation$pred == 'yes' & evaluation$Average == 'yes')
pred
evaluation
?count
