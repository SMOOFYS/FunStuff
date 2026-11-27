// CISP 440 Homework 7.42 Fall 2023
// Mini DES Cracker
// Student: [Your Name]
// Date: March 2025 (late submission lol)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ============================================================
//   THESE ARE THE SUBSTITUTION TABLES FROM miniDESv2.cpp
//   (you have to copy them exactly from the posted file)
// ============================================================

unsigned char f0[256] = {
    0x3A,0x72,0x91,0xC5,0x4B,0x1E,0xD8,0x2F,0xB4,0x6E,0x09,0xA7,0x5C,0xF1,0x83,0xD6,
    0x2B,0xC8,0x74,0x19,0xE3,0xAF,0x50,0x96,0x0D,0xB9,0x67,0xF4,0x31,0xCA,0x8E,0x25,
    // ... (I didn't type all 256 - you MUST paste the real ones here!)
    // Keep going until you have all 256 values for f0, f1, f2, f3
    // This is just showing the pattern
};

unsigned char f1[256] = { /* paste real f1 table here */ };
unsigned char f2[256] = { /* paste real f2 table here */ };
unsigned char f3[256] = { /* paste real f3 table here */ };

// ============================================================
//   INVERSE TABLES - we made these with the other program
//   Paste the output from your inverse table generator here
// ============================================================

unsigned char inv_f0[256] = {
    // paste the 0x?? values your program printed for f0_inv
};

unsigned char inv_f1[256] = { /* ... */ };
unsigned char inv_f2[256] = { /* ... */ };
unsigned char inv_f3[256] = { /* ... */ };

// ============================================================
//   ENCRYPT FUNCTION - copy this exactly from miniDESv2.cpp
//   (this is what was used to encrypt ePic.bmp)
// ============================================================

void encrypt_block(unsigned char *block, unsigned char key) {
    // Most likely this is what it looks like (common student mini-DES)
    // CHANGE THIS TO MATCH THE REAL CODE FROM miniDESv2.cpp !!

    unsigned char temp = *block;

    temp = f0[temp ^ key];
    temp = f1[temp];
    temp = f2[temp ^ key];
    temp = f3[temp];

    *block = temp;
}

// ============================================================
//   DECRYPT FUNCTION - reverse the order of substitutions
// ============================================================

void decrypt_block(unsigned char *block, unsigned char key) {
    unsigned char temp = *block;

    // If encryption was: f3(f2(f1(f0(x ^ key))))
    // Then decryption is: f0_inv( f1_inv( f2_inv( f3_inv(x) ) ) )   maybe ^ key at end or start

    temp = inv_f3[temp];
    temp = inv_f2[temp];
    temp = inv_f1[temp];
    temp = inv_f0[temp];

    // Some versions XOR key at the beginning instead of end
    // Try both versions - comment/uncomment as needed
    // temp ^= key;     // try with this line
    // or
    // temp = inv_f0[temp ^ key];   // or move XOR here, etc.

    *block = temp;
}

// ============================================================
//   MAIN - brute force all 256 keys
// ============================================================

int main(void) {
    FILE *in_file;
    FILE *out_file;
    unsigned char *buffer;
    long file_size;
    int i, k;
    char filename[40];

    printf("Mini-DES Brute Force Decryptor for ePic.bmp\n");
    printf("Trying all 256 possible keys...\n\n");

    in_file = fopen("ePic.bmp", "rb");
    if (in_file == NULL) {
        printf("Error: Cannot open ePic.bmp\n");
        return 1;
    }

    // Get file size
    fseek(in_file, 0, SEEK_END);
    file_size = ftell(in_file);
    fseek(in_file, 0, SEEK_SET);

    // Allocate memory
    buffer = (unsigned char *)malloc(file_size);
    if (buffer == NULL) {
        printf("Memory allocation failed!\n");
        fclose(in_file);
        return 1;
    }

    // Read whole file
    fread(buffer, 1, file_size, in_file);
    fclose(in_file);

    // Try every possible 8-bit key
    for (k = 0; k <= 255; k++) {
        // Make a copy of original encrypted data
        unsigned char *copy = (unsigned char *)malloc(file_size);
        memcpy(copy, buffer, file_size);

        // Decrypt every byte with this key
        for (i = 0; i < file_size; i++) {
            decrypt_block(&copy[i], (unsigned char)k);
        }

        // Save result
        sprintf(filename, "decrypted_key_%03d.bmp", k);
        out_file = fopen(filename, "wb");
        if (out_file != NULL) {
            fwrite(copy, 1, file_size, out_file);
            fclose(out_file);
            printf("Created: %s  (key = %3d = 0x%02X)\n", filename, k, k);
        }

        free(copy);
    }

    free(buffer);

    printf("\nAll done!\n");
    printf("Now open the decrypted_*.bmp files in Windows Photo Viewer or Paint.\n");
    printf("Look for the one that actually looks like a normal picture.\n");
    printf("That key is the correct one.\n");

    printf("\nMy final answer will be:\n");
    printf("Correct key: __________\n");
    printf("Inverse function composition order: inv_f0 ◦ inv_f1 ◦ inv_f2 ◦ inv_f3\n");
    // ^^^ change this order if your testing shows different sequence

    return 0;
}