export default function updateUniqueItems(map) {
    if (!(map instanceof Map)) {
        throw new TypeError("Cannot process")
    }
    for (let [name, quantity] of map) {
        if (quantity === 1) {
            map.set(name, 100);
        }
    }
    return map;
}