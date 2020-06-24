%global packname SummarizedExperiment
%global packver 1.18.1

%global __suggests_exclude ^R\\((AnnotationDbi|BiocStyle|GenomicFeatures|HDF5Array|TxDb\\.Hsapiens\\.UCSC\\.hg19\\.knownGene|airway|annotate|hgu95av2\\.db|rhdf5)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          SummarizedExperiment container
BuildRequires:    R-devel >= 3.2.0, texlive-latex, R-methods, R-GenomicRanges >= 1.33.6, R-Biobase
BuildRequires:    R-DelayedArray >= 0.3.20, R-utils, R-stats, R-tools, R-Matrix, R-BiocGenerics >= 0.15.3
BuildRequires:    R-S4Vectors-devel >= 0.25.14, R-IRanges-devel >= 2.21.6, R-GenomeInfoDb >= 1.13.1
BuildArch:        noarch

%description
The SummarizedExperiment container contains one or more assays, each
represented by a marix-like object of numeric or other mode. The rows
typically represent genomic ranges of interest and the columns represent
samples.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/doc
%{_datadir}/R/library/%{packname}/extdata
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/scripts
%{_datadir}/R/library/%{packname}/unitTests

%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.18.1-1
- update to 1.18.1
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.0-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.10.1-1
- update to 1.10.1

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.8.1-1
- update to 1.8.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.6.3-1
- initial package

