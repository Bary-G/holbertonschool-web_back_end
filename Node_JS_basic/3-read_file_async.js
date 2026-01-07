const fs = require('fs').promises;
const path = require('path');

async function countStudents(cheminFichier) {
  try {
    // Vérifie si le fichier est accessible
    await fs.access(cheminFichier);

    // Lecture asynchrone du fichier
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

    const valeursColonne = resultat.map(r => r["firstname"]).filter(v => v);
    console.log(`Number of students: ${valeursColonne.length}`);

    const correspondancesCS = resultat.filter(r => r["field"] === "CS");
    console.log(
      `Number of students in CS: ${correspondancesCS.length}. List: ${correspondancesCS.map(r => r["firstname"]).join(', ')}`
    );

    const correspondancesSWE = resultat.filter(r => r["field"] === "SWE");
    console.log(
      `Number of students in SWE: ${correspondancesSWE.length}. List: ${correspondancesSWE.map(r => r["firstname"]).join(', ')}`
    );
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
