import subprocess
import qiime

qiime.split_libraries.preprocess(fasta_files, qual_files, mapping_file, barcode_type = 'no-barcode', min_seq_len, max_seq_len, min_qual_score, starting_ix, keep_primer, max_ambig, max_primer_mm, trim_seq_len, dir_prefix, max_bc_errors, max_homopolymer, retain_unassigned_reads, keep_barcode, attempt_bc_correction, qual_score_window, disable_primer_check, reverse_primers, reverse_primer_mismatches, record_qual_scores, discard_bad_windows, median_length_filtering, added_demultiplex_field, truncate_ambi_bases)