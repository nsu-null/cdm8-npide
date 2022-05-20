asect 0
    inc r0
    inc r1
    jsr sum_r0_r1_r2
    inc r2
    inc r3
    halt

sum_r0_r1_r2:
    add r1, r0
    add r2, r0
    rts

asect 0xd0
    dc "hello"

end