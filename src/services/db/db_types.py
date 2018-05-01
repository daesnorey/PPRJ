""""
Db_types file contain DbTypes class
"""

class DbTypes(object):
    """DbTypes."""

    NULL = 'DBT_NULL'
    NOT_NULL = 'DBT_NOT_NULL'
    DATE_MONTH = 'DBT_DATE_MONTH'
    DATE_YEAR = 'DBT_DATE_YEAR'

    def __init__(self):
        self.__sentences = {DbTypes.NULL: 'IS NULL',
                            DbTypes.NOT_NULL: 'IS NOT NULL',
                            DbTypes.DATE_MONTH: 'EXTRACT(MONTH FROM {}) = EXTRACT(MONTH FROM SYSDATE)',
                            DbTypes.DATE_YEAR: 'EXTRACT(YEAR FROM {}) = EXTRACT(YEAR FROM SYSDATE)'}

    def get_sentences(self, input_type=None):
        """Method get_sentences."""
        if not input_type:
            return self.__sentences
        else:
            return self.__sentences[input_type]

    @staticmethod
    def get_sentence(input_type):
        """Method get_sentence."""
        __db_types = DbTypes()
        if input_type in __db_types.get_sentences():
            return __db_types.get_sentences(input_type)
        else:
            raise KeyError("Tipo no encontrado")

    @staticmethod
    def exist(input_type):
        """Method exist."""
        return input_type in DbTypes().get_sentences()
