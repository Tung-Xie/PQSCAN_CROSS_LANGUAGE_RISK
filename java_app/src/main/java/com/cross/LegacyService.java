package com.cross;
import java.security.*;
public class LegacyService {
    public void init() throws Exception {
        // 同樣的 RSA-1024
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(1024);
        // 同樣的 MD5
        MessageDigest.getInstance("MD5").digest();
    }
}
