"""oracle.py.

db_connection.py file will contain the connection behaviour
to the database
"""
import copy
import cx_Oracle


class Oracle(object):
    """Oracle class will handle the conection to the database."""

    def __init__(self):
        """Constructor."""
        self.__data_base = None
        self.__cursor = None

    def __open(self, debug=False):
        """Connect to the database."""
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
        """Get cursor connection."""
        if self.__cursor is None:
            self.__open()

        return self.__cursor

    def execute(self, query, bindvars=None, commit=False):
        """Execute query, return cursor."""
        response = self.get_cursor().execute(query, bindvars)

        if commit is True:
            self.__data_base.commit()

        return response

#######################################################################
    def get_join_select(self, fields=None, conditions=None,
                        join_fields=None, *table):
        """Method get_query.

        @param table: table name in database
        @param fields: dictionary which contain the fields to affect.
        @param condition: dictionary which contain the fields and
        values to filter
        """
        if not fields:
            fields = []
        if not conditions:
            conditions = {}
        if not join_fields:
            join_fields = {}

        __inst = self.get_join_instruction(fields, len(table), join_fields)
        __inst += self.get_conditions(1, conditions)

        query = __inst
        for number in range(len(table)):
            str_replace = ":table" + str(number)
            query = query.replace(str_replace, table[number])

        return query

    def get_join_instruction(self, fields, n_tables=1, join=None):
        """get_instruction.

        This method will evaluate the action and will return the right
        instruction
        """
        if not join:
            join = []
        __ini = "SELECT :fields FROM :table0"
        if n_tables > 1:
            for index in range(n_tables - 1):
                to_join = join[index]
                str_table = ":table" + str(index + 1)
                str_join = ""
                __ini += " INNER JOIN " + str_table
                print "to_join", to_join
                for field in to_join:
                    print "field", field
                    if str_join:
                        str_join += " AND "
                    str_join += str_table + "." + field
                    str_join += "= :table0." + field
                __ini += " ON " + str_join

        __inst = ""

        for field in fields:
            if __inst:
                __inst += ","

            __inst += field

        if not fields:
            __inst = "*"

        response = __ini.replace(":fields", __inst)
        return response
#######################################################################

    def get_query(self, table, fields=None, conditions=None, action=1):
        """Method get_query.

        @param table: table name in database
        @param fields: dictionary which contain the fields to affect.
        @param condition: dictionary which contain the fields and values to
        filter
        @param action: 0=INSERT, 1=SELECT, 2=UPDATE, 3=DELETE
        """
        if not fields:
            fields = []
        if not conditions:
            conditions = {}
        __inst = self.get_instruction(action, fields)
        __inst += self.get_conditions(action, conditions)

        query = __inst.replace(":table", table)

        return query

    def get_instruction(self, action, fields):
        """get_instruction.

        This method will evaluate the action and will return the right
        instruction
        """
        __ini = ""

        if action == 0:
            __ini = "INSERT INTO :table (:fields) VALUES (:values)"
        elif action == 1:
            __ini = "SELECT :fields FROM :table"
        elif action == 2:
            __ini = "UPDATE :table SET :fields"
        elif action == 3:
            __ini = "DELETE FROM :table"
            return __ini

        __inst = ""
        __values = ""
        for field in fields:
            if __inst:
                __inst += ","
                __values += ","

            if action == 2:
                __inst += field + "=:" + field
            else:
                __inst += field
                __values += ":" + field

        if not fields and action == 1:
            __inst = "*"

        response = __ini.replace(":fields", __inst).replace(":values",
                                                            __values)
        return response

    def get_conditions(self, action, conditions):
        """Method get_conditions.

        this method will evaluate the action and the conditions
        if the action is 0 or there are no conditions then it returns an empty
        string
        otherwise it return the right condition
        """
        s_conditions = len(conditions)
        if action == 0 or s_conditions == 0:
            return ""

        __condition = " WHERE "
        __cond = ""

        for condition in conditions:
            if __cond:
                __cond += " AND "
            __cond += condition + "=:" + condition

        __condition += __cond
        return __condition

    def save(self, table, generic_object, name_id):
        """Method save.

        @attribute table
        @attribute generic_object
        @attribute name_id
        """
        __fields = copy.copy(generic_object)
        del __fields[name_id]

        id_object = generic_object[name_id]
        response = {}

        try:
            if id_object > 0:
                print "Update"
                __condition = {name_id: id_object}
                __update_query = self.get_query(table, __fields, __condition,
                                                action=2)
                print __update_query
                self.execute(__update_query, generic_object, True)
            else:
                print "Insert"
                __insert_query = self.get_query(table, fields=__fields,
                                                action=0)
                print __insert_query
                self.execute(__insert_query, __fields, True)
            response = dict(error=0, text="success")
        except Exception as e:
            print e
            response = dict(error=0001, text="There was an error saving")

        return response

    def delete(self, table, name_id, id_object):
        """Method delete.

        @attribute table
        @attribute name_id
        @attribute id_object
        """
        if not id_object:
            return dict(error=0002, text="Data incomplete at delete")

        __conditions = {name_id: id_object}

        __delete_query = self.get_query(table, conditions=__conditions,
                                        action=3)

        response = {}

        try:
            self.execute(__delete_query, __conditions, True)
            response = dict(error=0, text="success")
        except Exception:
            response = dict(error=0002, text="There was an error deleting")

        return response
