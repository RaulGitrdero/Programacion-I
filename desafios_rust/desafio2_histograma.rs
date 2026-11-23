/// Desafio 2: Generador de Histograma
/// Toma una lista de numeros y genera un histograma con asteriscos.
/// Cada barra es proporcional al valor del numero.


use std::io::{self, BufRead, Write};


fn imprimir_histograma(numeros: &[f64], ancho_max: usize) {
    // Si la lista no trae nada, avisamos y salimos
    if numeros.is_empty() {
        println!("No hay numeros para graficar.");
        return;
    }

    
    let max = numeros.iter().cloned().fold(f64::NEG_INFINITY, f64::max);


    if max <= 0.0 {
        println!("Todos los valores son <= 0, no se puede graficar.");
        return;
    }


    println!("\n--- Histograma ---");

    for (i, &n) in numeros.iter().enumerate() {

        let barras = if n > 0.0 {

            ((n / max) * ancho_max as f64).round() as usize
        } else {

            0
        };

        println!("{:>3} ({:>8.2}) | {}", i + 1, n, "*".repeat(barras));
    }
    println!("------------------");
}

fn main() {
    println!("Generador de Histograma");
    println!("Ingresa numeros separados por espacios (Enter para terminar):");

    print!("> ");
    io::stdout().flush().unwrap();


    let stdin = io::stdin();

    let mut linea = String::new();

    stdin.lock().read_line(&mut linea).unwrap();


    let numeros: Vec<f64> = linea

        .trim()
        .split_whitespace()
        .filter_map(|token| token.parse::<f64>().ok())
        .collect();


    if numeros.is_empty() {
        println!("No se ingresaron numeros validos.");
        return;
    }

   
    println!("Numeros recibidos: {:?}", numeros);

    imprimir_histograma(&numeros, 40);
}


#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_histograma_no_falla_con_valores_positivos() {

        imprimir_histograma(&[1.0, 5.0, 3.0, 8.0, 2.0], 20);
    }

    #[test]
    fn test_histograma_vacio() {

        imprimir_histograma(&[], 20);
    }

    #[test]
    fn test_histograma_un_elemento() {

        imprimir_histograma(&[42.0], 20);
    }
}
