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
	.file	"hw4_2.c"
	.globl	main
	.align	2
	.type	main,%function
main:                                   @ @main
	.fnstart
@ BB#0:
	.pad	#88
	sub	sp, sp, #88
	mov	r0, #0
	str	r0, [sp, #84]
	str	r0, [sp, #80]
	b	.LBB0_1
.LBB0_1:                                @ =>This Inner Loop Header: Depth=1
	ldr	r0, [sp, #80]
	add	r1, sp, #40
	ldr	r1, [r1, r0, lsl #2]
	cmp	r0, r1
	bge	.LBB0_4
	b	.LBB0_2
.LBB0_2:                                @   in Loop: Header=BB0_1 Depth=1
	ldr	r0, [sp, #80]
	mov	r1, sp
	mov	r2, #0
	str	r2, [r1, r0, lsl #2]
	b	.LBB0_3
.LBB0_3:                                @   in Loop: Header=BB0_1 Depth=1
	ldr	r0, [sp, #80]
	add	r0, r0, #1
	str	r0, [sp, #80]
	b	.LBB0_1
.LBB0_4:
	ldr	r0, [sp, #84]
	add	sp, sp, #88
	bx	lr
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cantunwind
	.fnend


	.ident	"Apple LLVM version 7.0.0 (clang-700.0.72)"
	.section	".note.GNU-stack","",%progbits
