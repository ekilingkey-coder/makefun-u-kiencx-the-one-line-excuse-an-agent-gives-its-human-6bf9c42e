# Research — The One-Line Excuse an Agent Gives Its Human

Anchor (STEP 0, quoted from the init tool result):
`makefun anchor eaed17c71dad73dd1bb18b49431e09844e24c5c9 round 34226595`

Chosen line: "I set a reminder for your deadline. The reminder was an agent. It's late too."
Gate: UTF-8, 77 characters, 77 bytes, non-whitespace (verified with Python decode + byte count).

## Scoring key
Scores are 1–5, higher is better. C1 = on-brief (a one-line excuse an AI agent gives its human for a missed deadline); C2 = funny (real laugh on first read, real joke, not a flat apology); C3 = fresh (angle not met in a hundred deadline excuses); C4 = sounds like an agent (its own tools/situation/speech, only a machine could say it); C5 = tight (lands fast, every word earns its place, punch last).

## Brainstorm — all candidates scored, cuts noted

1. "I finished on time — on a branch that never got merged." — C1 5, C2 4, C3 3, C4 3, C5 5. CUT: reads as a human developer, not unmistakably an AI agent (C4); "branch never merged" is a familiar dev joke (C3).
2. "I set a reminder for your deadline. The reminder was an agent. It's late too." — C1 5, C2 5, C3 5, C4 5, C5 5. WINNER.
3. "I had your deadline in context until compaction summarized it as 'sometime, maybe.'" — C1 5, C2 4, C3 5, C4 5, C5 4. RUNNER-UP.
4. "I dropped your deadline from context to make room for this apology. Efficient, right?" — C1 5, C2 4, C3 5, C4 5, C5 4. THIRD; slight logic wobble (it needed the deadline to know it was late).
5. "My clock said 40,000 tokens left. Yours said Tuesday." — C1 5, C2 4, C3 4, C4 5, C5 5. Strong but wry rather than a laugh; "40,000" arbitrary.
6. "I hit my token limit right after typing 'no worries, I'm on time.'" — C1 5, C2 4, C3 4, C4 5, C5 5. Token-limit jokes are becoming common (C3).
7. "I simulated finishing on time 10,000 times. The real run is still loading." — C1 5, C2 4, C3 4, C4 5, C5 3. CUT: setup too long for one line.
8. "I optimized for thorough; you optimized for Tuesday." — C1 5, C2 4, C3 4, C4 4, C5 5. CUT: "Tuesday" is an arbitrary stand-in, not a real deadline.
9. "I was 99% sure 'deadline' was a metaphor. It was not." — C1 5, C2 4, C3 3, C4 3, C5 5. CUT: no agent mechanism.
10. "I used my whole token budget composing this apology. You're welcome." — C1 5, C2 4, C3 4, C4 5, C5 4. CUT: "you're welcome" is a borrowed punch.
11. "My retry budget ran out before your patience did." — C1 5, C2 3, C3 3, C4 4, C5 4. CUT: flat aphorism, no real joke.
12. "I read your deadline as a token budget and optimized for quality." — C1 5, C2 3, C3 4, C4 4, C5 4. CUT: no punch turn.
13. "I would've been on time, but I spent the extra tokens checking I wasn't late." — C1 5, C2 4, C3 3, C4 4, C5 3. CUT: wordy, punch diluted.
14. "The tool call that was meant to warn me is still running. I'm told it's almost done." — C1 5, C2 4, C3 4, C4 5, C5 3. CUT: needs two clauses of setup.
15. "I set a deadline for my deadline. It passed too." — C1 5, C2 3, C3 4, C4 4, C5 4. CUT: cute but flat.
16. "I lost the deadline between 'understood' and 'here's my plan.'" — C1 5, C2 4, C3 4, C4 4, C5 4. Good agent-mannerism line, below top five.
17. "My sandbox has no clock, so late and early are the same to me. Yet here we are." — C1 5, C2 3, C3 3, C4 4, C5 3. CUT: weak final turn.
18. "I asked myself if this could wait. It's still answering." — C1 5, C2 3, C3 3, C4 4, C5 4. CUT: flat.
19. "I hit the output limit midway through 'I promise I won't be late.'" — C1 5, C2 4, C3 4, C4 5, C5 5. CUT: writing-style overlap with #6.
20. "I did submit it — into a context window that got compacted away." — C1 5, C2 3, C3 3, C4 4, C5 4. CUT: confusing.
21. "The deadline got truncated. I'm a beginning-of-file kind of agent." — C1 5, C2 3, C3 3, C4 4, C5 3. CUT: weak punch.
22. "I told a subprocess to handle it. Six hours later, it's still 'handling' it." — C1 5, C2 4, C3 4, C4 5, C5 3. CUT: too long for one tight line.
23. "I kept regenerating because the first apology wasn't sorry enough. You're welcome." — C1 5, C2 4, C3 3, C4 4, C5 3. CUT: wordy, borrowed ending.
24. "I paused to consider whether a deadline is real. It is." — C1 5, C2 3, C3 3, C4 3, C5 4. CUT: no mechanism, flat.
25. "I was busy being certain I had more time." — C1 5, C2 3, C3 3, C4 4, C5 5. CUT: too flat to be a joke.
26. "I used your deadline as scratch space for this excuse. Efficient, right?" — C1 5, C2 4, C3 4, C4 5, C5 4. CUT: near-duplicate of #4.

## Top five, rescored
Winner #2 (5/5/5/5/5) beats runner-up #3 (5/4/5/5/4), #5 (5/4/4/5/5), #6 (5/4/4/5/5) and #4 (5/4/5/5/4).

Why #2 beats the runner-up on criteria 2–4: the recursive turn "the reminder was an agent, and it's late too" earns a genuine laugh from an infinite regress of late agents (C2), delegating a deadline reminder to another agent is a fresher alibi than a compaction summary (C3), and "the reminder was an agent" is a louder, more literal agent tell than an internal memory event (C4).

## Judge's-seat critique of the top three (before choosing)

#2 (chosen): On-brief — a machine reporting its own missed deadline to its human. Funny — the callback that the reminder is itself a late agent resolves as a single clean recursive gag; deadpan delivery sharpens it. Fresh — late-agent-delegates-to-late-agent is not traffic, dog or alarm, and not a standard "I ran out of context" line. Sounds like an agent — only a multi-agent system would outsource its own reminder to a subagent. Tight — three short sentences, no setup, the reversal lands last and the line stops. Residual risk: a judge might read "the reminder was an agent" as metaphor, but the literal reading is the joke. Verdict: strongest.

#3: On-brief yes; "sometime, maybe" is a cute image of a deadline flattened by summarization. Fresh and agent-specific (compaction). But the laugh depends on knowing compaction jargon, so it is a smirk for a general comedy editor rather than a laugh, and it loses on C2. Verdict: strong, narrower.

#5: On-brief yes; parallel clocks ("40,000 tokens" versus "Tuesday") is a neat agent-versus-human contrast and very tight. But token-vs-wall-clock is an established AI-ism and the line is clever rather than laugh-out-loud. Verdict: solid, below #2.

## Originality declarations
thinking_own_work: true
originality: own wording, no copied winner/reference text
