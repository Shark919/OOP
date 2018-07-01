package u9;

public interface EventQueue {
	public int size();
	/* Die Länge der EventQueue wird zurück gegeben */
	public boolean isEmpty();
	/* Fragt, ob die Warteschlange leer ist */
	public void insert(Event event);
	/* Ein Ereignis wird in die Warteschlange nach dem Zeitstempel einsortiert */
	public Event first() throws EmptyQueueException;
	/* Das erste Element der Warteschlange wird gelesen */
	public Event removeFirst() throws EmptyQueueException;
	/* Das erste Element der Warteschlange wird aus der Warteschlange entfernt und als Ergebnis der Methode zurückgegeben */
}
