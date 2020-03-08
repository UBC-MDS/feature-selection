def forward_selection(scorer, X, y, min_features=1, max_features=5):
    '''
    The Forward Selection is an algorithm used to select features.
    It starts as an empty model, and add the variable with the
    best improvement in the model. The process is iteratively 
    repeated and it stops when the remaining variables doesn't
    improve the accuracy of the model.

    Parameters
    ----------
    scorer : function
        A custom user-supplied function that accepts X and y (as defined below)
        as input and returns the index of the column with the lowest weight.
    X : array-like of shape
        training dataset
    y : array-like of shape
        test dataset
    min_features : int (default=None)
        number of minimum features to select
    max_features : int (default=10)
        number of maximum features to select

    Returns
    -------
    numpy ndarray
      Numeric array of selected features

    Examples
    --------
    >>> from sklearn.linear_model import LinearRegression
    >>> from sklearn.datasets import make_friedman1
    >>> data, target = make_friedman1(n_samples=200, n_features=15, random_state=0)
    >>> def my_scorer_fn2(X, y):
    >>>      lm = LinearRegression().fit(X, y)
    >>>      return 1 - lm.score(X, y)
    >>>
    >>> forward_selection(my_scorer_fn, data, target, max_features=7)
    array([0, 2, 3, 7, 9, 12, 13])
    '''
    ftr_select = []
    scores = []
    fn_score = []
    ftr_no_select = list(range(0, X.shape[1]))
    flag = False
    X_new = []

    for j in range(0, max_features):
        for i in ftr_no_select:
            X_new = X[:, ftr_select + [i] ]
            fn_score.append(scorer(X_new, y))

        # create data frame with the scores
        data = {'number': ftr_no_select, 'fn_score':fn_score}
        df = pd.DataFrame(data)

        best_one = np.max(df.fn_score) 
        if (len(ftr_select) > 0 and best_one < np.max(scores) and len(ftr_select) > min_features):
            flag = True
            break            

        x = df[df.fn_score == best_one].number
        scores.append(best_one)
        ftr_select.append(int(x))
        ftr_no_select.remove(int(x))

        data = {}
        fn_score = []

    return ftr_select