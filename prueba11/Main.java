package prueba11;
public class Main {

    public static conjuntoTDA CopiarConjunto(conjuntoTDA original) {
		conjuntoTDA copia = new conjuntoAO();
		conjuntoTDA aux = new conjuntoAO();
		copia.InicializarConjunto();
		aux.InicializarConjunto();
		int elemento;
		while (! original.ConjuntoVacio()) {
			elemento = original.Elegir();
			aux.Agregar(elemento);
			original.Sacar(elemento);}
		while (! aux.ConjuntoVacio()) {
			elemento = aux.Elegir();
			original.Agregar(elemento);
			copia.Agregar(elemento);
			aux.Sacar(elemento);}
		return copia;
	}
	
	public static void MostrarConjunto (conjuntoTDA original) {
		conjuntoTDA conjunto1 = CopiarConjunto(original);
		System.out.print("[");
		while (! conjunto1.ConjuntoVacio()) {
			int elemento2 = conjunto1.Elegir();
			System.out.print(elemento2);
			conjunto1.Sacar(elemento2);
			if (! conjunto1.ConjuntoVacio())
				System.out.print(", ");
			else
				System.out.println("]");
		}
	}

    public static void main(String [] args){
        conjuntoTDA prueba = new conjuntoAO();
        prueba.InicializarConjunto();
        prueba.Agregar(1);
		prueba.Agregar(3);
		prueba.Agregar(5);
		prueba.Agregar(7);
		prueba.Agregar(9);
		MostrarConjunto(prueba);
    }
}