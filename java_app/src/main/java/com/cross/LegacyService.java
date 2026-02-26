package com.cross;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import java.security.*;

public class LegacyService {
    public void runLegacy() throws Exception {
        // [High Risk] RSA-1024
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(1024);
        
        // [High Risk] MD5
        MessageDigest.getInstance("MD5").digest("data".getBytes());

        // [Medium Risk] AES-128-CBC
        byte[] keyBytes = new byte[16]; // 128 bits
        SecretKeySpec keySpec = new SecretKeySpec(keyBytes, "AES");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, new IvParameterSpec(new byte[16]));
    }
}
