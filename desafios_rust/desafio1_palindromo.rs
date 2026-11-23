/// Desafio 1: Palindromos
/// Determina si una cadena ingresada por el usuario es un palindromo,
/// ignorando espacios, puntuacion y capitalizacion



//use es el import de python std::io es el modulo para entrada/salida (teclado y pantalla). con {} importas varias cosas a la vez
use std::io::{self, Write};


fn limpiar(s: &str) -> String {
    s.chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| c.to_lowercase().next().unwrap())
        .collect()
}

/// Verifica si la cadena limpia es un palindromo.
fn es_palindromo(s: &str) -> bool {
    
    let limpio = limpiar(s);

    let invertido: String = limpio.chars().rev().collect();
    limpio == invertido
}

// main es donde arranca todo programa de Rust
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
        println!("\"{}\" ES un palindromo ✓", entrada);
    } else {
        println!("\"{}\" NO es un palindromo ✗", entrada);
    }
}

//estos test no son parte del programa principal buscan revisar el funcionamiento
//rustc .\desafio1_palindromo.rs
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
