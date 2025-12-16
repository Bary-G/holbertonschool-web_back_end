export default function updateStudentGradeByCity(array, city, grades) {
    if (!Array.isArray(array)) {
        return [];
    }
    if (typeof city !== "string") {
        return [];
    }
    if (!Array.isArray(grades)) {
        return [];
    }
    return array.filter(item => typeof item.location === "string" && item.location === city).map(student => {
        const gradeObj = grades.find(g => g.studentId === student.id);
        return {
            ...student,
            grade: gradeObj ? gradeObj.grade : 'N/A'
        };
    });
}