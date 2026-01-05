console.log("Welcome to Holberton School, what is your name?");
process.stdin.on("data", (data) => {
    const username = data.toString().trim();
    console.log(`Your name is: ${username}`);
    console.log("This important software is now closing");
    process.exit()
});