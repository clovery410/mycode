import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class GlobalEnvironment {
	public static final int AS_COUNT = 100;
	public static final int OBJECT_COUNT = 200;
	
	public void initialize() {
		// initialize neighbors etc.
	}
	
	public void cacheUpdate(AutonomousSystem as, RequestObject object) {
		if (as.isCached(object)) {
			// Cached in local AS already.
			return;
		}
		
		if (object.getSize() <= as.getAvailableFreeSpace()) {
			as.cacheObject(object);			
			
		} else {
			List<RequestObject> objects = new ArrayList<>();
			objects.add(object);
			objects.addAll(as.getCachedObjects());
			PriorityQueue<ObjectWithGlobalValue> pq = new PriorityQueue<>();
			for (RequestObject requestObject : objects) {
				double globalValue = calculateGlobalValue(as, requestObject);
				pq.add(new ObjectWithGlobalValue(requestObject, globalValue));
			}
			
			if (object.equals(pq.peek().object)) {
				// The global value of current request object is the lowest one,
				// so don't cache and forward the request.
			} else {
				as.cacheObject(object);
				while (as.getAvailableFreeSpace() < 0) {
					RequestObject objectToUncache = pq.poll().object;
					as.uncacheObject(objectToUncache);
				}
			}
		}
	}
	
	private double calculateGlobalValue(AutonomousSystem as, RequestObject object) {
		double globalValue = 0;
		if (!isCachedInAnyConnectedAutonomousSystem(as, object)) {
			globalValue = as.getRequestFreq(object);
			for (AutonomousSystem.Neighbor neighbor : as.getNeighbors()) {
				AutonomousSystem connectedAs = neighbor.as;
				globalValue += connectedAs.getRequestFreq(object) * (1 - neighbor.linkCost);
			}
			
		} else {
			double minLinkCost = 1;
			for (AutonomousSystem.Neighbor neighbor : as.getNeighbors()) {
				AutonomousSystem connectedAs = neighbor.as;
				if (connectedAs.isCached(object)) {
					minLinkCost = Math.min(minLinkCost, neighbor.linkCost);
				}
			}
			globalValue = as.getRequestFreq(object) * minLinkCost;
			
			for (AutonomousSystem.Neighbor neighbor : as.getNeighbors()) {
				AutonomousSystem connectedAs = neighbor.as;
				if (!connectedAs.isCached(object)) {
					minLinkCost = 1;
					for (AutonomousSystem.Neighbor neighbor2 : connectedAs.getNeighbors()) {
						if (neighbor2.as.isCached(object)) {
							minLinkCost = Math.min(minLinkCost, neighbor2.linkCost);
						}
					}
					globalValue += (minLinkCost - Math.min(minLinkCost, neighbor.linkCost));
				}
			}
		}
		
		return globalValue;
	}
	
	private boolean isCachedInAnyConnectedAutonomousSystem(
			AutonomousSystem as, RequestObject object) {
		for (AutonomousSystem.Neighbor neighbor : as.getNeighbors()) {
			if (neighbor.as.isCached(object)) {
				return true;
			}
		}
		return false;
	}
	
	private static class ObjectWithGlobalValue implements Comparable<ObjectWithGlobalValue> {
		private RequestObject object;
		private double globalValue;
		
		public ObjectWithGlobalValue(RequestObject object, double globalValue) {
			this.object = object;
			this.globalValue = globalValue;
		}

		@Override
		public int compareTo(ObjectWithGlobalValue o) {
			return globalValue < o.globalValue ? -1 : 1;
		}
	}
}
