package u9;
import java.time.LocalDateTime;

public class Event {

	private LocalDateTime time;
	private EventTypes eventType;
	
	public Event(EventTypes eventType) {
		this.time = LocalDateTime.now();
		this.eventType = eventType;
	}

	public enum EventTypes {
		KAFEETRINKEN, DUSCHEN, STUDIEREN, LERNEN, ARBEITEN, ESSEN, KOCHEN, HAUSAUFGABEN, SCHLAFEN, PUTZEN
	}
	
	public LocalDateTime getTime() {
		return this.time;
	}
	
	public EventTypes getEventTypes() {
		return this.eventType;
	}
	
	public String toString() {
		return this.time + " | " + this.eventType;
	}
}

