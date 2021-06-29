export default function getListStudentIds(listOfStudents) {
  if (!Array.isArray(listOfStudents)) return [];
  return listOfStudents.map((element) => element.id);
}
