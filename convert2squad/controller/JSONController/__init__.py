from typing import List

class JsonController:
    def __init__(self):
        self.data = []

    def name_of_paper(self, title: str) -> None:
        """
        Adds extra information to the object : Name of the paper

        Args:
            title (str): title of the paper
        """
        self.name = title

    def add_paragraph(self, context: str, list_of_q: List[str], list_of_ans: List[str]) -> None:
        """
        Adds a paragraph

        Args:
            context (str): text used to extract information
            list_of_q (List[str]): list of question
            list_of_ans (List[str]): list of answers
        """
        qas = []
        for q, a in zip(list_of_q, list_of_ans):
            if a and a in context:
                answer_start = context.index(a)
            else:
                answer_start = []

            qas.append({
                "question": q,
                "id": str(len(qas) + 1),
                "answers": [
                    {
                        "text": a if a else [],
                        "answer_start": answer_start
                    }
                ]
            })

        paragraph = {
            "context": context,
            "qas": qas
        }
        self.data.append(paragraph)

    def to_json(self) -> dict:
        """
        Returns the Object as a dictionary (JSON serializable)

        Returns:
            dict: JSON Serializable dictionary
        """
        return {
            "data": self.data,
            "version": "2.0"
        }
