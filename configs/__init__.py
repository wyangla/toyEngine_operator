rawCorpusPath = r'C:\desktop\workspace\dissertation_imp\dataset\yelp_dataset\dataset\review.json' # for testing
corpusPath = r'C:\desktop\workspace\toyProject\toyEngine_operator\corpus'
testCorpusPath = r'C:\desktop\workspace\toyProject\toyEngine_operator\corpus\test_1' # for testing, sub directions contains docs from different sources

sourceList = ['test_1', 'test_2'] # list of souces for generating the inverted index 

uPropFields = {
    'tf' : 'unit_generator.calculators.tf',
    'oh' : 'unit_generator.calculators.oh'
    }

logLevel = 'DEBUG'


languageProcessorMap = {'English': 'processors.Doc_processor_tf',
                        'Chinese': 'processors.Doc_processor_ch'}    # TODO: add language detector