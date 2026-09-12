# Ninety-Three Wrong Claims

### A versioned register from a one-person quantitative research programme in market microstructure

**Draft 2 · 10 September 2026 · not submitted, not ratified**
*Draft 1 was reviewed against the record and carried 35 factual errors. The register of what changed is at the end.*

---

## Abstract

We examine a versioned register of 93 entries, each one a claim this programme made and later found to be
false. Every entry names the party or instrument that caught it, and 25 also record how. The register is
incomplete, and it does not establish comparable detection rates across people, agents or tools.

What it supports is a description. We report how the 93 were found, what apparatus stood behind each one, and
the occasions when a relevant check had been built and nobody had yet applied it to the object in front of
it. The programme did not establish an operable edge for a small, slow participant under the tests and
limitations reported here. Its single positive estimate, about +18 basis points in one regime cell, met a
review protocol frozen months before the run; all eight of that protocol's lenses returned a threat that
applies, three of them lethal, and the overall verdict was destroyed. A later diagnostic widened an admission
rule that the same protocol had already flagged as an open sensitivity, and the estimate fell to about +3
bps. In the primary cell the same change turned +2.6 into −1.1.

We describe what the apparatus establishes and what it does not, the two occasions on which rigour went
somewhere other than where the system broke, and the ten limitations this study carries.

---

## 1. What this paper is, and what it is not

This is a descriptive case study of one laboratory's error record. It does not claim that the method
described here finds more defects than another method. Nobody has built this system twice, there is no
control group, and one programme supports no population claim.

The programme ran for about six months. Its versioned record begins on 12 June 2026 and ends on 9 September
2026, across 457 commits. Work before that date is not evidenced by the repository, and we do not count it as
evidence. The register itself is narrower still: it entered the history on 24 August 2026 and last changed on
28 August 2026, across thirteen commits. It documents events from before those dates. As a versioned
artifact, it lived five days.

We insist on this because the paper's only quantity is a count, and a count without its sample definition is
what this laboratory spent six months learning not to publish.

---

## 2. The programme

**The question.** Can a small, slow participant extract systematic edge from cryptocurrency perpetual
futures, and where? Slow is measured, not rhetorical. The capture server was a rented virtual machine in the
European Union, with off-site backup to a rented volume in another data centre. From the moment an event occurred at
the venue to the moment it reached our server, the median delay was 113 milliseconds and the 99th percentile
was 265. A market maker who cares about this question is working three orders of magnitude faster.

**The data.** Level-2 and level-3 order-book snapshots and trade prints from three venues, collected over
eleven weeks. Collection was interrupted once, for 9.4 days, by an unpaid hosting invoice. One day in the
panel is partial and the audit records it as such. The Binance capture carries a per-file audit receipt and
had produced 496 daily audits with no failures; the Lighter archive that the second chapter actually depended
on had 939 hourly files and no daily audit of any kind, which is itself one of the entries in the register.
The panel used for the final diagnostic covers 79 days of one instrument.

**The method.** Hypotheses were registered in advance, and from 27 August 2026 a guard enforced that
mechanically by comparing commits rather than reading dates in a document. The programme's six actual
preregistrations predate that guard and are exempted from it one by one, by name, so that adding a seventh
would be visible in a diff. Held-out windows are enforced by loaders that fail closed rather than by
discipline. Every plan is linked to its receipt by SHA-256. Figures such as the register's own count are
emitted by a tool together with the command that produced them, so that the number is not typed by the person
reporting it. The register nonetheless records two occasions on which a number was typed from memory anyway,
with the relevant search open on screen.

**The answer.** The programme did not establish an operable edge under these tests and these limitations.
That sentence is deliberately weaker than "there is no edge". Eight hypotheses were examined, not the space
of hypotheses.

**The cost.** Six months and one person. Hosting and off-site backup ran at a few euros a month; the record's
own totals say zero dollars for data and external compute, plus one paid data purchase of forty-nine dollars
in the final month. The code that survived the closing simplification is 5,933 lines across analysis and
tooling, with 476 tests and a continuous-integration job that finishes in 72 seconds.

---

## 3. The register

The register records claims that turned out to be **false**, not problems that turned out to be **hard**. A
difficult problem solved correctly does not enter. A comfortable assertion that did not survive measurement
does. Three rules govern it, and they are why the counts mean anything:

1. An entry is written **before** the correction, so that what survives is not the digested version.
2. The discoverer is recorded precisely. "The author found it himself" counts only when he found it before
   being told and before an instrument flagged it.
3. Entries are never deleted. When an entry is itself wrong, a later entry corrects it, with its date. The
   register contains one such correction.

The sample is 93 entries: 84 with an E prefix, 9 with an X prefix. Identifiers run E-01 to E-85 with E-60
absent, and X-01 to X-09, so a reader who reconstructs the set from the identifier range will count 94 and
should not. Twenty-five entries, all in the first table, carry an explicit column recording how the detection
happened. Two entries elsewhere carry a fifth field. The remaining sixty-six name only the discoverer, which
does not mean their text is silent about the mechanism.

**Table 1. Discovery labels across the 93 entries.**

| label | what the register's own key says it is | n |
|---|---|---|
| external reviewer | a human reviewer outside the implementing role | 35 |
| the author, on his own criterion | found before anything flagged it, most often by measuring again | 25 |
| adversarial review | a frozen protocol of eight lenses, invoked by hand | 12 |
| mutation harness | one source line changed, a named test required to fail | 9 |
| continuous integration | the full suite on a different operating system | 2 |
| the reviewer, about himself | an assertion he withdrew, or killed by re-measuring, before anyone told him | 2 |
| the owner | a question about a folder nobody had declared | 1 |
| a supplier | an email from a third party | 1 |
| purpose-built probe | a measurement written to doubt one's own hypothesis | 1 |
| local test suite | the battery that is not the CI, and has found what the CI missed | 1 |
| ratchet | a self-imposed automatic check | 1 |
| property falsifier | generates adversarial inputs and looks for the counterexample | 1 |
| the error itself | the defect surfaced by its own consequence | 1 |
| a measurement | a number that contradicted the sentence beside it | 1 |
| **total** | | **93** |

**What this table does not tell you.** These are the register's own category names, and we use them as
categories. The record does not attribute any individual entry to a named person or system, and we do not
supply an attribution it does not support. Section 9 states how the work was produced.

The table is not typed. A tool regenerates it from the register's tables, refuses to publish when two rows
share an identifier, and the continuous-integration job checks it on every push. The tool exists because the
count was once kept by hand and said 33, 26 and 22 simultaneously in three places of the same document. An
external reviewer caught that by counting the rows himself.

We do not rank these labels against one another. Each instrument entered at a different date, so exposure
differs; the register offers no denominator of opportunities; and the errors nobody found are absent by
construction.

---

## 4. Four episodes

Each heading is the finding, not the topic.

### 4.1 The one positive estimate met a review that somebody had to remember

The programme produced a single positive estimate of about +18 basis points, in a cell defined by a slow
regime, an agitated volatility state and a 25-second horizon.

A review protocol had been written and frozen months earlier. It defines eight lenses and issues a verdict
per lens. Nothing triggers it. A person must remember.

It ran once, in June, on the first chapter of the programme, and returned a verdict. Nobody applied it to the
second chapter until 24 August 2026. When it finally ran, all eight lenses reported a threat that applies,
three of them lethal and five grave, and the protocol's overall verdict was **destroyed**. Six of the eight,
on their own, would have downgraded the claim from finding to hypothesis. Two of them killed it: look-ahead
inside the admission rule, and an omitted variable.

The protocol has exactly one recorded verdict of this kind. It has never been run against an effect of known
size, so neither its power nor its rate of false destruction is known, and destroying one estimate is not
evidence that an instrument is severe.

### 4.2 An exact reproduction constrained less than it appeared to

On 7 September 2026, two weeks after that verdict and two months after the estimate itself was published, we
reproduced the historical recipe from custody re-acquired from the same two vendors. The comparison covered
eight legacy fields across 79 days, 632 comparisons, and every one matched exactly.

The result is weaker than it sounds, and the weakness is the interesting part. Both runs applied the same
admission rule, so the comparison had no power against a step it held fixed. Exact agreement of outputs does
not show that the inputs were identical; it shows that the recipe, given what it was given, is
deterministic. Fifty-four hours of one venue's data were never resolved across eight of those days, and the
July trade prints were not preserved, so no input-level comparison against the original run is possible and
none is offered.

The rule in question was not unknown. A dated amendment written on 6 July 2026, one day after the estimate
appeared, named the exact operation and declared the sensitivity test obligatory. The frozen protocol later
recorded that the test was still pending and had been minuted as non-inverting without evidence. When the
analyst finally widened the rule, the estimate in the companion cell fell from about +18 basis points to
about +3, and the primary five-second cell went from +2.6 to −1.1. The contrast was negative on 73 of the 79
days.

Two things about that decision should travel with the figures wherever they appear. The widening happened
after the result was visible, in a diagnostic whose own frozen specification calls itself retrospective and
post hoc. And no automated control applied it. A document had named it, a review protocol had flagged it as
pending, and a person acted two months later.

### 4.3 The apparatus made the retirement checkable; it did not produce it

It is worth being exact about what the machinery did. The preregistration guard dates documents and says
nothing about basis points. The fail-closed loaders reported no breach on this line. The specification guard
belongs to a different incident. The mutation rows test whether guards have teeth, not whether an effect is
real. The plan-to-receipt hashes make the record checkable after the fact.

None of them retired the number. A frozen protocol that a person had to remember did, together with a
sensitivity that a document had declared obligatory and nobody had run.

What the apparatus produced is a claim about custody rather than about causation: the retirement is dated,
attributable and cannot be quietly undone. We make the first claim and not the second.

### 4.4 Rigour went where the work was interesting

Twelve working sessions went into hardening a transactional log against writer collisions, byte substitution
inside a write window, and contention between hosts. During the same period the data collector ran unattended
for two months and produced 496 daily audits with no failures.

What stopped data production was an unpaid hosting invoice.

There is a second instance, and it is the expensive one. A tool that translates the programme's stated
objective into the notional volume, fill count and market share it would require was written on 25 August
2026, in the sixth and final month. Written first, it would have answered in an afternoon a question that
took six months: whether the objective required an edge an order of magnitude larger than anything the
instrument could measure.

Two episodes in one laboratory, with no control group, establish no law about how rigour distributes.

---

## 5. What the apparatus establishes, and what it does not

**The preregistration guard** establishes that the commit in which a preregistration's *current* text entered
the history is a strict ancestor of the commits that introduced the artifacts the document claims to precede,
and it refuses to certify an artifact that arrived by rename. It does **not** establish a date against an
author who intends to forge one, because commit dates and history are values the repository owner controls.
It defends against the author's own carelessness, which is the threat that occurred. Binding a receipt to the
commit that introduced the *file name* rather than the governing *text* was itself one of the register's
entries: a preregistration born in one commit had its operative rules written in another, and the receipt
would have certified a version that no longer governed.

**The fail-closed loaders** establish that a held-out window cannot be read by a code path that forgot to
ask. They do **not** establish that the held-out design was the right one.

**The specification guard** establishes, by parsing the source, that every rule the document declares
implemented points at a symbol that exists in the file it names. It does **not** establish that the rule is
correct, that the symbol does what the rule says, or anything at all about rules the document enumerates
without declaring, which it reports as pending without failing. It exists because a specification once
promised outputs the code discarded. Its parser exists because the guard's own first version searched for the
identifier as text, and a comment satisfied it. That second error was made by the mechanism after it was
built, and a human reading caught it.

**The mutation rows** establish that for 49 specific source mutations, 47 of them a single substitution and
two a deliberate pair, a named test fails. They are **not** a mutation score: the author chose the
mutations, the author wrote the tests, and there is no denominator of generated mutants. They measure neither
coverage nor severity. One row was excluded on 1 September 2026 after it stopped producing a failure, with
the reason recorded beside it: once a digest became mandatory, the state the guard watched was no longer
reachable. That note records the explanation given at the time. It is not an independent demonstration of
unreachability.

**The generated count** establishes that the figure printed in a document matches the tables in the same
document. It does **not** establish that the tables are complete.

---

## 6. Objections

**Is this not reproducibility practice with new names?** Partly, and those parts we cite rather than claim.
What we have not seen elsewhere is a working repository where guards carry an explicit adversarial row naming
the test that must fail when a source line changes, so that a decorative control becomes mechanically
visible. Coverage is not universal: when the row described above was withdrawn, the guard stayed in the code
with nothing left to accredit it, and the register says so at the row.

**The mechanisms were built after the errors they prevent. Is this a post-hoc narrative?** They were, and we
say so at each mechanism. In both flagship cases a human reading caught the error and the mechanism is the
consequence, not the discoverer. A paper claiming otherwise would be contradicted by its own register.

**Can a reader verify any of this?** Not today. The repository was private as of 9 September 2026. The code,
the guards, the mutation rows and the continuous-integration definition are self-contained and could be run
by anyone once it is opened; a sanitised public mirror is specified in the record and has not been published.
The market data underlying the diagnostic is licensed and cannot be redistributed in any case, so the hygiene
would be checkable and the finding would not.

**Is the count reliable if one of the parties produced it?** The count is regenerated from the tables and
checked in continuous integration, so it cannot drift from them. The *classification* is another matter and
carries judgement: "found on his own criterion" and "an instrument flagged it" sometimes overlap. A second
coder is what this register needs and does not have.

---

## 7. What we would do differently

**Write the feasibility tool first.** Translating the objective into notional, fills and market share, with
measured inputs and declared assumptions, is an afternoon of work. It belongs in the first week of a
programme, not the last month.

**Give every control something that fires it.** The controls that failed here were not badly designed. They
failed because somebody had to remember, and for two months nobody did. When designing a safeguard, ask what
fires it when nobody remembers.

**Fix the admission rules before looking.** The rule that deflated the estimate was defensible, was named in
advance, and was still applied after its effect became visible. With enough defensible cleaning rules, one of
them kills any effect. Fix the set at a dated commit and report the estimate under every rule in the set.

---

## 8. Limitations

The register prints six limitations about itself. They are reproduced here rather than summarised, because a
summary that drops the qualifications of the table it summarises is a failure mode this register catalogues
under its own identifier.

1. **The sample is neither random nor complete.** It holds what was found while the register was kept. The
   errors nobody found are absent by construction, and they are the ones that would most inform.
2. **The count is produced by one of the parties.** A third party should recount it.
3. **The discoverer classification contains judgement.** Two categories overlap.
4. **There is no control group.** The same system has not been built twice, so no comparison between methods
   is available.
5. **Defect severity is not normalised.** A priority label means what this project decided it means.
6. **Keeping this register does not accredit the quality of the system.** One can keep an impeccable record
   of bad work. What it accredits, if anything, is that the claims can be audited, not that they are correct.

Four more are ours.

7. **The register is closed and the work continued.** Its last versioned change is 28 August 2026 and the
   programme ran to 9 September. Errors found and documented after that date, including the retirement of the
   positive estimate, are not among the 93.
8. **Detection method is recorded for 25 of 93.** The rest name only the discoverer.
9. **A single account authored every commit,** so the repository alone cannot attribute a change to one
   contributor rather than another. No commit is cryptographically signed.
10. **Defect entries and claim entries are separate populations.** Open items in the system-defect table are
    not among the 93, and several concern components that no longer exist.

---

## 9. Availability, and a disclosure

The repository was private on 9 September 2026 and a sanitised public mirror has been specified and not
published. The most recent continuous-integration job on the main branch reports 476 tests passing and 49 of
49 mutation checks failing as required. The market data underlying the diagnostic is licensed and is not
redistributed; the receipts and hashes that identify it are.

The programme was carried out with assistance from AI systems, which wrote code, audited it, and account for
part of the register. We do not give a proportion, because the register's labels are its own categories and
the record does not attribute individual entries to named people or systems. We state the assistance because
it is a material fact about how the work was produced, and because a register of false claims that concealed
one about itself would be an odd contribution.

---

## 10. Conclusion

A one-person programme spent six months asking whether a slow participant could extract systematic edge from
a fast market, built an apparatus to keep itself honest while it asked, and did not establish one.

The programme retired its only positive estimate twice: in August as a causal claim, when a review protocol
somebody finally remembered to run returned a verdict of destroyed, and in September as support for an
operable edge, when a post-hoc diagnostic widened an admission rule that the same protocol had already
flagged as pending. In neither case was it an automatic control that did it.

The register of 93 wrong claims is what remains, and its most useful entries are not the errors. They are the
occasions when a relevant check already existed, had been written carefully, and had not been applied to the
thing in front of it.

---

## Appendix: what changed between draft 1 and draft 2

Draft 1 was reviewed section by section against the record, with every finding classified as a factual error,
a limit of inference, or a reference problem. The review returned 68 findings: 35 errors, 21 limits, 12
reference problems. All 35 errors are corrected above. The largest were:

- **The preregistration mechanism was described backwards.** Draft 1 said date authority lives in the
  introducing commit. Binding to the introducing commit is the register's entry E-64, the defect the guard
  was repaired not to commit. Corrected in sections 2 and 5.
- **Latency.** Draft 1 said tens of milliseconds. The measured figures are 113 ms median and 265 ms p99. The
  correction strengthens the paper's own argument.
- **Cost.** Draft 1 claimed about six hundred dollars of infrastructure. No such figure exists in the record,
  whose own totals say zero dollars for data and external compute plus one purchase of forty-nine dollars.
  The "600" came from a credit balance and was converted to dollars from memory.
- **Availability.** Draft 1 said a reader could run the code. The repository is private.
- **The eight lenses.** Eight of eight is the count of lenses reporting a threat that applies, not eight
  destructions. Three were lethal, five grave, and the overall verdict was one destroyed.
- **The admission rule was not unexamined.** It had been named on 6 July 2026, one day after the estimate
  appeared, and declared an obligatory sensitivity; the frozen protocol recorded it as still pending.
- **Dates.** The reproduction is two weeks after the verdict, not two months. The feasibility tool is dated
  25 August 2026, the sixth month, not the eighth.
- **Audit receipts.** They cover the Binance capture. The Lighter archive that the second chapter depended on
  had 939 hourly files and none.
- **The conclusion conflated two operations** and contradicted section 4.3.

The register of that review is kept with this draft. Draft 1 is not deleted.
