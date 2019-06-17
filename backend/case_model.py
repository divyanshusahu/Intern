from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class CaseModel(Model) :
	class Meta :
		table_name = "cases"
		host = "http://localhost:8000"
	case_id = UnicodeAttribute(hash_key=True)
	job_id = UnicodeAttribute(range_key=True)