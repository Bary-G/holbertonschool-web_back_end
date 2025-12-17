export default function groceriesList() {
    const name = ["Apples", "Tomatoes", "Pasta", "Rice", "Banana"]
    const quantity = [10, 10, 1, 1, 5]
    return new Map(name.map((item, index) => [item, quantity[index]]));
}