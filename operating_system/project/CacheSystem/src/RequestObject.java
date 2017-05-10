
public class RequestObject {
	private int id;
	private int size;
	
	public RequestObject(int id, int size) {
		this.id = id;
		this.size = size;
	}

	public int getId() {
		return id;
	}

	public int getSize() {
		return size;
	}
	
	@Override
	public boolean equals(Object obj) {
		RequestObject other = (RequestObject) obj;
		return this.id == other.id;
	}
}
