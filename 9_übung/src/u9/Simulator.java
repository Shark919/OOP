package u9;
import static u9.Event.EventTypes;

import java.util.Random;

/**
 * 
 * @author Chrisoph Meise, Tim Walz
 * Objektorientierte Programmierung
 * Tutorium Freitag 08 - 10 Uhr
 * 
 * Aufgabe 1
 * a ) Iteratoren werden in objektorientierten Programmiersprachen zur Verfügung gestellt um über Datenstrukturen
 * iterieren zu können, ohne die interne Konsistenz dieser zu gefährden (Stichwort Datenkapselung). 
 *
 * b) Innere Klassen sind zumeist Hilfsklassen, welche nur lokal (d.h. innerhalb einer Klasse) benötigt werden. Durch
 * sie kann eine Weitere Absraktionsebene geschaffen werden. Besonders häufig werden sie bei der Oberflächenentwicklung 
 * oder der Verwendung von Quantoren verwendet.
 */
public class Simulator {

	public static void main(String[] args) throws InterruptedException {
		LinkedListEventQueue<Event> myList = new LinkedListEventQueue<Event>();
		
		System.out.println("The new generated list should be empty: " + myList.isEmpty());
		
		Random random = new Random();
		for (int i = 0; i < 15; i++)
		{
		    EventTypes randomEvent = EventTypes.values()[random.nextInt(EventTypes.values().length)];
		    Thread.sleep(10);
		    myList.insert(new Event(randomEvent));
		}
		
		try {
			System.out.println("First element is: " + myList.first());
			System.out.println("size of list is: " + myList.size());
			System.out.println("Removing first element: " + myList.removeFirst());
			System.out.println("size of list is: " + myList.size());
			System.out.println("Is the list empty? " + myList.isEmpty());
		} catch (EmptyQueueException e) {
			e.printStackTrace();
		}
	}

}
