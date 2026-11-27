/*
    Floating point arithmetic the HARD way.

    Dan Ross Jan 2013

    Converts a floating point number from a string representation to
    an 8-bit representation using only INTEGER operations. And vice-versa.
    This is usually done for us by the preprocessor/compiler and library
    functions like atof().

    This program illustrates that float operations are computationally expensive.
    Thus, they are either done in software to save chip space, or in specialized
    hardware to save execution time - this is the classic tradeoff in computer science.

    Here, we are pretending that neither our hardware or our compiler support floating
    point operations. So we have to make our own!

    BIT FORMAT:
    1 sign bit
    4 mantissa bits
    3 exponent bits in excess 4 format (range is -4 to 3)
    EXAMPLE: 3.5 = 11.1 = 1.1100 x 2^1 = 0 1100 101

    RANGE:
    smallest magnitude: binary 1.0000 x 2 ^ -4 = 00.06250000
    largest magnitude: binary 1.1111 x 2 ^ 3 = 15.50000000 (2 leading digits req'd)
    highest precision: binary 1.0001 x 2 ^ -4 = 00.06640625 (8 trailing digits req'd)

    INPUT STRINGS:
    Input strings must be of the form: -X.X
    with 1 to 2 leading zeros and 1 to 8 trailing zeros
    and an optional minus sign
    Examples:
        0.0
        00.0000
        -1.2
        42.7777
        00.06640625

    Note: A Finite Acceptor in the preprocessor would check the string format
    before converting it to binary

*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#pragma warning( disable : 4996)
#pragma warning( disable : 4244)

int my_pow(int base, int exp)
{
    int x = 1;
    for(int i = 0; i < exp; i++)
        x *= base;

    return x;
}

void print8bits(unsigned char x)
{
    for(unsigned char mask = 0x80; mask; mask >>= 1) {
        if(mask & x)
            printf("1");
        else
            printf("0");
    }
}

void print16bits(unsigned short x)
{
    for(unsigned short mask = 0x8000; mask; mask >>= 1) {
        if(mask & x)
            printf("1");
        else
            printf("0");
    }
}

void print32bits(unsigned long x)
{
    for(unsigned long mask = 0x80000000; mask; mask >>= 1) {
        if(mask & x)
            printf("1");
        else
            printf("0");
    }
}

unsigned char my_atof(char * str)
{
    char strIn[20];

    int negative = 0;
    if(str[0] == '-') {
        negative = 1;
        strcpy(strIn, str + 1);
    } else
        strcpy(strIn, str);

    int len = strlen(strIn);

    #define S_WHOLE_SIZE 3
    char s_whole[S_WHOLE_SIZE] = "00";
    #define S_FRACT_SIZE 9
    char s_fract[S_FRACT_SIZE] = "00000000";

    int x = 0;
    while(strIn[x] != '.')x++;

    for(int i = x - 1, j = 0; i >= 0; i--, j++)
        s_whole[j] = strIn[i];

    for(int i = x + 1, j = S_FRACT_SIZE - 2; i < len; i++, j--)
        s_fract[j] = strIn[i];

    unsigned char i_whole = 0;
    for(int i = 0; i < S_WHOLE_SIZE - 1; i ++)
        i_whole += (s_whole[i] - '0') * my_pow(10, i);

    if(i_whole > 15){
        printf("atof conversion Overflow %s", str);
        exit(0);
    }

    unsigned long i_fract = 0;
    for(int i = 0; i < S_FRACT_SIZE - 1; i ++)
        i_fract += (s_fract[i] - '0') * my_pow(10, i);
    unsigned long powof2 = 50000000;
    unsigned char b_fract = 0;
    unsigned char mask = 0x80;
    for(int i = 0; i < S_FRACT_SIZE - 1; i ++) {
        if(i_fract >= powof2) {
            b_fract |= mask;
            i_fract -= powof2;
        }
        mask >>= 1;
        powof2 >>= 1;
    }

    unsigned short buffer = 0;
    buffer = i_whole;
    buffer <<= 8;

    buffer |= b_fract;

    if(!buffer && i_fract){
        printf("atof conversion Underflow %s", str);
        exit(0);
    }

    int exponent = 7;
    unsigned short mask2 = 0x8000;
    while(!(buffer & mask2)) {
        exponent--;
        mask2 >>= 1;
    }

    if(exponent > 3){
        printf("atof conversion Overflow %s", str);
        exit(0);
    }

    if(exponent < -4){
        printf("atof conversion Underflow %s", str);
        exit(0);
    }

    unsigned char theFloat = 0;

    buffer <<= (7 - exponent);

    buffer >>= 8;

    theFloat = buffer;

    theFloat &= 0x78;

    exponent += 4;

    theFloat |= exponent;

    if(negative) theFloat |= 0x80;

    return theFloat;
}

void my_ftoa(unsigned char f, char * strOut)

{

    int ch_p = 0;



    if(f & 0x80) strOut[ch_p++] = '-';



    int exponent;

    exponent = (f & 0x07) - 4;

    f &= 0x78;

    f |= 0x80;

    unsigned short buffer = 0;

    buffer = f;

    buffer <<= 8;

    buffer >>= (7 - exponent);

    unsigned char i_whole;

    i_whole = (buffer & 0xFF00) >> 8;

    unsigned char b_fract;

    b_fract = (buffer & 0x00FF);
    unsigned long i_fract = 0;
    if(b_fract & 0x80) i_fract += 50000000;
    if(b_fract & 0x40) i_fract += 25000000;
    if(b_fract & 0x20) i_fract += 12500000;
    if(b_fract & 0x10) i_fract += 6250000;
    if(b_fract & 0x08) i_fract += 3125000;
    if(b_fract & 0x04) i_fract += 1562500;
    if(b_fract & 0x02) i_fract += 781250;
    if(b_fract & 0x01) i_fract += 390625;

    strOut[ch_p] = '0';

    while(i_whole >= 10){

        strOut[ch_p]++;

        i_whole -= 10;

    }

    ch_p++;



    strOut[ch_p] = '0';

    while(i_whole >= 1){

        strOut[ch_p]++;

        i_whole -= 1;

    }

    ch_p++;



    strOut[ch_p] = '.';

    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 10000000){
        strOut[ch_p]++;
        i_fract -= 10000000;
    }
    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 1000000){
        strOut[ch_p]++;
        i_fract -= 1000000;
    }
    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 100000){
        strOut[ch_p]++;
        i_fract -= 100000;
    }
    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 10000){
        strOut[ch_p]++;
        i_fract -= 10000;
    }
    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 1000){
        strOut[ch_p]++;
        i_fract -= 1000;
    }
    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 100){
        strOut[ch_p]++;
        i_fract -= 100;
    }
    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 10){
        strOut[ch_p]++;
        i_fract -= 10;
    }
    ch_p++;

    strOut[ch_p] = '0';
    while(i_fract >= 1){
        strOut[ch_p]++;
        i_fract -= 1;
    }
    ch_p++;

    strOut[ch_p] = 0;
}

unsigned char addFloats(unsigned char f1, unsigned char f2)
{
    if(f1 == 0) return f2;
    if(f2 == 0) return f1;

    int exp1 = (f1 & 0x07) - 4;
    int mant1 = 16 + ((f1 & 0x78) >> 3);
    int exp2 = (f2 & 0x07) - 4;
    int mant2 = 16 + ((f2 & 0x78) >> 3);

    if(exp1 < exp2) {
        mant1 >>= (exp2 - exp1);
        exp1 = exp2;
    } else if(exp2 < exp1) {
        mant2 >>= (exp1 - exp2);
    }

    int mant_sum = mant1 + mant2;
    int exp_sum = exp1;

    while(mant_sum >= 32) {
        mant_sum >>= 1;
        exp_sum++;
    }
    while(mant_sum < 16 && mant_sum > 0) {
        mant_sum <<= 1;
        exp_sum--;
    }

    int new_frac = mant_sum & 0x0F;
    int new_exp = exp_sum + 4;
    if(new_exp < 0) new_exp = 0;
    if(new_exp > 7) new_exp = 7;

    return (new_frac << 3) | new_exp;
}

unsigned char multiplyFloats(unsigned char f1, unsigned char f2)
{
    if(f1 == 0 || f2 == 0) return 0;

    int exp1 = (f1 & 0x07) - 4;
    int mant1 = 16 + ((f1 & 0x78) >> 3);
    int exp2 = (f2 & 0x07) - 4;
    int mant2 = 16 + ((f2 & 0x78) >> 3);

    long mant_prod = (long)mant1 * mant2;
    int exp_prod = exp1 + exp2;

    while(mant_prod >= 512) {
        mant_prod >>= 1;
        exp_prod++;
    }
    while((mant_prod >> 4) < 16 && (mant_prod >> 4) > 0) {
        mant_prod <<= 1;
        exp_prod--;
    }

    int new_frac = (mant_prod >> 4) & 0x0F;
    int new_exp = exp_prod + 4;
    if(new_exp < 0) new_exp = 0;
    if(new_exp > 7) new_exp = 7;
    unsigned char theFloat = (new_frac << 3) | new_exp;

    printf("Packed Prod: "); print8bits(theFloat); printf("\n");

    return theFloat;
}

void main()
{
    char strIn1[40] = "0.125";
    char strIn2[40] = "4.5";
    char strOut[40];
    unsigned char f1 = my_atof(strIn1);
    unsigned char f2 = my_atof(strIn2);
    unsigned char f3;

    printf("A = 0.125 B = 4.5\n");
    printf("A Packed: ");
    print8bits(f1);
    printf(" B Packed: ");
    print8bits(f2);
    printf("\n");
    printf("A Expanded: 0000 0000 0000 0000 0000 0001.0000 0000 e1=-3\n");
    printf("B Expanded: 0000 0000 0000 0000 0000 0001.0010 0000 e2= 2\n");

    f3 = multiplyFloats(f1, f2);
    my_ftoa(f3, strOut);
    printf("0.125 * 4.5 = %s\n\n", strOut);

    f1 = my_atof("1.0");
    f2 = my_atof("2.0");
    f3 = multiplyFloats(f1, f2);
    my_ftoa(f3, strOut);
    printf("1.0 * 2.0 = %s\n", strOut);
    f1 = my_atof("4.5");
    f2 = my_atof("0.125");
    f3 = addFloats(f1, f2);
    my_ftoa(f3, strOut);
    printf("4.5 + 0.125 = %s\n", strOut);

    f1 = my_atof("1.0");
    f2 = my_atof("1.0");
    f3 = addFloats(f1, f2);
    my_ftoa(f3, strOut);
    printf("1.0 + 1.0 = %s\n\n", strOut);

    for(int i = 0; i < 256; i++) {
        my_ftoa((unsigned char)(i & 0x7F), strOut);
        printf("%s\n", strOut);
    }

    printf("\nThe numbers are packed much closer together near zero. The gaps between numbers get larger as the values get bigger.\n");
}
