def dummy_metric(y_true, y_pred):
    return 0.5


def eval(model, X_val, y_val):
    y_pred = model.predict(X_val)
    # replace dummy_metric with actual metric
    score = dummy_metric(y_val, y_pred)
    return score
