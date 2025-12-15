import Currency from "./3-currency.js";

export default class Pricing {
    constructor(amount, currency) {
        if (typeof amount !== "number") {
            throw new TypeError("Amount must be a number");
        }
        if (!(currency instanceof Currency)) {
            throw new TypeError("Currency must be a Currency instance");
        }
        this._amount = amount;
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }

    set amount(newamount) {
        if (typeof newamount === "number") {
            this._amount = newamount;
        } else {
            throw new Error("Amount must be a number");
        }
    }

    get currency() {
        return this._currency;
    }

    set currency(newcurrency) {
        if (newcurrency instanceof Currency) {
            this._currency = newcurrency;
        } else {
            throw new Error("Currency must be a Currency instance");
        }
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }

    static convertPrice(amount, conversionRate) {
        if (typeof amount !== "number") {
            throw new TypeError("Amount must be a number");
        }
        if (typeof conversionRate !== "number") {
            throw new TypeError("Conversion rate must be a number");
        }
        return amount * conversionRate;
    }
}