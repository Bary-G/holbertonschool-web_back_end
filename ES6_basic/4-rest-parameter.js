export default function returnHowManyArguments(...args) {
  let num = 0;
  for (let num of args) num += 1;
  return args.length;
}