package u9;
import java.awt.print.Printable;
import java.util.Iterator;

public class LinkedListEventQueue<E> implements EventQueue, Iterable<E> {
	
	private ListNode head;
	private ListNode tail;

	public LinkedListEventQueue() {
		head = new ListNode();
		tail = null;
	}

	private class ListNode {
		Event elem;
		ListNode next;
		
		public ListNode(Event event, ListNode next) {
			this.elem = event;
			this.next = next;
		}
		
		public ListNode() {
			this.elem = null;
			this.next = null;
		}
		
		public String toString() {
			return this.elem.getTime() + " | " + this.elem.getEventTypes();
		}
	}
	
	private class QueueIterator implements Iterator<E> {
		ListNode current;
		
		@Override
		public boolean hasNext() {
			return current != null;
		}

		@Override
		public E next() {
			if (current == null) {
				return null;
			}
			E res = (E) current.elem;
			current = current.next;
			return res;
		}
	}
	
	@Override
	public int size() {
		int size = 0;
		ListNode current = head;
		while (current.next != null) {
			current = current.next;
			size ++;
		}
		return size;
	}

	@Override
	public boolean isEmpty() {
		return head.next == null;
	}

	@Override
	public void insert(Event event) {
		ListNode tmp = new ListNode(event, null);
		if(isEmpty()) {
			head.next = tail = tmp;
		} else {
			if (event.getTime().isAfter(tail.elem.getTime()) || event.getTime().isEqual(tail.elem.getTime())) {
				tail.next = tmp;
				tail = tmp;
			} else {
				ListNode current = head.next;
				while (current.next != null) {
					if (current.next.elem.getTime().isAfter(event.getTime())) {
						tmp.next = current.next;
						current.next = tmp;
					}
					current = current.next;
				}
			}
		
		}
	}

	@Override
	public Event first() throws EmptyQueueException {
		if(isEmpty()) {
			throw new EmptyQueueException();
		} else {
			return head.next.elem;
		}
	}

	@Override
	public Event removeFirst() throws EmptyQueueException {
		if (isEmpty()) {
			throw new EmptyQueueException();
		} else {
			Event toRemove = head.next.elem;
			head.next = head.next.next;
			return toRemove;
		}
		
	}

	@Override
	public Iterator<E> iterator() {
		return null;
	}
}

	



