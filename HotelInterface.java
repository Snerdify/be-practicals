import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.Map;

public interface HotelInterface extends Remote {
  boolean bookRoom(String guestName, int roomNumber) throws RemoteException;

  boolean cancelBooking(String guestName) throws RemoteException;

  Map<String, Integer> getBookings() throws RemoteException;
}
