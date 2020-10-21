%global packname GenomicAlignments
%global packver 1.22.1

%global __suggests_exclude ^R\\((BSgenome\\.Dmelanogaster\\.UCSC\\.dm3|BSgenome\\.Hsapiens\\.UCSC\\.hg19|BiocStyle|DESeq2|GenomicFeatures|RNAseqData\\.HNRNPC\\.bam\\.chr14|ShortRead|TxDb\\.Dmelanogaster\\.UCSC\\.dm3\\.ensGene|TxDb\\.Hsapiens\\.UCSC\\.hg19\\.knownGene|edgeR|pasillaBamSubset)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          Representation and manipulation of short genomic alignments
BuildRequires:    R-devel >= 3.5.0, tetex-latex, R-methods, R-BiocGenerics >= 0.15.3, R-S4Vectors-devel >= 0.23.19
BuildRequires:    R-IRanges-devel >= 2.15.12, R-GenomeInfoDb >= 1.13.1, R-GenomicRanges >= 1.37.2
BuildRequires:    R-SummarizedExperiment >= 1.9.13, R-Biostrings >= 2.47.6, R-Rsamtools-devel >= 1.31.2
BuildRequires:    R-utils, R-stats, R-BiocParallel

%description
Provides efficient containers for storing and manipulating short genomic 
alignments (typically obtained by aligning short reads to a reference genome). 
This includes read counting, computing the coverage, junction detection, and 
working with the nucleotide content of the alignments.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_libdir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/unitTests

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 José Abílio Matos <jamatos@fc.up.pt> - 1.22.1-2
- rebuild for R 4

* Sat Feb  1 2020 Tom Callaway <spot@fedoraproject.org> - 1.22.1-1
- update to 1.22.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.22.0-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.22.0-1
- update to 1.22.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.18.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.18.1-1
- update to 1.18.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1.14.1-1
- update to 1.14.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.12.1-1
- initial package
