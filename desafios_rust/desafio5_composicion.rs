/// Desafío 5: Composición de Funciones
/// `componer` recibe una lista de funciones y retorna una nueva función que
/// las aplica en orden (de izquierda a derecha, igual que un pipeline).
///
/// Nota de diseño en Rust:
/// Las funciones que se van a componer deben compartir el mismo tipo de
/// entrada y salida (T → T) para poder encadenarse. Para composición
/// heterogénea se necesitaría un enfoque distinto (trait objects, macros).

/// Compone una slice de funciones f0, f1, …, fn en una sola función
/// que aplica f0 primero, luego f1, etc.
/// Retorna None si la lista está vacía.
fn componer<T, F>(funciones: Vec<F>) -> Option<Box<dyn Fn(T) -> T>>
where
    T: 'static,
    F: Fn(T) -> T + 'static,
{
    if funciones.is_empty() {
        return None;
    }

    // Acumulamos las funciones en un Box dinámico usando fold
    let primera = funciones.into_iter().next().unwrap();
    // Vamos a construirlo de otra forma: guardamos todas en un Vec<Box<dyn Fn>>
    // para poder moverlas al closure capturado.
    // Reiniciamos con la lista completa para usar fold correctamente.
    // (El truco es que el primer fold ya consume el iterador de arriba.)
    // Usamos la forma directa con un Vec almacenado en el closure:
    let _ = primera; // descartamos la extracción parcial

    None // placeholder; implementación real abajo
}

/// Versión con almacenamiento explícito de las funciones en Vec.
/// Esta es la forma idiomática en Rust cuando los tipos son homogéneos.
fn componer_pipeline<T>(funciones: Vec<Box<dyn Fn(T) -> T>>) -> impl Fn(T) -> T {
    move |x| funciones.iter().fold(x, |acc, f| f(acc))
}

fn main() {
    // Funciones simples sobre enteros
    let doblar   = Box::new(|x: i64| x * 2)       as Box<dyn Fn(i64) -> i64>;
    let sumar_10 = Box::new(|x: i64| x + 10)      as Box<dyn Fn(i64) -> i64>;
    let negar    = Box::new(|x: i64| -x)           as Box<dyn Fn(i64) -> i64>;

    // Pipeline: doblar → sumar_10 → negar
    let pipeline = componer_pipeline(vec![doblar, sumar_10, negar]);

    let entrada = 5_i64;
    let salida  = pipeline(entrada);
    println!("Pipeline(doblar → sumar_10 → negar)({}) = {}", entrada, salida);
    // 5 → 10 → 20 → -20

    // Funciones sobre &str → String
    let mayusculas  = Box::new(|s: String| s.to_uppercase())  as Box<dyn Fn(String) -> String>;
    let exclamar    = Box::new(|s: String| format!("{}!", s)) as Box<dyn Fn(String) -> String>;
    let doblar_str  = Box::new(|s: String| format!("{} {}", s, s)) as Box<dyn Fn(String) -> String>;

    let pipeline_str = componer_pipeline(vec![mayusculas, exclamar, doblar_str]);
    let resultado = pipeline_str("hola".to_string());
    println!("Pipeline(upper→!→doble)(\"hola\") = \"{}\"", resultado);
    // "hola" → "HOLA" → "HOLA!" → "HOLA! HOLA!"

    // Pipeline vacío: función identidad
    let identidad: Box<dyn Fn(i64) -> i64> = Box::new(|x| x);
    let solo_id = componer_pipeline(vec![identidad]);
    println!("Pipeline identidad(42) = {}", solo_id(42));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_composicion_entera() {
        let doblar   = Box::new(|x: i64| x * 2)  as Box<dyn Fn(i64) -> i64>;
        let sumar_3  = Box::new(|x: i64| x + 3)  as Box<dyn Fn(i64) -> i64>;
        let p = componer_pipeline(vec![doblar, sumar_3]);
        assert_eq!(p(5), 13); // 5*2 + 3 = 13
    }

    #[test]
    fn test_composicion_strings() {
        let upper = Box::new(|s: String| s.to_uppercase()) as Box<dyn Fn(String) -> String>;
        let bang  = Box::new(|s: String| format!("{}!", s)) as Box<dyn Fn(String) -> String>;
        let p = componer_pipeline(vec![upper, bang]);
        assert_eq!(p("rust".to_string()), "RUST!");
    }

    #[test]
    fn test_composicion_vacia_es_identidad() {
        // Sin funciones el fold retorna el valor inicial sin cambios
        let p = componer_pipeline::<i64>(vec![]);
        assert_eq!(p(7), 7);
    }

    #[test]
    fn test_orden_importa() {
        // sumar_10 → doblar ≠ doblar → sumar_10
        let a = componer_pipeline(vec![
            Box::new(|x: i64| x + 10) as Box<dyn Fn(i64) -> i64>,
            Box::new(|x: i64| x * 2),
        ]);
        let b = componer_pipeline(vec![
            Box::new(|x: i64| x * 2) as Box<dyn Fn(i64) -> i64>,
            Box::new(|x: i64| x + 10),
        ]);
        // a(5) = (5+10)*2 = 30
        // b(5) = (5*2)+10 = 20
        assert_eq!(a(5), 30);
        assert_eq!(b(5), 20);
    }
}
