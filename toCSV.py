import tabula

tabula.convert_into("alunos.pdf", "alunos.csv", output_format="csv", pages="all")
tabula.convert_into("alunos.pdf", "alunos.json", output_format="json", pages="all")
