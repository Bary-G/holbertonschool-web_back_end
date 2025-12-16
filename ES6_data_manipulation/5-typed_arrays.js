export default function createInt8TypedArray(length, position, value) {
    if (typeof length !== "number") {
        return 0;
    }
    if (typeof position !== "number") {
        return 0;
    }
    if (typeof value !== "number") {
        return 0;
    }
    if (position < 0 || position >= length) {
        throw new Error("Position outside range");
    }
    const buffer = new ArrayBuffer(length);
    const view = new DataView(buffer);
    view.setInt8(position, value);

    return view;
}