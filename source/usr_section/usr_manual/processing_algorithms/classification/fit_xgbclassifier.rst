
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-FitXgbclassifier:

*****************
Fit XGBClassifier
*****************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Implementation of the scikit-learn API for `XGBoost <https://xgboost.readthedocs.io/en/stable/>`_ `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_.

..
  ## AUTOGENERATED DESCRIPTION END

An XGBoost (Extreme Gradient Boosting) classifier is an ensemble learning algorithm based on decision trees.XGBoost builds an ensemble of decision trees and uses gradient boosting to improve model accuracy.

Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select a training dataset or create one by clicking the processing algorithm icon, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/classification/img/fitxgb_interface.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Classifier` [string]
    Scikit-learn python code. See `XGBClassifier <https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=XGBClassifier#xgboost.XGBClassifier>`_ for information on different parameters.
    Default::

        from xgboost import XGBClassifier
        classifier = XGBClassifier\(n_estimators=100\)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**

:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:FitXgbclassifier``::

    ----------------
    Arguments
    ----------------

    classifier: Classifier
        Default value:    from xgboost import XGBClassifier
    classifier = XGBClassifier(n_estimators=100)
        Argument type:    string
        Acceptable values:
            - String value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    dataset: Training dataset (optional)
        Argument type:    file
        Acceptable values:
            - Path to a file
    outputClassifier: Output classifier
        Argument type:    fileDestination
        Acceptable values:
            - Path for new file

    ----------------
    Outputs
    ----------------

    outputClassifier: <outputFile>
        Output classifier

..
  ## AUTOGENERATED COMMAND USAGE END

