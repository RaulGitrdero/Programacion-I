/// Desafío 1: Palíndromos
/// Determina si una cadena ingresada por el usuario es un palíndromo,
/// ignorando espacios, puntuación y capitalización.

use std::io::{self, Write};

/// Limpia la cadena: convierte a minúsculas y retiene solo caracteres alfanuméricos.
fn limpiar(s: &str) -> String {
    s.chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| c.to_lowercase().next().unwrap())
        .collect()
}

/// Verifica si la cadena limpia es un palíndromo.
fn es_palindromo(s: &str) -> bool {
    let limpio = limpiar(s);
    let invertido: String = limpio.chars().rev().collect();
    limpio == invertido
}

fn main() {
    print!("Ingresa una palabra o frase: ");
    io::stdout().flush().unwrap();

    let mut entrada = String::new();
    io::stdin().read_line(&mut entrada).unwrap();
    let entrada = entrada.trim();

    if entrada.is_empty() {
        println!("No ingresaste nada.");
        return;
    }

    if es_palindromo(entrada) {
        println!("\"{}\" ES un palíndromo ✓", entrada);
    } else {
        println!("\"{}\" NO es un palíndromo ✗", entrada);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_palindromos_simples() {
        assert!(es_palindromo("oso"));
        assert!(es_palindromo("Ana"));
        assert!(es_palindromo("A man a plan a canal Panama"));
        assert!(es_palindromo("Anita lava la tina"));
    }

    #[test]
    fn test_no_palindromos() {
        assert!(!es_palindromo("hola"));
        assert!(!es_palindromo("mundo"));
    }

    #[test]
    fn test_cadena_vacia() {
        assert!(es_palindromo(""));
    }
}
