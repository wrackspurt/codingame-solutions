/*
BANK ROBBERS
Difficulty: Easy
Link: https://www.codingame.com/training/easy/bank-robbers
*/

import java.util.*;
import java.io.*;
import java.math.*;


class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int R = in.nextInt();
        int V = in.nextInt();
        int[] vaultsTime = new int[V];
        int free = V - R;
        for (int i = 0; i < V; i++) {
            int C = in.nextInt();
            int N = in.nextInt();
            vaultsTime[i] = (int) (Math.pow(10, N) * Math.pow(5, C - N));
        }

        for (int i = 0; i < free; i++) {
            int min = 0;
            for (int j = 0; j < R; j++) {
                if (vaultsTime[j] < vaultsTime[min])
                    min = j;

                }

                vaultsTime[min] += vaultsTime[R + i];
            }

            int max = 0;
            for (int i = 0; i < V; i++) {
                if (vaultsTime[i] > max)
                   max = vaultsTime[i];
                }

        System.out.println(max);
    }
}

