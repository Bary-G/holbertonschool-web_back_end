export default function getStudentIdsSum(array) {
    if (!Array.isArray(array)) {
        return 0;
    }
    return array.reduce((sum, item) => sum + item.id, 0);
}