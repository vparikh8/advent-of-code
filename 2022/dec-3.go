package main

import (
	"bufio"
    "fmt"
    "log"
    "os"
    "strings"
)

func main() {

	// open file
    f, err := os.Open("input-dec-3.txt")
    if err != nil {
        log.Fatal(err)
    }
    // remember to close the file at the end of the program
    defer f.Close()

    // read the file word by word using scanner
    scanner := bufio.NewScanner(f)

    total := 0
    num := 0
    var bags [3]string
    counter := 0
    first := ""
    second := ""
    third := ""
    seen := ""
    for scanner.Scan() {
    	bags[counter] = scanner.Text()
    	counter++

    	if counter == 3 {

    		counter = 0
    		first = bags[0] 
    		second = bags[1]
    		third = bags[2]

    		for _, letter := range first {
	        	if strings.Contains(second, string(letter)) && strings.Contains(third, string(letter)) {
	        		if !strings.Contains(seen, string(letter)) {
	        			seen += string(letter)
	        			num = int(letter)
	        			// check if lowercase
	        			if num >= 97 && num <= 122 {
	        				total += (num - 96)
	        			} else {
	        				total += (num - 64) + (26)
	        			}
        			}
	        	}
    		}
    		seen = ""
    	}
    }

    if counter == 3 {

		counter = 0
		first = bags[0] 
		second = bags[1]
		third = bags[2]

		for _, letter := range first {
        	if strings.Contains(second, string(letter)) && strings.Contains(third, string(letter)) {
    			num = int(letter)
    			// check if lowercase
    			if num >= 97 && num <= 122 {
    				total += (num - 96)
    			} else {
    				total += (num - 64) + (26)
    			}
        	}
		}
	}

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Println(total)

	// str := "ab£"
    // chars := []rune(str)
    // for i := 0; i < len(chars); i++ {
    //     char := string(chars[i])
    //     println(char)
    // }
}




/*


vJrrdQlGBQWPTBTF
fcpTMnMqMfTnZpgMfPbFBWzHPpBPzbCPPH
mcVMfcsqZgmgVcmfgcmZmqZNJhrlrdhNhDdrRRJSvDTRhJlD
pMFRmLwHMbRPmMbPPddvqqrrNSTFVttdrN
hgfpgCGZcjpcgfvNtdrtjvrdtSrd
gZgsBBBlZggBGhsfhpzlzLDLmLRDRMLDPw
hChhMFCvqtTMwbSSHgTZWHZd
jjBNPjJJNfsNjVnVJJNcNfPwGbSbDZnZZgHrddwHrrgWGb
mBBRRmBBQBmNJWhCzqllzhRCCv
lQgpngNgQvHdSgWwjMRmDjmMDHmm
zCLVzfzzbbCzsZZPbZPLfFJJMDWWRcDsmJRcjmwTmlRj
BblftzBtlFznptSQQQppNG
wJJwqCtCGRcVlqlM
BQpppjBQLczTrvHRjH
QQQFnmQWWRfnpQBpQpfDCwCdbPDCwbNNPtdJPCZw
gpJjshBpgjZGppJqBGJjJZzTwzTmcvzwwcmvwsCFdmcF
WPSSWWSQLVdDDfWltDWLPfttvFCVmzCCTFnmwcnnnCTCzVVv
tLldLltDQfflrRWNqBRjgHBpJNZjHj
bzVJjVnjbCGVLZQLmmsJZZQQ
RrwwzhPScWSwrhvZZvZlZvvSTsQS
HwFhzFWdPHfcPwPWPdhWffnngpjtnjgtpnfGCGnG
CPwQtftDQfPDBPBCfDDDCDptszcpVVddcRczVLVdccRGrLWs
FqlSnhlqhmhMbHqqSQlHbcrRrsWzRdzdWVzLRGRrVF
MbQmSnHZhqZMQMTJCttjCgPCwfgDwT
CCSpvHtZHSwftFtdtbfR
QJmNPmjjJNgNVNSzDlmRqbWlqWWfcqfWqbwfqR
MDhJzmSMDmsZrLhssrvh
ZhznnrLzcHhHSjsjSBSsBnSS
dTwqDdqDRQjNdwqjldggDvBJfmBfTSBbBSvfSJsmff
DjCldNglVwFVgZHHHzhCMcLhMC
vBnShjwwSshmQPmtJLpJtn
rDLFCWrClWCMWWVrbFVJqpQqpHmtbzJPQzJmzb
ZMCCDCMNrTWTrgScgGRhsvcsGLSG
LQpJglQQRjQsppfsQbjfbQlBgBhFhrvghhZCdPZZZthPgv
zVHDMSWVVMVWDzmnVMHDSMMzZvNFFrFvPCdmdFdNdrBPZhhd
ncqqSzMVCcGWVSCTWCDcVTffLLLbJsLLsRLblRQTps
zjGzLQtFzzRgwwLhVrqw
dfClCdHZsmffZDWlBZHCDBmhJbqTgbwgqbTnwrgrqRbT
HsdwPCsWDpDsBpfdWdHldWpsGvvccPvGcvzQvFQvccjNztQt
wmVVgFPrFdwJrlNHQHSHCCHL
tWBtvnBqZZMpcvmmqMBRCQQLCLWCHfNQQCSGWL
BBsnmcpqPswFsTws
BQRpFPJJJJPmPRqZNFVhcczHHzggwjBhghgzHw
snTsTLtrlvSSSslsGdcwmjhgggvjHhmH
nSsWWTtCbbDSnlRRZCfFRNZmCVJf
tRRMCWLtJWQLqLrmLHVLqmqh
JszPjSbGbsnGnSZprVpFhvFqvhrqZZ
zgbGSDBbPsTgbDBzzSDnDnPTcWlWJCQlNttNwwwMcMctcW
hlVRvPvzqqtRdwRRJsst
HHVNVBMBjHLTjVjwDjsbjJwbdmbbss
NBZHMCNVCCpgLTWggBpgNLTvqCPnGhQhCCGlqlhfcvvGfn
mwbfbfbDCqRJZRbCSvmfWTQFczTznnnFTFnrzJsz
BdhHlLjpjjjncSprnsSFWS
ljhVBPjSdHPRfZRZDvVRZM
tGqbqBSsntRgNqwNNVVHVN
hclFvJZvCDFppDpZpHNggMTwdlrMQNVgHM
CCFmcZLDFpvzZhCFJvZvmwjSRWsBLWsnfWjRRGGfnsst
GdGQQFdcMPwMdLFvWsNWFDLfss
SqjhtjnrbVznSztSqtzpjztVvTmNNmmfMMfDDMDDNTqfgsqv
rVhhZjppVrhpVzRbjSnzHPMwlJCJQdcRPPlPPcHJ
JVQLVgVZghFtFlhghtvSzsddmrdvssmzSWtd
HTMJCBMCjnwNBnCbTNwMdWfzvzsrsvffWbdsmfPr
BGnnpDnTjjHJwDBNpqlFQVQFQclcRFQqpR
BRhbrQDttbTTtRDtTRRzLHWZLZHGSqWLCBNWqLNL
fwFPPSjmsmJGLsNH
dvfSdvfVMjPTttTzczgTcd
dZgggwzgvsggtdstZTZgdfnhSJSSJDDhnDBdppnGnhSp
VQWRQWVCRLFGnThJCpFJ
LbmmbQVcHcmmlWjmVlVQNVRzvwwZvTrsrNwNwzZrMvfsqt
lDZQSlHDbLccRPQhCNhG
gtsntgvdvBvvqgsTgBggdrWRNzPhWczPbWcdWCccGGGP
sTBttvrFnnMTMJngbqfLlZLpwFVljwppZZDl
zNNNgqpgmLgqlHBHsMGslH
WdWFrFwhcwWRwhddcRWcdQbcDDslzBDszsHbGBDfbHfzVlVl
ZvhRrvPQwvWFQRZvFdJttSPgCmNppCNzJnJS
fCzRRNGfqNRvwpQhwrGcwZZT
gJnStgMmLhdHndSSTjcTrTpcmrjjcrrw
FFJBbdddFPPhFFNWCF
btrHRSBBSNLLRPLwhbhpqpfWhQppWZ
zCzTvvmgDvgDZhqWZZthtDZh
ttTjMsvCgRRLRSsBRG
LsSFFTTDWdCsmFTlLSsLDDRRQCvhpRQGNGQBJBhGGMNB
zqPtqZnjPPrPvJHBMHrJrMpv
VbqfjZfwgtfjPgZPgtwDLTLcTlcFdWLdcdVTJF
pfMCDmpHbdMQQdQFFG
gdjldRsVFRntQnqR
rlJVsWgWPWjsslSpDbScmSDPHfCd
lnFFGgBFBslDFGbFSjnNTjjppSrQHhnT
zcvmCRcvZmcZzWpTQhQrrTSPtHWH
CRccrZJmdJlwDJwgswGg
hllrrDzggGppgSSLNWgW
jlTlPwwqjjntVpWWPNnP
wjjJqvQjJjQJbTjlFqhBMzfDDmMCGBMHDCGb
jvQPhhtCRtfmqHHjqHHJsl
FFSTcBTBTMwFGCTwMTcGwTVnsHSJzqqJJJplmlpJHszZZzZD
dLMdVMNGBdGFMTNTRRLrQWCQhgWQbhgf
gdRgdgzzrvrzggDwgDGpPLzrbNljMTsbWWjWjZbTjLZMWcWj
tFfCQHJJnJMJTJjNNMjl
HmtffVttqHQmBCBQCqfFnCwRqpDvPRrGppRggNzdwgzp
DHSqzQbzWlRLDzMZNpVLgnpNLggw
cZcdTmPPthPdsvvdhPGTvJgwnpgjjTgNNwMVngNBjNfn
PPdJPvrtGtcFdFFchDRHDqHzZWSQQCrQWQ
BcgnLBLsFvRnGRRRlzfJbbPJzwHPwPFz
hCDjWMDVNfVllfzddw
qqMqpWCMjDTWNWTBLpgsgLvZwtGLLg
zczPgpGzhnbmbchhHwqwhSwfwHCFWw
VJdmVLlLdVJSJWHSTFwH
rlttQLVLdvvZpgcGbmDrzGMD
WSvtpqqtqccttVQpVvJNJSVNCmTlnCWwTTnWlBBBjwCBTlTP
ZgfPHfPfMHsDCwnlGBwTMGBM
rgdffZhPrrLsdLZpvcFSJJNvpJhcJv
qVdqJGvzgJzJgwzgWvdJzpblcRRWmLFFcLBmllFRRMRFRH
TGGSsSssNPTSLlRLcPHMmnPB
tTjTZtNGhrCjQNCjQQDTCSjZvfJbdgqrdpwqfVzwgzvdvVgb
VTmwcTVSMHwbMwbDVBTcMpJfpfnWqdJbZpJldfsjZn
hNtPhtzFzPQGCCGFFCGtnqQqWZWplsjWdlnlldJn
vRCRzvvFFFvhrRthPtLrtNGSwBVDScDSgHHjwwcBgSgTSL
dWCsWbWWchblsmbWVZqqsSpsGfBqBVBB
DtTtjPJrgjjtTTwgPwwjrTgnLqSBZQLqngQppqnfBVQfGp
PJPwwtDwHGGJtJRFHmhCFRCvdmHR
mMsMJSCjllsSSmBBclsMsJHDbcHqqbHpqHGbDZHbqHpb
RnQnGVnzGzFQgzWzpzvpqDHW
QVhRTfGLLFGTTFFwhnQVNfFwJsJsMjsBMrlsjrJlPSPlTrls
JNMJSVSGVCjnWZMZWWcH
gLTcqbqhqbbgzgnjpnjjWHnP
wqlbcrfTwrvcLBwwRtJwsNRstRsCCN
MlBssQBchZDLNJZgmvGg
fdzHMfHSzSprfgSvvJbmvDGNDW
PCHTRfjHnzHMzzfrCPCpMTlFhcFstqVwVCFllQcBtqss
TtFnnFJfDhtdfJJcFtfnsfcFjBjLDjHrDLrCjMjwCLLrZjrS
qQmWmQzvWpRQGvgpGGRGRzmWwZMwBLCHMZjbBBCLwrHSLrqr
MRllgRWWMlsJFnlFclJT
SRRrRDRBRTdbdMRZBZMprTCJCnWGvChJGzLSWWzsGhCs
wwqHPtFwjwTHLHvGTsGW
FlPtqTNVcTVtwtmjRbBZfQbfZbQmRRMR
WSWfQttffsHSfRRRStfnCsQQqlJpbhnrnmNzJbzqNbbrpmnb
FGFPddBcBwDPzpzbWlpzDbbh
ZPdPPLMFdGwFFGdwGdZwcZgTtSTVCsRRSgSRTQWTTtCTtH
vHsfGHTvSvHHHsGHctMgtHrJwbJJwrjgbrdzjWCrdrrw
hqZRLmmZpFhcLhFmrzJQbzzmQQJWJJbm
LNZFcpPlhBRhqDDllRtnMssGfBsnttGTnttT
VDVrLrZZcjrhhFrZppGlglGMPFwFWNQw
bzszSBHBWNGcscpN
TJqBqSfTBBqBHzJqddBqzcLnLjnhCRTvvRrnDrvrvZRn
GLzrNWbtMptHDmNDglgmlD
fZtcfCRvtBcQjdjgmmjj
RhBhhqfSPPpttrnPnVVW
BhVRJGwWqtHjZqTDLZ
gQnfpBdPNpQrPNSfBdndnpTTDFZttDLLzZzTzCLNLZZD
mQQPsgrldpgdBQgSbGVcmcRwGMWhwVwW
DrLCctBCLQtSSQcLbcQHWvvvlWHHnWlWBlNRRB
wqdmpgqsZhzGphwwpZGsppRvfnJsWfHWvfFfWFsfvlNN
mwmhVppTqpGqpNZpqTbSLLttDrDDtPQTtr
qwqmgnglDnlgtQzQJzJQhmWQ
pTpTpssdsVvNsdTSZGdSdjvCRcqcRcVWVczhWChtchzWcR
sGTvPqZvSGdZZGdsvNGdPHrFHFBDlDLwPgBFLLBB
BBBGsGGBrBBrqWVqRnWBBBWpzFwMhjMFSFPzzSwPFPpzzFvg
HtCdDdDctZDtbHCffcbddbNfvjvFSPFjMhMgLwPgjbFhjFFj
NJTDdltNgCNDZJJZCDJZDfJtrWWnQGBqlRVVlrBsnlrqqmnr
PwZhgbZSWSqqGznv
tTPVVmptcsrNrsTNpjRzqfHvvGfGWjfjqGzHWn
RVRtVDRmsRtrctmJDtgBBhBhbFgJPFFMFJgP
jPzzCCPzTtTfzrRtgSNVRHvFQVvbpQppVN
sSnDlBGBwJbFNplVlN
cLwSwdMhSwcBcsBZgWjCTCWfCLffrg
RSNPvTTNqFTSvNrSBvBGJGzmFMslgCMJCgmzlc
fDVfpptLWQfnVLffVHbQDQCclJzGGCtGmmGJmzMshzGh
VfQnWZfZDbdnVHWcfWnfHWVvPrTSNZqSwSqPjjvBwRqrNS
FLRpmRwcpjfzjSnD
tGvPNvBnPQggPQQvPgNHDjSSjDzzthjzfHrjlT
JGqvWNCCGQBWGBQvVLsCMMRLRnRMnwMc
fGJbzgBffCGpPGDVnG
mcTccshvbbdRNRsNjdLjnVlHVnHLqVpDpDqD
wdmsWvWssbZTcWvRhfzMQtrzMgrfrZJgfQ
NfSbvZHZNRSbQbbQgZrMjhLwMrjLjwHLCmmh
NTWdJBFcWJFcdsFJqcqPwqmjpMrLCMpLMwLP
dNJctnFBVfSGgvnfZz
GSnRJfGfRJgMDMGWnfzdmptpFJppLvwLwvLt
hbjZzrQbblqcLtpwlHvFplTH
qrzqbschrQCqqjPcCVcCGDfGMWDgWNGDDSfgnf
vmMpCdTndCvMdmnFcCRJWBJGcZJRJB
NDNwGzshPLrwVVNsjswhGzjFSfFFQQRSJWRBFcFRfsWFQB
NwNhNjVzhhzzrgzdqqvqtnqvlqdggG
MdPLVSSlMMVMmlLBBLFdvZNWqWztStttRRNqzqNGTq
DhJfhghhCgwChJgJwHHzbsHpnZRtTWqqfZRGTnWTZtNqNRWR
hwHpJbprwpQhDHDCbCCzsClBvrLMVFPvmPlMMVMdLrvj
DssDrqRsWsNfzfsWLRzjgTdBlgzFpMlgTFTglT
ttCZnSQmSQmgjGQGQgDlBp
bhDnCmbwVmCwwtZttPwbRWsRJcqWJfcfsfrqVrqq
ldBgTMTRvBDVnCCCTdSRTqNjbjSbPPPPqtfPqtPJFJ
cZHZrszLrrrZHrbNjNtbJCfqNJLt
GZzCzWZGGsGzmzZcmGssZzZVvnVdBDddRRDnVlWgRTDdBM
RjNrrjwGDDqqGJsHtzpMHHGz
QCbWgbShmBCCPClmmWFHzJzTbDdsMJsTtpTD
fffQfnSCWDBfhCDLRrNrwcrqVqwNqn
zmRrDRzqjmLLHzDjLsHLflJlVVJlWWTDTfdMtlWJ
pPQQnbvSpvNbgfgfVtMVJfgdtG
SnpnVFcPnNnPvpNSFNSbhHLhrjhCqRsRBRrHCLhzmC
CZZzlnCZNlGGcbVrbtVlMtct
MgFQDFgQRLLHhJgDFqQJQLgdtVTrttSrPSmcbmTtvSqvVSTV
hFQDDfMDfLgHwWfBzWwwsZGW
bHVDdHVHTPMvnSQnWSDQgDmm
GhrCJfbfrhfbRJcqGqlwZtnBRtBWSQgQWWnWQW
lfcCrqJhlfFqphpplNCrNVMPMPLbsLPLzFVHVLsVdz
VDhFCZhtFdPqwwcp
SvnvHNNnTvbwNNgnHwTHgwBTLcdqmmfmqLGmmTRLPfpdGP
BNWsHJgSnwgMMgMBBWMDVJjtjZrDJZzztJhjQr
HDsSHLRnpjbpbbRDbqLjLjjGGVffMVGMdvnfMcNvfBBGcB
TCzQQztwwNTMqMdBVv
hCQWmtCzZthPPZPrLjSbJqjSjLLFjLpr
ZrrZqJDcZSCFLLHBFcjjHF
TgvnDTlTtQwgBfwwwzLjGLdF
VbnVngMtvDTTVMQDQMDQlsbZJChCmCPhprrZqhqZSZPJ
glMGHBJTJJTplgwcCgcqcFhhbWncFm
sSswtPfRDmWcCqfchq
RZSdSzsVzNPSwSSQsdzSSQpGLjJTMpBGrJrLLrplZBpG
WQqqwLqQlnlWDwtbVbtCNfVbpV
dFTRjBPhcBgBrFhTPhrbVptJpNNbbtJCbJSL
hjcmcRmgPPcRcPDmHHzGLWmsDmzH
rWFmrRmmccSZJWvSLZTH
hDPhGbhSjtbpqJLvJHjLHTqj
pnplBlfBPPhlgfDbDhglPMMrwrRRSSncwccQzddzmC
LbccJCGzbcCJcfGczcnmNnvNmZNLSDZZWPWS
dwstRhTsrsFddPZqvNWP
BBggRrQstBwBRTHWTprRCHHGVljfCGCfcljHjbGV
FHVBSVDvnsFDwwSVwwvGVSMFWhWcWptMWchWMtPPcWtNNWcj
TgqJrJTRmRCNrbcLjprLnp
qQTlfdlZQgmfqqnFVznvQwvnsBsV
TGpDDMQGMZNtfvDJdtWd
jbrmstmllRmNvVhmmvJVhv
tbrRzFFLlRrjFlLlTQgLQwwLMwgTZBTB
QFgFWQQfSgLFGmtnnVmqCPWmPH
TTzjgTbRRqnRsCPCsP
NDMMgZjzcJvbjhMcjZbbbJJNpdpBfBvSBBQwBSQLQSpSplBG
zcRNsQSSMjRsNNZZFBLQHHFFBPWF
tvwCtgvqLJNnNBCH
fNNwqrqNMpTrDlcs
MMHMVPRJHJWvqzWctbtQQdQz
DFfNFffDnTllfTfFfmzsjqcdtQGQpbddQQbssn
mlFNCgFNNNLrmLFCThhhzJBvhSJPVhMgMh
PWjhljbHFhjbFMWhjbPfhbTGZvlGcGlCLvvwtGCNZGvc
SRqBqBrmQWQrgQrrqrJBLZNccLNZmTCtvTGtCvCt
rJDzDSSBrzdqQWDPHFMjMFdjHMVnbM
qqLwvvtrLFqqfqrjjjdBZfBCBBJdlT
ZGZpRZHbQDzDWRRRVdBzSSlBdzjjzdJJ
ZGpgNDQmWGDRmRpZMQbvPPtnnFnLsstFmnFrPL
TdhcfZhdZZdpdbPWttCWrrCN
MBMMqRLgpGpFFWbNsvLwvCPCCP
mpBMnBRMBGqJfZcfZZHZlhfm
CdmGdnMcMwHjhDtFFnrj
vPbVbPBPPpgpgWJpvTjqDZZqSHqVZShrDj
BppjjgvbJjbpNbzPfNcGCLlCRcmLLflllGcc
qDtgVttGFtlslStS
gCZbbHCjvJbZjCbJhHhHJrZcslJcLzLllcLNFssMSsTlSM
CWbWrZgWBQQBBpfdPm
hstPtCGtltlTClllPJLScVdPdJjLPJMV
NHRbDZDQSDFFjjdJ
RqbQpgBmqZvqZNQqgZmmbszpTtthtCswhjslwwpTWC
CVdwBJJdppbbwdBVrJbrJbGPlMFSLrjrPjmPFFmPRRDF
NNWHHhNZTcQWhnNFlmSSlRmLjnPPRF
qWsccHTZccsNsZcvTcNtStpBtbdVwpfBwbVCBq
lPQHNJhMPMPFlNMHBqZBwQwQwQZwcCqw
bWddDzbWbftdDSDbgttgnSDWccLwcvBczqcqGZzLccZTZwwc
spWrssWrnDtDpfSWDtsFqlFPjNMjRJVVNNPJNp
bCCfcWVLTHfSSdHwhH
sGQSZSzQJmmQsphwHHHsndnpHN
zPSqrmZPFCvFTbWMLV
tLtVBGLJqGqVGbzGSCsSsSqQsFvZCSQv
gRgdWlHTBHgjjHlWpWjWjrwdCfQRZFSssQQQZmQmMSvZfFMQ
lPHlpWgjTldprNWHNNdHjTctcLbVcnNJJGbVzBhnbhhJ
zVrSwzzJbVrbqFCVVVwVCztWDDtfTZsWDZTLZZmSWsDm
bpgHlgBbbGGGglBGRNvMpWfTDjmDfWDjfRZZWLtmZs
bGbvQHMpQccFJPPh
VGqCPmPjfGqCdMqVMhjhmPChDJDJzvrrbrBvrdrpnJDpJDQr
TSRsgHRSFHTlHvJvBDvvzlptbv
ZFLTsRRgZTgWscHTfWNWNPPBfGqmmMfV
TvTrrrCVCVwqjPrWfWhjfH
RRmgmnggltRgNpzRsdfqWWjdFdvNHfdh
zZlRzDGGZmbmmZbvGJVccwCMVcVVTLwDwC
QPsNlvvvSccbbNQcSPvDVSvzTLLCgRVzCJgTJpgCpphgzh
MDqHwFrMffgFpgpJLzTz
ZtdrffBrdqmBBmfwMtDtQPPPbjcNvnllnlbNtScn
HbbbcpTHHMMqNTCddCVBQvgPzJPJWQBQjvpBvQ
FFrDGtntFFwhrRFDFthfRhRmSJPJvvJZjZjWJJvJQJnvWjjg
rtfFfLmLRmNgdHqcLNHd
FpFHCFWtFSnCWnBfJJfgMJDGHDGGsG
rhrLrrhLrbtZThLfgsfGNDfgTgNcDs
QmPjbdqjmbbbrmhQqQZrZStRdlnnFdlRzVVVWlnpzR
bBMwwjzhbjhssvsGZBSZLr
JFtnDtRzJtffJHWNtHncRRrvGZvSnllZZZsgvlnvVvlv
RRPHPHFPHHdcHtzNfMQhdCwbqCmbMChhqq
pWGdFSWwwjLdvgNNvggl
mTNbmRPHmmVNmvZhnhBssBlhnb
HPTzRPffJJNzjCFpDWDz
MHlgzsqHlbmzgsHzlsbcRWPdPtjZFqhGGdrPrjPJGrVP
vpwwvQwCnhNQpSnLdVtrrZGZtZjdVSdJ
hfffwvTpvLwDpCLvDnQDHbmRRTcWRHMWWHWMmWMW
WHlNHWWldjpwntnWBPpPQFZFBFhZBZCZ
TqqvgvmgfmvDVLLfqqLsrFBRhrrBFJQBGPgPZGCR
mcDbcDmzLcmDDzfVzTQNjNzNztdzjNdwSHlH
*/