const fs = require('fs').promises;

async function countStudents(filePath) {
  try {
    await fs.access(filePath);

    const content = await fs.readFile(filePath, 'utf8');
    const lines = content.split('\n').filter((line) => line.trim() !== '');
    const headers = lines[0].split(',');

    const records = lines.slice(1).map((line) => {
      const values = line.split(',');
      return headers.reduce((obj, key, i) => {
        const newObj = obj;
        newObj[key] = values[i];
        return newObj;
      }, {});
    });

    const students = records.map((r) => r.firstname).filter(Boolean);
    const csStudents = records.filter((r) => r.field === 'CS');
    const sweStudents = records.filter((r) => r.field === 'SWE');

    const output = [
      `Number of students: ${students.length}`,
      `Number of students in CS: ${csStudents.length}. List: ${csStudents.map((r) => r.firstname).join(', ')}`,
      `Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.map((r) => r.firstname).join(', ')}`,
    ].join('\n');

    console.log(output);

    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
