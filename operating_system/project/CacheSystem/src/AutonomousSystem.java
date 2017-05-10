import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class AutonomousSystem {
	
	public static class Neighbor {
		public final AutonomousSystem as;
		public final double linkCost;
		
		public Neighbor(AutonomousSystem as, double linkCost) {
			this.as = as;
			this.linkCost = linkCost;
		}
	}
	
	private int id;
	private int availableFreeSpace;
	private HashSet<RequestObject> cachedObjects;
	private List<Neighbor> neighbors;
	private int requestFreqs[] = new int[GlobalEnvironment.OBJECT_COUNT];
	
	public int getId() {
		return id;
	}
	
	public int getAvailableFreeSpace() {
		return availableFreeSpace;
	}
	
	public List<Neighbor> getNeighbors() {
		return neighbors;
	}
	
	public int getRequestFreq(RequestObject object) {
		return requestFreqs[object.getId()];
	}
	
	public Set<RequestObject> getCachedObjects() {
		return cachedObjects;
	}
	
	public boolean isCached(RequestObject object) {
		return cachedObjects.contains(object);
	}
	
	public void cacheObject(RequestObject object) {
		cachedObjects.add(object);
		availableFreeSpace -= object.getSize();
	}
	
	public void uncacheObject(RequestObject object) {
		cachedObjects.remove(object.getId());
		availableFreeSpace += object.getSize();
	}
}
