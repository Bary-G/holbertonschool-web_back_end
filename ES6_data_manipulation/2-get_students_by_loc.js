export default function getStudentsByLocation(array, city) {
    if (!Array.isArray(array)) {
        return [];
    }
    if (typeof city !== "string") {
        return [];
    }
    return array.filter(item => typeof item.location === "string" && item.location === city);
}