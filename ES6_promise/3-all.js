import * as utils from "./utils.js";

export default function handleProfileSignup() {
    return Promise.all([utils.uploadPhoto(), utils.createUser()])
        .then(result => {
            const photo = result[0];
            const user = result[1];
            console.log(`${photo.body} ${user.firstName} ${user.lastName}`)
        })
        .catch(error => (console.log("Signup system offline")))
}