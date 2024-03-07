package programmers.level2.java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Parking {
    String carNum;
    String in;
    String out;
    int fee;

    public Parking(String carNum) {
        this.carNum = carNum;
    }

    public void setTime(String time, String type) {
        if (type.equals("IN")) {
            this.in = time;
        }
        if (type.equals("OUT")) {
            this.out = time;
        }
    }

    public String getIn() {
        return this.in;
    }

    public String getOut() {
        return this.out != null ? this.out : "23:59";
    }

    public boolean done() {
        return this.in != null && this.out != null;
    }

    public void free() {
        this.in = null;
        this.out = null;
    }

    @Override
    public String toString() {
        return (this.carNum + " " + this.in + " " + this.out);
    }

}

class Solution {
    public int[] solution(int[] fees, String[] records) {
        // 1. get records
        Map<String, Parking> map = new HashMap<>();
        for (String record : records) {
            String[] car = record.split(" ");

            String time = car[0];
            String carNum = car[1];
            String type = car[2];

            if (map.containsKey(carNum)) {
                Parking parking = map.get(carNum);
                if (parking.done()) {
                    parking.fee += this.calculateFee(fees, parking.in, parking.out);
                    parking.free();
                }

                parking.setTime(time, type);
            } else {
                Parking parking = new Parking(carNum);
                parking.setTime(time, type);
                map.put(carNum, parking);
            }
        }

        // 2. calculate fee
        String[] cars = map.keySet().toArray(new String[map.size()]);
        Arrays.sort(cars);

        int[] result = new int[cars.length];
        for (int i = 0; i < cars.length; i++) {
            Parking parking = map.get(cars[i]);
            String inStr = parking.getIn();
            String outStr = parking.getOut();

            result[i] += parking.fee;
            result[i] += this.calculateFee(fees, inStr, outStr);

        }

        return result;
    }

    private int calculateFee(int[] fees, String inStr, String outStr) {
        int in = this.timeToMinute(inStr);
        int out = this.timeToMinute(outStr);
        int parkingTime = this.getParkingTime(in, out);

        int baseTime = fees[0];
        int baseFee = fees[1];
        int addTime = fees[2];
        int addFee = fees[3];

        System.out.println(inStr + " " + outStr);
        System.out.println(baseFee + " " + parkingTime + " " + baseTime + " " + addTime);

        int additionalFee = 0;
        if (parkingTime > baseTime) {
            int additionalTime = (int) Math.ceil((double) (parkingTime - baseTime) / addTime);
            additionalFee = additionalTime * addFee;
        }

        return baseFee + additionalFee;
    }

    private int timeToMinute(String time) {
        // time: "05:43"
        String[] list = time.split(":");
        int hour = Integer.parseInt(list[0]);
        int minute = Integer.parseInt(list[1]);

        return hour * 60 + minute;
    }

    private int getParkingTime(int in, int out) {
        return out - in;
    }

}