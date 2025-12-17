export default function cleanSet(set, startString) {
    if (!(set instanceof Set)) {
        return "";
    }
    if (typeof startString !== "string") {
        return "";
    }
    if (startString === "") {
        return "";
    }
    return Array.from(set)
        .filter(item => typeof item === 'string' && item.startsWith(startString))
        .map(item => item.slice(startString.length))
        .join('-');
}