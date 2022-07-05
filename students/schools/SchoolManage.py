class SchoolManage():
    def checkSchoolExists(_model_, Id, action):
        if action == 'all':
            get_data_school = _model_.objects.filter(id=Id).values().first()
            return get_data_school
        elif action == 'student_count':
            get_data_student = _model_.objects.filter(school_id=Id).count()
            return get_data_student   

