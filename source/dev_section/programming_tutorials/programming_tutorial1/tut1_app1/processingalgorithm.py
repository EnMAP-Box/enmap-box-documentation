# 0
from qgis.core import *
from .core import regressionBasedUnmixing

# 1
class RegressionBasedUnmixingProcessingAlgorithm(QgsProcessingAlgorithm):

    P_RASTER = 'inraster'
    P_VECTOR = 'invector'
    P_FIELD = 'field'
    P_COVERAGE = 'coverage'
    P_OVERSAMPLING = 'oversampling'
    P_OUTPUT_FRACTION = 'outfraction'
# 2
    def group(self):
        return 'Workshop'

    def groupId(self):
        return 'workshop' # internal id

    def displayName(self):
        return 'Regression-based Unmixing'

    def name(self):
        return 'RegressionBasedUnmixing' # internal id
# 3
    def initAlgorithm(self, configuration=None):

        # Define required user inputs.
        self.addParameter(QgsProcessingParameterRasterLayer(
            name=self.P_RASTER, description='Raster'))
        self.addParameter(QgsProcessingParameterVectorLayer(
            name=self.P_VECTOR, description='Vector', types=[2])) # polygons only
        self.addParameter(QgsProcessingParameterField(
            name=self.P_FIELD, description='Class attribute', parentLayerParameterName=self.P_VECTOR,
            type=QgsProcessingParameterField.Numeric))
        self.addParameter(QgsProcessingParameterNumber(
            name=self.P_COVERAGE, description='Minimum pixel coverage', type=QgsProcessingParameterNumber.Double,
            defaultValue=0.9, minValue=0, maxValue=1))
        self.addParameter(QgsProcessingParameterNumber(
            name=self.P_OVERSAMPLING, description='Oversampling factor', type=QgsProcessingParameterNumber.Integer,
            defaultValue=5, minValue=0, maxValue=10))
        self.addParameter(QgsProcessingParameterRasterDestination(
            name=self.P_OUTPUT_FRACTION, description='Output fraction'))
# 4
    def processAlgorithm(self, parameters, context, feedback):
        assert isinstance(feedback, QgsProcessingFeedback)

        # try to execute the core algorithm
        try:

            # pass all selected input parameters to the core algorithm
            regressionBasedUnmixing(
                filename=self.parameterAsOutputLayer(parameters, self.P_OUTPUT_FRACTION, context),
                rasterFilename=self.parameterAsRasterLayer(parameters, self.P_RASTER, context).source(),
                vectorFilename=self.parameterAsVectorLayer(parameters, self.P_VECTOR, context).source(),
                classAttribute=self.parameterAsString(parameters, self.P_FIELD, context),
                oversampling=self.parameterAsInt(parameters, self.P_OVERSAMPLING, context),
                coverage=self.parameterAsDouble(parameters, self.P_COVERAGE, context))

            # return all output parameters
            return {self.P_OUTPUT_FRACTION: self.parameterAsOutputLayer(parameters, self.P_OUTPUT_FRACTION, context)}

        # handle any uncatched exceptions
        except:
            # print traceback to console and pass it to the processing feedback object
            import traceback
            traceback.print_exc()
            for line in traceback.format_exc().split('\n'):
                feedback.reportError(line)
            return {}
# 5
    def shortHelpString(self):

        html = '' \
       '<p>This algorithm derives landcover pixel fractions from the given raster and vector maps, fits a ' \
       '<a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html">RandomForestRegressor</a> ' \
       'to that dataset and applies it to the the raster, predicting a (multi-class) landcover fraction map.</p>' \
       '<h3>Raster</h3>' \
       '<p>Input raster.</p>' \
       '<h3>Vector</h3>' \
       '<p>Input vector with landcover polygons.</p>' \
       '<h3>Class attribute</h3>' \
       '<p>Attribute defining the class ids (values between 1 and number of classes).</p>' \
       '<h3>Minimam pixel coverage</h3>' \
       '<p>Threshold between 0 and 1 that defines the minimal coverage a pixel must have to be concidered as training sample.</p>' \
       '<h3>Output fraction</h3>' \
       '<p>Output raster.</p>'
        return html
# 6
    def helpUrl(self, *args, **kwargs):
        return 'https://enmap-box-workshop2019.readthedocs.io'
# 7
    def createInstance(self):
        return type(self)()
