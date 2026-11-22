/// Desafío 4: Implementación propia de map, filter y reduce
/// Versiones genéricas que toman closures y listas, igual que las funciones
/// built-in de Python pero expresadas con los tipos de Rust.

// ── map ──────────────────────────────────────────────────────────────────────
/// Aplica `f` a cada elemento de `lista` y retorna un Vec con los resultados.
fn mi_map<T, U, F>(lista: &[T], f: F) -> Vec<U>
where
    F: Fn(&T) -> U,
{
    lista.iter().map(f).collect()
}

// ── filter ───────────────────────────────────────────────────────────────────
/// Retorna un Vec con los elementos de `lista` que cumplen el predicado `pred`.
fn mi_filter<T, F>(lista: &[T], pred: F) -> Vec<&T>
where
    F: Fn(&T) -> bool,
{
    lista.iter().filter(|x| pred(x)).collect()
}

// ── reduce ───────────────────────────────────────────────────────────────────
/// Acumula `lista` con `f` partiendo de `inicial`.
/// Si la lista está vacía, retorna `inicial`.
fn mi_reduce<T, U, F>(lista: &[T], inicial: U, f: F) -> U
where
    F: Fn(U, &T) -> U,
{
    lista.iter().fold(inicial, f)
}

fn main() {
    let numeros = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // map: elevar al cuadrado
    let cuadrados = mi_map(&numeros, |x| x * x);
    println!("map (cuadrados)      : {:?}", cuadrados);

    // filter: solo pares
    let pares = mi_filter(&numeros, |x| *x % 2 == 0);
    println!("filter (pares)       : {:?}", pares);

    // reduce: suma total
    let suma = mi_reduce(&numeros, 0, |acc, x| acc + x);
    println!("reduce (suma)        : {}", suma);

    // reduce: producto total
    let producto = mi_reduce(&numeros, 1, |acc, x| acc * x);
    println!("reduce (producto)    : {}", producto);

    // Combinación: suma de cuadrados de pares
    let pares_vals: Vec<i32> = pares.into_iter().copied().collect();
    let cuadrados_pares = mi_map(&pares_vals, |x| x * x);
    let suma_cuad_pares = mi_reduce(&cuadrados_pares, 0, |acc, x| acc + x);
    println!("suma cuadrados pares : {}", suma_cuad_pares); // 4+16+36+64+100 = 220
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_map_doblar() {
        let v = vec![1, 2, 3];
        assert_eq!(mi_map(&v, |x| x * 2), vec![2, 4, 6]);
    }

    #[test]
    fn test_filter_positivos() {
        let v = vec![-2, -1, 0, 1, 2, 3];
        let pos = mi_filter(&v, |x| *x > 0);
        assert_eq!(pos, vec![&1, &2, &3]);
    }

    #[test]
    fn test_reduce_suma() {
        let v = vec![1, 2, 3, 4, 5];
        assert_eq!(mi_reduce(&v, 0, |acc, x| acc + x), 15);
    }

    #[test]
    fn test_reduce_lista_vacia() {
        let v: Vec<i32> = vec![];
        assert_eq!(mi_reduce(&v, 99, |acc, x| acc + x), 99);
    }

    #[test]
    fn test_map_strings() {
        let v = vec!["hola", "mundo"];
        let upper = mi_map(&v, |s| s.to_uppercase());
        assert_eq!(upper, vec!["HOLA", "MUNDO"]);
    }
}
