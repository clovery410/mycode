	.text
	.syntax unified
	.eabi_attribute	67, "2.09"	@ Tag_conformance
	.cpu	arm7tdmi
	.eabi_attribute	6, 2	@ Tag_CPU_arch
	.eabi_attribute	8, 1	@ Tag_ARM_ISA_use
	.eabi_attribute	17, 1	@ Tag_ABI_PCS_GOT_use
	.eabi_attribute	20, 1	@ Tag_ABI_FP_denormal
	.eabi_attribute	21, 1	@ Tag_ABI_FP_exceptions
	.eabi_attribute	23, 3	@ Tag_ABI_FP_number_model
	.eabi_attribute	34, 0	@ Tag_CPU_unaligned_access
	.eabi_attribute	24, 1	@ Tag_ABI_align_needed
	.eabi_attribute	25, 1	@ Tag_ABI_align_preserved
	.eabi_attribute	38, 1	@ Tag_ABI_FP_16bit_format
	.eabi_attribute	18, 4	@ Tag_ABI_PCS_wchar_t
	.eabi_attribute	26, 2	@ Tag_ABI_enum_size
	.eabi_attribute	14, 0	@ Tag_ABI_PCS_R9_use
	.file	"hw4_1.c"
	.globl	abc
	.align	2
	.type	abc,%function
abc:                                    @ @abc
	.fnstart
@ BB#0:
	.pad	#20
	sub	sp, sp, #20
	mov	r2, r1
	mov	r3, r0
	str	r0, [sp, #16]
	str	r1, [sp, #12]
	ldr	r0, [sp, #16]
	add	r0, r0, r1
	str	r0, [sp, #8]
	str	r2, [sp, #4]            @ 4-byte Spill
	str	r3, [sp]                @ 4-byte Spill
	add	sp, sp, #20
	bx	lr
.Lfunc_end0:
	.size	abc, .Lfunc_end0-abc
	.cantunwind
	.fnend

	.globl	main
	.align	2
	.type	main,%function
main:                                   @ @main
	.fnstart
@ BB#0:
	.save	{r11, lr}
	push	{r11, lr}
	.setfp	r11, sp
	mov	r11, sp
	.pad	#8
	sub	sp, sp, #8
	mov	r0, #1
	mov	r1, #3
	bl	abc
	mov	r1, #0
	str	r0, [sp, #4]            @ 4-byte Spill
	mov	r0, r1
	mov	sp, r11
	pop	{r11, lr}
	bx	lr
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cantunwind
	.fnend


	.ident	"Apple LLVM version 7.0.0 (clang-700.0.72)"
	.section	".note.GNU-stack","",%progbits
