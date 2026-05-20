public class MiniParkingSystem{
    public static String checkingASlot(int[] carSlots, int slotNumber){
        if(carSlots[slotNumber] == 0){
            return "Empty";
        }
        else if(carSlots[slotNumber] == 1){
            return "Occupied";
        }

    }

    public static String parkingACar(int[] carSlots, int slotNumber){
        String checkingSlot = checkingASlot(carSlots, slotNumber);

        if(checkingSlot == "Empty"){
            carSlot[slotNumber] = 1;
            return "Now Occupied";
        }
        else{
            return "Already Occupied Before Now";
        }
    }

    public static String unparkingACar(int[] carSlots, int slotNUmber){
        String parkingCar = parkingACar(carSlots, slotNumber);

        if(parkingCar == "Now Occupied"){
            carSlot[slotNumber] = 0;
            return "Car Unparked";
        }
        else if(parkingCar == "Already Occupied Before Now"){
            return "Car Not Yours"
        }

    }

}
