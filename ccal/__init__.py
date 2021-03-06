from os.path import abspath

VERSION = '0.6.11'

print('CCAL version {} @ {}'.format(VERSION, abspath(__file__)))

from .tcga.tcga.make_case_annotations import make_case_annotations
from .tcga.tcga.read_copynumber_gistic2 import read_copynumber_gistic2
from .tcga.tcga.read_correlate_copynumber_vs_mrnaseq import read_correlate_copynumber_vs_mrnaseq
from .tcga.tcga.read_mutsignozzlereport2cv import read_mutsignozzlereport2cv
from .nmf_map.nmf_map.NMFMap import NMFMap
from .nmf_map.nmf_map.get_elements_near_state_centroids import get_elements_near_state_centroids
from .cluster.cluster.nmf_consensus_cluster_with_multiple_k import nmf_consensus_cluster_with_multiple_k
from .cluster.cluster.nmf_consensus_cluster import nmf_consensus_cluster
from .cluster.cluster.hierarchical_consensus_cluster_with_multiple_k import hierarchical_consensus_cluster_with_multiple_k
from .cluster.cluster.hierarchical_consensus_cluster import hierarchical_consensus_cluster
from .information.information.compute_information_coefficient import compute_information_coefficient
from .information.information.compute_entropy import compute_entropy
from .information.information.compute_information_distance import compute_information_distance
from .context.context.make_1d_signal_matrix import make_1d_signal_matrix
from .context.context.summarize_1d_context_matrix import summarize_1d_context_matrix
from .context.context.make_1d_context_matrix import make_1d_context_matrix
from .context.context.fit_skew_t_pdf import fit_skew_t_pdf
from .context.context.plot_context import plot_context
from .context.context.make_2d_signal_matrix import make_2d_signal_matrix
from .context.context.fit_skew_t_pdfs import fit_skew_t_pdfs
from .context.context.compute_context import compute_context
from .classify.classify.train_and_classify import train_and_classify
from .probability.probability.plot_bayesian_nomogram import plot_bayesian_nomogram
from .probability.probability.infer_assuming_independence import infer_assuming_independence
from .probability.probability.infer import infer
from .probability.probability.compute_posterior_probability import compute_posterior_probability
from .probability.probability.compute_joint_probability import compute_joint_probability
from .plot.plot.make_html_and_plotly_file_paths import make_html_and_plotly_file_paths
from .plot.plot.plot_pie import plot_pie
from .plot.plot.plot_box_or_violin import plot_box_or_violin
from .plot.plot.make_random_color import make_random_color
from .plot.plot.plot_points import plot_points
from .plot.plot.make_colorscale import make_colorscale
from .plot.plot.plot_heat_map import plot_heat_map
from .plot.plot.plot_distributions import plot_distributions
from .plot.plot.plot_bubble_map import plot_bubble_map
from .plot.plot.plot_and_save import plot_and_save
from .plot.plot.plot_bar import plot_bar
from .plot.plot.plot_table import plot_table
from .hdf5.hdf5.read_where_and_map_column_names import read_where_and_map_column_names
from .gsea.gsea._compute_gene_scores import compute_euclidean_distance
from .gsea.gsea._compute_gene_scores import compute_pearsons_correlation
from .gsea.gsea._compute_gene_scores import compute_cosine_similarity
from .gsea.gsea.single_sample_gseas import single_sample_gseas
from .gsea.gsea.single_sample_gsea import single_sample_gsea
from .gsea.gsea.gsea import gsea
from .regress.regress.train_and_regress import train_and_regress
from .match.match.make_summary_match_panel import make_summary_match_panel
from .match.match._match import match_randomly_sampled_target_and_features_to_compute_margin_of_errors
from .match.match._match import permute_target_and_match_target_and_features
from .match.match._match import match_target_and_features
from .match.match.make_match_panel import make_match_panel
from .match.match.make_match_panels import make_match_panels
from .match.match.make_comparison_panel import make_comparison_panel
from .matrix_factorization.matrix_factorization.solve_for_nmf_h import solve_for_nmf_h
from .matrix_factorization.matrix_factorization.nmf import nmf
from .geo.geo.get_and_parse_geo_data import get_and_parse_geo_data
from .gct_gmt.gct_gmt.access_gmt import read_gmts
from .gct_gmt.gct_gmt.access_gmt import read_gmt
from .gct_gmt.gct_gmt.access_gmt import write_gmt
from .gct_gmt.gct_gmt.access_gct import read_gct
from .gct_gmt.gct_gmt.access_gct import write_gct
from .linear_model.linear_model.correlate import correlate
from .cryptograph.cryptograph.access_passcode import hash_passcode
from .cryptograph.cryptograph.access_passcode import match_passcode_with_passcode_hash
from .cryptograph.cryptograph.crypt_with_aes import encrypt_directory_files
from .cryptograph.cryptograph.crypt_with_aes import decrypt_directory_files
from .cryptograph.cryptograph.crypt_with_aes import encrypt_file
from .cryptograph.cryptograph.crypt_with_aes import decrypt_file
from .cryptograph.cryptograph.hash_ import hash_str_to_32_bytes
from .cryptograph.cryptograph.hash_ import hash_directory_files
from .cryptograph.cryptograph.hash_ import hash_file
from .cryptograph.cryptograph.hash_ import hash_list_of_str
from .support.support.df import drop_df_slice_greedily
from .support.support.df import drop_df_slice
from .support.support.df import split_df
from .support.support.git import create_gitkeep
from .support.support.git import get_git_versions
from .support.support.git import clean_git_url
from .support.support.git import in_git_repository
from .support.support.iterable import group_iterable
from .support.support.iterable import flatten_nested_iterable
from .support.support.iterable import replace_bad_objects_in_iterable
from .support.support.iterable import group_and_apply_function_on_each_group_in_iterable
from .support.support.iterable import get_unique_iterable_objects_in_order
from .support.support.iterable import make_object_int_mapping
from .support.support.log import get_now
from .support.support.log import initialize_logger
from .support.support.log import echo_or_print
from .support.support.log import log_and_return_response
from .support.support.conda import install_and_activate_conda
from .support.support.conda import add_conda_to_path
from .support.support.conda import conda_is_installed
from .support.support.conda import get_conda_environments
from .support.support.conda import get_conda_prefix
from .support.support.exit_ import exit_
from .support.support.dict_ import merge_dicts_with_callable
from .support.support.dict_ import write_dict
from .support.support.compression import gzip_compress_file
from .support.support.compression import gzip_decompress_file
from .support.support.compression import gzip_decompress_and_bgzip_compress_file
from .support.support.series import cast_series_to_builtins
from .support.support.series import make_membership_df_from_categorical_series
from .support.support.series import get_extreme_series_indices
from .support.support.volume import mount_volume
from .support.support.volume import unmount_volume
from .support.support.volume import get_volume_name
from .support.support.volume import make_volume_dict
from .support.support.machine import get_machine
from .support.support.machine import get_shell_environment
from .support.support.machine import have_program
from .support.support.machine import shutdown_machine
from .support.support.machine import reboot_machine
from .support.support.subprocess_ import run_command
from .support.support.subprocess_ import run_command_and_monitor
from .support.support.network import download
from .support.support.network import get_open_port
from .support.support.python import get_installed_pip_libraries
from .support.support.python import install_python_libraries
from .support.support.python import get_object_reference
from .support.support.multiprocess import multiprocess
from .support.support.math import rescale_x_y_coordiantes_in_polar_coordiante
from .support.support.json_ import read_json
from .support.support.json_ import write_json
from .support.support.str_ import cast_str_to_builtins
from .support.support.str_ import title_str
from .support.support.str_ import untitle_str
from .support.support.str_ import split_str_ignoring_inside_quotes
from .support.support.str_ import str_is_version
from .support.support.path import establish_path
from .support.support.path import copy_path
from .support.support.path import remove_paths
from .support.support.path import remove_path
from .support.support.path import clean_path
from .support.support.path import clean_name
from .dimension_scale.dimension_scale.mds import mds
from .variant.variant.access_vcf import get_variants_from_vcf_gz
from .variant.variant.access_vcf import parse_vcf_row_and_make_variant_dict
from .variant.variant.access_vcf import update_variant_dict
from .variant.variant.access_vcf import count_gene_impacts_from_variant_dicts
from .variant.variant.access_vcf import get_vcf_info
from .variant.variant.access_vcf import get_vcf_info_ann
from .variant.variant.access_vcf import get_vcf_sample_format
from .variant.variant.access_vcf import get_variant_start_and_end_positions
from .variant.variant.access_vcf import get_variant_type
from .variant.variant.access_vcf import is_inframe
from .variant.variant.access_vcf import get_maf_variant_classification
from .variant.variant.access_vcf import get_genotype
from .variant.variant.access_vcf import get_allelic_frequencies
from .variant.variant.access_vcf import get_population_allelic_frequencies
from .variant.variant.access_vcf import count_vcf_gz_rows
from .variant.variant.access_vcf_dict import read_vcf_gz_and_make_vcf_dict
from .variant.variant.VariantHDF5 import VariantHDF5
from .variant.variant.access_maf import split_maf_by_tumor_sample_barcode
from .variant.variant.access_maf import make_maf_from_vcf
from .kernel_density.kernel_density.estimate_kernel_density import estimate_kernel_density
from .kernel_density.kernel_density.compute_bandwidths import compute_bandwidths
from .cross_validate.cross_validate.cross_validate import cross_validate
from .feature.feature.get_gff3_attribute import get_gff3_attribute
from .feature.feature.index_gff3_df_by_name import index_gff3_df_by_name
from .feature.feature.read_gff3_gz import read_gff3
from .feature.feature.FeatureHDF5 import FeatureHDF5
from .sequencing_process.sequencing_process.process_fastq_gz import check_fastq_gzs
from .sequencing_process.sequencing_process.process_fastq_gz import check_fastq_gzs_using_fastqc
from .sequencing_process.sequencing_process.process_fastq_gz import trim_fastq_gzs_using_skewer
from .sequencing_process.sequencing_process.process_fastq_gz import align_fastq_gzs_using_bwa_mem
from .sequencing_process.sequencing_process.process_fastq_gz import align_fastq_gzs_using_hisat2
from .sequencing_process.sequencing_process.process_fastq_gz import count_transcripts_using_kallisto_quant
from .sequencing_process.sequencing_process.bgzip_and_tabix import bgzip_and_tabix
from .sequencing_process.sequencing_process.download_clinvar_vcf_gz import download_clinvar_vcf_gz
from .sequencing_process.sequencing_process.make_reference_genome import make_reference_genome
from .sequencing_process.sequencing_process.process_vcf_gz import concatenate_vcf_gzs_using_bcftools_concat
from .sequencing_process.sequencing_process.process_vcf_gz import rename_chromosome_of_vcf_gz_using_bcftools_annotate
from .sequencing_process.sequencing_process.process_vcf_gz import annotate_vcf_gz_using_snpeff
from .sequencing_process.sequencing_process.process_vcf_gz import annotate_vcf_gz_using_bcftools_annotate
from .sequencing_process.sequencing_process.process_vcf_gz import filter_vcf_gz_using_bcftools_view
from .sequencing_process.sequencing_process.simulate_sequences_using_dwgsim import simulate_sequences_using_dwgsim
from .sequencing_process.sequencing_process.process_bam import sort_and_index_bam_using_samtools_sort_and_index
from .sequencing_process.sequencing_process.process_bam import index_bam_using_samtools_index
from .sequencing_process.sequencing_process.process_bam import mark_duplicates_in_bam_using_picard_markduplicates
from .sequencing_process.sequencing_process.process_bam import check_bam_using_samtools_flagstat
from .sequencing_process.sequencing_process.process_bam import check_fastq_gz_or_bam_using_fastqp
from .sequencing_process.sequencing_process.process_bam import get_variants_from_bam_using_freebayes_and_multiprocess
from .sequencing_process.sequencing_process.process_bam import get_variants_from_bam_using_freebayes
from .sequencing_process.sequencing_process.process_bam import get_variants_from_bam_using_strelka
from .linear_algebra.linear_algebra.solve_ax_equal_b import solve_ax_equal_b
from .sequence.sequence.process_sequence import transcribe_dna_sequence
from .sequence.sequence.process_sequence import reverse_transcribe_rna_sequence
from .sequence.sequence.process_sequence import reverse_complement_dna_sequence
from .sequence.sequence.process_sequence import translate_nucleotide_sequence
from .sequence.sequence.process_sequence import split_codons
from .sequence.sequence.get_chromosome_size_from_fasta_gz import get_chromosome_size_from_fasta_gz
from .sequence.sequence.establish_fai_index import establish_fai_index
from .sequence.sequence.get_sequence_from_fasta_gz import get_sequence_from_fasta_gz
from .genome.genome.Genome import is_valid_vcf_gz
from .genome.genome.Genome import Genome
from .nd_array.nd_array.get_1d_array_unique_objects_in_order import get_1d_array_unique_objects_in_order
from .nd_array.nd_array.check_nd_array_for_bad_value import check_nd_array_for_bad_value
from .nd_array.nd_array.compute_log_ratio_between_2_1d_arrays import compute_log_ratio_between_2_1d_arrays
from .nd_array.nd_array.normalize_nd_array import normalize_nd_array
from .nd_array.nd_array.compute_nd_array_margin_of_error import compute_nd_array_margin_of_error
from .nd_array.nd_array.drop_bad_value_and_apply_function_on_2_1d_arrays import drop_bad_value_and_apply_function_on_2_1d_arrays
from .nd_array.nd_array.compute_empirical_p_value import compute_empirical_p_value
from .nd_array.nd_array.cluster_1d_arrays import cluster_1d_arrays
from .nd_array.nd_array.apply_function_on_2_2d_arrays_slices import apply_function_on_2_2d_arrays_slices
from .nd_array.nd_array.get_intersections_between_2_1d_arrays import get_intersections_between_2_1d_arrays
from .nd_array.nd_array.clip_nd_array_by_standard_deviation import clip_nd_array_by_standard_deviation
from .nd_array.nd_array.shuffle_each_2d_array_slice import shuffle_each_2d_array_slice
from .nd_array.nd_array.make_nd_grid_coordinates import make_nd_grid_coordinates
from .nd_array.nd_array.cluster_2d_array_slices_by_group import cluster_2d_array_slices_by_group
from .nd_array.nd_array.apply_function_on_2_1d_arrays_and_compute_empirical_p_value import apply_function_on_2_1d_arrays_and_compute_empirical_p_value
from .nd_array.nd_array.nd_array_is_sorted import nd_array_is_sorted
from .nd_array.nd_array.compute_empirical_p_values_and_fdrs import compute_empirical_p_values_and_fdrs
from .nd_array.nd_array.get_coordinates_for_reflection import get_coordinates_for_reflection
from .nd_array.nd_array.shift_and_log_nd_array import shift_and_log_nd_array


explore_components = nmf_consensus_cluster_with_multiple_k

explore_states = hierarchical_consensus_cluster_with_multiple_k

