from mongoengine import Document, EmbeddedDocument, fields


class EmployeeProjects(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    name = fields.StringField(max_length=255, required=False)
    startDate = fields.DateTimeField()
    endDAte = fields.DateTimeField()

class EmployeeSkills(EmbeddedDocument):
    tech = fields.StringField(max_length=200, required=True, null=False)
    experience = fields.StringField(
        max_length=255, required=True, null=True)
    level = fields.StringField(max_length=255, required=False)

class Employee(Document):
    empId = fields.StringField(max_length=10, required=True, null=False)
    empName = fields.StringField(max_length=100, required=True)
    workLocation = fields.StringField(max_length=255, required=False)
    skills = fields.EmbeddedDocumentListField(EmployeeSkills)
    projects = fields.EmbeddedDocumentListField(EmployeeProjects)
