//C++11 or greater
#include<cinttypes>
#include<array>
#include<vector>
#include<stdexcept>

const std::array<uint8_t,256> P2P_SBOX={
  0x7c,0x9c,0xe8,0x4a,0x13,0xde,0xdc,0xb2,0x2f,0x21,0x23,0xe4,0x30,0x7b,0x3d,0x8c,
  0xbc,0x0b,0x27,0x0c,0x3c,0xf7,0x9a,0xe7,0x08,0x71,0x96,0x00,0x97,0x85,0xef,0xc1,
  0x1f,0xc4,0xdb,0xa1,0xc2,0xeb,0xd9,0x01,0xfa,0xba,0x3b,0x05,0xb8,0x15,0x87,0x83,
  0x28,0x72,0xd1,0x8b,0x5a,0xd6,0xda,0x93,0x58,0xfe,0xaa,0xcc,0x6e,0x1b,0xf0,0xa3,
  0x88,0xab,0x43,0xc0,0x0d,0xb5,0x45,0x38,0x4f,0x50,0x22,0x66,0x20,0x7f,0x07,0x5b,
  0x14,0x98,0x1d,0x9b,0xa7,0x2a,0xb9,0xa8,0xcb,0xf1,0xfc,0x49,0x47,0x06,0x3e,0xb1,
  0x0e,0x04,0x3a,0x94,0x5e,0xee,0x54,0x11,0x34,0xdd,0x4d,0xf9,0xec,0xc7,0xc9,0xe3,
  0x78,0x1a,0x6f,0x70,0x6b,0xa4,0xbd,0xa9,0x5d,0xd5,0xf8,0xe5,0xbb,0x26,0xaf,0x42,
  0x37,0xd8,0xe1,0x02,0x0a,0xae,0x5f,0x1c,0xc5,0x73,0x09,0x4e,0x69,0x24,0x90,0x6d,
  0x12,0xb3,0x19,0xad,0x74,0x8a,0x29,0x40,0xf5,0x2d,0xbe,0xa5,0x59,0xe0,0xf4,0x79,
  0xd2,0x4b,0xce,0x89,0x82,0x48,0x84,0x25,0xc6,0x91,0x2b,0xa2,0xfb,0x8f,0xe9,0xa6,
  0xb0,0x9e,0x3f,0x65,0xf6,0x03,0x31,0x2e,0xac,0x0f,0x95,0x2c,0x5c,0xed,0x39,0xb7,
  0x33,0x6c,0x56,0x7e,0xb4,0xa0,0xfd,0x7a,0x81,0x53,0x51,0x86,0x8d,0x9f,0x77,0xff,
  0x6a,0x80,0xdf,0xe2,0xbf,0x10,0xd7,0x75,0x64,0x57,0x76,0xf3,0x55,0xcd,0xd0,0xc8,
  0x18,0xe6,0x36,0x41,0x62,0xcf,0x99,0xf2,0x32,0x4c,0x67,0x60,0x61,0x92,0xca,0xd3,
  0xea,0x63,0x7d,0x16,0xb6,0x8e,0xd4,0x68,0x35,0xc3,0x52,0x9d,0x46,0x44,0x1e,0x17
};

const std::array<uint8_t,256> P2P_INVSBOX={
  0x1b,0x27,0x83,0xb5,0x61,0x2b,0x5d,0x4e,0x18,0x8a,0x84,0x11,0x13,0x44,0x60,0xb9,
  0xd5,0x67,0x90,0x04,0x50,0x2d,0xf3,0xff,0xe0,0x92,0x71,0x3d,0x87,0x52,0xfe,0x20,
  0x4c,0x09,0x4a,0x0a,0x8d,0xa7,0x7d,0x12,0x30,0x96,0x55,0xaa,0xbb,0x99,0xb7,0x08,
  0x0c,0xb6,0xe8,0xc0,0x68,0xf8,0xe2,0x80,0x47,0xbe,0x62,0x2a,0x14,0x0e,0x5e,0xb2,
  0x97,0xe3,0x7f,0x42,0xfd,0x46,0xfc,0x5c,0xa5,0x5b,0x03,0xa1,0xe9,0x6a,0x8b,0x48,
  0x49,0xca,0xfa,0xc9,0x66,0xdc,0xc2,0xd9,0x38,0x9c,0x34,0x4f,0xbc,0x78,0x64,0x86,
  0xeb,0xec,0xe4,0xf1,0xd8,0xb3,0x4b,0xea,0xf7,0x8c,0xd0,0x74,0xc1,0x8f,0x3c,0x72,
  0x73,0x19,0x31,0x89,0x94,0xd7,0xda,0xce,0x70,0x9f,0xc7,0x0d,0x00,0xf2,0xc3,0x4d,
  0xd1,0xc8,0xa4,0x2f,0xa6,0x1d,0xcb,0x2e,0x40,0xa3,0x95,0x33,0x0f,0xcc,0xf5,0xad,
  0x8e,0xa9,0xed,0x37,0x63,0xba,0x1a,0x1c,0x51,0xe6,0x16,0x53,0x01,0xfb,0xb1,0xcd,
  0xc5,0x23,0xab,0x3f,0x75,0x9b,0xaf,0x54,0x57,0x77,0x3a,0x41,0xb8,0x93,0x85,0x7e,
  0xb0,0x5f,0x07,0x91,0xc4,0x45,0xf4,0xbf,0x2c,0x56,0x29,0x7c,0x10,0x76,0x9a,0xd4,
  0x43,0x1f,0x24,0xf9,0x21,0x88,0xa8,0x6d,0xdf,0x6e,0xee,0x58,0x3b,0xdd,0xa2,0xe5,
  0xde,0x32,0xa0,0xef,0xf6,0x79,0x35,0xd6,0x81,0x26,0x36,0x22,0x06,0x69,0x05,0xd2,
  0x9d,0x82,0xd3,0x6f,0x0b,0x7b,0xe1,0x17,0x02,0xae,0xf0,0x25,0x6c,0xbd,0x65,0x1e,
  0x3e,0x59,0xe7,0xdb,0x9e,0x98,0xb4,0x15,0x7a,0x6b,0x28,0xac,0x5a,0xc6,0x39,0xcf,
};

using KeyType=std::array<uint8_t,4>;
using TextType=std::vector<uint8_t>;

uint8_t P2P_LookUp(const KeyType sKey,uint8_t value){
  uint8_t t=value+sKey[value&0b11];
  return P2P_SBOX[t];
}

uint8_t ComputeKey(uint8_t plainText,uint8_t cipherText,uint8_t lastCipherText){
  uint8_t diff=plainText^cipherText;
  return P2P_INVSBOX[diff-lastCipherText];
}

KeyType P2P_KeyScheduler(std::vector<uint8_t> key){
  //This key scheduler is incredibly flawed. 
  //Reduces any key down to 24bits

  if(key.size()>20)
    key.resize(20);

  KeyType sKey;
  sKey.fill(0);

  for(auto k:key){
    sKey[0]+=k;
    sKey[1]-=k;
    sKey[2]+=k/3;
    sKey[3]^=k;
  }

  return sKey;
}

TextType P2P_Encrypt(KeyType sKey,const TextType &plainText){
  TextType cypherText;
  uint8_t prev=0;

  for(auto p:plainText){
    uint8_t t=p^P2P_LookUp(sKey,prev);
    cypherText.push_back(t);
    prev=t;
  }

  return cypherText;
}

TextType P2P_Decrypt(KeyType sKey,const TextType &cipherText){
  TextType plainText;
  uint8_t prev=0;

  for(auto c:cipherText){
    uint8_t t=c^P2P_LookUp(sKey,prev);
    plainText.push_back(t);
    prev=c;
  }

  return plainText;
}

KeyType P2P_Crack(const TextType &plainText,const TextType &cypherText){
  //The first lookup for the sbox is always going to refrence the first byte
  //of the sKey no matter what because no prexisting byte to refrence for 
  //sKey selection

  //Every byte after the first will refrence the previous cypherText byte
  //making it possable to fill out the last two byte of the sKey without 
  //much effort. 

  KeyType sKey;
  sKey.fill(0);

  auto ComputeSubKey=[&plainText,&cypherText](uint8_t searchFor)->uint8_t{
    for(uint64_t i=1;i<cypherText.size();i++){
      auto c=cypherText[i];
      auto p=plainText[i];
      auto l=cypherText[i-i];
      if((l&0b11)==searchFor)
        return ComputeKey(p,c,l);
    }
    throw std::runtime_error("shouldn't get here but woops.");
  };

  
  sKey[0]=ComputeKey(plainText[0],cypherText[0],0);
  sKey[1]=sKey[0]*-1;//sKey,1 will be the inverse of sKey,0

  sKey[2]=ComputeSubKey(2);
  sKey[2]=ComputeSubKey(3);

  return sKey;
}