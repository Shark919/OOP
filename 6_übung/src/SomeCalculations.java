import java.util.Arrays;

/**
 * 
 * @author Christop Meise, Tim Walz
 * @version 1.0
 * OOP Tutorium Freitag 08-10:00 Uhr
 *
 */

public class SomeCalculations {

	/**
	 * Rekursive Berechnung der Quersumme von ganzen Zahlen
	 * @param number as integer value
	 * @return Quersumme 
	 */
	public static int querSumme(int number) {
		if (number < 10) {
			return number;
		} else {
			return number % 10 + querSumme(number / 10);
		}
	}
	
	/**
	 * Berechnet ob die Querumme einer Zahl und die Zahl selber
	 * durch drei teilbar ist
	 * @param number as integer value
	 * @return true | false
	 */
	public static boolean multipleOf3(int number) {
		Boolean isMultipleOf3 = false;
		if (querSumme(number) % 3 == 0 & number % 3 == 0 & number != 0) {
			return true;
		}
		return isMultipleOf3;
	}
	
	// Hinweis: Wir verwenden assertions zum Testen unserer Funktionen. Um diese in Eclipse
	// zu Berücksichtigen, muss in der Run-Cofiguration -> Arguments -> VM Arguments '-ea' als
	// Wert gesetzt sein.
	public static void main(String[] args) {
		int[] testArray = {0,1,2,3,5,10,16,84,88,12564};
		int[] solvedArrayQuersumme = {0,1,2,3,5,1,7,12,16,18};
		boolean[] solvedArrayMultipleOf3 = {false, false, false, true, false, false, false, true, false, true};
		
		System.out.println("Der Test startet mit folgenden Werten:");
		System.out.println("Getestete Werte: " + Arrays.toString(testArray));
		System.out.println("Erwartete Werte für querSumme() sind: " + Arrays.toString(solvedArrayQuersumme));
		System.out.println("Erwartete Werte für multipleOf3() sind: " + Arrays.toString(solvedArrayMultipleOf3));
		
		for (int i = 0; i < testArray.length; i++) {
			assert querSumme(testArray[i]) == solvedArrayQuersumme[i] : "Die Quersumme von " + testArray[i] + " wurde mit " + querSumme(testArray[i]) + " falsch berechnet";
			assert multipleOf3(testArray[i]) == solvedArrayMultipleOf3[i] : "Die Methode multipleOf3() lieferte für " + testArray[i] + " das Falsche Ergebnis"; 
		}
		
		System.out.println("Tests beendet");
	}
}
