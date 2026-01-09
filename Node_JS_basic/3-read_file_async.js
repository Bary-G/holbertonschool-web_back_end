const fs = require('fs').promises;

async function countStudents(cheminFichier) {
  try {
    await fs.access(cheminFichier);

    const contenu = await fs.readFile(cheminFichier, 'utf8');
    const lignes = contenu.split('\n').filter(l => l.trim() !== '');
    const enTêtes = lignes[0].split(',');

    const resultat = lignes.slice(1).map(ligne => {
      const valeurs = ligne.split(',');
      return enTêtes.reduce((obj, clé, i) => {
        obj[clé] = valeurs[i];
        return obj;
      }, {});
    });

    const valeursColonne = resultat.map(r => r['firstname']).filter(v => v);
    const correspondancesCS = resultat.filter(r => r['field'] === 'CS');
    const correspondancesSWE = resultat.filter(r => r['field'] === 'SWE');

    const output = [
      `Number of students: ${valeursColonne.length}`,
      `Number of students in CS: ${correspondancesCS.length}. List: ${correspondancesCS.map(r => r['firstname']).join(', ')}`,
      `Number of students in SWE: ${correspondancesSWE.length}. List: ${correspondancesSWE.map(r => r['firstname']).join(', ')}`
    ].join('\n');
    console.log(output)
    return output;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
