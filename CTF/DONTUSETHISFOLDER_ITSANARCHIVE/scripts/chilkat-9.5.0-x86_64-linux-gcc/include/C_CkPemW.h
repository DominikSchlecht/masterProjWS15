// This is a generated source file for Chilkat version 9.5.0.53
#ifndef _C_CkPemWH
#define _C_CkPemWH
#include "chilkatDefs.h"

#include "Chilkat_C.h"

CK_VISIBLE_PUBLIC HCkPemW CkPemW_Create(void);
CK_VISIBLE_PUBLIC HCkPemW CkPemW_Create2(BOOL bCallbackOwned);
CK_VISIBLE_PUBLIC void CkPemW_Dispose(HCkPemW handle);
CK_VISIBLE_PUBLIC BOOL CkPemW_getAppendMode(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_putAppendMode(HCkPemW cHandle, BOOL newVal);
CK_VISIBLE_PUBLIC void CkPemW_getDebugLogFilePath(HCkPemW cHandle, HCkString retval);
CK_VISIBLE_PUBLIC void CkPemW_putDebugLogFilePath(HCkPemW cHandle, const wchar_t *newVal);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_debugLogFilePath(HCkPemW cHandle);
CK_VISIBLE_PUBLIC int CkPemW_getHeartbeatMs(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_putHeartbeatMs(HCkPemW cHandle, int newVal);
CK_VISIBLE_PUBLIC void CkPemW_getLastErrorHtml(HCkPemW cHandle, HCkString retval);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_lastErrorHtml(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_getLastErrorText(HCkPemW cHandle, HCkString retval);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_lastErrorText(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_getLastErrorXml(HCkPemW cHandle, HCkString retval);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_lastErrorXml(HCkPemW cHandle);
CK_VISIBLE_PUBLIC BOOL CkPemW_getLastMethodSuccess(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_putLastMethodSuccess(HCkPemW cHandle, BOOL newVal);
CK_VISIBLE_PUBLIC int CkPemW_getNumCerts(HCkPemW cHandle);
CK_VISIBLE_PUBLIC int CkPemW_getNumCsrs(HCkPemW cHandle);
CK_VISIBLE_PUBLIC int CkPemW_getNumPrivateKeys(HCkPemW cHandle);
CK_VISIBLE_PUBLIC int CkPemW_getNumPublicKeys(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_getPrivateKeyFormat(HCkPemW cHandle, HCkString retval);
CK_VISIBLE_PUBLIC void CkPemW_putPrivateKeyFormat(HCkPemW cHandle, const wchar_t *newVal);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_privateKeyFormat(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_getPublicKeyFormat(HCkPemW cHandle, HCkString retval);
CK_VISIBLE_PUBLIC void CkPemW_putPublicKeyFormat(HCkPemW cHandle, const wchar_t *newVal);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_publicKeyFormat(HCkPemW cHandle);
CK_VISIBLE_PUBLIC BOOL CkPemW_getVerboseLogging(HCkPemW cHandle);
CK_VISIBLE_PUBLIC void CkPemW_putVerboseLogging(HCkPemW cHandle, BOOL newVal);
CK_VISIBLE_PUBLIC void CkPemW_getVersion(HCkPemW cHandle, HCkString retval);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_version(HCkPemW cHandle);
CK_VISIBLE_PUBLIC BOOL CkPemW_AddCert(HCkPemW cHandle, HCkCertW cert, BOOL includeChain);
CK_VISIBLE_PUBLIC BOOL CkPemW_AddPrivateKey(HCkPemW cHandle, HCkPrivateKeyW privateKey);
CK_VISIBLE_PUBLIC BOOL CkPemW_AddPrivateKey2(HCkPemW cHandle, HCkPrivateKeyW privKey, HCkCertChainW certChain);
CK_VISIBLE_PUBLIC BOOL CkPemW_AddPublicKey(HCkPemW cHandle, HCkPublicKeyW pubkey);
CK_VISIBLE_PUBLIC BOOL CkPemW_Clear(HCkPemW cHandle);
CK_VISIBLE_PUBLIC HCkCertW CkPemW_GetCert(HCkPemW cHandle, int index);
CK_VISIBLE_PUBLIC BOOL CkPemW_GetEncodedItem(HCkPemW cHandle, const wchar_t *itemType, const wchar_t *itemSubType, const wchar_t *encoding, int index, HCkString outStr);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_getEncodedItem(HCkPemW cHandle, const wchar_t *itemType, const wchar_t *itemSubType, const wchar_t *encoding, int index);
CK_VISIBLE_PUBLIC HCkPrivateKeyW CkPemW_GetPrivateKey(HCkPemW cHandle, int index);
CK_VISIBLE_PUBLIC HCkPublicKeyW CkPemW_GetPublicKey(HCkPemW cHandle, int index);
CK_VISIBLE_PUBLIC BOOL CkPemW_LoadP7b(HCkPemW cHandle, HCkByteData p7bData);
CK_VISIBLE_PUBLIC HCkTaskW CkPemW_LoadP7bAsync(HCkPemW cHandle, HCkByteData p7bData);
CK_VISIBLE_PUBLIC BOOL CkPemW_LoadP7bFile(HCkPemW cHandle, const wchar_t *path);
CK_VISIBLE_PUBLIC HCkTaskW CkPemW_LoadP7bFileAsync(HCkPemW cHandle, const wchar_t *path);
CK_VISIBLE_PUBLIC BOOL CkPemW_LoadPem(HCkPemW cHandle, const wchar_t *pemContent, const wchar_t *password);
CK_VISIBLE_PUBLIC HCkTaskW CkPemW_LoadPemAsync(HCkPemW cHandle, const wchar_t *pemContent, const wchar_t *password);
CK_VISIBLE_PUBLIC BOOL CkPemW_LoadPemFile(HCkPemW cHandle, const wchar_t *path, const wchar_t *password);
CK_VISIBLE_PUBLIC HCkTaskW CkPemW_LoadPemFileAsync(HCkPemW cHandle, const wchar_t *path, const wchar_t *password);
CK_VISIBLE_PUBLIC BOOL CkPemW_RemoveCert(HCkPemW cHandle, int index);
CK_VISIBLE_PUBLIC BOOL CkPemW_RemovePrivateKey(HCkPemW cHandle, int index);
CK_VISIBLE_PUBLIC BOOL CkPemW_SaveLastError(HCkPemW cHandle, const wchar_t *path);
CK_VISIBLE_PUBLIC HCkJavaKeyStoreW CkPemW_ToJks(HCkPemW cHandle, const wchar_t *alias, const wchar_t *password);
CK_VISIBLE_PUBLIC BOOL CkPemW_ToPem(HCkPemW cHandle, HCkString outStr);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_toPem(HCkPemW cHandle);
CK_VISIBLE_PUBLIC BOOL CkPemW_ToPemEx(HCkPemW cHandle, BOOL extendedAttrs, BOOL noKeys, BOOL noCerts, BOOL noCaCerts, const wchar_t *encryptAlg, const wchar_t *password, HCkString outStr);
CK_VISIBLE_PUBLIC const wchar_t *CkPemW_toPemEx(HCkPemW cHandle, BOOL extendedAttrs, BOOL noKeys, BOOL noCerts, BOOL noCaCerts, const wchar_t *encryptAlg, const wchar_t *password);
CK_VISIBLE_PUBLIC HCkPfxW CkPemW_ToPfx(HCkPemW cHandle);
#endif