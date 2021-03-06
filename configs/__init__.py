rawCorpusPath = r'C:\desktop\workspace\dissertation_imp\dataset\yelp_dataset\dataset\review.json' # for testing
testCorpusPath = r'C:\desktop\workspace\toyProject\toyEngine_operator\corpus\test_3'  # contain 3 docs for testing

corpusPath = r'C:\desktop\workspace\toyProject\toyEngine_operator\corpus'
cachedFilePath = r'C:\desktop\workspace\toyProject\toyEngine\persistance\cached'    # for persist the processed docs


sourceList = ['test_1', 'test_2'] # list of souces for generating the inverted index 

uPropFields = {
    'tf' : 'unit_generator.calculators.tf',
    'oh' : 'unit_generator.calculators.oh'
    }

logLevel = 'DEBUG'


languageProcessorMap = {'English': 'processors.processor_plugins.Processor_plugin_en',
                        'Chinese': 'processors.processor_plugins.Processor_plugin_en'}    # TODO: add language detector

processedDocNamePrefix = '__proc__'

cpuNum = 4;