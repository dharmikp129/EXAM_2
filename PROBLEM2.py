# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:46:52 2022

@author: dharm
"""
path = "C:/Users/dharm/Downloads/peak.csv"
# methods for class evfit  ----
.rsquared <- function(obs, est) {
  m <- mean(obs)
  SSobs <- sum((m - obs)^2)
  SSres <- sum((obs - est)^2)
  return( 1 - SSres/SSobs)
}

print.evfit <- function(x, ...) {
  rp <- x[["T_Years_Event"]]
  if(!is.null(rp)) print(rp) else summary(x)
}

summary.evfit <- function(object, ...) {
  cat("", "Values:", sep = "")
  str(unname(object$values))

  if (object[["freq.zeros"]] > 0) {
    cat("Zero flow extremes: ", sum(object$values == 0) , " observations (",
        round(object[["freq.zeros"]], 2), "%)\n",
        "Using the ", c("un")[!object$is.censored], "censored time series.", sep = "")
  }

  cat("\n\n", "L-Moments:\n", sep = "")
  print(object$lmom)

  cat("\n", "Fitted Parameters of the Distribution:\n", sep = "")
  print.dist(object$parameters)
}

print.dist <- function(x) {
  if (is.list(x) && length(x) > 1) {
    for(i in seq_along(x)) print.dist(x[i])
    return(invisible())
  }

  distribution <- format(names(x)[1], width = 4)
  values <- lapply(x[[1]], function(x) signif(x, digits = 6))
  values <- paste(format(paste0(names(x[[1]]), ":"), width = 7),
                  format(values, width = 8), sep="", collapse = ",  ")

  cat("", distribution, "   ", values, "\n", sep = "")
}


# Gringorten Plotting Position for extreme values
gringorten <- function(x) {
  rank <- rank(x, na.last = "keep", ties.method = "first")
  len <- sum(!is.na(x))

  xx <- (rank - 0.44)/(len + 0.12)
  return(xx)
}


plot.evfit <- function(x, legend = TRUE, col = 1, extreme = x$extreme,
                       xlab = NULL, ylab = expression(italic(x)), log = TRUE,
                       ylim = NULL,
                       rp.axis = NULL, rp.lab = "Return period",
                       freq.axis = TRUE,
                       freq.lab = expression(paste("Frequency " *(italic(F)),
                                                   " = Non-Exceedance Probability P ",
                                                   (italic(X) <= italic(x)))),
                       ...)
{

  dist <- names(x[["parameters"]])
  # if there's more than one distribution to fit, ignore user specified color
  if (length(dist) > 1) col <- seq_along(dist)
  ylim <- if(is.null(ylim)) c(0, max(x$values, na.rm = TRUE)) else ylim

  # plot obersvations (points)
  if (log) {
    if(is.null(xlab)) xlab <- expression("Reduced variate,  " * -log(-log(italic(F))))
    evplot(x$values, xlab = xlab, ylab = ylab, col = col[1], rp.axis = FALSE,
           ylim = ylim, ...)
  } else {
    if(is.null(xlab)) xlab <- freq.lab
    plot(gringorten(x$values), x$values, col = col[1],
         xlim = c(0, 1), ylim = ylim,
         xlab = xlab, ylab = ylab, ...)
  }
