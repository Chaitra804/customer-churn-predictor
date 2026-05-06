from sklearn.metrics import classification_report # pyright: ignore[reportMissingModuleSource]

def evaluate(model, X_val, y_val):
    y_pred = model.predict(X_val)
    print(classification_report(y_val, y_pred))