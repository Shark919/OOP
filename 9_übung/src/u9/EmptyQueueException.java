package u9;

public class EmptyQueueException extends Exception {

	public EmptyQueueException() {
		System.err.println("Queue is empty!");
	}
}
