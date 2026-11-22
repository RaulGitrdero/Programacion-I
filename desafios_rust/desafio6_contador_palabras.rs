/// Desafío 6: Contador de Palabras
/// Lee un archivo de texto, cuenta las ocurrencias de cada palabra,
/// y escribe las estadísticas en un nuevo archivo.
///
/// Uso: cargo run --bin desafio6 <archivo_entrada> [archivo_salida]
/// Si no se indica salida, escribe a "estadisticas_palabras.txt".

use std::collections::HashMap;
use std::env;
use std::fs;
use std::io::{self, Write};

/// Lee el contenido del archivo y retorna un HashMap<palabra, conteo>.
/// Las palabras se normalizan a minúsculas y se eliminan signos de puntuación.
fn contar_palabras(texto: &str) -> HashMap<String, usize> {
    let mut mapa: HashMap<String, usize> = HashMap::new();

    for token in texto.split_whitespace() {
        // Eliminar puntuación de los extremos y convertir a minúsculas
        let palabra: String = token
            .chars()
            .filter(|c| c.is_alphabetic() || *c == '-')  // guiones internos permitidos
            .collect::<String>()
            .to_lowercase();

        if !palabra.is_empty() {
            *mapa.entry(palabra).or_insert(0) += 1;
        }
    }

    mapa
}

/// Convierte el HashMap en un Vec ordenado de mayor a menor frecuencia,
/// y por orden alfabético cuando hay empate.
fn ordenar_por_frecuencia(mapa: &HashMap<String, usize>) -> Vec<(&str, usize)> {
    let mut lista: Vec<(&str, usize)> = mapa
        .iter()
        .map(|(k, &v)| (k.as_str(), v))
        .collect();

    lista.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(b.0)));
    lista
}

/// Genera el contenido del archivo de estadísticas.
fn generar_reporte(mapa: &HashMap<String, usize>) -> String {
    let total_tokens: usize = mapa.values().sum();
    let palabras_unicas = mapa.len();
    let ordenadas = ordenar_por_frecuencia(mapa);

    let mut salida = String::new();

    salida.push_str("=== Estadísticas de palabras ===\n\n");
    salida.push_str(&format!("Total de palabras (con repetición) : {}\n", total_tokens));
    salida.push_str(&format!("Palabras únicas                    : {}\n\n", palabras_unicas));
    salida.push_str(&format!("{:<25} {:>8}\n", "PALABRA", "CONTEO"));
    salida.push_str(&"-".repeat(35));
    salida.push('\n');

    for (palabra, conteo) in &ordenadas {
        salida.push_str(&format!("{:<25} {:>8}\n", palabra, conteo));
    }

    salida
}

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Uso: {} <archivo_entrada> [archivo_salida]", args[0]);
        eprintln!("Ejemplo: {} mi_texto.txt estadisticas.txt", args[0]);
        std::process::exit(1);
    }

    let ruta_entrada = &args[1];
    let ruta_salida = if args.len() >= 3 {
        args[2].clone()
    } else {
        "estadisticas_palabras.txt".to_string()
    };

    // Leer archivo de entrada
    let contenido = fs::read_to_string(ruta_entrada)
        .map_err(|e| {
            eprintln!("Error leyendo '{}': {}", ruta_entrada, e);
            e
        })?;

    println!("Archivo leído: {} ({} bytes)", ruta_entrada, contenido.len());

    // Contar palabras
    let mapa = contar_palabras(&contenido);
    let reporte = generar_reporte(&mapa);

    // Escribir estadísticas
    let mut archivo = fs::File::create(&ruta_salida)?;
    archivo.write_all(reporte.as_bytes())?;

    println!("Estadísticas escritas en: {}", ruta_salida);
    println!("Palabras únicas encontradas: {}", mapa.len());

    // Mostrar top-5 en consola
    println!("\nTop 5 palabras más frecuentes:");
    for (palabra, conteo) in ordenar_por_frecuencia(&mapa).iter().take(5) {
        println!("  {:20} → {}", palabra, conteo);
    }

    Ok(())
}

// ── Texto de ejemplo incluido en el desafío ───────────────────────────────────
// (usado en los tests para no depender de archivos externos)
#[cfg(test)]
mod tests {
    use super::*;

    const TEXTO_EJEMPLO: &str = "\
        En un lugar de la Mancha de cuyo nombre no quiero acordarme \
        no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero \
        adarga antigua rocín flaco y galgo corredor \
        Una olla de algo más vaca que carnero salpicón las más noches \
        duelos y quebrantos los sábados lantejas los viernes \
        algún palomino de añadidura los domingos \
        consumían las tres partes de su hacienda";

    #[test]
    fn test_contar_basico() {
        let mapa = contar_palabras(TEXTO_EJEMPLO);
        // "de" aparece varias veces
        assert!(*mapa.get("de").unwrap_or(&0) >= 4);
        // "la" aparece al menos una vez
        assert!(*mapa.get("la").unwrap_or(&0) >= 1);
    }

    #[test]
    fn test_total_palabras() {
        let mapa = contar_palabras(TEXTO_EJEMPLO);
        let total: usize = mapa.values().sum();
        assert!(total > 0);
    }

    #[test]
    fn test_minusculas() {
        let texto = "Hola hola HOLA";
        let mapa = contar_palabras(texto);
        assert_eq!(mapa.get("hola"), Some(&3));
        assert_eq!(mapa.len(), 1);
    }

    #[test]
    fn test_puntuacion_ignorada() {
        let texto = "perro, perro. perro! ¿perro?";
        let mapa = contar_palabras(texto);
        assert_eq!(mapa.get("perro"), Some(&4));
    }

    #[test]
    fn test_texto_vacio() {
        let mapa = contar_palabras("");
        assert!(mapa.is_empty());
    }

    #[test]
    fn test_orden_frecuencia() {
        let texto = "a a a b b c";
        let mapa = contar_palabras(texto);
        let ordenadas = ordenar_por_frecuencia(&mapa);
        assert_eq!(ordenadas[0], ("a", 3));
        assert_eq!(ordenadas[1], ("b", 2));
        assert_eq!(ordenadas[2], ("c", 1));
    }

    #[test]
    fn test_reporte_contiene_header() {
        let mapa = contar_palabras("hola mundo");
        let reporte = generar_reporte(&mapa);
        assert!(reporte.contains("Estadísticas"));
        assert!(reporte.contains("PALABRA"));
        assert!(reporte.contains("hola"));
        assert!(reporte.contains("mundo"));
    }
}
