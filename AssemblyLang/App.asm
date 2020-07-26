; -----------------------------------------------------------------------------
; Note that the parameters have already been passed in rdi, rsi.  We
; just have to return the value in rax.
; -----------------------------------------------------------------------------

        global add
        section .text
add:
        mov     rax, rdi               ; result (rax) initially holds x
        add     rax, rsi                ; is x less than y?
        ret