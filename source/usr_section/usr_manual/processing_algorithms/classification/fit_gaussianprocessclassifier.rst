
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-FitGaussianprocessclassifier:

*****************************
Fit GaussianProcessClassifier
*****************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Gaussian process `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ \(GPC\) based on Laplace approximation.
The implementation is based on Algorithm 3.1, 3.2, and 5.1 of Gaussian Processes for Machine Learning \(GPML\) by Rasmussen and Williams.

Internally, the Laplace approximation is used for approximating the non-Gaussian posterior by a Gaussian. Currently, the implementation is restricted to using the logistic link function. For multi-`class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ classification, several binary one-versus rest `classifiers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ are fitted. Note that this class thus does not implement a true multi-class Laplace approximation.
See `Gaussian Processes <http://scikit-learn.org/stable/modules/gaussian_process.html>`_ for further information.

..
  ## AUTOGENERATED DESCRIPTION END

Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select a training dataset or create one by clicking the processing algorithm icon, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/classification/img/gaussian_process_interface.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Classifier` [string]
    Scikit-learn python code. See `GaussianProcessClassifier <http://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html>`_ for information on different parameters.
    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.gaussian_process import GaussianProcessClassifier
        from sklearn.gaussian_process.kernels import RBF

        gpc = GaussianProcessClassifier\(RBF\(\), max_iter_predict=1\)
        classifier = make_pipeline\(StandardScaler\(\), gpc\)

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

``>qgis_process help enmapbox:FitGaussianprocessclassifier``::

    ----------------
    Arguments
    ----------------

    classifier: Classifier
        Default value:    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF

    gpc = GaussianProcessClassifier(RBF(), max_iter_predict=1)
    classifier = make_pipeline(StandardScaler(), gpc)
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

