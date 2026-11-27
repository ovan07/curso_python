from repository.alumnos_repository import AlumnosRepository
from model.alumnos_model import Alumno

class AlumnosService:
    repo = AlumnosRepository()

    def alta_alumno(self, alumno: Alumno):
        if self.repo.find_by_curso_email(alumno.curso, alumno.email):
            return None
        return self.repo.save(alumno)

    def buscar_alumnos(self):
        return self.repo.find_all()

    def buscar_alumnos_curso(self, curso):
        return self.repo.find_by_curso(curso)

    # def buscar_alumno_curso_email(self, curso, email):
    #     alumno = self.repo.find_by_curso_email(curso, email)
    #     print(alumno)
    #     if not alumno:
    #         return None
    #     return Alumno(**alumno)

    def eliminar_alumno(self, email):
        self.repo.delete_by_email(email)
