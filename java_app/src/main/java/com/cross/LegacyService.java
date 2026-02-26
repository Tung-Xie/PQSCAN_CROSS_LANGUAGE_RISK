package com.cross;
import java.security.*;
public class LegacyService {
    public void run() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(1024);
        MessageDigest.getInstance("MD5").digest();
    }
}
