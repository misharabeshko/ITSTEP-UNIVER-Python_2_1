from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass



class Report(Document):
    def render(self) -> str:
        return "Формування та рендеринг звіту (Report)"

class Invoice(Document):
    def render(self) -> str:
        return "Формування та рендеринг рахунку (Invoice)"

class Contract(Document):
    def render(self) -> str:
        return "Формування та рендеринг контракту (Contract)"



class DocumentFactory:
    @staticmethod
    def create(doc_type: str) -> Document:
        doc_type = doc_type.lower()
        if doc_type == "report":
            return Report()
        elif doc_type == "invoice":
            return Invoice()
        elif doc_type == "contract":
            return Contract()
        else:
            raise ValueError(f"Невідомий тип документа: {doc_type}")



document_types = ["report", "invoice", "contract"]

for doc_name in document_types:
    doc = DocumentFactory.create(doc_name)
    print(doc.render())

