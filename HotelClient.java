import java.rmi.Naming;
import java.rmi.RemoteException;
import java.util.InputMismatchException;
import java.util.Map;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            HotelInterface hotelService = (HotelInterface) Naming.lookup("rmi://localhost:1099/HotelService");

            while (true) {
                System.out.println("1. Book a room");
                System.out.println("2. Cancel booking");
                System.out.println("3. View booked rooms");
                System.out.println("4. Exit");
                System.out.print("Enter your choice: ");

                try {
                    int choice = scanner.nextInt();
                    scanner.nextLine();

                    switch (choice) {
                        case 1:
                            System.out.print("Enter guest name: ");
                            String guestName = scanner.nextLine();
                            System.out.print("Enter room number: ");
                            int roomNumber = scanner.nextInt();
                            boolean booked = hotelService.bookRoom(guestName, roomNumber);
                            if (booked) {
                                System.out.println("Room booked successfully.");
                            } else {
                                System.out.println("Booking failed. Guest may already have a booking.");
                            }
                            break;
                        case 2:
                            System.out.print("Enter guest name to cancel booking: ");
                            String guestToCancel = scanner.nextLine();
                            boolean canceled = hotelService.cancelBooking(guestToCancel);
                            if (canceled) {
                                System.out.println("Booking canceled successfully.");
                            } else {
                                System.out.println("Cancel booking failed. Guest may not have a booking.");
                            }
                            break;
                        case 3:
                            displayBookedRooms(hotelService);
                            break;
                        case 4:
                            System.out.println("Exiting...");
                            System.exit(0);
                            break;
                        default:
                            System.out.println("Invalid choice. Please enter a valid option.");
                    }
                } catch (InputMismatchException e) {
                    System.out.println("Invalid input. Please enter a valid number.");
                    scanner.nextLine();
                } catch (RemoteException e) {
                    System.out.println("RemoteException: " + e.getMessage());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void displayBookedRooms(HotelInterface hotelService) throws RemoteException {
        Map<String, Integer> bookings = hotelService.getBookings();
        if (bookings.isEmpty()) {
            System.out.println("No rooms booked yet.");
        } else {
            System.out.println("Booked Rooms:");
            for (Map.Entry<String, Integer> entry : bookings.entrySet()) {
                System.out.println("Room " + entry.getValue() + " - " + entry.getKey());
            }
        }
    }
}
