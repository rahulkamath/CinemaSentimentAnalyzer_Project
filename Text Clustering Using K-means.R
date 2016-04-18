install.packages("tm")
library(tm)
docs <- Corpus(DirSource('C:/Users/laptop/Downloads/documents-export-2016-04-17'))

summary(docs)

#inspect a particular document
writeLines(as.character(docs[[10]]))

dtm <- DocumentTermMatrix(docs)  
dtm

#Organizing terms by frequency
freq <- colSums(as.matrix(dtm))   
length(freq)

ord <- order(freq)  

#Gets the 20 top frequency terms
freq[head(ord,20)]
     
#To remove sparse terms
dtms <- removeSparseTerms(dtm, 0.1) # This makes a matrix that is 10% empty space, maximum.   
inspect(dtms)

freqr <- colSums(as.matrix(dtms))   
freqr
   
freq <- sort(colSums(as.matrix(dtm)), decreasing=TRUE)   
head(freq, 20)

#Terms with frequency atleast equal to 50
findFreqTerms(dtms, lowfreq=50)

wf <- data.frame(word=names(freq), freq=freq)   
head(wf)

#
install.packages("ggplot2")
library(ggplot2)
p <- ggplot(subset(wf, freq>100), aes(word, freq))   
p <- p + geom_bar(stat="identity")   
p <- p + theme(axis.text.x=element_text(angle=45, hjust=1))  
p

#Creating a wordcloud for term frequency
install.packages("wordcloud")
library(wordcloud)

set.seed(142) 
#Words which appear atleast 25 times
wordcloud(names(freq), freq, min.freq=25)

#Colored WordCloud
set.seed(142)   
wordcloud(names(freq), freq, min.freq=20, scale=c(5, .1), colors=brewer.pal(6, "Dark2"))

#Clustering
dtmss <- removeSparseTerms(dtm, 0.15) # This makes a matrix that is only 15% empty space, maximum.   
inspect(dtmss)

#Hierarchial Clustering
install.packages("cluster")
library(cluster)   
d <- dist(t(dtmss), method="euclidian")   
fit <- hclust(d=d, method="ward.D2")   
fit 
plot(fit, hang=-1)

plot.new()
plot(fit, hang=-1)
groups <- cutree(fit, k=5)   # "k=" defines the number of clusters you are using   
rect.hclust(fit, k=5, border="red") # draw dendogram with red borders around the 5 clusters 

#K-Means Clustering
install.packages("fpc")
library(fpc)   
d <- dist(t(dtmss), method="euclidian")   
kfit <- kmeans(d, 3)  #no. of clusters=3
clusplot(as.matrix(d), kfit$cluster, color=T, shade=T, labels=2, lines=0)

