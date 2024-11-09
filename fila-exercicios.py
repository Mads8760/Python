#Questão: Imagine uma fila utilizada para gerenciar a ordem de atendimento em um consultório médico"
#Se quatro pacientes são adicionados à fila e dois são atendidos, quem serão os próximos dois pacientes na ordem de atendimento?"
#Considere os pacientes “Paciente 1”, “Paciente 2”, “Paciente 3” e “Paciente 4”

#adicionanado a fila
consulta = ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 4"]
print(consulta)

#2 pacientes atendidos
atendidos = consulta.pop(0)
atendidos = consulta.pop(0)
#primeiro elemento da fila apos atendimento
print(consulta[0])
# proximos pacientes da fila
print(consulta)
