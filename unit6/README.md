# Unit 6: Malicious Software

## 6.1 Malicious Software

Malicious software (malware) is any hostile or intrusive program designed to harm computer systems. It **invades, disables or disrupts** normal operation of devices (PCs, servers, mobile) and networks. Malware can steal, encrypt or delete data and hijack core functions (like a flu infecting a body). Examples include viruses, worms, trojans, spyware, ransomware, and many others. Common effects of malware attacks are data theft, service disruption, credential capture and system damage.

- **Definition:** Malware is an umbrella term for any software intentionally created to harm or exploit systems.
- **Effects:** Malware can spy on user activity, delete or corrupt files, and change system behavior without consent.

## 6.2 Types of Malicious Software

Malware can be classified by behavior and propagation. The table below summarizes major types:

| **Type**            | **Behavior/Description**                                                                                                      | **Example**            |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **Virus**           | Self-replicates by infecting host files or programs; requires user action to spread. Can corrupt or overwrite data.           | ILOVEYOU virus         |
| **Worm**            | Self-contained malware that replicates over networks without a host program. Consumes bandwidth and may open backdoors.       | Code Red worm          |
| **Trojan Horse**    | Disguised as legitimate software but carries a malicious payload. Installs backdoors, keyloggers or additional malware.       | Zeus banking Trojan    |
| **Spyware**         | Secretly monitors user actions and collects data (e.g. keystrokes, browsing habits).                                          | Keylogger implant      |
| **Adware/Riskware** | Presents unwanted ads or risky features; often bundled with free software. (Less harmful but intrusive.)                      | Ad-supported programs  |
| **Ransomware**      | Encrypts files or systems and demands payment for decryption. (A form of extortion Trojans.)                                  | WannaCry, CryptoLocker |
| **Backdoor**        | Provides unauthorized remote access by bypassing normal authentication. Often installed by attackers or trojans.              | Custom backdoor Trojan |
| **Rootkit**         | Toolset that hides malware and grants privileged access to an attacker. Operates at kernel or firmware level, hard to detect. | Stuxnet rootkit        |
| **Botnet/Zombie**   | A network of infected machines (“bots” or “zombies”) under attacker control. Used for DDoS, spam, mining.                     | Mirai botnet           |

Each type may have sub-classes. For example, worms include email worms (spread via email) and network worms; trojans include downloader trojans, banker trojans, etc. Types are often distinguished by _propagation method_ (e.g. worms vs. viruses) or _function_ (e.g. spyware vs. ransomware).

## 6.3 Advanced Persistent Threat (APT)

An **Advanced Persistent Threat (APT)** is a highly skilled, long-term cyberattack targeting a specific organization. APTs are usually state-sponsored or organized crime groups. They **persist** undetected, stealthily gathering intelligence or data. Characteristics include careful planning, customized malware, and continuous network presence.

**APT Life Cycle (three stages):**

- **Stage 1 – Infiltration:** Attackers gain initial access, often via spear-phishing or social engineering. For example, targeted phishing emails to executives (“whaling”) may install initial malware payloads.
- **Stage 2 – Lateral Movement:** The attacker installs backdoors or remote-access tools and moves laterally within the network. They capture credentials, escalate privileges, and map the network to locate valuable resources.
- **Stage 3 – Exfiltration:** Once enough data is gathered, it is exfiltrated covertly. Stealth is maintained (e.g. using encryption, or distractive DoS attack), and the malware remains to enable future access.

**Key Points:** APT attackers are well-funded and knowledgeable; their goals include espionage, data theft, or sabotage. Detection is difficult because APT malware operates quietly. Indicators include unusual account activity and hidden backdoors.

## 6.4 Virus

A **virus** is a type of malware that can replicate by infecting other programs or files. It spreads when an infected file is executed; typically user action is needed (opening a malicious attachment or program). Once active, a virus may attach copies of itself to executable files or system areas. Viruses can corrupt files, erase data, or render a system unusable.

- **Replication:** Infects host files or boot sectors; payload triggers on file execution.
- **Propagation:** Often spread via removable media or email attachments; e.g. historical viruses spread on floppy disks or as infected macros.
- **Examples:** The ILOVEYOU worm (also a virus) and Michelangelo virus that overwrote disks.
- **Payloads:** Can include file corruption, data deletion, or activation of additional malware (e.g. trojans/droppers).

## 6.5 Worms

A **worm** is self-contained malware that replicates and spreads over networks without needing a host program or user action. Worms scan for vulnerable machines and copy themselves, often causing network congestion or installing backdoors.

- **Key Property:** Propagates independently – unlike viruses, does not require attaching to a host file.
- **Effects:** Consumes bandwidth and memory, can crash networks. May install other malicious code (e.g. a backdoor Trojan).
- **Examples:** The Code Red worm exploited a Windows web server flaw. The Conficker worm exploited network services.
- **Delivery:** Often exploit vulnerabilities in network services (e.g. SMB, mail servers) or use social engineering (as email worms).

## 6.6 Spam E-mail and Trojans

- **Spam E-mail:** Unsolicited bulk emails (often advertising) that can carry malware attachments or links. A “malspam” or malicious spam email delivers malware to victims. For example, the Melissa email spam in 1999 spread a macro virus. Modern spam often contains trojan downloaders or phishing links.
- **Trojan Horse:** Malware disguised as benign software. When the user runs it, the hidden malicious payload activates. Trojans do not self-replicate, but they _deliver_ malware (downloaders, keyloggers, ransomware, etc.). They often require social engineering to get users to run them (e.g. a “free game” that contains a banking trojan).

**Key Points:** Trojans and malspam go together – attackers send Trojanized attachments via email. Unlike worms, Trojans depend on deception (and spam filters) to reach victims. Trojan examples include backdoor trojans, banker trojans, and remote-access trojans.

## 6.7 System Corruption

Malware may carry a **system corruption** payload that _damages or alters system software/configuration_. This includes:

- **File Corruption:** Overwriting or encrypting system files (some viruses erase or scramble files).
- **Registry Changes:** Modifying system registry (on Windows) to disable antivirus or hide malware.
- **OS Damage:** Overwriting boot sector or BIOS (some viruses and rootkits do this) to prevent system startup.
- **Program Interruption:** Causing crashes or disabling system utilities.

Such corruption renders a computer unstable or unusable. _System corruption_ is often the goal of destructive malware (e.g. the CIH “Chernobyl” virus that overwrote BIOS).

## 6.8 Zombie and Botnet

- **Bot (Robot):** Malware code that can be remotely commanded by an attacker. Once a machine is infected by a bot program, the attacker (“botmaster”) controls it without the user’s awareness.
- **Zombie:** A computer compromised by a bot is called a _zombie_. It “has no will of its own” and follows the attacker’s commands.
- **Botnet:** A network of thousands to millions of zombies under one botnet control. Used for large-scale attacks: spamming, distributed denial-of-service (DDoS), or cryptocurrency mining.
- **Example:** The Mirai botnet turned IoT devices into zombies to launch record-breaking DDoS attacks.

Botnets are powerful attack agents. Security teams fight them by detecting unusual traffic from internal machines or using sinkholing techniques.

## 6.9 Keyloggers, Phishing, Spyware

Phishing is a social-engineering attack that uses deceptive emails or websites to trick users into revealing sensitive information. Spyware is malware that secretly records user activities or data. A keylogger is a form of spyware that logs every keystroke on the device. These threats aim to steal credentials, payment info, or personal data without the user’s knowledge.

- **Keylogger:** Software (often installed by a Trojan or rootkit) that records all keystrokes on a keyboard. Captures passwords, credit-card numbers, and chat messages.
- **Phishing:** Attackers impersonate a legitimate entity (bank, social site, etc.) in emails or messages to lure victims into revealing credentials. For example, a fake bank login page steals your password. Phishing is a top cause of identity theft.
- **Spyware:** Any software that covertly collects user data. It can track browsing history, capture screenshots, or report on user actions. Spyware often installs without clear notice (e.g. bundled with free downloads).

## 6.10 Backdoors and Rootkits

- **Backdoor:** A method (or program) that allows an attacker to access a system by bypassing normal authentication. Backdoors can be intentionally left by developers (for maintenance) or secretly installed by attackers. Once in place, they let attackers remotely control the system, install more malware, or exfiltrate data.
- **Rootkit:** A stealthy toolkit that hides malware and maintains privileged access. Rootkits operate at a low level (kernel or firmware), making them hard to detect. They often load before the OS boots (bootloader/firmware rootkits) or patch the OS kernel to conceal files/processes. Rootkits give attackers ongoing “root” or administrator control without alerting users.

**Example:** The Flame rootkit (targeted spyware) hid itself in system processes. Rootkits often accompany backdoors or keyloggers, and removal usually requires booting from a clean media.

## 6.11 Countermeasures for Malwares

Key defenses against malware include:

- **Antimalware Software:** Install and regularly update antivirus/antimalware tools on all devices. These use signature-based scanning (known malware fingerprints) and heuristics/behavior analysis to detect threats. Keep virus definitions up to date.
- **Email and Content Filtering:** Use spam filters to block malicious emails and web filters to block harmful websites. Scan attachments on email servers to remove malspam before delivery.
- **Patching & Updates:** Frequently apply security updates to the OS and applications. This closes vulnerabilities that worms and exploits use to spread.
- **Principle of Least Privilege:** Users should operate with minimal privileges. Restrict administrator rights to reduce damage from infections.
- **Network Defenses:** Firewalls and intrusion prevention systems (IPS) can block suspicious traffic. Monitor network activity for anomalies (e.g. unusual outbound data or connections).
- **Backups:** Maintain recent backups of critical data. In case of ransomware or destructive malware, systems can be restored from clean backups.
- **User Education:** Train users to recognize phishing and social-engineering attempts. Teach safe practices (no clicking unknown links/attachments, verifying senders).
- **Behavior Monitoring:** Deploy endpoint detection that watches for suspicious behavior (e.g. a process modifying many files). Behavioral analysis can catch zero-day malware that lacks signatures.

By combining these measures – up-to-date defenses, secure configurations, and awareness – organizations can greatly reduce malware risk. As TechTarget notes, effective antimalware strategies “identify known and previously unseen malicious files or actions” and block them before damage occurs.
