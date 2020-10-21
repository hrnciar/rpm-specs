%global packname  GenomeInfoDb

%global __suggests_exclude ^R\\((BSgenome\\.Celegans\\.UCSC\\.ce2|BSgenome\\.Hsapiens\\.NCBI\\.GRCh38|BSgenome\\.Scerevisiae\\.UCSC\\.sacCer2|BiocStyle|GenomicFeatures|TxDb\\.Dmelanogaster\\.UCSC\\.dm3\\.ensGene)\\)

Name:             R-%{packname}
Version:          1.24.0
Release:          2%{?dist}
Summary:          Utilities for manipulating chromosome and other 'seqname' identifiers
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/GenomeInfoDb.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         tex(latex)
BuildRequires:    R-devel >= 3.1.0 R-methods R-stats4 R-stats R-utils R-BiocGenerics >= 0.13.8
BuildRequires:    R-S4Vectors-devel >= 0.25.12 R-IRanges-devel >= 2.13.12 R-GenomeInfoDbData
BuildRequires:    R-RCurl
BuildArch:        noarch

%description
The Seqnames package contains data and functions that define and allow 
translation between different chromosome sequence naming conventions (e.g., 
"chr1" versus "1"), including a function that attempts to place sequence 
names in their natural, rather than lexicographic, order.

%prep
%setup -c -q -n %{packname}

sed -i 's/\r//' GenomeInfoDb/NEWS

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

sed -i 's/\r//' %{buildroot}%{_datadir}/R/library/%{packname}/doc/Accept-organism-for-GenomeInfoDb.Rnw
sed -i 's/\r//' %{buildroot}%{_datadir}/R/library/%{packname}/doc/GenomeInfoDb.Rnw

%check
# All sorts of missing Suggests prevents this from working.
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/NEWS
%doc %{_datadir}/R/library/%{packname}/doc/
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/extdata/
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/registered/
%{_datadir}/R/library/%{packname}/unitTests/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.24.0-1
- update to 1.24.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.22.0-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 1.22.0-1
- update to 1.22.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1.14.0-1
- update to 1.14.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 1.12.1-1
- update to 1.12.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.2-1
- initial package
