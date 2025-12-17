export default function hasValuesFromArray(set, array) {
    if (!set instanceof Set) {
        return false
    }
    if (!Array.isArray(array)) {
        return [];
    }
    return array.every(element => set.has(element));
}