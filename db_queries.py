# all SQL-queries to DB used in tests

class DBQueries():

    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def get_all_projects(self):
        self.db_cursor.execute('''
            SELECT Projects.id, Resourses."name" as project_name, 
            Resourses.description as project_description, 
            Projects.color as project_color, Projects.department_id, 
            Departments.organization_id, Projects.created_at, 
            Projects.updated_at 
            FROM public.projects as Projects 
            LEFT JOIN public.resources as Resourses 
            ON Resourses.id = Projects.resource_id 
            LEFT JOIN public.departments as Departments 
            ON Projects.department_id = Departments.id 
            ORDER BY Projects.id''')
        return self.db_cursor.fetchall()


    def get_project_by_name(self, name):
        self.db_cursor.execute(f'''
            SELECT Projects.id, Resourses."name" as project_name, Resourses.description as project_description,
            Projects.color as project_color, Projects.department_id, Departments.organization_id,
            Projects.created_at, Projects.updated_at
            FROM public.projects as Projects
            LEFT JOIN public.resources as Resourses
            ON Resourses.id = Projects.resource_id
            LEFT JOIN public.departments as Departments
            ON Projects.department_id = Departments.id
            WHERE Resourses."name" = '{name}'
            ORDER BY Projects.id
        ''')
        record_found = self.db_cursor.fetchall()
        if len(record_found) == 0:
            return None
        return record_found[0]  # index 0 because expecting only one record


    def get_project_by_id(self, id):
        self.db_cursor.execute(f'''
            SELECT Projects.id, Resourses."name" as project_name, Resourses.description as project_description,
            Projects.color as project_color, Projects.department_id, Departments.organization_id,
            Projects.created_at, Projects.updated_at
            FROM public.projects as Projects
            LEFT JOIN public.resources as Resourses
            ON Resourses.id = Projects.resource_id
            LEFT JOIN public.departments as Departments
            ON Projects.department_id = Departments.id
            WHERE Projects.id = '{id}'
            ORDER BY Projects.id
        ''')
        record_found = self.db_cursor.fetchall()
        if len(record_found) == 0:
            return None
        return record_found[0]  # index 0 because expecting only one record

