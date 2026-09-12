# Ninety-Three Wrong Claims

A one-person quantitative research programme kept a register of every claim it made that later turned out
to be false, together with who or what caught each one. The programme looked for a trading edge in crypto
perpetual futures and did not find one. The register is what it found instead.

This repository holds the register, the paper that analyses it, and the tool that counts it.

**How this was made.** One person ran the programme working with AI systems, which wrote code, audited it,
and account for most of the entries in this register. That is not a footnote. The register is largely a
record of what those systems claimed and got wrong, and of who or what caught each one. The paper states the
same thing in section 10.

## The one number

Clone this repository and run the counter. It parses the register's own tables and prints this:

```bash
python tools/recuento_auditoria.py --check
```

| who or what caught it | entries |
|---|---:|
| an external human reviewer | 35 |
| the author, on his own criterion, most often by re-measuring | 25 |
| an automated adversarial review | 12 |
| the mutation harness | 9 |
| continuous integration | 2 |
| the reviewer, about his own claim | 2 |
| eight further labels, one entry each | 8 |
| **total** | **93** |

The number in the register is not typed by anyone. It is regenerated from the tables by the tool in
`tools/`, which refuses to publish if two entries share an id. That control exists because the count once
said three different figures at once in the same document, and an external reviewer caught it by counting
the rows himself. Both facts are entries in the register.

## What you are looking at

The programme ran on crypto perpetual-futures microstructure with one question: whether a slow participant,
on a rented server with about 113 ms of median feed latency, could extract systematic edge. The versioned
record runs from 12 June 2026 to 9 September 2026, across 457 commits.

It produced one positive estimate. A frozen adversarial protocol, written months earlier and invoked by
hand for the first time in two months, destroyed it on 24 August 2026. A later re-analysis widened an
admission rule the protocol had already flagged as an open sensitivity, and the estimate fell from about
+18 basis points to about +3, and went negative in the primary cell. The programme retired it and stopped.

None of that is unusual. What is unusual is that somebody wrote down all ninety-three times the programme
was wrong, while it was happening, with the discoverer named.

## The limits, before you read further

1. **93 is the denominator of what was recorded**, not of errors made, and not of the chances each
   mechanism had to catch something. The errors nobody found are absent by construction, and those are the
   interesting ones.
2. **One laboratory, one annotator, and the annotator is one of the parties.** No inter-rater agreement.
3. **No control group.** Nobody has built the same system twice, so this cannot show that one method finds
   more defects than another. The table above ranks nothing.
4. **The detection method is recorded for 25 of the 93.** The other 68 name only the discoverer.
5. **One account authored all the commits**, so the repository alone cannot attribute a change to one party.
6. **The register stops on 28 August 2026** while the work continued to 9 September. Claims found and
   corrected after that date are not in it.
7. **The underlying market data cannot be redistributed** under its provider's terms, so the trading result
   is not reproducible from this repository. The register, the count and the tool are.

## What is here

| path | what it is |
|---|---|
| `register/AUDITORIA_DEL_METODO.md` | the register, in Spanish, as it was kept. 93 entries plus system defects and structural corrections |
| `paper/ninety-three-wrong-claims.en.md` | the paper, English. Draft 2, not submitted and not peer reviewed |
| `paper/noventa-y-tres-afirmaciones-falsas.es.md` | the same paper in Spanish |
| `tools/recuento_auditoria.py` | the counter. Standard library only, no dependencies |

The register is in Spanish because that is the language it was kept in, and translating it after the fact
would make it a different document. The paper is in both languages.

### What was changed before publishing

The register published here is not byte for byte the internal document. Eleven strings were redacted across
the register and the two papers, and the rule was to remove identity and keep the finding:

- the hosting provider and the off-site backup provider became "another provider" and "off-site";
- the data centre where the backup lives became "another data centre";
- the two commercial data vendors became "the first provider" and "the second provider", which is what the
  papers already called them;
- the names of a running service and of the alert channel became their roles.

No entry id, date, count or discoverer column was touched, and the counter still reproduces 93 from the
published file. The reason for redacting is that a server from this programme is still running, and naming
its provider, its data centre and its service names narrows a target without telling the reader anything
they need. The laboratory has required this pass on any public mirror since 5 July 2026; the first version
of this repository skipped it, and an adversarial review caught that before anything was published.

The counter is published as it ran, with one change: the path to the register is now an argument instead of
being computed by walking four directories up from the file. Everything else is byte for byte what was in
the laboratory, including the comments that explain the two failures it exists to prevent.

## Why this exists

The laboratory's own diagnosis, written into the register before any of this was published: rigour does not
distribute itself. It concentrates where the work is interesting. Twelve sessions went into hardening a
transactional log against writer collisions; what actually stopped data production was an unpaid hosting
invoice. A tool that translated the programme's goal into the notional volume it would require was written
in the final month, and it would have answered in one afternoon a question that took the whole programme.

## Licence

Code under [Apache 2.0](LICENSE). Documents under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use them, quote them, and say where they came
from.

Manuel Beardo Campo, independent researcher. Nothing here is peer reviewed or ratified by anyone.
