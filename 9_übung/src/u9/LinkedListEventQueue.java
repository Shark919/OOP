package u9;
import java.util.Iterator;

public class LinkedListEventQueue<E> implements EventQueue, Iterable<E> {
	
	private ListNode<E> head;
	private ListNode<E> tail;

	public LinkedListEventQueue() {
		head = new ListNode<E>();
		tail = null;
	}

	private class ListNode<E> {
		Event elem;
		ListNode<E> next;
		
		public ListNode(Event event, ListNode<E> next) {
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
	
	@Override
	public int size() {
		int size = 0;
		ListNode<E> current = head;
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
		ListNode<E>tmp = new ListNode<E>(event, null);
		if(isEmpty()) {
			head.next = tail = tmp;
		} else {
			if (event.getTime().isAfter(tail.elem.getTime()) || event.getTime().isEqual(tail.elem.getTime())) {
				tail.next = tmp;
				tail = tmp;
			} else {
				ListNode<E> current = head.next;
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
		// TODO Auto-generated method stub
		return null;
	}

}

	



