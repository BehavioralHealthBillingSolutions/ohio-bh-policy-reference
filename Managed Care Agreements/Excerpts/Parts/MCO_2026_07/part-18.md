# ODM Medicaid Managed Care Organization Provider Agreement — reference excerpt

> **INCOMPLETE REFERENCE EXCERPT — NOT THE COMPLETE OFFICIAL DOCUMENT.**
> Do not substitute this transcription for the official agreement.

**Source revision:** July 2026
**Complete official document:** [Publisher PDF](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf)
**Original PDF SHA-256:** `5911ba372c1f5ae4783b4b649344483f24f9f5c2066b4c2e7b4e2163b9d24428`
**Original PDF pages:** 450
**Omission explanation:** Original PDF pages 363–404 are intentionally omitted: the Milliman rate-summary report, including its attachments and notices. Redistribution permission has not been established. The Appendix M divider is retained; the excerpt resumes at Appendix N.

Page labels below use 1-based PDF viewer page numbers, not printed page numbers. Source text is presented in fenced plain-text blocks to avoid interpreting it as Markdown. Tables/columns and images must be checked in the original PDF. Contents-page references to omitted sections remain as original source references; those sections are not included here.

[Omission register](../../OMISSIONS.md)


[Reading index](INDEX.md) · [Omission register](../../OMISSIONS.md)

## Original PDF page 335

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=335)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
319 
 
ii. 
Review the completed ISCA and accompanying documents; 
iii. 
Conduct interviews with MCO staff responsible for completing the ISCA, as well as 
staff responsible for the MCO's information systems; 
iv. 
Analyze the information obtained through the ISCA, conduct follow-up interviews 
with MCO staff, and write a statement of findings about the MCO's information 
system; 
v. 
Assess the ability of the MCO to link data from multiple sources; 
vi. 
Examine MCO processes for data transfers; 
vii. 
If the MCO has a data warehouse, evaluate its structure and reporting capabilities; 
viii. 
Review MCO processes, documentation, and data files to ensure they comply with 
state and federal specifications for encounter data submissions; and 
ix. 
Assess the claims adjudication process and capabilities of the MCO. 
3. Business Continuity and Disaster Recovery 
a. The MCO must develop and be continually ready to invoke a comprehensive business 
continuity and disaster recovery (BC-DR) plan that addresses operations, staff, and systems 
that support this Agreement. 
b. The BC-DR plan must align with the current version of NIST Special Publication 800-34 and 
must include documented recovery strategies, defined recovery time objectives (RTO), 
recovery point objectives (RPO), periodic testing (at least annually or as defined by ODM), 
testing scenarios, lessons learned, and corrective actions for systems supporting ODM 
operations and data.  
c. The MCO's BC-DR plan, and any significant updates to the plan, must be submitted to ODM 
for review 60 calendar days prior to its effective date. 
d. The MCO must periodically, but not less than annually, test its BC-DR plan through 
simulated disasters and lower level failures. 
i. 
As specified in Appendix P, Chart of Deliverables, the MCO must provide a summary 
of its BC-DR test results (Summary of BC-DR Plan Test Results), including any 
corrective actions, to ODM within 30 calendar days of receiving the results. 
4. Acceptance Testing 
a. General 
i. 
Before the MCO may submit production files to ODM, the MCO must conduct 
acceptance testing of any data electronically submitted to ODM as follows: 
 Whenever the MCO changes the method, preparer, or file layout of the 
electronic data; and/or
```

## Original PDF page 336

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=336)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
320 
 
 When ODM determines that the MCO's data submissions have an error 
or failure rate of 2% or higher. 
b. New or Modified Information System 
i. 
The MCO must include ODM in user acceptance testing and end-to-end integration 
testing when significant system changes are made that impact the user experience 
and/or end-to-end data flow. System changes include any of the following: 
 Existing system updates; 
 New system implementations (replacing system or component with 
another); 
 New infrastructure support systems (replacing an infrastructure 
component [e.g., SFTP or EDI system]); 
 File format changes; and 
 File transmission protocol changes. 
ii. 
User acceptance testing must include training if there is a perceivable change to 
workflows or user screens. 
iii. 
Data files that are submitted to ODM must be tested and accepted prior to 
implementing in production. ODM will notify the MCO in writing when a test has 
been deemed successful and the changes are approved. 
iv. 
ODM reserves the right to verify the MCO's capability to report elements in the 
minimum data set prior to executing the provider agreement for the next contract 
period. 
5. Claims Adjudication and Payment Processing Requirements 
a. Timely Filing 
i. 
The MCO must accept claims for 365 calendar days from the date of service, as 
described in OAC rule 5160-1-19. In addition, the MCO must follow the overpaid 
claims and timely filing exceptions described in the rule. 
b. Claims Adjudication 
i. 
The MCO must integrate with the OMES for claims, third party liability (TPL), 
authorizations, and any other types of data or processes as directed by ODM. 
ii. 
The MCO must electronically accept claims from the OMES and adjudicate all claims 
to final status (payment or denial) within the timeframes specified in Appendix L, 
Payment and Financial Performance. The diagram in Exhibit K.1 provides a high-level 
overview of the claims flow. 
iii. 
All claims forwarded from the OMES to the MCO for processing are to be considered 
clean as these claims meet the threshold edits applied at the submission of the claim
```

## Original PDF page 337

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=337)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
321 
 
through the EDI and meet the X12/TR3 standard. If the claim forwarded from the 
OMES to the MCO does not have the necessary documentation to adjudicate the 
claim, the MCO may suspend the claim until documentation is provided. If system 
changes are required to properly adjudicate claims, the MCO must notify ODM of the 
intent to suspend claims for programmatic and/or systems concerns via their 
compliance mailbox and follow the Claims Payment Systemic Errors requirements to 
report any potential impact to providers as outlined in this appendix. 
iv. 
If there is information on the provider network management (PNM) system 
generated provider master file (PMF) or any other supplemental file generated by an 
ODM system to support claims payment, the MCO must use the PMF or other ODM 
system generated supplemental file information to adjudicate the claim(s). 
v. 
The MCO must utilize the ODM PNM as the system of record and reconcile claims 
against the ODM PNM PMF data points as directed by ODM. 
vi. 
The MCO must provide updated claim status demonstrating all claims activity daily to 
ODM. 
vii. 
The MCO must provide its network providers detailed instructions on claims 
submission procedures, including information provided by ODM about the role of 
ODM's OMES. 
viii. 
The MCO must provide out-of-network providers detailed instructions on claims 
submission procedures, including information provided by ODM about the role of 
ODM's OMES, within one business day of the earlier of receiving a request from an 
out-of-network provider or becoming aware that an out-of-network provider has 
rendered services to a member. 
ix. 
The MCO must notify providers via ODM's OMES, who have submitted claims of 
claim status (paid, denied, and all claims not in a final paid or denied adjudicated 
status [hereinafter referred to as "suspended"]) within 30 calendar days of receipt by 
the MCO or its designee. Such notification may be in the form of a claim 
payment/remittance advice produced on a routine monthly or more frequent basis. 
x. 
If a provider and/or a provider's clearinghouse submits a Health Insurance Portability 
and Accountability Act (HIPAA) compliant 276 electronic data interchange (EDI) 
transaction to the MCO and/or the MCO's clearinghouse via ODM's OMES, the 
MCO/clearinghouse must respond with a complete HIPAA compliant 277 EDI 
transaction within the required Council for Affordable Quality Healthcare, Inc. 
(CAQH) Committee on Operating Rules for Information Exchange (CORE) timeframes 
with the HIPAA compliant claim status category code(s) and claim status code(s) that 
will provide information on all denied, paid, or suspended claims to the submitter. 
xi. 
The MCO must accept and use, and must require its providers to use, third party 
liability (TPL) data maintained by ODM's OMES for the MCO's and provider's TPL 
activities.
```

## Original PDF page 338

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=338)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
322 
 
c. Edits 
i. 
The MCO must implement claims edits (e.g., Strategic National Implementation 
Process [SNIP], National Correct Coding Initiative [NCCI]) at the direction of ODM. 
d. Grouping Methodology 
i. 
When the MCO uses a grouping methodology to pay inpatient and/or outpatient 
hospital claims, or ambulatory surgery center claims, the MCO is expected to use the 
same grouper software and inpatient only procedure listing (determined by 
Medicare, 3M, or other grouping product) that ODM uses to process fee-for-service 
(FFS) claims.  
e. Electronic Visit Verification (EVV) 
i. 
The MCO must have foundational knowledge of the Ohio EVV system and processes 
to issue resolve as needed. The MCO must direct providers, individuals receiving 
services, and direct care workers to appropriate resources either at the health plan, 
ODM EVV vendor, or ODM to address provider questions/concerns. The MCO must 
inform providers of the use of the EVV data collection system and how the data will 
be utilized by the MCO. 
ii. 
Applicable Services Subject to EVV Requirements  
 The MCO must use data collected from the EVV data collection system 
to validate all claim lines subject to EVV against EVV data (100% review) 
during the claim adjudication process. EVV validation must be the last 
step in claims adjudication for the MCO. The MCO must determine 
which claims lines are to be sent for EVV validation based on Provider 
Type/Provider Specialty, and service code (and modifier as applicable). 
The following list of services are subject to EVV validation:  
a. State Plan Home Health Aide; 
b. State Plan Home Health Nursing Registered Nurse (RN);  
c. State Plan Home Health Nursing Licensed Practice Nurse (LPN);  
d. Private Duty Nurse (PDN)/Independent Nursing;  
e. Home Health Physical Therapy;  
f. HH Occupational Therapy;   
g. HH Speech Language Pathology;  
h. RN Assessment; and 
i. 
RN Consultation.
```

## Original PDF page 339

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=339)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
323 
 
iii. 
EVV Claims Validation  
 The MCO must inform providers of the outcome of the claim validation 
review for each claim line. The MCO claim adjudication system shall be 
flexible to allow the ability to deny payment, as directed by ODM, for 
EVV claim lines during validation. The MCO Remittance Advice (RA) 
and/or the 835 transaction (via the Remittance Advice Remark Code 
(RARC) and Claim Adjustment Reason Code (CARC) are to be used to 
communicate success or no success of claim line validations.  
 For services that ODM directs as only requiring an informational warn 
edit:  
a. The MCO must code their claims adjudication system to post ODM 
directed RARC on a claim line that does not have an EVV visit match. 
The RARC will be reported on the 835 transaction to inform 
providers that the claim has been paid, but future claim payments 
may be impacted if the provider does not make changes.  
 For services that ODM directs as requiring a denial based on no EVV 
validation:  
a. The MCO must code their claims adjudication system to post ODM 
directed denials, and RARC and CARC codes on the claim line that 
does not have an EVV visit match. The RARC and CARC codes will be 
reported on the 835 transaction to inform providers of the denial. 
iv. 
EVV Reporting 
 The MCO must submit a monthly report of all EVV-related claim lines to 
ODM in a format specified by ODM, as specified in Appendix P, Chart of 
Deliverables. File format must be in the exact file structure, headers, 
field names, and value constraints specified in the submission template 
provided by ODM. Submissions that deviate from the template are 
considered nonconforming.  
 The MCO must review the monthly visit report provided by ODM to 
identify trends, provide outreach and education to providers, and 
identify potential fraud, waste, or abuse.  
 The MCO must report fraud, waste, and abuse to ODM in accordance 
with Appendix G, Program Integrity.  
 ODM may request a targeted audit or review of EVV program 
components in accordance with Appendix G, Program Integrity. 
 The MCO must work collaboratively with the EVV vendor to establish 
connectivity, to conduct system testing, and to adhere to technical 
specifications until all scenarios are passed and the system is production 
ready. The MCO must also collaborate with the EVV vendor to 
implement any system updates or changes as necessary.
```

## Original PDF page 340

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=340)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
324 
 
 MCO’s claims matching rate must align to the overall match rate for 
ODM. If the 6-month average claims matching rate for the MCO 
deviates from the state mean by more than one standard deviation, the 
MCE must, at ODMs request, submit a written explanation to ODM. 
ODM may request a corrective action plan upon review of submitted 
explanation. 
f. Systems Audit 
i. 
The MCO and any subcontractor systems must undergo an annual independent third-
party assessment conducted by an assessor with no conflict of interest, 
demonstrating compliance with ARC-AMPE (Partner Entity requirements) or any 
successor ODM-designated standard. The MCO must provide assessment summaries, 
detailed findings, and documented remediation plans with tracked status until 
closure upon request by ODM. Where alternative assessments (i.e., SOC 2 Type II or 
HITRUST) are used, the MCO must provide a documented crosswalk demonstrating 
alignment to ARC-AMPE requirements. 
ii. 
If the MCO or any subcontractor systems utilizes a cloud hosting provider, the cloud 
provider must be Fed-RAMP certified or undergo an annual third party audit that 
certifies compliance with NIST 800-53 Rev 4 (or current version) moderate baseline. 
iii. 
The MCO, and any subcontractors that adjudicate claims, must undergo a System and 
Organizational Control (SOC) 2 Type II or an alternative privacy and security systems 
audit that is prior approved by ODM. This audit must be completed prior to 
implementation and at least annually thereafter. 
iv. 
As specified in Appendix P, Chart of Deliverables, the MCO must submit the results of 
the systems audit (Systems Audit Results), including any corrective action, to ODM 
within two weeks of receiving the final report. 
g. Claims Payment Systemic Errors 
i. 
For the purpose of this appendix, a claims payment systemic error (CPSE) is defined 
as the MCO's claims adjudication incorrectly underpaying, overpaying, denying, or 
suspending claims that impact five or more providers. 
ii. 
The MCO must submit the MCO's CPSE report (CPSE Report) to ODM as specified in 
Appendix P, Chart of Deliverables. 
iii. 
The MCO must submit all communications regarding CPSEs to 
MedicaidCPSE@medicaid.ohio.gov, unless otherwise directed by ODM. 
iv. 
The MCO must follow all CPSE instructions as directed by ODM, including the CPSE 
reporting template instructions and guidelines. 
v. 
The MCO must ensure each identified error has a unique ID to tie each reported line 
to a specific error the MCO is addressing. For each error, the MCO must provide a 
specified begin date, and when resolved, a definitive end date. For each CPSE, the 
following information is required:
```

## Original PDF page 341

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=341)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
325 
 
 A detailed description and scope of all active CPSEs; 
 The date the CPSE was first confirmed; 
 The type(s) of provider(s) impacted; 
 The number of providers impacted; 
 The timeline for fixing the CPSE; 
 The number of claims impacted; and 
 The date of claims adjustments or required provider action. 
vi. 
The MCO must report all CPSEs on a monthly CPSE report posted on the MCO's Ohio 
Medicaid website. 
 The CPSE report must be public facing for anyone to view. 
 The MCO must post the online CPSE report as specified in Appendix P, 
Chart of Deliverables, and must label the report to reflect the updated 
date. 
 The MCO's CPSE online report must include, at a minimum, the 
following information: 
a. A detailed description and scope of all CPSEs; 
b. The date the CPSE was first confirmed; 
c. The type(s) of provider(s) impacted; 
d. The timeline for fixing the CPSE; and 
e. The date of claims adjustments or required provider action. 
vii. 
The MCO must have policies and procedures to identify, communicate, and correct 
CPSEs. The policies and procedures must include the expected timelines for CPSE 
identification to confirmation, system configuration, and claim reprocessing. The 
MCO must keep its CPSE policies and procedures current to reflect the CPSE 
requirements. Upon request, the MCO must submit its CPSE policies and procedures 
to ODM for review. ODM reserves the right to request changes if necessary. 
h. Non-CPSE Errors 
i. 
The MCO must correct errors in provider payments that do not meet the definition of 
claims payment systematic errors per this appendix within 30 calendar days from the 
date of identification of the error. 
i. 
Software Updates 
i. 
The MCO's claims adjudication systems must apply software updates based on a 
validated risk analysis and no less frequently than quarterly. The MCO must
```

## Original PDF page 342

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=342)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
326 
 
implement major software version releases based on a validated risk analysis and not 
more than 180 calendar days from release date. If the MCO maintains its own 
software, the schedule and description of changes for future updates must be 
provided to ODM for review. 
j. 
Implementing ODM Rate Changes 
i. 
The MCO must load ODM rate changes into applicable systems by either the rate 
change implementation date or within 20 calendar days of being notified by ODM of 
the change, whichever date is later. The effective date of the rate change must be 
the date specified by ODM, regardless of when the MCO's system(s) are updated. If 
necessary, the MCO must back date the effective date and reprocess claims to 
ensure any claim received after the specified date of the rate change is adjudicated 
accurately. If the MCO is unable to load rate changes timely, the MCO must report 
the issue on the CPSE report. Reporting the inability to load rate changes timely on 
the CPSE report does not limit ODM from taking compliance actions against the MCO 
in accordance with Appendix N, Compliance Actions, for the MCO’s failure to load 
rate changes on a timely basis.  
k. Processing Delays 
i. 
The MCO must not engage in any practice that unfairly or unnecessarily delays the 
processing or payment of any claim for services to a member. 
l. 
Notice to Providers 
i. 
The MCO must provide a 30 calendar day advance notice to providers of any new 
edits or system changes related to claims adjudication or payments processing. 
ii. 
The MCO must provide a notice of intent to recover an overpayment in accordance 
with Appendix G, Program Integrity. 
6. Electronic Data Interchange 
a. The MCO's technology strategy and systems must have the capability to accept and transmit 
real-time transactions as directed by ODM. 
b. The MCO must comply with all applicable provisions of HIPAA, including EDI standards for 
code sets and the following electronic transactions: 
i. 
ASC X12 837 – Health care claims (institutional, professional, and dental); 
ii. 
ASC X12 837 Post-adjudicated claims data reporting (PACDR) – Health care claims 
(institutional, professional, and dental); 
iii. 
ASC X12 270/271 – Eligibility and benefit verification and response; 
iv. 
ASC X12 276/277 – Health care claim status request and response; 
v. 
ASC X12 Unsolicited 277 Claim Status transaction and/or the 277 Claim 
Acknowledgement (CA);
```

## Original PDF page 343

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=343)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
327 
 
vi. 
ASC X12 269 – Health care benefit coordination verification; 
vii. 
ASC X12 274 – Health care provider information/directory; 
viii. 
ASC X12 275 – Patient information; 
ix. 
ASC X12 278 – Authorization/referral request and response; 
x. 
ASC X12 824 – Application advice; and 
xi. 
ASC X12 835 – Health care payment and remittance status (or electronic funds 
transfer). 
c. The MCO must implement EDI transactions in conformance with the appropriate version of 
the transaction implementation guide, as specified by applicable federal requirements. 
d. The MCO must be able to accept, send, and process multiple versions of X12 transactions 
concurrently. 
e. The MCO must have the capacity to accept the following transactions from ODM consistent 
with EDI processing specifications in the transaction implementation guides and in 
conformance with the Companion Guides issued by ODM: 
i. 
ASC X12 837 – Health care claims (institutional, professional, and dental); 
ii. 
SC X12 270/271 – Eligibility and benefit verification and response; 
iii. 
ASC X12 276/277 – Health care claim status request and response; 
iv. 
ASC X12 278 – Authorization/referral request and response; 
v. 
ASC X12 275 – Patient information; 
vi. 
ASC X12 820 – Payroll deducted and other group premium payment for insurance 
products; and 
vii. 
ASC X12 834 – Benefit enrollment and maintenance. 
f. The MCO must comply with the HIPAA-mandated EDI transaction standards and code sets as 
set forth in federal requirements. The MCO must keep codes up to date and meet all 
implementation dates as directed by ODM. 
g. The capacity of the MCO and/or applicable trading partners and business associates to 
electronically conduct claims processing and related transactions must be demonstrated to 
the satisfaction of ODM. 
h.    The MCO must complete and submit to ODM an EDI trading partner agreement by the 
timeframe and in a format specified by ODM. 
i.     If the MCO fails to identify an error on its behalf with EDI transactions within two business 
days and/or correct it within three months, it may be liable for the cost incurred by ODM for 
additional transaction fees if it must correct and retransmit EDI transactions due to the error 
at any time thereafter.
```

## Original PDF page 344

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=344)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
328 
 
j.     The MCO must connect a production mirror to the EDI CERT Region by March 1, 2024. The 
EDI CERT region will be used to add new trading partners and to allow trading partners to 
test in accordance with OAC rule 5160-1-20 requirements before they are authorized for 
production (PROD). The MCO must collaborate with ODM for adequate testing and 
validation for new transactions, policy changes, and other changes before running in PROD. 
7. Encounter Data Submission Requirements 
a. The MCO must collect data on services furnished to members through a claims system and 
must report encounter data to ODM. The MCO must submit encounter electronically to 
ODM as specified in this appendix. 
b. Information concerning the proper submission of electronic data interchange (EDI) 
encounter transactions is available on ODM's website. ODM's website contains Encounter 
Data Companion Guides for the Managed Care 837 dental, professional, and institutional 
transactions. Additional Companion Guides for transactions that should be used in 
conjunction with encounters, including the U277 Unsolicited Claim/Encounter Status 
Notifications, the 824 Application Advice, and the TA1 Transmission Acknowledgement are 
also available on ODM's website. The MCO must use the Encounter Data Companion Guides 
in conjunction with the X12 Implementation Guides for EDI transactions. 
c. The MCO must submit a test file in the ODM-specified medium in the required formats as 
directed by ODM. Test files must be submitted, reviewed, and approved by ODM prior to 
the MCO submitting production encounter data files. 
d. For subcontracted payment arrangements in which the subcontractor directly pays 
particular claims (i.e., delegated arrangements in which the delegate is responsible for 
paying claims on behalf of the MCO to providers), the MCO must submit encounters that 
include the amounts paid by the subcontractor to the provider and include claim-level 
detailed information. 
e. For subcapitated payment arrangements (i.e., the vendor/provider is paid a fixed amount 
regardless of whether or what services are rendered), the MCO must shadow price the 
encounter and submit encounters that include the amount that would have been paid if the 
vendor/provider was not capitated and include claim-level detailed information. 
f. The MCO must submit encounters no later than seven calendar days from completion of the 
claim (i.e., remittance advice generated). The MCO must submit encounters for capitated 
providers within seven calendar days of receipt of the encounter. 
g. As specified in Appendix G, Program Integrity, in accordance with 42 CFR 438.604 and 42 
CFR 438.606, the MCO must submit a certification letter with the submission of an 
encounter data file. 
h. The MCO must submit valid encounter submissions that include the application of specific 
edits, including checking for member eligibility, MCO enrollment, valid current procedural 
terminology (CPT) codes, cross field editing, and include valid line-level detail with 
meaningful claim adjustment reason codes (CARCs) and remittance advice remark codes 
(RARCs) accurately reflecting the data submitted to the provider indicating final status of 
adjudication. ODM reserves the right to direct the MCO's editing and payment.
```

## Original PDF page 345

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=345)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
329 
 
i. 
The MCO must submit valid claim and line-level denials that reflect the data submitted on 
the claim and accurately reflect the adjudication results. 
j. 
The MCO must submit encounters for all claim activities, including instances when the MCO 
applies adjustments at the individual line level or in a mass adjustment update. Encounter 
submissions must reflect all claims activity. 
k. The MCO must have software edits that check for and prevent duplicates on encounter data 
submissions. 
l. 
The MCO must follow the 837 PACDR standards for dental, professional, and institutional 
encounter data submissions, including allowed amount and paid amount in accordance with 
42 CFR 438.242(c)(3). 
m. The MCO must have processes and staffing to ensure that if ODM discovers errors or a 
conflict with a previously adjudicated encounter or claim, the MCO is able to adjust or void 
the encounter within the specified number of days as directed by ODM. 
n. The MCO must comply with the encounter data quality measures as calculated by ODM. 
Information concerning ODM's encounter data quality measures, including the 
methodology, is available in the Methodology for Encounter Data Quality Measures 
document located on the ODM website. ODM reserves the right to revise this document as 
needed. 
o. Exceptions to any of the requirements in this section must be prior approved by ODM. 
8. Non-Claims Data Submission Requirements 
a. All data on any services provided to members that are not reflected as claims or encounters 
will be submitted through the Managed Care Entity Non-Claims Reporting Template as 
specified in Appendix P, Chart of Deliverables. This includes but is not limited to non-
emergency transportation and other value -added or additional services. 
9. Electronic Health Records 
a. The MCO must encourage, support, and facilitate its network providers' adoption and 
effective use of electronic health records (EHRs), including for population health and quality 
improvement. 
b. The MCO must identify and track internally which network providers have or have not 
adopted EHRs and how effectively they use EHRs, including for population health and quality 
improvement. 
10. Health Information Exchanges 
a. The MCO must participate with both of Ohio's health information exchanges (HIEs) and be 
capable of exchanging protected health information, connecting to inpatient and 
ambulatory electronic health records, connecting to care coordination information 
technology system records, and supporting secure messaging or electronic querying 
between providers, patients, and the MCO. This must include but is not limited to using the
```

## Original PDF page 346

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=346)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
330 
 
HIEs for admission, discharge, and transfer (ADT) data and closing referral loops for social 
determinants of health (SDOH). 
b. The MCO must support and facilitate its network providers' exchange of data with Ohio's 
two HIEs. 
c. The MCO must require its network hospitals to provide admission, discharge, and transfer 
(ADT) data to both HIEs. 
d. As specified in Appendix P, Chart of Deliverables, the MCO must submit an annual report 
(Network Provider HIE Participation Report) to ODM providing the number and percentage 
of network providers, by provider type, connected to one or both HIEs and the type of 
participation. 
e. As specified in Appendix P, Chart of Deliverables, the MCO must submit to ODM an annual 
plan to support use of HIEs (HIE Provider Support Plan), including, but not limited to, 
collaborative MCO efforts that facilitate and support consistent and accurate data 
submission from health care providers to the HIEs. 
11. Interoperability 
a. In accordance with 42 CFR 438.242, the MCO must implement and maintain an application 
programming interface (API) that permits third party applications to retrieve, with the 
approval and at the direction of a member, member health information and data 
maintained by the MCO. 
b. In accordance with 42 CFR 438.62, the MCO must implement a process for the electronic 
exchange of the United States core data for interoperability (USCDI) data classes and 
elements with other MCOs, the SPBM, the OhioRISE Plan, ODM, and any other payer 
designated by the member. 
c. The MCO must implement a process for the electronic exchange of the USCDI data classes 
and elements with care coordination entities and providers serving the member. 
d.  As specified in Appendix P, Chart of Deliverables, the MCO must report metrics on the use 
of the Patient Access API. 
12. Artificial Intelligence and Machine Learning 
a. All systems using, models, tools, or capabilities using Artificial Intelligence or Machine 
Learning that interact with ODM data must be subject to documented governance and must 
incorporate fairness, accountability, security and privacy, transparency, and human-
centered design throughout their lifecycle, including pre-implementation review, ongoing 
monitoring, and risk management, including controls to prevent unauthorized data 
exposure, model leakage, misuse of ODM data, and documentation of data sources and 
training inputs.. 
i. 
Fairness  
 Performance of use cases, systems, and tools must be assessed for 
potential bias or disparate impact prior to implementation.
```

## Original PDF page 347

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=347)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
331 
 
 Uses cases, tools, and systems employ mitigating controls to ensure 
correction of biased outputs.  
 AI use cases, tools, and systems process personal information in a way 
that members would reasonably expect and are not used in a way that 
has unjustified adverse effects on members. 
 AI use cases, tools, and systems must comply with all applicable law and 
regulations regarding non-discrimination, including section 1557 of the 
Affordable Care Act.  
ii. 
Accountability 
 AI uses cases, tools, and systems provide meaningful benefits to 
members and are implemented in a way that incorporates human 
oversight and accountability. 
 Performance metrics are tailored for each AI implementation and are 
reviewed regularly to ensure AI use cases, tools, and systems are 
performing as expected. 
 AI use cases, tools, and systems incorporate a human in the loop. 
 User and stakeholder input is considered in adopting or modifying AI 
use cases, tools, and systems. Performance metrics are understandable 
and actionable by stakeholders. 
iii. 
Security and Privacy 
 AI use cases, tools, and systems are subject to pilot testing and review 
prior to deployment.  
 AI use cases, tools, and systems use only the minimum necessary PHI or 
PII for AI training and operations. Employing data minimization, 
tokenization, or other Privacy Enhancing Technologies whenever 
appropriate to mitigate the risk pose to privacy or security of personal 
information. 
 Systems and tools must comply with all legal, regulatory, and other 
relevant portions of this agreement as it relates to information security 
and privacy. Member PHI and PII shall not be provided to unconstrained 
tools or systems, publicly accessible service or training models. 
 AI uses cases, tools, and systems must be developed and implemented 
consistent with an Artificial Intelligence risk and governance framework, 
such as NIST AI Risk Management Framework.
```

## Original PDF page 348

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=348)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
332 
 
iv. 
Transparency 
 Members must be notified, by conspicuous posting on the plan’s 
website, of AI use cases, tools and systems used to make decisions 
affecting their health and welfare. 
 AI use cases, tools, and systems must operate in a way that is 
explainable, with established metrics that provide actionable insights. 
 Clear guidance must be provided to end users of AI use cases, tools, and 
systems. 
 The plan must be able to explain what the role and function of each AI 
use cases, tool, or system is, how any why the AI makes decisions 
regarding member health and safety.  
v. 
Human Centeredness 
 AI use cases, tools, and systems are designed and implemented with the 
goal of improving member experience, service delivery, and health 
outcomes.  
b. An up-to-date inventory of all Artificial Intelligence use cases, tools, and systems used by the 
plan, including tools or systems provided by first tier downstream or related entities must 
be provided to ODM by the final Friday of each quarter, beginning Q1 SFY 2027, in 
accordance with the specifications outlined in Appendix P, chart of deliverables. 
c. Prohibited Uses of Artificial Intelligence – AI uses cases, tools, or systems may not: 
i. 
Determine service denial, limitation, or termination independent of an human final 
decisionmaker. 
ii. 
Incorporate biometrics without express ODM approval. 
iii. 
Train public AI models using Member PHI or PII data. 
iv. 
Record or transcribe meetings with ODM. 
d. ODM review of moderate and high-risk AI use cases, tools, and systems 
i. 
AI use cases, tools, and systems that are moderate and high-risk must be reviewed 
and approved by ODM prior to implementation in the Ohio Medicaid line of business. 
Moderate and high-risk use cases, tools, and systems include, but are not limited to, 
those that: 
 Directly impact member eligibility, access to services, or benefit 
determinations. 
 Used for member engagement, care coordination, or utilization 
management.
```

## Original PDF page 349

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=349)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
333 
 
 Affect directly or indirectly, service authorization, provider enforcement 
actions, or compliance outcomes.  
ii. 
Consistent with the Appendix P, chart of deliverables, all moderate and high-risk use 
cases must be submitted to the aifocusteam@medicaid.ohio.gov and the plan’s ODM 
contract administrator. 
e. Member engagement regarding the use of AI 
i. 
The plan must provide members with meaningful, context appropriate notice 
regarding the uses of AI when: 
 Members interact with systems or chatbots using AI 
 Members are the subject of a decision made using AI 
f. Adverse Event Monitoring and Reporting 
i. 
The plan must create communication channels for stakeholders, members, and 
advocates to report adverse events arising from the use of an AI use case, tool, or 
system. 
ii. 
Adverse Events are harmful, erroneous, or unexpected behavior of an AI use case, 
tool, or system, including but not limited to incorrect decisions (e.g. improper 
discrimination, improper denials of benefits or services), security or privacy incidents, 
system failures, or misuse.  
iii. 
Each Adverse Event and the details of how the plan mitigated the harm must be 
reported to ODM, including: 
 The AI use case, tool, or system involved. 
 Number and general description of the affected members or 
stakeholders 
 Description of the harm, error, or unexpected behavior and connection 
to the AI use case, tool, or system.  
 Description of steps taken to remediate the harm and notify affected 
persons. 
g. ODM may provide additional requirements regarding specific uses of AI tools or software.
```

## Original PDF page 350

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=350)

```text
Medicaid Managed Care Organization 
Appendix K 
Information Systems, Claims, and Data 
 
Rev. 7/2026  
 
334 
 
Exhibit K.1 Claims High-Level Message Flow
```

## Original PDF page 351

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=351)

```text
Medicaid Managed Care Organization 
Appendix L 
Payment and Financial Performance 
 
Rev. 7/2026  
 
335 
 
APPENDIX L – PAYMENT AND FINANCIAL PERFORMANCE 
1. Monthly Premium Payment 
a. ODM will remit payment to the MCO via an electronic funds transfer (EFT), or at the 
discretion of ODM, by paper warrant. 
b. ODM will confirm all premium payments paid to the MCO during the month via a monthly 
remittance advice (RA). 
c. ODM will provide a record of each recipient detail level payment via Health Insurance 
Portability and Accountability Act (HIPAA) compliant 820 transactions. 
2. Delivery (Childbirth) Payments for Modified Adjusted Gross Income Members  
a. ODM will reimburse the MCO for Modified Adjusted Gross Income (MAGI) member 
childbirth deliveries using the methodology outlined in the MAGI Delivery Payment 
Reporting Procedures and Specifications for ODM Managed Care Organizations document. 
b. The delivery payment represents the facility and professional service costs associated with 
the delivery event, postpartum care rendered in the hospital immediately following the 
delivery event, and the additional costs associated with multiple birth events; no prenatal or 
neonatal experience is included in the delivery payment. 
3. Institution for Mental Disease Stays 
a. If a member age 21 through 64 has an Institution for Mental Disease (IMD) inpatient 
hospital stay exceeding 15 calendar days per calendar month, ODM will recover a 
percentage of the MCO's monthly capitation payment based on the total number of 
calendar days the member was in the IMD. 
4. Submission of Financial Statements 
a. National Association of Insurance Commissioners Financial Statements 
i. 
As specified in Appendix P, Chart of Deliverables, the MCO must submit quarterly and 
annual National Association of Insurance Commissioners (NAIC) financial statements 
(NAIC Quarterly Financial Statement and NAIC Annual Financial Statement) to ODM. 
ii. 
The NAIC financial statements must include all required filings, schedules, exhibits, 
and components as stated in the NAIC health statement instructions. 
iii. 
The MCO must provide ODM with an electronic copy of the NAIC statements in the 
NAIC-approved format. 
iv. 
The MCO must submit NAIC financial statements to ODM even if the Ohio 
Department of Insurance (ODI) does not require the MCO to submit these 
statements to ODI.
```

## Original PDF page 352

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=352)

```text
Medicaid Managed Care Organization 
Appendix L 
Payment and Financial Performance 
 
Rev. 7/2026  
 
336 
 
b. Annual Audit Report 
i. 
As specified in Appendix P, Chart of Deliverables, the MCO must submit a copy of its 
annual audit report (Annual Audit Report) required by ODI in accordance with ORC 
section 1751.321. 
c. NAIC/Cost Report Reconciliation 
i. 
As specified in Appendix P, Chart of Deliverables, the MCO must submit an annual 
NAIC/Cost Report Reconciliation. 
d. Health Insuring Corporation Tax 
i. 
As specified in Appendix P, Chart of Deliverables, the MCO must submit quarterly 
Health Insuring Corporation (HIC) tax reports (HIC Tax Report) to ODM. 
e. Other Financial Reports and Information 
i. 
The MCO must maintain a system to evaluate and monitor the financial viability of all 
risk bearing subcontractors, FDRs, or network providers, including but not limited to 
accountable care organizations (ACOs), health maintenance organizations (HMOs), 
independent physician/provider associations (IPAs), medical groups, and federally 
qualified health centers (FQHCs). 
ii. 
The MCO must provide any financial reports and information as deemed necessary 
by ODM, in a format determined by ODM, to properly monitor the financial condition 
of the MCO, its subcontractors, FDRs, and network providers. 
5. Financial Performance Measures and Standards 
a. The MCO must comply with the following financial performance measures and standards. 
i. 
Current Ratio 
 The MCO's current ratio, calculated in accordance with the ODM 
Methods for Financial Performance Measures, must not fall below 1.00. 
ii. 
Medical Loss Ratio 
 As specified in Appendix P, Chart of Deliverables, the MCO must submit 
an annual medical loss ratio (MLR) reporting tool and documentation 
(MLR Reporting Tool and Documentation). 
 The MCO's MLR, calculated in accordance with 42 CFR 438.8 and ODM 
directives, must not fall below 86%. 
iii. 
Administrative Expense Ratio 
 The MCO's administrative expense ratio, calculated in accordance with 
the ODM Methods for Financial Performance Measures, must not 
exceed 15%.
```

## Original PDF page 353

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=353)

```text
Medicaid Managed Care Organization 
Appendix L 
Payment and Financial Performance 
 
Rev. 7/2026  
 
337 
 
iv. 
Defensive Interval 
 The MCO's defensive interval, calculated in accordance with the ODM 
Methods for Financial Performance Measures, must not fall below 30 
calendar days. 
6. Insurance Requirements 
a. General 
i. 
The MCO must procure and maintain, for the duration of this Agreement, insurance 
against claims for injuries to persons or damages to property that may arise from or 
in connection with the MCO's performance under this Agreement. 
ii. 
The MCO must procure and maintain, for the duration of this Agreement, insurance 
for claims arising out of its performance under this Agreement, including but not 
limited to loss, damage, theft, or other misuse of data, infringement of intellectual 
property, invasion of privacy, and breach of data. 
b. Minimum Scope and Limit of Insurance 
i. 
The MCO's coverage must be at least as broad as: 
 Commercial General Liability (CGL): written on an "occurrence" basis, 
including products, completed operations, property damage, bodily 
injury, and personal and advertising injury with limits no less than 
$1,000,000 per occurrence. If a general aggregate limit applies, either 
the general aggregate limit must apply separately to this Agreement or 
the general aggregate limit must be twice the required occurrence limit. 
Defense costs must be outside the policy limit. 
 Automobile Liability: covering Code 1 (any auto), or if the MCO has no 
owned autos, Code 8 (hired) and 9 (non-owned), with a limit no less 
than $1,000,000 per accident for bodily injury and property damage. 
 Workers' Compensation insurance: as required by the state of Ohio, or 
the state in which the work will be performed, that meets statutory 
limits, and employer's liability insurance with a limit of no less than 
$1,000,000 per accident for bodily injury or disease. If the MCO is a sole 
proprietor, partnership, or has no statutory requirement for workers' 
compensation, the MCO must provide a letter stating that it is exempt 
and agreeing to hold the state of Ohio harmless from loss or liability for 
such. 
 Professional Liability insurance: covering all staff with a minimum limit 
of $1,000,000 per incident and a minimum aggregate of $3,000,000. If 
the MCO's policy is written on a "claims made" basis, the MCO must 
provide ODM with proof of continuous coverage at the time the policy is 
renewed. If for any reason the policy expires, or coverage is terminated, 
the MCO must purchase and maintain "tail" coverage through the 
applicable statute of limitations.
```

## Original PDF page 354

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=354)

```text
Medicaid Managed Care Organization 
Appendix L 
Payment and Financial Performance 
 
Rev. 7/2026  
 
338 
 
 Technology Professional Liability (Errors and Omissions) insurance: 
appropriate to the MCO's professional services provided under this 
Agreement, with limits not less than $2,000,000 per occurrence or 
claim, $2,000,000 aggregate. Coverage must be sufficiently broad to 
respond to the duties and obligations as is undertaken by the MCO in 
this Agreement and must cover all applicable MCO personnel who 
perform professional services under this Agreement. 
 Cyber Liability (first and third party): coverage, with limits not less than 
$5,000,000 per claim, $10,000,000 aggregate, must be sufficiently broad 
to respond to the duties and obligations as is undertaken by the MCO in 
this Agreement and must include but not be limited to claims involving 
infringement of intellectual property, including but not limited to 
infringement of copyright, trademark, trade dress, invasion of privacy 
violations, information theft, damage to or destruction of electronic 
information, release of private information, alteration of electronic 
information, extortion, and network security. The coverage must 
provide for breach response costs, as well as regulatory fines and 
penalties and credit monitoring expenses, with limits sufficient to 
respond to these obligations. 
ii. 
The insurance obligations under this Agreement are the minimum insurance 
coverage requirements and/or limits for this Agreement. Any insurance proceeds in 
excess of or broader than the minimum required coverage and/or minimum required 
limits, which are applicable to a given loss, must be available to ODM. 
iii. 
No representation is made that the minimum insurance requirements of this 
Agreement are sufficient to cover the obligations of the MCO under this Agreement. 
c. Required Provisions 
i. 
The MCO's insurance policies must contain, or be endorsed to contain, the following 
provisions: 
 Additional Insured Status 
a. Except for Workers' Compensation and Professional Liability 
insurance, the state of Ohio, its officers, officials, and employees 
must be covered as additional insureds with respect to liability 
arising out of work or operations performed by or on behalf of the 
MCO under this Agreement, including materials, parts, or 
equipment furnished in connection with such work or operations. 
b. Coverage can be provided in the form of an endorsement to the 
MCO's insurance. 
7. Primary Coverage 
a. For any claims related to this Agreement, the MCO's insurance coverage must be primary 
insurance. Any insurance or self-insurance maintained by the state of Ohio, its officers,
```

## Original PDF page 355

[Open original page](https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf#page=355)

```text
Medicaid Managed Care Organization 
Appendix L 
Payment and Financial Performance 
 
Rev. 7/2026  
 
339 
 
officials, and employees must be in excess of the MCO's insurance and must not contribute 
with it. 
8. Umbrella or Excess Insurance Policies 
a. The MCO may use umbrella or excess commercial liability policies in combination with 
primary policies to satisfy the limit requirements above. Such umbrella or excess 
commercial liability policies must apply without any gaps in the limits of coverage and be at 
least as broad as and follow the form of the underlying primary coverage required above. 
b. Notice of Cancellation 
i. 
The MCO must provide ODM with a written notice of cancellation or material change 
to any insurance policy required above 30 calendar days in advance, except for non-
payment cancellation. 
ii. 
Material change is defined as any change to the insurance limits, terms, or conditions 
that would limit or alter ODM's available recovery under any of the policies required 
above. 
iii. 
A lapse in any required insurance coverage during this Agreement will be a breach of 
this Agreement. 
c. Waiver of Subrogation 
i. 
The MCO must grant to the state of Ohio a waiver of any right to subrogation which 
any insurer of the MCO may acquire against the state of Ohio by virtue of the 
payment of any loss under such insurance. 
ii. 
The MCO must obtain any endorsement necessary to affect this waiver of 
subrogation; however, the waiver of subrogation provision applies regardless of 
whether or not the state of Ohio has received a waiver of subrogation endorsement 
from the insurer. 
d. Deductibles and Self-Insured Retentions 
i. 
Deductibles and self-insured retentions must be declared to and approved by ODM. 
ODM may require the MCO to provide proof of ability to pay losses and related 
investigations, claims administration, and defense expenses within the retention. The 
policy language must provide, or be endorsed to provide, that the deductible or self-
insured retention may be satisfied by either the named insured or ODM. 
e. Claims Made Policies 
i. 
If any of the required policies provide coverage on a claims-made basis: 
1. The retroactive date must be shown and must be before the date of this 
Agreement or the beginning of performance under this Agreement. 
2. Insurance must be maintained, and evidence of insurance must be 
provided for at least five years after completion of this Agreement.
```

