
def brootforce():
    cv = model_selection.kFold(shuffle = True,random_state = 1)
    RMSE = []
    for i in np.arange(1,x_reduced_train.shape[1]+1):
        score = np.sqrt(-1 *model_selection.cross_val_score(lm,x_train,y_train,cv = cv,scoring= "neg_mean_squared_error").mean())
        RMSE.append(score)