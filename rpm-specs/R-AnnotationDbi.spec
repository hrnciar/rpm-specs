%global packname AnnotationDbi
%global packver 1.50.0

%global __suggests_exclude ^R\\((GO.db|KEGG.db|hgu95av2.db|hom.Hs.inp.db|org.At.tair.db|org.Hs.eg.db|org.Sc.sgd.db|reactome.db|TxDb\\.Hsapiens\\.UCSC\\.hg19\\.knownGene|AnnotationForge|graph|EnsDb.Hsapiens.v75|BiocStyle)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic 2.0
BuildArch:        noarch
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          Manipulation of SQLite-based annotations in Bioconductor
BuildRequires:    R-devel >= 2.7.0, tetex-latex
BuildRequires:    R-methods, R-utils, R-stats4, R-BiocGenerics >= 0.29.2, R-Biobase >= 1.17.0
BuildRequires:    R-IRanges-devel, R-DBI, R-RSQLite, R-S4Vectors-devel >= 0.9.25

%description
Implements a user-friendly interface for querying SQLite-based annotation data
packages.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%doc %{_datadir}/R/library/%{packname}/NEWS
%doc %{_datadir}/R/library/%{packname}/NOTES-Herve
%doc %{_datadir}/R/library/%{packname}/TODO
%{_datadir}/R/library/%{packname}/DBschemas
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/help
%doc %{_datadir}/R/library/%{packname}/doc
%{_datadir}/R/library/%{packname}/extdata
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/script
%{_datadir}/R/library/%{packname}/unitTests

%changelog
* Tue Jun 16 2020 Tom Callaway <spot@fedoraproject.org> - 1.50.0-2
- fixup doc files

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.50.0-1
- initial package
