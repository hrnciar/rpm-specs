%global packname  biomaRt

%global __suggests_exclude ^R\\((annotate)\\)

Name:             R-%{packname}
Version:          2.44.0
Release:          1%{?dist}
Summary:          R Interface to BioMart databases
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/biomaRt.html
Source0:          http://www.bioconductor.org/packages/2.9/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         texlive-latex
BuildRequires:    R-devel >= 3.0.0, R-AnnotationDbi, R-progress, R-stringr, R-httr, R-openssl, R-BiocFileCache, R-rappdirs, R-XML, R-utils
BuildArch:        noarch

%description
In recent years a wealth of biological data has become available in public 
data repositories. Easy access to these valuable data resources and firm 
integration with data analysis is needed for comprehensive bioinformatics data 
analysis. biomaRt provides an interface to a growing collection of databases 
implementing the BioMart software suite (http://www.biomart.org). The package 
enables retrieval of large amounts of data in a uniform way without the need 
to know the underlying database schemas or write complex SQL queries. Examples 
of BioMart databases are Ensembl, COSMIC, Uniprot, HGNC, Gramene, Wormbase and 
dbSNP mapped to Ensembl. These major databases give biomaRt users direct 
access to a diverse set of data and enable a wide range of powerful online 
queries from gene annotation to database mining.

%prep
%setup -c -q -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

%check
# Enable if R-annotate ever arrives in Fedora.
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}/
%doc %{_datadir}/R/library/%{packname}/doc/
%doc %{_datadir}/R/library/%{packname}/html/
%doc %{_datadir}/R/library/%{packname}/CITATION
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/Meta/
%{_datadir}/R/library/%{packname}/R/
%{_datadir}/R/library/%{packname}/help/
%{_datadir}/R/library/%{packname}/scripts/

%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 2.44.0-1
- update to 2.44.0
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-13
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-12
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 2.18.0-8
- updating brings in a pile of unpackaged deps, so just rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Tom Callaway <spot@fedoraproject.org> - 2.18.0-1
- update to 2.18.0

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 2.16.0-1
- update to 2.16.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Tom "spot" Callaway <tcallawa@redhat.com> 2.10.0-1
- initial package for Fedora
