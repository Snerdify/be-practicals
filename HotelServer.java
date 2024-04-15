import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class HotelServer extends UnicastRemoteObject implements HotelInterface {
  private Map<String, Integer> bookings;
  private Lock lock;

  public HotelServer() throws RemoteException {
    bookings = new HashMap<>();
    lock = new ReentrantLock();
  }

  @Override
  public boolean bookRoom(String guestName, int roomNumber) throws RemoteException {
    try {
      lock.lock();

      if (!bookings.containsKey(guestName)) {
        if (!bookings.containsValue(roomNumber)) {
          bookings.put(guestName, roomNumber);
          System.out.println("Booking successful for " + guestName + " in room " + roomNumber);
          return true;
        } else {
          System.out.println("Room " + roomNumber + " is already booked by someone else.");
        }
      } else {
        System.out.println(guestName + " already has a booking.");
      }

      return false;
    } finally {
      lock.unlock();
    }
  }

  @Override
  public synchronized boolean cancelBooking(String guestName) throws RemoteException {
    if (bookings.containsKey(guestName)) {
      int roomNumber = bookings.remove(guestName);
      System.out.println("Booking canceled for " + guestName + " in room " + roomNumber);
      return true;
    } else {
      System.out.println(guestName + " does not have a booking.");
      return false;
    }
  }

  @Override
  public synchronized Map<String, Integer> getBookings() throws RemoteException {
    return new HashMap<>(bookings);
  }

  public static void main(String[] args) {
    try {
      HotelServer server = new HotelServer();
      java.rmi.registry.LocateRegistry.createRegistry(1099);
      java.rmi.Naming.rebind("HotelService", server);
      System.out.println("HotelServer is ready.");
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
