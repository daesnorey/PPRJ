"""
db_connection.py file will contain the connection behaviour
to the database
"""
import re
import cx_Oracle


class Oracle(object):
    """
    Oracle class will handle the conection to the database
    """

    def __init__(self):
        self.__data_base = None
        self.__cursor = None

    def __open(self, debug=False):
        """ Connect to the database """

        username = 'PPRJ'
        password = 'PPRJ123'
        hostname = '127.0.0.1'
        servicename = 'XE'
        port = 1521

        dsn_tns = cx_Oracle.makedsn(hostname, port, servicename)

        if debug is True:
            print dsn_tns

        try:
            self.__data_base = cx_Oracle.connect(username, password, dsn_tns)
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                print 'Please check your credentials.'
                # sys.exit()?
            else:
                print e

            # Very important part!
            raise

        # If the database connection succeeded create the cursor
        # we-re going to use.
        self.__cursor = self.__data_base.cursor()

    def __close(self):
        if self.__data_base is not None:
            self.__data_base.close()
            self.__data_base = None
        self.__cursor = None

    def get_cursor(self):
        """ get cursor connection """
        if self.__cursor is None:
            self.__open()

        return self.__cursor

    def execute(self, query, bindvars=None, commit=False):
        """ execute query
            return cursor
        """
        response = self.get_cursor().execute(query, bindvars)

        if commit is True:
            self.__data_base.commit()

        return response

    def get_query(self, table, fields=[], conditions=[], action=1):
	"""get_query.
	   @param table: table name in database
           @param fields: dictionary which contain the fields to affect.
           @param condition: dictionary which contain the fields and values to filter
           @param action: 0=INSERT, 1=SELECT, 2=UPDATE, 3=DELETE
        """

        __inst  = self.get_instruction(action, fields)
	__inst += self.get_conditions(action, fields)

	print __inst


    def get_instruction(self, action, fields):
	"""get_instruction
	   This method will evaluate the action and will return the right instruction
	"""

        __ini = ""

        if action == 0:
                __ini = "INSERT INTO :table (:fields) VALUES (:fields)"
        elif action == 1:
                __ini = "SELECT :fields FROM :table"
        elif action == 2:
                __ini = "UPDATE :table SET :fields"
	elif action == 3:
                __ini = "DELETE FROM :table"
                return __ini

        __inst = ""
        for field in fields:
            if __inst:
                __inst += ","

            if action == 2:
                __inst += field + "=:" + field
            else:
                __inst += field

        print __inst

    def get_conditions(self, action, conditions):
	"""get_conditions
	   this method will evaluate the action and the conditions
	   if the action is 0 or there are no conditions then it returns an empty string
	   otherwise it return the right condition
	"""

	if action == 0 or len(conditions) == 0:
		return ""

	__condition = " WHERE "
	__cond = ""

	for condition in conditions:
            if __cond:
                __cond += " AND "
            __cond += condition + "=:" + condition

	__condition += __cond

	return __condition

    def get_update_query(self, table, fields, conditions):
        """
        get_update_query
        """

        __query = "UPDATE :table SET :instructions WHERE :conditions"

        __inst = ""
        __cond = ""

        for field in fields:
            if __inst:
                __inst += ","
            __inst += field + "=:" + field

        for condition in conditions:
            if __cond:
                __cond += " AND "
            __cond += condition + "=:" + condition

        dic = dict(table=table, instructions=__inst, conditions=__cond)

        pattern = re.compile(r'\b(' + '|:'.join(dic.keys()) + r')\b')
        result = pattern.SUB(lambda x: dic[x.group()], __query)

        return result
    
