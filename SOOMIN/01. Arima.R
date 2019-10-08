library(astsa)
library(fpp)
library(tidyverse)
library(anytime)
library(xts)

train <- read.csv("DACON_CONTEST_2019/data/train.csv")
View(train)
# window(data)

data("AirPassengers")
View(AirPassengers)

# X452 2018-02-15 ~ 2018-04-30
View(train)
train$Time <- anytime(train$Time)
train452 <- train[c(13645:15445),c('Time','X452')]
train452

train452_ts <- xts(train452[,2], 
                    order.by=train452[,1])
plot(train452_ts,ylab="Time", type="c", pch=20, 
     xaxt="n", xlab="")

# train452_tsDcomp <- decompose(train452_ts,
#                               type = "additive")
# ?monthplot()
# 
# models <- list (
#   mod_arima = auto.arima(train452_ts, order = c(1,0,2)),
#   mod_exponential = ets(train452_ts, ic='aicc', restrict=FALSE),
#   # mod_neural = nnetar(train452_ts, p=12, size=25),
#   # mod_tbats = tbats(train452_ts, ic='aicc', seasonal.periods=12),
#   # mod_bats = bats(train452_ts, ic='aicc', seasonal.periods=12),
#   # mod_stl = stlm(train452_ts, s.window=12, ic='aicc', robust=TRUE, method='ets'),
#   mod_sts = StructTS(train452_ts)
# )


(fit = Arima(train452_ts, order = c(1,0,2)))
checkresiduals(fit)
autoplot(forecast(fit))
forecast(fit)

arima(ts(train452_ts), order = c(1,0,2))
forecast.Arima(arima(ts(train452_ts), order = c(1,0,2)),  h=24)


auto.arima(ts(train452_ts))

?forecast()

 # ------------------
data("AirPassengers")
library(forecast)
ap_ts <- window(AirPassengers, start=1949, end=1958.99)
str(ap_ts)

models <- list (
  mod_arima = auto.arima(ap_ts, ic='aicc', stepwise=FALSE),
  mod_exponential = ets(ap_ts, ic='aicc', restrict=FALSE),
  mod_neural = nnetar(ap_ts, p=12, size=25),
  mod_tbats = tbats(ap_ts, ic='aicc', seasonal.periods=12),
  mod_bats = bats(ap_ts, ic='aicc', seasonal.periods=12),
  mod_stl = stlm(ap_ts, s.window=12, ic='aicc', robust=TRUE, method='ets'),
  mod_sts = StructTS(ap_ts)
)
?forecast()
forecasts <- lapply(models, forecast, 12)
forecasts$naive <- naive(ap_ts, 12)


























